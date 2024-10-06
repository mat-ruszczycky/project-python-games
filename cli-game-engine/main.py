# CLI Game Engine

# Comment this
from src.core.game_state import GameState
from src.core.game_engine import GameEngine

# Comment this
from src.io.input_handler_interface import InputHandlerInterface
from src.io.output_handler_interface import OutputHandlerInterface
from src.io.output_handler import OutputHandler
from src.io.input_handler import InputHandler

# Comment this
def gameLoop(
    state: GameState,
    inputHandler: InputHandlerInterface,
    outputHandler: OutputHandlerInterface,
) -> None:
    outputHandler.displayMessage(f"Game is running, isPlaying: {state.isPlaying}")


# Comment this
if __name__ == "__main__":
    gameState = GameState()
    inputHandler = InputHandler()
    outputHandler = OutputHandler()
    engine = GameEngine(gameState, inputHandler, outputHandler)
    engine.play(lambda state: gameLoop(state, inputHandler, outputHandler))