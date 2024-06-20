from time import time
from observer import Observer

class Animation:
    def __init__(self, obj, attr, begin, end, len):
        self.__obj = obj
        self.__attr = attr
        self.__begin = begin
        self.__end = end
        self.__observer = Observer()
        self.__len = len
        self.__playing = False

    def play(self):
        self.__observer.notify("animation_played")
        self.__playing = True
        self.__start_t = time()

    def heartbeat(self):
        if self.__playing:
            tim = time()
            if tim - self.__start_t >= self.__len:
                setattr(self.__obj, self.__attr, self.__end)
                self.__observer.notify("animation_finished")
                return False
            t = (tim - self.__start_t) / self.__len
            attr = getattr(self.__obj, self.__attr)
            if isinstance(attr, tuple) and len(attr) == 2:
                tup = (self.__begin[0] + (self.__end[0]-self.__begin[0]) * (1-(1-t)**3),
                       self.__begin[1] + (self.__end[1]-self.__begin[1]) * (1-(1-t)**3))
                setattr(self.__obj, self.__attr, tup)
            else:
                try:
                    setattr(self.__obj, self.__attr, self.__begin - (self.__end-self.__begin) * (1-(1-t)**3))
                except Exception as e:
                    raise e
            return True
        return True