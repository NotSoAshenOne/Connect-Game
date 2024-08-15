import math
#from main import Board

class Computer_Player:



    DEPTH_LIMIT = 6
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
    
    # def greedy_move(self, game_board):
    #     """Use greedy algorithm"""
        


    # def find_move(self, column, player, depth, score, game_board_copy):
    #     if depth <= self.DEPTH_LIMIT:
    #         if game_board_copy.place_coin(column, player) == True:
    #         #if game_board_copy.check_win()
    #             if player == self.player:
    #                 return (-(score+1), column)
    #             else:
    #                 return (-(score+1), column)
    #         else:
    #             next = min((self.find_move(0, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())), (self.find_move(1, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())),
    #                        (self.find_move(2, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())), (self.find_move(3, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())),
    #                        (self.find_move(4, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())), (self.find_move(5, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())),
    #                        (self.find_move(6, (player+1)%2 + 1, depth +1, score+1, game_board_copy.copy())))
    #             return (score + next[0], column)
    #     else:
    #         return (0, column)
        
    # def computer_play(self):
    #     next_move = min((self.find_move(0, self.player, 0, 0, self.game_board.copy())),(self.find_move(1, self.player, 0, 0, self.game_board.copy())),(self.find_move(2, self.player, 0, 0, self.game_board.copy())),
    #                     (self.find_move(3, self.player, 0, 0, self.game_board.copy())),(self.find_move(4, self.player, 0, 0, self.game_board.copy())),(self.find_move(5, self.player, 0, 0, self.game_board.copy())),
    #                     (self.find_move(6, self.player, 0, 0, self.game_board.copy())))
    #     print(next_move)
    #     win = self.game_board.place_coin(next_move[1], self.player)
    #     return win

    def negamax(self, game_board, player, depth):

        if depth < self.DEPTH_LIMIT:
            if game_board.getNumMoves() == game_board.columns * game_board.rows:
                return (0, -1)

            for x in range(0,game_board.columns):
                row = game_board.next_row(x)
                if game_board.check_full(x) == False and game_board.check_win(row, x, player) == True:
                    return ((game_board.columns * game_board.rows) - (game_board.getNumMoves()/2), x)
                
            best_score = -game_board.columns+game_board.rows
            best_column = -1

            for x in range(0,game_board.columns):
                print(x)
                if game_board.check_full(x) == False:
                    game_board_copy = game_board.copy()
                    print("copy ", x," ", game_board_copy)
                    game_board_copy.place_coin(x, player)
                    score = -((self.negamax(game_board_copy, (player%2)+1, depth+1))[0])
                    if score > best_score:
                        best_score = score
                        best_column = x

            return (best_score, best_column)
        else:
            score = 0
            for x in range(0,game_board.columns):
                row = game_board.next_row(x)
                if game_board.check_full(x) == False and game_board.check_win(row, x, player) == True:
                    return ((game_board.columns * game_board.rows) - (game_board.getNumMoves()/2), x)
                if game_board.check_full(x) == False and x in [2,3,4]:
                    score = game_board.columns
            return (score,0) 
                    
    
    def play(self):
        
        column = self.negamax(self.game_board, self.player, 0)[1]
        print(column)
        win = self.game_board.place_coin(column, self.player)
        return win
     

        



