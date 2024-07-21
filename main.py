import numpy as np
import math

def intro():
    print("Welcome to the connect game!")
    print("\n")
    play = input("Do you want to play? (y/n)")
    return play.lower() == 'y'

class board:
    def init_board(self):
        self.connect_board = np.zeros((6,7))
    
    def check_full(self, column):
        return self.connect_board[0][column] != 0
    




    
