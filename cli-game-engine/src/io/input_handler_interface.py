# CLI Game Engine

# Comment this
from abc import ABC, abstractmethod

# Comment this
class InputHandlerInterface(ABC):
    @abstractmethod
    def getUserInput(self, prompt: str) -> str:
        pass