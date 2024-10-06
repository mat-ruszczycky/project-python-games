# CLI Game Engine

from src.core.game_state import GameState
from src.core.game_engine import GameEngine
from src.io.output_handler import OutputHandler

def gameLoop(state: GameState) -> None:
    outputHandler = OutputHandler()
    outputHandler.displayMessage(f"Game is running, isPlaying: {state.isPlaying}")

if __name__ == "__main__":
    gameState = GameState()
    engine = GameEngine(gameState)
    engine.play(gameLoop)