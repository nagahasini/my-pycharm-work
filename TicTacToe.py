
game_board=["   " for i in range(9)]
def print_board():
        row1 = "|{:^3}|{:^3}|{:^3}|".format(game_board[0], game_board[1], game_board[2])
        row2 = "|{:^3}|{:^3}|{:^3}|".format(game_board[3], game_board[4], game_board[5])
        row3 = "|{:^3}|{:^3}|{:^3}|".format(game_board[6], game_board[7], game_board[8])
        print()
        print(row1)
        print(row2)
        print(row3)
        print()


def game(label):
    print("your turn {}".format(label))
    choices=int(input("choose the box u take(0-9): "))
    if game_board[choices-1]=="   ":
     game_board[choices-1]=label
    else:
        print("place taken")


def check_victory(label):
    # Check rows
    if (game_board[0] == game_board[1] == game_board[2] == label or  # Top row
            game_board[3] == game_board[4] == game_board[5] == label or  # Middle row
            game_board[6] == game_board[7] == game_board[8] == label):  # Bottom row
        return True

    # Check columns
    if (game_board[0] == game_board[3] == game_board[6] == label or  # Left column
            game_board[1] == game_board[4] == game_board[7] == label or  # Middle column
            game_board[2] == game_board[5] == game_board[8] == label):  # Right column
        return True

    # Check diagonals
    if (game_board[0] == game_board[4] == game_board[8] == label or  # Diagonal from top-left to bottom-right
            game_board[2] == game_board[4] == game_board[6] == label):  # Diagonal from top-right to bottom-left
        return True

    return False


while True:
    print_board()
    game('X')
    print_board()
    if check_victory('X'):
        print('X won')
        break
    game('O')
    if check_victory('O'):
        print('O won')
        break


