import math
import random

class Computer_Player:

    DEPTH_LIMIT = 6

    def __init__(self, game_board, difficulty, player):
        self.game_board = game_board
        self.difficulty = difficulty
        self.player = player
        self.columns = [i for i in range(1, game_board.rows+1)]

    def greedy(self, game_board, player):
        """Finds the next move by using the greedy algorithm"""
        best_connections = 0
        best_column = []

        for x in range(0, game_board.columns):
            row = game_board.next_row(x)
            connections = max(game_board.check_vertical(row, x, player), game_board.check_horizontal(row, x, player), game_board.check_u_diagonal(row, x, player), game_board.check_d_diagonal(row, x, player))
            if connections >= best_connections:
                if connections == best_connections:
                    best_column.append(x)
                if connections > best_connections:
                    best_column = [x]
        return random.choice(best_column)

    def negamax(self, game_board, player, depth):
        """Determines the next move by using the recursive minmax algorithm"""
        if depth < self.DEPTH_LIMIT:
            if game_board.getNumMoves() == game_board.columns * game_board.rows:    #Checks if the table is filled.
                return (0, -1)

            for x in range(0,game_board.columns):   # Checks if the player can win in the next move.
                row = game_board.next_row(x)
                if game_board.check_full(x) == False and game_board.check_win(row, x, player) == True:
                    return ((game_board.columns * game_board.rows) - (game_board.getNumMoves()/2), x)
                
            best_score = -game_board.columns+game_board.rows
            best_column = -1

            for x in range(0,game_board.columns):   # Recursively checks the next possible moves, giving higher scores to those that cause the player to win.
                if game_board.check_full(x) == False:
                    game_board_copy = game_board.copy()
                    game_board_copy.place_coin(x, player)
                    score = -((self.negamax(game_board_copy, (player%2)+1, depth+1))[0])
                    if score > best_score:
                        best_score = score
                        best_column = x
            return (best_score, best_column)
        else:
            # In the case that the depth limit is reached, checks if any moves can win otherwise gives a score based on the column
            # with the middle 3 having a higher score than the outside 4.
            score = 0
            for x in range(0,game_board.columns):
                row = game_board.next_row(x)
                if game_board.check_full(x) == False and game_board.check_win(row, x, player) == True:
                    return ((game_board.columns * game_board.rows) - (game_board.getNumMoves()/2), x)
                if game_board.check_full(x) == False and x in [2,3,4]:
                    score = game_board.columns
            return (score,0) 
                    
    def play_minmax(self):
        column = self.negamax(self.game_board, self.player, 0)[1]
        win = self.game_board.place_coin(column, self.player)
        return win
    
    def play_greedy(self):
        column = self.negamax(self.game_board, self.player, 0)[1]
        win = self.game_board.place_coin(column, self.player)
        return win
     

        



