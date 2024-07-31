import math
#from main import Board

class Computer_Player:



    DEPTH_LIMIT = 12
    column_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':1}

    def __init__(self, game_board, difficulty, player):
        self.game_board = game_board
        self.difficulty = difficulty
        self.player = player
        self.columns = [i for i in range(1, game_board.rows+1)]

    def find_next_move(self, game_board):
        """Use some dynamic progamming algorithm to choose the best move"""
        if self.difficulty == "easy":
            self.greedy_move(self.game_board)
        else:
            self.computer_play()
    
    def greedy_move(self, game_board):
        """Use greedy algorithm"""
        


    def find_move(self, column, player, depth, score, game_board_copy):
        if depth <= self.DEPTH_LIMIT:
            print(column)
            if game_board_copy.place_coin(column, player) == True:
                return (4, column)
            else:
                next = max(([self.computer_play(i, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())] for i in range(1,8)))
                return (score + next[0], column)
        else:
            return
        
    def computer_play(self):
        next_move = self.find_move((i for i in self.columns), self.player, 0, 0, self.game_board.copy())
        win = self.game_board.place_coin(next_move[1], self.player)
        return win


