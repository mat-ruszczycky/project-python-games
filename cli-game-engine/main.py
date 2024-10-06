# CLI Game Engine

# Comment this
from src.core.game_state import GameState
from src.core.game_engine import GameEngine
from src.core.game_manager import GameManager, GameScene

# Comment this
from src.io.input_handler_interface import InputHandlerInterface
from src.io.output_handler_interface import OutputHandlerInterface
from src.io.output_handler import OutputHandler
from src.io.input_handler import InputHandler

# Define some scene logic functions
def introSceneLogic():
    print("This is the intro scene.")
    print("Welcome to the game!")

def gameOverSceneLogic():
    print("This is the game over scene.")
    print("Game over. You lost!")

# Comment this
def gameLoop(
    state: GameState,
    inputHandler: InputHandlerInterface,
    outputHandler: OutputHandlerInterface,
) -> None:
    gameManager = GameManager()

    # Create scenes and link them together
    introScene = GameScene("Intro", introSceneLogic)
    gameManager.addScene(introScene)

    gameOverScene = GameScene("Game Over", gameOverSceneLogic)
    gameManager.addScene(gameOverScene)

    # Link the scenes
    introScene.setNextScene(gameOverScene)
    gameOverScene.setPreviousScene(introScene)

    # Start the game and transition through scenes
    outputHandler.displayMessage(f"Game is running, isPlaying: {state.isPlaying}")
    currentScene = introScene
    currentScene.run()

# Comment this
if __name__ == "__main__":
    gameState = GameState()
    inputHandler = InputHandler()
    outputHandler = OutputHandler()
    engine = GameEngine(gameState, inputHandler, outputHandler)
    engine.play(lambda state: gameLoop(state, inputHandler, outputHandler))