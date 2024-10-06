# CLI Game Engine

class GameState:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, '_initialized'):
            self.isPlaying = False
            self._initialized = True  # Prevents re-initialization

    def startGame(self) -> None:
        self.isPlaying = True

    def stopGame(self) -> None:
        self.isPlaying = False
