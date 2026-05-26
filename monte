import random
from copy import deepcopy

class TicTacToe:

    def __init__(self):

        self.board = [' ' for i in range(9)]
        self.current_winner = None

    def available_moves(self):

        return [i for i in range(9)
                if self.board[i] == ' ']

    def empty_squares(self):

        return ' ' in self.board

    def make_move(self, square, letter):

        if self.board[square] == ' ':

            self.board[square] = letter

            return True

        return False


# monte carlo node

class MCTSNode:

    def __init__(self, state, parent=None):

        self.state = deepcopy(state)
        self.parent = parent

        self.children = []

        self.visits = 0
        self.wins = 0

    def best_child(self):

        return max(
            self.children,
            key=lambda c: c.wins/c.visits
            if c.visits > 0 else -1
        )


def random_playout(state, player):

    current = player

    while state.empty_squares():

        move = random.choice(state.available_moves())

        state.make_move(move, current)

        current = 'O' if current == 'X' else 'X'

    return current


def monte_carlo_tree_search(root_state,
                             iterations=100):

    root = MCTSNode(root_state)

    for i in range(iterations):

        node = root

        state = deepcopy(root_state)

        if state.empty_squares():

            move = random.choice(state.available_moves())

            state.make_move(move, 'X')

            child = MCTSNode(state, node)

            node.children.append(child)

            node = child

        result = random_playout(state, 'O')

        while node:

            node.visits += 1

            if result == 'X':
                node.wins += 1

            node = node.parent

    return root.best_child()


game = TicTacToe()

best = monte_carlo_tree_search(game, 100)

print("visits =", best.visits)
print("wins =", best.wins)
