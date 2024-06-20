from sprites import *
from scene_sprites import *
from observer import Observer
from threading import Thread
from time import sleep

class SceneBase:
    def __init__(self, manager):
        self._renderables = []
        self._clickables = []
        self._scene_manager = manager
    
    def process_input(self, events):
        pass #print("uh-oh, you didn't override this in the child class")

    def update(self):
        pass #print("uh-oh, you didn't override this in the child class")

    def render(self, screen):
        pass #print("uh-oh, you didn't override this in the child class")
    
    def change_scene(self, scene_name):
        self._scene_manager._current_scene = self._scene_manager._scenes[scene_name]

class TitleScene(SceneBase):
    def __init__(self, manager):
        self._renderables = []
        self._clickables = []
        self._scene_manager = manager

    def render(self, screen):
        screen.fill((205, 127, 50))

class GameScene(SceneBase):
    def __init__(self, manager):
        self._renderables = GameSceneRenderables()
        self._clickables = GameSceneClickables()
        self._scene_manager = manager
        self.__observer = Observer()
        self.__observer.subscribe("move_piece", self.move_piece)
        self.__observer.subscribe("remove_piece", self.remove_piece)
        self.__observer.subscribe("win_animation", self.win_animation)
        self.__observer.subscribe("mark_pieces", self.mark_pieces)
        self.__observer.subscribe("unmark_pieces", self.unmark_pieces)

    def process_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for clickable in self._clickables:
                    if clickable.check_click(event.pos):
                        clickable.on_click_event()
    
    def render(self, screen):
        screen.fill((205, 127, 50))

        for layer in self._renderables:
            for sprite in layer:
                if sprite.is_active() and sprite.get_image():
                    screen.blit(sprite.get_image(), sprite.get_rect())

    def get_dot_pos(self, board_pos):
        return self._renderables[1][board_pos].get_rect().center

    def move_piece(self, piece_idx, board_pos):
        idx = 2 if piece_idx > 0 else 3
        piece_idx = abs(piece_idx) - 1
        self._renderables[idx][piece_idx].move_to(self.get_dot_pos(board_pos))

    def remove_piece(self, removed_idx, piece_idx):
        idx = 2 if piece_idx > 0 else 3
        piece_idx = abs(piece_idx) - 1
        if idx == 2:
            self._renderables[idx][piece_idx].move_to((800-100*removed_idx, 100))
        else:
            self._renderables[idx][piece_idx].move_to((200+100*removed_idx, 900))

    def win_animation(self):
        t = Thread(target=self._win_animation_thread)
        t.start()

    def _win_animation_thread(self):
        sleep(2)
        for i in range(0, 9):
            self._renderables[2][i].reset()
            self._renderables[3][i].reset()

    def mark_pieces(self, pos_list):
        for pos in pos_list:
            self._renderables[4][pos].activate()

    def unmark_pieces(self):
        for sprite in self._renderables[4]:
            sprite.deactivate()
