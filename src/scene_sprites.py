from sprites import *
from buttons import *

class GameSceneRenderables:
    def __new__(cls, *args, **kwargs):
        ret = []

        def new_layer():
            ret.append([])

        def add(obj):
            ret[-1].append(obj)

        new_layer()

        for offset in [300, 200, 100]:
            for delta in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                    add(BoardDot((500+offset*delta[0], 500+offset*delta[1])))

        for offset in [300, 200, 100]:
            for mult in [-1, 1]:
                add(BoardLine(500-offset, 500+offset, 505+offset*mult, 495+offset*mult))
                add(BoardLine(505+offset*mult, 495+offset*mult, 500-offset, 500+offset))

        add(BoardLine(200, 400, 495, 505))
        add(BoardLine(600, 800, 495, 505))
        add(BoardLine(495, 505, 200, 400))
        add(BoardLine(495, 505, 600, 800))

        new_layer()

        for y in range(100, 1000, 100):
            add(Piece((100, y), (255, 255, 255), (205, 205, 205)))

        new_layer()

        for y in range(900, 0, -100):
            add(Piece((900, y), (0, 0, 0), (50, 50, 50)))

        new_layer()

        for offset in [300, 200, 100]:
            for delta in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                add(SelectedDot((500+offset*delta[0], 500+offset*delta[1])))

        return ret
    
class GameSceneClickables:
    def __new__(cls, *args, **kwargs):
        ret = []

        def add(obj):
            ret.append(obj)

        cnt = 0
        for offset in [300, 200, 100]:
            for delta in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                add(BoardButton((500+offset*delta[0], 500+offset*delta[1]), 30, cnt))
                cnt += 1

        return ret
