import sys
from game.settings import *
from game import color as clr

__author__ = 'bengt'


class Piece(object):
    """Pieces are laid out on the board on an 8x8 grid."""

    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.state = 'BOARD'
        self.flipped = False
        self.colour = colour

        self.drawing = {
            "WHITE": self.draw_white,
            "BLACK": self.draw_black,
            "BOARD": self.draw_board,
            "MOVE": self.draw_move}

    def draw(self):
        result = ''
        if self.state in self.drawing:
            result = self.drawing[self.state]()

        return result

    def draw_white(self):
        if self.flipped:
            if self.colour:
                return clr.format_color('><', fg=clr.rgb(4, 4, 4), bg=clr.rgb(5, 5, 5))

            return 'WF'
        else:
            if self.colour:
                return clr.format_color('  ', bg=clr.rgb(5, 5, 5))

            return 'WW'

    def draw_black(self):
        if self.flipped:
            if self.colour:
                return clr.format_color('><', fg=clr.rgb(2, 2, 2), bg=clr.rgb(1, 1, 1))
            return 'BF'
        else:
            if self.colour:
                return clr.format_color('  ', bg=clr.rgb(1, 1, 1))

            return 'BB'

    def draw_board(self):
        if self.colour:
            return clr.format_color('  ', bg=clr.rgb(0, 3, 0))
        else:
            return '..'

    def draw_move(self):
        if self.colour:
            return clr.format_color('><', fg=clr.rgb(5, 0, 0), bg=clr.rgb(0, 3, 0))

        return 'MM'

    def set_black(self):
        self.state = 'BLACK'

    def set_white(self):
        self.state = 'WHITE'

    def flip(self):
        if self.state == BLACK:
            self.state = WHITE
        elif self.state == WHITE:
            self.state = BLACK
        else:
            raise ValueError

        self.flipped = True

    def set_move(self):
        self.state = MOVE

    def get_position(self):
        return self.x, self.y

    def get_state(self):
        return self.state

    def set_flipped(self):
        self.flipped = True

    def reset_flipped(self):
        self.flipped = False

    def set_board(self):
        self.state = BOARD

    def is_flipped(self):
        return self.flipped

    def __repr__(self):
        return '({0},{1})'.format(self.x, self.y)