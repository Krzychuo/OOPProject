import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._image = None
        self._rect = None
        self._active = False

    def get_image(self):
        return self._image

    def get_rect(self):
        return self._rect
    
    def is_active(self):
        return self._active
    
    def set_position(self, pos):
        self._rect.center = pos