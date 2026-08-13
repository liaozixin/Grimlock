from textual.app import ComposeResult
from textual.widgets import Label, Static
from typing import Literal

class GSystemInfo(Static):
    def __init__(
            self, 
            type: Literal["error", "setup", "info", "success"],
            content: str,
            **kwargs
        ):
        super().__init__(**kwargs)
        self.info_type = type
        self.content = content

    def compose(self) -> ComposeResult:
        if self.info_type == "error":
            yield Label(f"[bold #f7768e]\\[SYSTEM FAILURE][/] {self.content}", id="sys_error_msg")

        elif self.info_type == "setup":
            yield Label(f"[bold #7dcfff]\\[SYSTEM PROTOCOL][/] {self.content}", id="sys_setup_msg")

        elif self.info_type == "info":
            yield Label(f"[bold #7aa2f7]\\[SYSTEM INFO][/] {self.content}", id="sys_info_msg")

        elif self.info_type == "success":
            yield Label(f"[bold #9ece6a]\\[AUTHENTICATED][/] {self.content}", id="sys_success_msg")