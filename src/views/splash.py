from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Vertical, Horizontal
from textual.widgets import Label

from ..components.cli_banner import GBanner
from ..components.cli_input import GInput
from ..components.cli_model_status_bar import GModelStatusBar
from ..components.cli_tips import GTips

class SplashScreen(Screen):
    def __init__(self, 
                 version: str, author: str, work_dir: str,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version_text = version
        self.author_text = author
        self.work_dir = work_dir

    def compose(self) -> ComposeResult:
        with Vertical(id="splash-container"):
            with Vertical(id="banner-container"):
                with Vertical(id="banner-wrapper"):
                    yield Label(self.author_text, id="splash-author")
                    yield GBanner()

            yield GInput()
            yield GModelStatusBar()
            yield GTips()

        if self.work_dir and self.version_text:
            with Horizontal(id="dock-bottom"):
                yield Label(self.work_dir, id="path-label-A")
                yield Label(f"v{self.version_text}", id="path-label-B")

        