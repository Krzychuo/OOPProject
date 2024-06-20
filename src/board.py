class Board():
    def __init__(self):
        self.__board = [[0 for _ in range(8)] for _ in range(3)]

    def get_board(self):
        return self.__board
    
    def get_piece(self, board_pos):
        return self.__board[board_pos//8][board_pos%8]
    
    def is_clear(self, board_pos):
        return self.sgn(self.get_piece(board_pos)) == 0
    
    def sgn(self, x):
        if x > 0: return 1
        if x < 0: return -1
        return 0

    def is_me(self, board_pos, col):
        return self.sgn(self.get_piece(board_pos)) == col
    
    def is_enemy(self, board_pos, col):
        return self.is_me(board_pos, -col)
    
    def place(self, board_pos, idx):
        self.__board[board_pos//8][board_pos%8] = idx

    def remove(self, board_pos):
        self.__board[board_pos//8][board_pos%8] = 0

    def is_valid_move(self, board_pos, board_pos2):
        r = board_pos%8
        r2 = board_pos2%8
        if r == r2:
            return abs(board_pos//8-board_pos2//8) == 1
        elif abs(r-r2) == 1 or abs(r-r2) == 7:
            return abs(board_pos//8-board_pos2//8) == 0
        else:
            return False 

    def move(self, board_pos, board_pos2):
        self.place(board_pos2, self.get_piece(board_pos))
        self.remove(board_pos)
    
    def check_mill(self, board_pos):
        for i in range(0, 26, 2):
            
                if i%8 == 6:
                    if board_pos == i or board_pos == i+1 or board_pos == i-6:
                        if self.sgn(self.get_piece(i)) == self.sgn(self.get_piece(i+1)) == self.sgn(self.get_piece(i-6)):
                            return True
                else:
                    if i <= board_pos <= i+2:
                        if self.sgn(self.get_piece(i)) == self.sgn(self.get_piece(i+1)) == self.sgn(self.get_piece(i+2)):
                            return True
                
        if board_pos%2 == 1:
            r = board_pos%8
            if self.sgn(self.get_piece(r)) == self.sgn(self.get_piece(r+8)) == self.sgn(self.get_piece(r+16)):
                return True
            
        return False