import pygame
from scene_manager import SceneManager

class GameManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls, *args, **kwargs) 
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        self.scene_manager = SceneManager()
    
    def heartbeat(self):
        pass
        
        

# if __name__ == "__main__":
#     gamemanager1 = GameManager()
#     gamemanager2 = GameManager()
#     print(gamemanager1 is gamemanager2)
