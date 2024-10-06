# CLI Game Engine

# Comment this 
from typing import Callable, Optional
from typing import List, Optional

# Comment this
class GameScene:

    def __init__(
        self, 
        name: str, 
        scene_logic: Callable[[], None], 
        previous_scene: Optional['GameScene'] = None, 
        next_scene: Optional['GameScene'] = None
    ) -> None:
        self.name = name
        self.scene_logic = scene_logic
        self.previous_scene = previous_scene
        self.next_scene = next_scene

    def run(self) -> None:
        print(f"Running scene: {self.name}")
        self.scene_logic()  # Execute the core logic for this scene

    def setPreviousScene(self, scene: Optional['GameScene']) -> None:
        self.previous_scene = scene

    def setNextScene(self, scene: Optional['GameScene']) -> None:
        self.next_scene = scene

    def gotoNextScene(self) -> Optional['GameScene']:
        if self.next_scene:
            print(f"Transitioning from {self.name} to {self.next_scene.name}")
        else:
            print(f"{self.name} has no next scene.")
        return self.next_scene

    def gotoPreviousScene(self) -> Optional['GameScene']:
        if self.previous_scene:
            print(f"Transitioning from {self.name} to {self.previous_scene.name}")
        else:
            print(f"{self.name} has no previous scene.")
        return self.previous_scene

# Comment this
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

