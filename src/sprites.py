import pygame
from sprite import Sprite

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
