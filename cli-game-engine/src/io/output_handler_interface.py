from abc import ABC, abstractmethod

class OutputHandlerInterface(ABC):
    @abstractmethod
    def displayMessage(self, message: str) -> None:
        pass