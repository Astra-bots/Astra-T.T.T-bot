from game import available_moves, check_winner


AI_PLAYER = "⭕"
HUMAN_PLAYER = "❌"


def bot_move(board):

    best_score = -float("inf")
    best_move = None

    for row, col in available_moves(board):

        board[row][col] = AI_PLAYER

        score = minimax(
            board,
            0,
            False
        )

        board[row][col] = " "

        if score > best_score:
            best_score = score
            best_move = (row, col)


    if best_move:
        row, col = best_move
        board[row][col] = AI_PLAYER



def minimax(board, depth, is_maximizing):

    result = check_winner(board)


    if result == AI_PLAYER:
        return 10 - depth

    if result == HUMAN_PLAYER:
        return depth - 10

    if result == "مساوی":
        return 0



    if is_maximizing:

        best_score = -float("inf")


        for row, col in available_moves(board):

            board[row][col] = AI_PLAYER

            score = minimax(
                board,
                depth + 1,
                False
            )

            board[row][col] = " "

            best_score = max(
                score,
                best_score
            )


        return best_score


    else:

        best_score = float("inf")


        for row, col in available_moves(board):

            board[row][col] = HUMAN_PLAYER

            score = minimax(
                board,
                depth + 1,
                True
            )

            board[row][col] = " "


            best_score = min(
                score,
                best_score
            )


        return best_score
