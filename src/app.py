from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container
from textual import on

from .context.app_context import AppContext
from .commands.command_system import CommandSystem
from .commands.base import CommandAction
from .components.cli_input import GInput

from .database.database import init_db

from .views.splash import SplashScreen


BASE_DIR = Path(__file__).resolve().parent

class Grimlock(App):

    CSS_PATH = [
        BASE_DIR / "style" / "app.tcss",
        BASE_DIR / "style" / "cli_input.tcss",
        BASE_DIR / "style" / "cli_banner.tcss",
        BASE_DIR / "style" / "cli_user_query.tcss",
        BASE_DIR / "style" / "cli_system_info.tcss",
        BASE_DIR / "style" / "cli_model_status_bar.tcss",
        BASE_DIR / "style" / "cli_tips.tcss",

        BASE_DIR / "style" / "splash.tcss",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_context = AppContext()
        self.command_system = CommandSystem(self)

    def compose(self) -> ComposeResult:
        yield Container(id="root_container")
                  
    def on_mount(self) -> None:
        init_db()

        self.theme = "tokyo-night"

        self.push_screen(SplashScreen(version=self.app_context.version, 
                                      author=self.app_context.author, 
                                      work_dir=self.app_context.work_dir))

    @on(GInput.Submitted)
    def handle_input(self, event: GInput.Submitted) -> None:
        text = event.value

        result = self.command_system.handle_input(text)


        match result.action:
            case CommandAction.NONE:
                pass

            case CommandAction.ERROR:
                self.notify(
                    result.data,
                    severity="error",
                    timeout=1
                )
  

        

