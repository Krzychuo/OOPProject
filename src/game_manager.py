from observer import Observer
from board import Board
from player import Player
import time

class GameManager:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls, *args, **kwargs) 
            cls._instance._init()
        return cls._instance
    
    def _init(self):
        self.reset_game()
        self.__observer = Observer()
        self.__observer.subscribe("click_position", self.click_position)
        self.__observer.subscribe("all_animations_finished", self.unlock)
        self.__observer.subscribe("animation_played", self.lock)
        self.__lock = False

    def reset_game(self):
        self._player1 = Player(1)
        self._player2 = Player(-1)
        self._board = Board()
        self._selected_piece = None
        self._white_pieces = 0
        self._black_pieces = 0
        self._white_reserve = 9
        self._black_reserve = 9
        self._current_player = self._player1
        self._state = 0
    
    def get_player_color(self):
        return self._current_player.get_color()
    
    def get_reserve(self):
        if self._current_player is self._player1:
            return self._white_reserve
        return self._black_reserve
    
    def get_pieces(self):
        if self._current_player is self._player1:
            return self._white_pieces
        return self._black_pieces
    
    def shrink_reserve(self):
        if self._current_player is self._player1:
            self._white_reserve -= 1
        else:
            self._black_reserve -= 1
    
    def switch_player(self):
        if self._current_player is self._player1:
            self._current_player = self._player2
        else:
            self._current_player = self._player1

    def add_piece(self):
        if self._current_player is self._player1:
            self._white_pieces += 1
        else:
            self._black_pieces += 1

    def remove_piece(self):
        if self._current_player is self._player1:
            self._white_pieces -= 1
        else:
            self._black_pieces -= 1

    def unlock(self):
        self.__lock = False

    def lock(self):
        self.__lock = True

    def click_position(self, board_pos):
        if self.__lock: return
        if self._state == 0:
            if self.get_reserve() > 0:
                if self._board.is_clear(board_pos):
                    self.__observer.notify("move_piece", 
                                           piece_idx=self.get_reserve() * self.get_player_color(), 
                                           board_pos=board_pos)
                    self._board.place(board_pos, self.get_reserve() * self.get_player_color())
                    self.shrink_reserve()
                    self.add_piece()
                    if self._board.check_mill(board_pos):
                        self._state = 1
                    else:
                        self.switch_player()
            else:
                if self._board.is_clear(board_pos):
                    if self._selected_piece != None and \
                        (self._board.is_valid_move(self._selected_piece, board_pos) or self.get_pieces() <= 3):
                        self.__observer.notify("move_piece", 
                                               piece_idx=self._board.get_piece(self._selected_piece), 
                                               board_pos=board_pos)
                        self._board.move(self._selected_piece, board_pos)
                        if self._board.check_mill(board_pos):
                            self._state = 1
                        else:
                            self.switch_player()
                    self._selected_piece = None
                elif self._board.is_enemy(board_pos, self.get_player_color()):
                    self._selected_piece = None
                else:
                    if self._selected_piece == board_pos:
                        self._selected_piece = None
                    else:
                        self._selected_piece = board_pos
        else:
            if self._board.is_enemy(board_pos, self.get_player_color()):
                self.switch_player()
                self.__observer.notify("remove_piece", 
                                       removed_idx=9-self.get_reserve()-self.get_pieces(),
                                       piece_idx=self._board.get_piece(board_pos))
                self.remove_piece()
                self._board.remove(board_pos)
                self._state = 0
                if self.get_pieces() == 2 and self.get_reserve() == 0:
                    self.__observer.notify("win_animation")
                    self.__lock = True
                    self.reset_game()
                    
        self.__observer.notify("update_selected", board_pos=self._selected_piece)
