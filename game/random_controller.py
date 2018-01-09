from game.controllers import Controller
import random

class RandomController(Controller):
    BLACK = 1
    WHITE = -1
    BOARD = 0

    def __init__(self, colour):
        self.colour = colour
        self.history = []

    def next_move(self, board):
        """ Will return a single valid move as an (x, y) tuple.
        """
        found_moves = [p.get_position() for p in board.get_move_pieces(self.get_colour())]
        return random.choice(found_moves)

    def get_colour(self):
        return self.colour

    def end_game(self, result):
        pass

    def __str__(self):
        return "Random"

    def __repr__(self):
        return "RandomController"
