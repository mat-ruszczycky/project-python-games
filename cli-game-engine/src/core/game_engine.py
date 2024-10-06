# CLI Game Engine

from src.core.game_state import GameState
from src.io.input_handler import InputHandler
from src.io.output_handler import OutputHandler

class GameEngine:
    def __init__(self, state: GameState, inputHandler: InputHandler, outputHandler: OutputHandler) -> None:
        self.state = state

    def shouldContinue(self, value: str) -> bool:
        return value.lower() == 'y'
    
    def stop(self) -> None:
        self.state.stop_game()
        print('Game is stopped.')

    def play(self, gameLoop: callable) -> None:
        self.state.start_game()
        print("Starting the game...")

        while self.state.isPlaying:
            gameLoop()

            userInput = input('Continue to play? (y/n): ').strip().lower()

            while userInput not in ['y', 'n']:
                print("Invalid input. Please enter 'y' to continue or 'n' to stop.")
                userInput = input('Continue to play? (y/n): ').strip().lower()

            if not self.shouldContinue(userInput):
                self.state.stop_game()
        
        self.stop()