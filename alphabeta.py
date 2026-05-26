import math

class TicTacToe:

    def __init__(self):

        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def available_moves(self):

        moves = []

        for i in range(9):

            if self.board[i] == ' ':
                moves.append(i)

        return moves

    def empty_squares(self):

        return ' ' in self.board

    def make_move(self, square, letter):

        if self.board[square] == ' ':

            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True

        return False

    def winner(self, square, letter):

        row = self.board[(square//3)*3 : (square//3+1)*3]

        if all([s == letter for s in row]):
            return True

        column = [self.board[square%3 + i*3] for i in range(3)]

        if all([s == letter for s in column]):
            return True

        return False


# alpha beta pruning

def alpha_beta(state, depth, alpha, beta, maximizing):

    if state.current_winner == 'X':
        return 10

    elif state.current_winner == 'O':
        return -10

    elif not state.empty_squares() or depth == 0:
        return 0

    if maximizing:

        max_eval = -math.inf

        for move in state.available_moves():

            state.make_move(move, 'X')

            eval = alpha_beta(state,
                              depth-1,
                              alpha,
                              beta,
                              False)

            state.board[move] = ' '
            state.current_winner = None

            max_eval = max(max_eval, eval)

            alpha = max(alpha, eval)

            if beta <= alpha:
                break

        return max_eval

    else:

        min_eval = math.inf

        for move in state.available_moves():

            state.make_move(move, 'O')

            eval = alpha_beta(state,
                              depth-1,
                              alpha,
                              beta,
                              True)

            state.board[move] = ' '
            state.current_winner = None

            min_eval = min(min_eval, eval)

            beta = min(beta, eval)

            if beta <= alpha:
                break

        return min_eval


game = TicTacToe()

game.make_move(0, 'X')
game.make_move(4, 'O')

answer = alpha_beta(game,
                    5,
                    -math.inf,
                    math.inf,
                    True)

print("alpha beta result =", answer)
