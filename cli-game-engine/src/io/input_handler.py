# CLI Game Engine

class InputHandler:

    def get_user_input(self, prompt: str) -> str:
        return input(prompt).strip().lower()