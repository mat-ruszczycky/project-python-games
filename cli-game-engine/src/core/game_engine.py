# CLI Game Engine

# Comment this
from src.core.game_state import GameState

# Comment this
from src.io.input_handler_interface import InputHandlerInterface
from src.io.output_handler_interface import OutputHandlerInterface

class GameEngine:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameEngine, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        state: GameState,
        inputHandler: InputHandlerInterface,
        outputHandler: OutputHandlerInterface,
    ) -> None:
        if not hasattr(self, "_initialized"):
            self.state = state
            self.inputHandler = inputHandler
            self.outputHandler = outputHandler
            self._initialized = True

    def shouldContinue(self, value: str) -> bool:
        return value.lower() == "y"

    def stop(self) -> None:
        self.state.stopGame()

    def play(self, gameLoop: callable) -> None:
        self.state.startGame()

        while self.state.isPlaying:
            gameLoop(self.state)

            userInput = self.inputHandler.getUserInput("Continue playing? (y/n): ")

            while userInput not in ["y", "n"]:
                self.outputHandler.displayMessage(
                    "Invalid input. Please enter 'y' to continue or 'n' to stop."
                )
                userInput = self.inputHandler.getUserInput("Continue playing? (y/n): ")

            if not self.shouldContinue(userInput):
                self.state.stopGame()

        self.stop()
