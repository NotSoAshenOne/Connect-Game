import numpy as np

class Board:
    """Class that defines the board.
        Contains the functionality for placing coins and checking win conditions"""
    
    def __init__(self, rows=6, columns=7, other_board = 's', numMoves=0,):
        self.rows = rows
        self.columns = columns
        self.numMoves = 0;
        if type(other_board) == str:
            self.connect_board = np.zeros((self.rows,self.columns))
        else:
            self.connect_board = other_board
        

    
    def show_board(self):
        """Prints a viewable version of the game board"""
        print(self.connect_board)

    
    def check_full(self, column):
        """Returns True if the 0 row is not 0 i.e. the column is full"""
        return self.connect_board[0][column] != 0
    
    def next_row(self, column):
        """Finds the next available row"""
        i = 0
        while i < self.rows and self.connect_board[i][column] == 0:
            i += 1
        return i - 1

    
    def place_coin(self, column, player):
        # i = self.rows - 1
        # while self.connect_board[i][column] != 0:
        #     i += -1
        # self.connect_board[i-1][column] = player
        i = 0
        while i < self.rows and self.connect_board[i][column] == 0:
            i += 1
        self.connect_board[i-1, column] = player
        self.setNumMoves()
        return self.check_win(i-1, column, player)

    def check_vertical(self, row, column, player):
        """Checks if there is a vertical 4 in a row, 
            Checks the total number of continuous coins vertical"""
        connected_up = 0
        connected_down = 0
        if row != self.rows - 1:
            i = row + 1
            while i < self.rows and self.connect_board[i][column] == player:
                connected_up += 1
                i += 1
        if row != 0:
            i = row - 1
            while i >= 0 and self.connect_board[i][column] == player:
                connected_down += 1
                i += -1
        connected_vertical = 1 + connected_up + connected_down
        return connected_vertical
    
    def check_horizontal(self, row, column, player):
        """Checks if there is a horizontal 4 in a row, 
            Checks the total number of continuous coins horizontal"""
        connected_left = 0
        connected_right = 0
        if column != 0:
            i = column - 1
            while i >= 0 and self.connect_board[row][i] == player:
                connected_left += 1
                i += -1
        if column != self.columns - 1:
            i = column + 1
            while i < self.columns and self.connect_board[row][i] == player:
                connected_right += 1
                i += 1
        connected_horizontal = 1 + connected_left + connected_right
        return connected_horizontal
    
    def check_u_diagonal(self, row, column, player):
        """Checks if there is a diagonal 4 in a row, 
            Checks the total number of continuous coins diagonal going up L -> R"""
        connected_right = 0
        connected_left = 0
        if column != self.columns - 1 and row != self.rows:
            i = row + 1
            j = column + 1
            while i < self.rows and j < self.columns and self.connect_board[i][j] == player:
                connected_right += 1
                i += 1
                j += 1
        if column != 0 and row != 0:
            i = row - 1
            j = column - 1
            while i >= 0 and j >= 0 and self.connect_board[i][j] == player:
                connected_left += 1
                i += -1
                j += -1
        connected_u_diagonal = 1 + connected_left + connected_right
        return connected_u_diagonal
    
    def check_d_diagonal(self, row, column, player):
        """Checks if there is a diagonal 4 in a row, 
            Checks the total number of continuous coins diagonal going down L -> R"""
        connected_right = 0
        connected_left = 0
        if column != self.columns - 1 and row != 0:
            i = row - 1
            j = column + 1
            while i >= self.rows and j < self.columns and self.connect_board[i][j] == player:
                connected_right += 1
                i += -1
                j += 1
        if column != 0 and row != self.rows - 1:
            i = row + 1
            j = column - 1
            while i < self.rows and j >= 0 and self.connect_board[i][j] == player:
                connected_left += 1
                i += 1
                j += -1
        connected_d_diagonal = 1 + connected_left + connected_right
        return connected_d_diagonal

    def check_win(self, row, column, player):
        """Checks if any of the diagonals contain a connect 4"""
        if self.check_d_diagonal(row, column, player) >= 4 or self.check_u_diagonal(row, column, player) >= 4 or self.check_horizontal(row, column, player) >= 4 or self.check_vertical(row, column, player) >= 4:
            return True
        else:
            return False
    
    def copy(self):
        return Board(self.rows, self.columns, np.copy(self.connect_board), self.numMoves)
    
    def getNumMoves(self):
        return self.numMoves
    def setNumMoves(self):
        self.numMoves += 1
    