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
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Nine men's morris")
        self.scenes = {
            "title_scene" : TitleScene(),
            "game_scene" : GameScene()
        }
        self.current_scene = self.scenes["game_scene"]

    def heartbeat(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.current_scene.process_input(None, None)
        self.current_scene.update()
        self.current_scene.render(self.screen)

        pygame.display.flip()
