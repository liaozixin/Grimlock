from textual.widget import Widget
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widgets import Label, ProgressBar
from textual.reactive import reactive
from textual.css.query import NoMatches

from rich.markup import escape

from typing import Optional, Literal

class GModelStatusBar(Widget):
    model_name: reactive[str] = reactive("Unset")
    model_provider: reactive[str] = reactive("Unknown")
    mode_auto_mode: reactive[Literal["Auto", "Manual"]] = reactive("Manual")
    context_usage: reactive[float] = reactive(0.0)

    model_dot_color: reactive[str] = reactive("#565f89")
    provider_dot_color: reactive[str] = reactive("#565f89")
    mode_auto_mode_dot_color: reactive[str] = reactive("#565f89")

    def __init__(self, 
                 model_name: str = "Unset", 
                 model_provider: str = "Unknown", 
                 mode_auto_mode: Literal["Auto", "Manual"] = "Manual",

                 context_usage: Optional[float] = 0.0,
                 model_dot_color: str = "#565f89", 
                 provider_dot_color: str = "#565f89",
                 mode_auto_mode_dot_color: str = "#565f89",

                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = model_name
        self.model_provider = model_provider
        self.mode_auto_mode = mode_auto_mode
        self.context_usage = context_usage

        self.context_usage = context_usage if context_usage is not None else 0.0

        self.model_dot_color = model_dot_color
        self.provider_dot_color = provider_dot_color
        self.mode_auto_mode_dot_color = mode_auto_mode_dot_color

    def compose(self) -> ComposeResult:
        with Horizontal(id="cli-model-bar-container"):
            yield Label(
                f"[{self.model_dot_color}]•[/] {self.model_name}", 
                id="model-name-label"
            )

            yield Label(
                f"[{self.provider_dot_color}]•[/] {self.model_provider}", 
                id="model-provider-label"
            )

            yield Label(
                f"[{self.mode_auto_mode_dot_color}]•[/] {self.mode_auto_mode}", 
                id="mode-auto-mode-label"
            )

            with Horizontal(id="context-progress-box"):
                yield Label("Context", id="context-text-label")
                yield ProgressBar(
                    total=1.0, 
                    show_eta=False,       
                    show_percentage=True,  
                    id="context-progress-bar"
                )

    def on_mount(self) -> None:
        progress_bar = self.query_one("#context-progress-bar", ProgressBar)
        progress_bar.update(progress=int(self.context_usage * 100))

    def watch_model_name(self, value: str) -> None:
        if self.is_mounted:
            self.query_one("#model-name-label", Label).update(
                f"[{self.model_dot_color}]•[/] {escape(value)}"
            )

    def watch_model_provider(self, value: str) -> None:
        if self.is_mounted:
            self.query_one("#model-provider-label", Label).update(
                f"[{self.provider_dot_color}]•[/] {escape(value)}"
            )

    def watch_mode_auto_mode(self, value: str) -> None:
        if self.is_mounted:
            self.query_one("#mode-auto-mode-label", Label).update(
                f"[{self.mode_auto_mode_dot_color}]•[/] {value}"
            )

    def watch_context_usage(self, value: float) -> None:
        if self.is_mounted:
            try:
                progress_bar = self.query_one("#context-progress-bar", ProgressBar)
                progress_bar.update(progress=value)
            except NoMatches:
                pass

    def watch_model_dot_color(self, _) -> None:
        self.watch_model_name(self.model_name)

    def watch_provider_dot_color(self, _) -> None:
        self.watch_model_provider(self.model_provider)

    def watch_mode_auto_mode_dot_color(self, _) -> None:
        self.watch_mode_auto_mode(self.mode_auto_mode)

    