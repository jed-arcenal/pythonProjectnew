def print_board(board):
    for row in board:
        for element in row:
            print(element, end=" ")
        print()


def initialize_board():
    rows, cols = 3, 3
    return [["-" for j in range(cols)]
            for i in range(rows)]


def check_if_winner(board, chip_type):
    rows, cols = 3, 3
    for i in range(rows):
        if board[i][0] == board[i][1] == board[i][2] == chip_type:
            return True
    for j in range(cols):
        if board[0][j] == board[1][j] == board[2][j] == chip_type:
            return True
    if board[0][0] == board[1][1] == board[2][2] == chip_type:
        return True
    if board[0][2] == board[1][1] == board[2][0] == chip_type:
        return True

    return False


def board_is_full(board):
    for row in board:
        for element in row:
            if element == "-":
                return False
    return True


def available_square(board, row, col):
    return board[row][col] == "-"


def mark_square(board, row, col, chip_type):
    board[row][col] == chip_type
    return  board[row][col] == chip_type


if __name__ == "__main__":
    board = initialize_board()
    print("Player 1: x\nPlayer 2: o\n")
    print_board(board)

    player = 1
    chip = "x"
    while True:
        print(f"Player {player}'s Turn({chip}): ")
        row = int(input("Enter a row number (0, 1, or 2): "))
        col = int(input("Enter a column number (0, 1, or 2): "))

        mark_square(board, row, col, chip)

        print_board(board)

        player = 2 if player == 1 else 1
        chip = "o" if chip == "x" else "x"




