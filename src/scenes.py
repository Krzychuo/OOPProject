from sprites import *

class SceneBase:
    def __init__(self):
        self.renderable = []
        self.clickable = []
    
    def process_input(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def update(self):
        print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        print("uh-oh, you didn't override this in the child class")

class TitleScene(SceneBase):
    def __init__(self):
        self.renderable = []
        self.clickable = []     

    def render(self, screen):
        screen.fill((205, 127, 50))

class GameScene(SceneBase):
    def __init__(self):
        self.renderable = []
        self.clickable = []

        self.renderable.append(BoardDot((50, 50)))   
    
    def render(self, screen):
        screen.fill((205, 127, 50))

        for sprite in self.renderable:
            screen.blit(sprite.get_image(), sprite.get_rect())