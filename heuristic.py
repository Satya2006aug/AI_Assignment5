import math

# heuristic function

def heuristic(board):

    combos = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]
    ]

    score = 0

    for combo in combos:

        values = [board[i] for i in combo]

        if values.count('X') == 2 and values.count(' ') == 1:
            score += 5

        if values.count('O') == 2 and values.count(' ') == 1:
            score -= 5

    return score


def heuristic_alpha_beta(board,
                         depth,
                         alpha,
                         beta,
                         maximizing):

    if depth == 0:
        return heuristic(board)

    empty = []

    for i in range(9):

        if board[i] == ' ':
            empty.append(i)

    if maximizing:

        value = -math.inf

        for move in empty:

            board[move] = 'X'

            value = max(
                value,
                heuristic_alpha_beta(board,
                                     depth-1,
                                     alpha,
                                     beta,
                                     False)
            )

            board[move] = ' '

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in empty:

            board[move] = 'O'

            value = min(
                value,
                heuristic_alpha_beta(board,
                                     depth-1,
                                     alpha,
                                     beta,
                                     True)
            )

            board[move] = ' '

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


board = [

    'X','X',' ',
    'O',' ',' ',
    ' ',' ','O'
]

result = heuristic_alpha_beta(board,
                              3,
                              -math.inf,
                              math.inf,
                              True)

print("heuristic alpha beta =", result)
