board = ["" for i in range(9)]
player = "x"

win_conbinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 2], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

def display_board():
    print(board[0] + " | " + board[1] + "|" + board[2])
    print(board[3] + " | " + board[4] + "|" + board[5])
    print(board[6] + " | " + board[7] + "|" + board[8])




def play_turn():
    while True:
        move = input("where do you want to make a move?")
        if move not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("invalid input!!, try again")
            display_board()
            continue
        elif board[int(move) - 1] != "":
            print("invalid input!!!, try again")
            display_board()
            continue
        else:
            move = int(move) - 1
            board[move] = player
            break




    def change_player():
        global player
        if player == "x":
            plater = " 0"
        else:
            if player == "0":
                player = "x"

def check_win():
    for i, h, r in win_conbinations:
        if board[i] == board[h] == board[r] != "":
            print(player + "wins!")
        else:
            continue

def check_tie():
    global winner
    if "" not in board:
        winner = " "
        print("it's a tie!")

def stop_gone():
    play_again = input("play again? or not? y/n")
    while True:
        if play_again.lower() == "y":
            for i in range(len(board)):
                board[i] = ""
        elif play_again.lower() == "n":
            exit()
        elif play_again not in ("y", "n"):
            print("invalid input")
            continue
    winner = None
    player = "x"


def play_the_game():
   while True:
        display_board()
        play_turn()



play_the_game()