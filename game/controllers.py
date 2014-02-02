from game.ai import AlphaBetaPruner
from game.settings import *

__author__ = 'bengt'


class Controller(object):
    def next_move(self, pieces):
        pass

    def get_colour(self):
        pass


class PlayerController(Controller):
    def __init__(self, colour):
        self.colour = colour

    def next_move(self, board):
        result = None
        while result is None:

            event = input('')
            if event[0] == '/':
                if event[1:] == 'quit' or event[1:] == 'q':
                    print('Quitting. Thank you for playing.')
                    exit()
            else:
                try:
                    x, y = event[0], event[1]
                    result = self._parse_coordinates(x, y)
                except (TypeError, ValueError):
                    print("Invalid coordinates, retry.")
        return result

    def get_colour(self):
        return self.colour

    def __str__(self):
        return "Player"

    def __repr__(self):
        return "PlayerController"

    @staticmethod
    def _parse_coordinates(x, y):
        return ord(x) - ord('a'), ord(y) - ord('0') - 1


class AiController(Controller):
    def __init__(self, id, colour):
        self.id = id
        self.colour = colour

    def next_move(self, board):
        pruner = AlphaBetaPruner(board.pieces, self.colour, BLACK if self.colour is WHITE else WHITE)
        result = pruner.alpha_beta_search()
        #print("AI: ", result)
        return result

    def get_colour(self):
        return self.colour

    def __str__(self):
        return "Ai"

    def __repr__(self):
        return "AiController[" + self.id + "]"