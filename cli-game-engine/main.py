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
    outputHandler.displayMessage("This is the intro scene.")
    outputHandler.displayMessage("Welcome to the game!")

def optionsSceneLogic():
    outputHandler.displayMessage("This is the options scene.")
    outputHandler.displayMessage("Welcome to the options - choose your destiny")

def mainSceneLogic():
    outputHandler.displayMessage("This is the main scene.")
    outputHandler.displayMessage("Welcome to the main - PLAY!")

def gameOverSceneLogic():
    outputHandler.displayMessage("This is the game over scene.")
    outputHandler.displayMessage("Game over. You lost!")

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

    opitonsScene = GameScene("Options", optionsSceneLogic)
    gameManager.addScene(opitonsScene)

    mainScene = GameScene("Main", mainSceneLogic)
    gameManager.addScene(mainScene)

    gameOverScene = GameScene("Game Over", gameOverSceneLogic)
    gameManager.addScene(gameOverScene)

    # Link the scenes
    introScene.setNextScene(mainScene)
    mainScene.setNextScene(gameOverScene)
    gameOverScene.setPreviousScene(introScene)

    # Init
    currentScene = introScene
    currentScene.run()

# Comment this
if __name__ == "__main__":
    gameState = GameState()
    inputHandler = InputHandler()
    outputHandler = OutputHandler()

    # Comment this
    engine = GameEngine(gameState, inputHandler, outputHandler)
    engine.play(lambda state: gameLoop(state, inputHandler, outputHandler))