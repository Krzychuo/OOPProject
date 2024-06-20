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

    def move_to(self, pos):
        self.set_position(pos)

class BoardDot(Sprite):
    def __init__(self, pos, active=True):
        super().__init__()
        self._image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self._image, (0, 0, 0), (15, 15), 15)
        self._rect = self._image.get_rect()
        self._active = active
        self.set_position(pos)

class BoardLine(Sprite):
    def __init__(self, x, x2, y, y2, active=True):
        super().__init__()
        if x > x2: x, x2 = x2, x
        if y > y2: y, y2 = y2, y
        self._image = pygame.Surface((x2-x, y2-y))
        pygame.draw.rect(self._image, (0, 0, 0), pygame.Rect(x, y, x2-x, y2-y))
        self._rect = self._image.get_rect()
        self._active = active
        self.set_position(((x+x2)/2, (y+y2)/2))

class Piece(Sprite):
    # ONE PIECE IS REAL
    def __init__(self, pos, color, color2, active=True):
        super().__init__()
        self._image = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.circle(self._image, color, (40, 40), 30)
        pygame.draw.circle(self._image, color2, (40, 40), 15)
        self._rect = self._image.get_rect()
        self._active = active
        self.set_position(pos)

class SelectedDot(Sprite):
    def __init__(self, pos):
        super().__init__()
        self._image = pygame.Surface((14, 14), pygame.SRCALPHA)
        pygame.draw.circle(self._image, (255, 0, 0), (7, 7), 7)
        self._rect = self._image.get_rect()
        self._active = False
        self.set_position(pos)

    def deactivate(self):
        self._active = False
    
    def activate(self):
        self._active = True
