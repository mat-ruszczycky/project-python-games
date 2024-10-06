# CLI Game Engine

# Comment this
from abc import ABC, abstractmethod

# Comment this
class OutputHandlerInterface(ABC):
    @abstractmethod
    def displayMessage(self, message: str) -> None:
        pass