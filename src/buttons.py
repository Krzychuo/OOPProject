from sprites import Sprite
from observer import Observer

class Button(Sprite):
    def __init__(self):
        super().__init__()
        self._hover = False

    def check_click(self, pos):
        pass

    def on_click_event(self):
        pass

class BoardButton(Button):
    def __init__(self, pos, rad, id):
        super().__init__()
        self._active = True
        self._pos = pos
        self._rad = rad
        self._id = id
        self.__observer = Observer()

    def check_click(self, pos):
        return (pos[0]-self._pos[0])**2 + (pos[1]-self._pos[1])**2 <= self._rad**2
    
    def on_click_event(self):
        #print(self._id)
        self.__observer.notify("click_position", board_pos=self._id)

    def on_hover_event(self):
        pass