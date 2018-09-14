def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return board


board = create_board()


def draw_board():
    for row in reversed(board):
        print(row)
    reversed(board)


def is_valid_location(board, col):
    if board[5][col] != 0:
        print("Die Reihe ist voll!")
    else:
        return True


def get_next_open_row(board, col):
    for row in range(len(board)):
        if board[row][col] == 0:
            return row
            break


def drop_piece(board, row, col):
            board[row][col] = turn + 1


draw_board()
game_over = False
turn = 0


while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 bitte wähle eine Reihe(0-6)"))
        if is_valid_location(board, col):
            drop_piece(board, get_next_open_row(board, col), col)
            draw_board()

    # Ask for Player 2 Input
    if turn == 1:
        col = int(input("Player 1 bitte wähle eine Reihe(0-6)"))
        if is_valid_location(board, col):
            drop_piece(board, get_next_open_row(board, col), col)
            draw_board()

    turn += 1
    turn = turn % 2

