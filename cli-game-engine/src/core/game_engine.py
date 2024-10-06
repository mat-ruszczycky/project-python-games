# CLI Game Engine

class GameEngine:
    def __init__(self) -> None:
        self.isPlaying = False

    def checkPlayCondition(self, value: str) -> bool:
        return value.lower() == 'y'
    
    def stop(self) -> None:
        self.isPlaying = False
        print('Game is stopped.')

    def play(self, gameLoop: callable) -> None:
        self.isPlaying = True
        print("Starting the game...")

        while self.isPlaying:
            gameLoop()

            user_input = input('Continue to play? (y/n): ').strip().lower()

            while user_input not in ['y', 'n']:
                print("Invalid input. Please enter 'y' to continue or 'n' to stop.")
                user_input = input('Continue to play? (y/n): ').strip().lower()

            self.isPlaying = self.checkPlayCondition(user_input)
        
        self.stop()

