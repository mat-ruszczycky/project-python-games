# CLI Game Engine

from src.core.game_state import GameState
from src.core.game_engine import GameEngine
from src.io.input_handler import InputHandler
from src.io.output_handler import OutputHandler

def gameLoop(state: GameState) -> None:
    print('Playing Game Title')

if __name__ == "__main__":
    gameState = GameState()
    inputHandler = InputHandler()
    outputHandler = OutputHandler()
    
    engine = GameEngine(gameState, inputHandler, outputHandler)
    engine.play(gameLoop)