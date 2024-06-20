from sprites import *
from scene_renderables import *

class SceneBase:
    def __init__(self, manager):
        self._renderable = []
        self._clickable = []
        self._scene_manager = manager
    
    def process_input(self, events, pressed_keys):
        pass #print("uh-oh, you didn't override this in the child class")

    def update(self):
        pass #print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        pass #print("uh-oh, you didn't override this in the child class")
    
    def change_scene(self, scene_name):
        self._scene_manager._current_scene = self._scene_manager._scenes[scene_name]

class TitleScene(SceneBase):
    def __init__(self, manager):
        self._renderable = []
        self._clickable = []
        self._scene_manager = manager

    def render(self, screen):
        screen.fill((205, 127, 50))

class GameScene(SceneBase):
    def __init__(self, manager):
        self._renderable = GameSceneRenderables()
        self._clickable = []
        self._scene_manager = manager
    
    def render(self, screen):
        screen.fill((205, 127, 50))

        for sprite in self._renderable:
            if sprite.is_active():
                screen.blit(sprite.get_image(), sprite.get_rect())