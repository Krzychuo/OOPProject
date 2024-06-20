from animation import Animation
from observer import Observer

class AnimationManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AnimationManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        self.__animations_playing = 0
        self.__observer = Observer()
        self.__observer.subscribe("animation_played", self.add_animation)
        self.__observer.subscribe("animation_finished", self.sub_animation)
        self.__animation_list = []

    def add_animation(self):
        self.__animations_playing += 1

    def sub_animation(self):
        self.__animations_playing -= 1
        if self.__animations_playing == 0:
            self.__observer.notify("all_animations_finished")

    def heartbeat(self):
        new_animation_list = []
        for animation in self.__animation_list:
            if animation.heartbeat():
                new_animation_list.append(animation)
        self.__animation_list = new_animation_list

    def create_animation(self, obj, attr, begin, end, len):
        anim = Animation(obj, attr, begin, end, len)
        self.__animation_list.append(anim)
        return anim
