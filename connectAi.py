import math
from main import Board

class Computer_Player:
    def __init__(self, game_board, difficulty):
        self.game_board = game_board
        self.difficulty = difficulty

    def find_next_move(self, game_board):
        """Use some dynamic progamming algorithm to choose the best move"""
        if self.difficulty == "easy":
            self.greedy_move(self.game_board)
        else:
            self.minimax_move(self.game_board)
    
    def greedy_move(self, game_board):
        """Use greedy algorithm"""
        


    def minimax_move(self, game_board):
        """Use minimax algorithm"""