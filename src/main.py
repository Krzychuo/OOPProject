import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_CENTERED'] = '1'
import pygame
from game_manager import GameManager
from scene_manager import SceneManager
from animation_manager import AnimationManager

def main():
    pygame.init()

    animation_manager = AnimationManager()
    scene_manager = SceneManager()
    GameManager()
    
    FPS = 180
    fps_clock = pygame.time.Clock()
    running = True

    while running:
        animation_manager.heartbeat()
        scene_manager.heartbeat(pygame.event.get())
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()