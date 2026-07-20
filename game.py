def create_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board):

    # ردیف‌ها
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]


    # ستون‌ها
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]


    # قطر اصلی
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]


    # قطر فرعی
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]


    # مساوی
    if all(
        board[i][j] != " "
        for i in range(3)
        for j in range(3)
    ):
        return "مساوی"


    return None



def available_moves(board):

    moves = []

    for i in range(3):
        for j in range(3):

            if board[i][j] == " ":
                moves.append((i, j))

    return moves
