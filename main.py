from connectBoard import Board
from connectAi import Computer_Player as CompPlayer
    
def intro():
    print("\nWelcome to the connect game!\n")
    print("This is just like the classic board game, two players take turns choosing columns to place coins into until someone gets four in a row.\n\
          Alternatively you can choose to play against a computer opponent in the same fashion.")
    print("\n")
    play = input("Do you want to play? (y/n)\n")
    ai = input("Who do you want to play against? [1...2]\n1. Another player\n2. The computer [Easy]\n3. The computer [Harder]\n")
    return ((play.lower() == 'y'), int(ai))

def game(ai):
    connect_board = Board(6,7)
    computer = CompPlayer(connect_board, 2)
    connect_board.show_board()
    win = False
    player = 1
    while win == False:
        if ai == 1:
            if player == 1 and win == False:
                column = int(input("Player 1, where would you like to place a coin?\n")) - 1
                while connect_board.check_full(column) == True:
                    column = int(input("This column is full. Please choose another one.\n")) - 1
                win = connect_board.place_coin(column, player)
                print("\n")
                connect_board.show_board()
                print("\n")
                if win == False:
                    player = 2
            if player == 2 and win == False:
                column = int(input("Player 2, where would you like to place a coin?\n")) - 1
                while connect_board.check_full(column) == True:
                    column = int(input("This column is full. Please choose another one.\n")) - 1
                win = connect_board.place_coin(column, player)
                print("\n")
                connect_board.show_board()
                print("\n")
                if win == False:
                    player = 1
        else:
            if player == 1 and win == False:
                column = int(input("Player 1, where would you like to place a coin?\n")) - 1
                while connect_board.check_full(column) == True:
                    column = int(input("This column is full. Please choose another one.\n")) - 1
                win = connect_board.place_coin(column, player)
                print("\n")
                connect_board.show_board()
                print("\n")
                if win == False:
                    player = 2
            if player == 2 and win == False:
                if ai == 2:
                    win = computer.play_greedy()
                else:
                    win = computer.play_minmax()
                print("\n")
                connect_board.show_board()
                print("\n")
                if win == False:
                    player = 1
            
    print(f"\nCongratulations Player{player}, you won!\n\n" )
    connect_board.show_board()
    

def main():
    start = intro()
    while start[0] == False:
        start = intro()
    game(start[1])
    exit()

main()


