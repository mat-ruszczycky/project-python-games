# CLI Game Engine

from src.core.game_state import GameState
from src.io.input_handler import InputHandler
from src.io.output_handler import OutputHandler

class GameEngine:
    _instance = None
   
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameEngine, cls).__new__(cls)
        return cls._instance

    def __init__(self, state: GameState) -> None:
        if not hasattr(self, '_initialized'):
            self.state = state
            self.input_handler = InputHandler()
            self.output_handler = OutputHandler()
            self._initialized = True

    def shouldContinue(self, value: str) -> bool:
        return value.lower() == 'y'
    
    def stop(self) -> None:
        self.state.stopGame()
        self.output_handler.displayMessage("Game is stopped.")

    def play(self, gameLoop: callable) -> None:
        self.state.startGame()
        self.output_handler.displayMessage("Game is starting...")

        while self.state.isPlaying:
            gameLoop(self.state)

            userInput = self.input_handler.getUserInput('Continue playing? (y/n): ')

            while userInput not in ['y', 'n']:
                self.output_handler.displayMessage("Invalid input. Please enter 'y' to continue or 'n' to stop.")
                userInput = self.input_handler.getUserInput('Continue playing? (y/n): ')

            if not self.shouldContinue(userInput):
                self.state.stopGame()
        
        self.stop()