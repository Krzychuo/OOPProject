import pygame

class BoardDot(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.__image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.__image, (0, 0, 0), (30, 30), 30)
        self.__rect = self.__image.get_rect()
        if pos:
            self.set_position(pos)
    
    def set_position(self, pos):
        self.__rect.center = pos

    def get_image(self):
        return self.__image

    def get_rect(self):
        return self.__rect