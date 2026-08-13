from typing import Callable, Dict, List
from textual.app import App

from .exit import ExitCommand
from .base import Command, CommandResult, CommandAction

class CommandSystem:
    
    def __init__(self, app: App):
        self.app = app
        self._commands: Dict[str, Command] = {}

        self._register_default_commands()
        

    def register(self, command: Command) -> None:
        self._commands[command.name.lower()] = command


    def _register_default_commands(self) -> None:
        self.register(
            ExitCommand(self.app)
        )

    
    def handle_input(self, text: str) -> CommandResult:
        if not text.startswith("/"):
            return CommandResult()
        
        parts = text[1:].strip().split()

        if not parts:
            return CommandResult()

        cmd_name = parts[0].lower()
        args = parts[1:]

        command = self._commands.get(cmd_name)

        if command is None:
            return CommandResult(
                action=CommandAction.ERROR,
                data=f"Unknown command: /{cmd_name}"
            )

        return command.execute(args)
        
