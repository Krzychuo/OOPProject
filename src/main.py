import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from game_manager import GameManager
from scene_manager import SceneManager

def main():
    pygame.init()

    scene_manager = SceneManager()
    game_manager = GameManager()
    
    FPS = 60
    fps_clock = pygame.time.Clock()
    running = True

    while running:
        game_manager.heartbeat()
        scene_manager.heartbeat(pygame.event.get())

        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()