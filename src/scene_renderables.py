from sprites import *

class GameSceneRenderables:
    def __new__(cls, *args, **kwargs):
        ret = []

        def add(obj):
            ret.append(obj)
        
        ret = []

        for offset in [300, 200, 100]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy != 0 or dx != 0:
                        add(BoardDot((400+offset*dy, 400+offset*dx)))

            for mult in [-1, 1]:
                add(BoardLine(400-offset, 400+offset, 405+offset*mult, 395+offset*mult))
                add(BoardLine(405+offset*mult, 395+offset*mult, 400-offset, 400+offset))

        add(BoardLine(100, 300, 395, 405))
        add(BoardLine(500, 700, 395, 405))
        add(BoardLine(395, 405, 100, 300))
        add(BoardLine(395, 405, 500, 700))

        # temp
        add(Piece((200, 400), (255, 255, 255), (205, 205, 205)))
        add(Piece((400, 200), (0, 0, 0), (50, 50, 50)))

        return ret
