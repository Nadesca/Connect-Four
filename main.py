def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return board


def draw_board():
    for row in board:
        print(row)


def drop_piece(board, col):
    for index in range(1, 8):
        if board[-index][col] == 0:
            board[-index][col] = turn + 1
            break
    draw_board()


def is_valid_location(board, col):
    if board[0][col] != 0:
        print("Die Reihe ist voll!")
    else:
        return True


def get_next_open_row(board, col):
    pass


board = create_board()
draw_board()
game_over = False
turn = 0


while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        selection = int(input("Player 1 bitte wähle eine Reihe aus (0-6)"))
        if is_valid_location(board, selection):
            drop_piece(board, selection)

    # Ask for Player 2 Input
    if turn == 1:
        selection = int(input("Player 2 bitte wähle eine Reihe aus (0-6)"))
        print(selection)
        if is_valid_location(board, selection):
            drop_piece(board, selection)

    turn += 1
    turn = turn % 2


