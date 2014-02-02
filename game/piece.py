import sys
from game.settings import *
from game import color as clr

__author__ = 'bengt'


class Piece(object):
    """Pieces are laid out on the board on an 8x8 grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 'BOARD'
        self.flipped = False

        self.drawing = {
            "WHITE": self.draw_white,
            "BLACK": self.draw_black,
            "BOARD": self.draw_board,
            "MOVE": self.draw_move}

    def draw(self):
        if self.state in self.drawing:
            self.drawing[self.state]()

        self.flipped = False

    def draw_white(self):
        if self.flipped:
            sys.stdout.write(
                #clr.format_color('><', fg=clr.rgb(4, 4, 4), bg=clr.rgb(5, 5, 5)))
                clr.format_color('WF'))
        else:
            #sys.stdout.write(clr.format_color('  ', bg=clr.rgb(5, 5, 5)))
            sys.stdout.write(clr.format_color('WW'))

    def draw_black(self):
        if self.flipped:
            sys.stdout.write(
                #clr.format_color('><', fg=clr.rgb(2, 2, 2), bg=clr.rgb(1, 1, 1)))
                clr.format_color('BF'))
        else:
            #sys.stdout.write(clr.format_color('  ', bg=clr.rgb(1, 1, 1)))
            sys.stdout.write(clr.format_color('BB'))

    @staticmethod
    def draw_board():
        #sys.stdout.write(clr.format_color('  ', bg=clr.rgb(0, 3, 0)))
        sys.stdout.write(clr.format_color('..'))

    @staticmethod
    def draw_move():
        sys.stdout.write(
            #clr.format_color('><', fg=clr.rgb(5, 0, 0), bg=clr.rgb(0, 3, 0)))
            clr.format_color('MM'))

    def set_black(self):
        self.state = 'BLACK'

    def set_white(self):
        self.state = 'WHITE'

    def flip(self):
        self.state = WHITE if self.state is BLACK else BLACK
        self.flipped = True

    def move(self):
        self.state = MOVE

    def get_position(self):
        return self.x, self.y

    def get_state(self):
        return self.state

    def set_flipped(self):
        self.flipped = True

    def set_board(self):
        self.state = BOARD