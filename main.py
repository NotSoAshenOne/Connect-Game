import numpy as np
import math

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.connect_board = np.zeros((self.rows,self.columns))
    
    def show_board(self):
        print(self.connect_board)

    
    def check_full(self, column):
        return self.connect_board[0][column] != 0
    
    def place_coin(self, column, player):
        i = self.rows
        while self.connect_board[i][column] != 0:
            i += -1
        self.connect_board[i][column] = player
        return self.check_win(i, column, player)

    def check_vertical(self, row, column, player):
        if row != self.rows - 1:
            i = row + 1
            connected_up = 0
            while i < self.rows and self.connect_board[i][column] == player:
                connected_up += 1
                i += 1
        if row != 0:
            i = row - 1
            connected_down = 0
            while i >= 0 and self.connect_board[i][column] == player:
                connected_down += 1
                i += -1
        connected_vertical = 1 + connected_up + connected_down
        return connected_vertical
    
    def check_horizontal(self, row, column, player):
        if column != 0:
            i = column - 1
            connected_left = 0
            while i >= 0 and self.connect_board[row][i] == player:
                connected_left += 1
                i += -1
        if column != self.columns - 1:
            i = column + 1
            connected_right = 0
            while i < self.columns and self.connect_board[row][i] == player:
                connected_right += 1
                i += 1
        connected_horizontal = 1 + connected_left + connected_right
        return connected_horizontal
    
    def check_u_diagonal(self, row, column, player):
        if column != self.columns - 1 and row != self.rows:
            i = row + 1
            j = column + 1
            connected_right = 0
            while i < self.rows and j < self.columns and self.connect_board[i][j] == player:
                connected_right += 1
                i += 1
                j += 1
        if column != 0 and row != 0:
            i = row - 1
            j = column - 1
            connected_left = 0
            while i >= 0 and j >= 0 and self.connect_board[i][j] == player:
                connected_left += 1
                i += -1
                j += -1
        connected_u_diagonal = 1 + connected_left + connected_right
        return connected_u_diagonal
    
    def check_d_diagonal(self, row, column, player):
        if column != self.columns - 1 and row != 0:
            i = row - 1
            j = column + 1
            connected_right = 0
            while i >= self.rows and j < self.columns and self.connect_board[i][j] == player:
                connected_right += 1
                i += -1
                j += 1
        if column != 0 and row != self.rows - 1:
            i = row + 1
            j = column - 1
            connected_left = 0
            while i < self.rows and j >= 0 and self.connect_board[i][j] == player:
                connected_left += 1
                i += 1
                j += -1
        connected_d_diagonal = 1 + connected_left + connected_right
        return connected_d_diagonal

    def check_win(self, row, column, player):
        if self.check_d_diagonal(row, column, player) >= 4 or self.check_u_diagonal(row, column, player) >= 4 or self.check_horizontal(row, column, player) >= 4 or self.check_vertical(row, column, player) >= 4:
            return True
        else:
            return False
    
def intro():
    print("Welcome to the connect game!")
    print("\n")
    play = input("Do you want to play? (y/n)")
    return play.lower() == 'y'

def game():
    connect_board = Board(6,7)
    win = False
    while win == False:
        connect_board.show_board()
        column = str(input("Player 1, where would you like to place a coin?")) - 1
        if connect_board.check_full(column) == True:
            

def main():
    while intro() == False:
        intro()
    game()

main()





    
