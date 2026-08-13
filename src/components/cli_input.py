from textual.widgets import Input, Label
from textual.app import ComposeResult
from textual.widget import Widget
from textual.containers import Horizontal
from textual.message import Message
from textual.binding import Binding
from textual import on

class GInput(Widget):

    BINDINGS = [
        Binding("ctrl+u", "clear_input", "Clear line", show=False)
    ]

    class Submitted(Message):
        def __init__(self, value: str) -> None:
            self.value = value
            super().__init__()

    def compose(self) -> ComposeResult:
        with Horizontal(id="cli-input-container"):
            yield Label(">", id="cli-prompt-label")
            yield Input(id="cli-command-input", type="text")
    
    def on_mount(self) -> None:
        self.query_one("#cli-command-input", Input).focus()

    @property
    def value(self) -> str:
        return self.query_one("#cli-command-input", Input).value
    
    @value.setter
    def value(self, new_value: str) -> None:
        self.query_one("#cli-command-input", Input).value = new_value

    def clear(self) -> None:
        self.value = ""  

    @on(Input.Submitted, "#cli-command-input")
    def _handle_internal_submit(self, event: Input.Submitted) -> None:
        event.stop() 
        
        command_text = self.value.strip()
        
        if command_text:
            self.post_message(self.Submitted(command_text))
            self.clear()
    
    def action_clear_input(self) -> None:
        self.clear()
    