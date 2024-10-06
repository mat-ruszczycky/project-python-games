# CLI Game Engine

class InputHandler:

    def getUserInput(self, prompt: str) -> str:
        return input(prompt).strip().lower()