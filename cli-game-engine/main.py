# CLI Game Engine

from src.core.game_engine import GameEngine

def gameLoop() -> None:
    print('Playing Game Title')

if __name__ == "__main__":
    engine = GameEngine
    engine().play(gameLoop)