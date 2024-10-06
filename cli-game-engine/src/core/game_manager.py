# CLI Game Engine

# Comment this 
from typing import Callable, Optional
from typing import List, Optional

# Comment this
class GameScene:

    def __init__(
        self, 
        name: str, 
        sceneLogic: Callable[[], None], 
        previousScene: Optional['GameScene'] = None, 
        nextScene: Optional['GameScene'] = None
    ) -> None:
        self.name = name
        self.sceneLogic = sceneLogic
        self.previousScene = previousScene
        self.nextScene = nextScene

    def run(self) -> None:
        print(f"Running scene: {self.name}")
        self.sceneLogic()  # Execute the core logic for this scene

    def setPreviousScene(self, scene: Optional['GameScene']) -> None:
        self.previousScene = scene

    def setNextScene(self, scene: Optional['GameScene']) -> None:
        self.nextScene = scene

    def gotoNextScene(self) -> Optional['GameScene']:
        if self.nextScene:
            print(f"Transitioning from {self.name} to {self.nextScene.name}")
        else:
            print(f"{self.name} has no next scene.")
        return self.nextScene

    def gotoPreviousScene(self) -> Optional['GameScene']:
        if self.previousScene:
            print(f"Transitioning from {self.name} to {self.previousScene.name}")
        else:
            print(f"{self.name} has no previous scene.")
        return self.previousScene

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

