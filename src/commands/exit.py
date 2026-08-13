from typing import List
from .base import Command, CommandResult, CommandAction

from textual.app import App

class ExitCommand(Command):

    def __init__(self, app: App):
        self.app = app

    @property
    def name(self) -> str:
        return "exit"

    def execute(self, args: List[str]) -> CommandResult:
        self.app.exit()
        return CommandResult()