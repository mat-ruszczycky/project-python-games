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

    def __init__(self, state: GameState, inputHandler: InputHandler, outputHandler: OutputHandler) -> None:
        if not hasattr(self, '_initialized'):
            self.state = state
            self.input_handler = inputHandler
            self.output_handler = outputHandler
            self._initialized = True

    def shouldContinue(self, value: str) -> bool:
        return value.lower() == 'y'
    
    def stop(self) -> None:
        self.state.stop_game()
        self.output_handler.display_message("Game is stopped.")

    def play(self, gameLoop: callable) -> None:
        self.state.start_game()
        self.output_handler.display_message("Game is starting...")

        while self.state.isPlaying:
            gameLoop()

            userInput = self.input_handler.get_user_input('Continue playing? (y/n): ')

            while userInput not in ['y', 'n']:
                self.output_handler.display_message("Invalid input. Please enter 'y' to continue or 'n' to stop.")
                userInput = self.input_handler.get_user_input('Continue playing? (y/n): ')

            if not self.shouldContinue(userInput):
                self.state.stop_game()
        
        self.stop()