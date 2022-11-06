
#W01
#Everth Urrutia


def main():
    selection = []
    play = player("")
    new_board = board()

    while not (check_winner(new_board) or draw_board(new_board)):
        display(new_board)
        move_player(play, new_board, selection)
        play = player(play)
    display(new_board)
    print("\nGood game. Thanks  for playing!")


def board():
    new_board = []
    for position in range(9):
        new_board.append(position + 1)
    return new_board


def display(board):
    print("\n %s | %s | %s" % (board[0], board[1], board[2]))
    print(' - + - + - ')
    print(" %s | %s | %s" % (board[3], board[4], board[5]))
    print(' - + - + - ')
    print(" %s | %s | %s" % (board[6], board[7], board[8]))



def draw_board(board):
    for position in range(9):
        if board[position] != "x" and board[position] != "o":
            return False
    return True


def move_player(player, board, selection):
    position = int(input(f"\n{player}'s turn to choose a square (1-9): "))
    if ((position in selection) == True) or (position < 1 or position > 9):
        print("You select and invalid option please select a valid option")
        
    else :
        selection.append(position)
        board[position - 1] = player
        



def player(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"


def check_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[2] == board[4] == board[6] or
            board[0] == board[4] == board[8])


main()
