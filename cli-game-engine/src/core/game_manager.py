# CLI Game Engine

class GameScene:

    def __init__(self, name: str, difficulty: int = 1) -> None:
        self.name = name
        self.state = "inactive"  # Can be 'inactive', 'active', 'paused', 'ended'
        self.difficulty = difficulty
        self.duration = 0
        self.sceneData = {}

    def start(self) -> None:
        self.state = "active"
        self.duration = 0
        print(f"Scene '{self.name}' started.")
    
    def pause(self) -> None:
        if self.state == "active":
            self.state = "paused"
            print(f"Scene '{self.name}' paused.")
    
    def resume(self) -> None:
        if self.state == "paused":
            self.state = "active"
            print(f"Scene '{self.name}' resumed.")
    
    def end(self) -> None:
        self.state = "ended"
        print(f"Scene '{self.name}' ended.")
    
    def update(self, deltaTime: int) -> None:
        if self.state == "active":
            self.duration += deltaTime
            print(f"Scene '{self.name}' updated. Duration: {self.duration}")


from typing import List, Optional

class GameManager:
    
    def __init__(self) -> None:
        self.scenes: List[GameScene] = [] 
    
    def addScene(self, scene: 'GameScene') -> None:
        self.scenes.append(scene)
        self.logSceneAction(f"Added scene: {scene.name}")
    
    def removeScene(self, scene: 'GameScene') -> None:
        if scene in self.scenes:
            self.scenes.remove(scene)
            self.logSceneAction(f"Removed scene: {scene.name}")
        else:
            self.logSceneAction(f"Scene {scene.name} not found.")
    
    def switchScene(self, scene_name: str) -> Optional['GameScene']:
        for scene in self.scenes:
            if scene.name == scene_name:
                self.logSceneAction(f"Switched to scene: {scene.name}")
                return scene
        self.logSceneAction(f"Scene {scene_name} not found.")
        return None
    
    def logSceneAction(self, message: str) -> None:
        print(message)

