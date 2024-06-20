import pygame
import sys
from scenes import *

class SceneManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SceneManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        self._screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Nine men's morris")
        self._scenes = {
            "title_scene" : TitleScene(self),
            "game_scene" : GameScene(self)
        }
        self._current_scene = self._scenes["game_scene"]

    def heartbeat(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self._current_scene.process_input(None, None)
        self._current_scene.update()
        self._current_scene.render(self._screen)

        pygame.display.flip()
