from abc import ABC, abstractmethod

class InputHandlerInterface(ABC):
    @abstractmethod
    def getUserInput(self, prompt: str) -> str:
        pass