from abc import ABC, abstractmethod
from typing import List
from enum import Enum, auto
from typing import Any, Optional
from dataclasses import dataclass

class CommandAction(Enum):
    NONE = auto()
    ERROR = auto()

@dataclass
class CommandResult:
    action: CommandAction = CommandAction.NONE
    data: Optional[Any] = None

class Command(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self, args: List[str]) -> CommandResult:
        pass

