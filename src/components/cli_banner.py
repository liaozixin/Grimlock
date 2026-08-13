from textual.widget import Widget
from textual.containers import Horizontal
from textual.app import ComposeResult
from textual.widgets import Label


TITLE_A = r"""
 ██████╗ ██████╗ ██╗███╗   ███╗
██╔════╝ ██╔══██╗██║████╗ ████║
██║  ███╗██████╔╝██║██╔████╔██║
██║   ██║██╔══██╗██║██║╚██╔╝██║ 
╚██████╔╝██║  ██║██║██║ ╚═╝ ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝
"""

TITLE_B = r"""
██╗      ██████╗  ██████╗██╗  ██╗
██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║     ██║   ██║██║     █████╔╝ 
██║     ██║   ██║██║     ██╔═██╗ 
███████╗╚██████╔╝╚██████╗██║  ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""

class GBanner(Widget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with Horizontal(id="cli-banner-container"):
            yield Label(TITLE_A.strip("\n"), id="banner-title-A")
            yield Label(TITLE_B.strip("\n"), id="banner-title-B")
            