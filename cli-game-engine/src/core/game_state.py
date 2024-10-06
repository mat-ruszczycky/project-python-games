# CLI Game Engine

class GameState:
    def __init__(self) -> None:
        self.isPlaying = False

    def startGame(self) -> None:
        self.isPlaying = True

    def stopGame(self) -> None:
        self.isPlaying = False