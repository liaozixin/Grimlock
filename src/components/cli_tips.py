from textual.widget import Widget
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widgets import Label
from rich.markup import escape

from ..utils.tips_generator import get_random_tip

class GTips(Widget):
    def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
            with Horizontal(id="cli-tips-container"):
                yield Label(
                f"[#d67549]• Tips[/] {escape(get_random_tip())}", 
                id="tips-label"
            )
