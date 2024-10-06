# CLI Game Engine

class GameState:
    def __init__(self) -> None:
        self.isPlaying = False

    def start_game(self) -> None:
        self.isPlaying = True

    def stop_game(self) -> None:
        self.isPlaying = False