import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
from game_manager import GameManager
from scene_manager import SceneManager

def main():
    pygame.init()

    scene_manager = SceneManager()
    GameManager()
    
    FPS = 60
    fps_clock = pygame.time.Clock()
    running = True

    while running:
        scene_manager.heartbeat(pygame.event.get())
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()