from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label

class GUserQuery(Widget):
    def __init__(self, query_text: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.query_text = query_text

    def compose(self) -> ComposeResult:
        with Horizontal(id="cli-query-container"):
            yield Label(">", id="cli-query-label")
            yield Label(f"{self.query_text}", id="cli-query-text")