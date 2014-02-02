#!/usr/bin/python3

import argparse
import sys
from collections import deque
import color as clr
from controllers import PlayerController, AiController
from settings import *


class Game(object):
    """Game ties everything together. It has a board,
    two controllers, and can draw to the screen."""

    def __init__(self, timeout=1000, colour='BLACK', display_moves=True, players=['player', 'ai']):
        self.board = Board()
        self.timeout = timeout
        self.ai_counter = 0

        self.player = colour
        self.players = players
        self.display_moves = display_moves

        self.controllers = deque([self._make_controller(p) for p in players])

        self.board.set_black(4, 3)
        self.board.set_black(3, 4)
        self.board.set_white(4, 4)
        self.board.set_white(3, 3)
        # self.board.set_white(4,4)
        # self.board.set_white(0,0)
        # self.board.set_black(0,1)
        # self.board.set_black(1,0)
        # self.board.set_black(1,1)

        # bottom right corner
        # self.board.set_black(2, 3)
        # self.board.set_black(3, 4)
        # self.board.set_black(4, 3)
        # self.board.set_white(2, 2)
        # self.board.set_white(3, 3)
        # self.board.set_white(4, 4)

        self.board.mark_moves(self.player)

    def _make_controller(self, controller_type):
        if controller_type == 'player':
            return PlayerController(self.player)
        else:
            self.ai_counter += 1
            return AiController(self.ai_counter, BLACK if self.player is WHITE else WHITE)

    def run(self):
        turn = 'player'
        while True:
            #os.system('clear')
            print("Playing as:       " + self.player)
            print("Displaying moves: " + str(self.display_moves))
            print("Current turn:     " + str(self.controllers[0]))
            self.board.draw()

            self.board.make_move(self.controllers[0].next_move(self.board), self.controllers[0].get_colour())

            self.controllers.rotate()


class Board(object):
    """Board represents the current state of the Reversi board."""

    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = list((Piece(x, y)
                            for x in range(0, self.width)
                            for y in range(0, self.height)))

    def draw(self):
        labels = "  a.b.c.d.e.f.g.h."
        #labels = "  0 1 2 3 4 5 6 7"
        print(labels)

        size = self.width * self.height
        i = 0
        for p in self.pieces:
            if i == 0:
                print(str(int(i / 8) + 1), end=' ')
                #print(str(int(i / 8)), end=' ')
            elif (i) % 8 == 0:
                print('', str(int(i / 8)))
                print(str(int(i / 8) + 1), end=' ')
                #print(str(int(i / 8)), end=' ')

            p.draw()

            i += 1
        print('', 8)
        print(labels)

    def set_white(self, x, y):
        self.pieces[x + (y * self.width)].set_white()

    def set_black(self, x, y):
        self.pieces[x + (y * self.width)].set_black()

    def flip(self, x, y):
        self.pieces[x + (y * self.width)].flip()

    def move(self, x, y):
        self.pieces[x + (y * self.width)].move()

    def set_flipped(self, x, y):
        self.pieces[x + (y * self.width)].set_flipped()

    def mark_moves(self, player):
        """
        Marks all 'BOARD' pieces that are valid moves as 'MOVE' pieces
        for the current player.

        Returns: void
        """
        for p in self.pieces:
            if p.get_state() == player:
                #for d in DIRECTIONS:
                #    self.mark_move(player, p, d)
                [self.mark_move(player, p, d) for d in DIRECTIONS]

    def mark_move(self, player, piece, direction):
        """
        Will mark moves from the current 'piece' in 'direction'
        """
        x, y = piece.get_position()
        opponent = BLACK if player == WHITE else WHITE
        tile = (x + (y * WIDTH)) + direction
        if self.pieces[tile].get_state() == opponent:
            while self.pieces[tile].get_state() == opponent:
                tile += direction
            if self.pieces[tile].get_state() == BOARD:
                self.pieces[tile].move()

    def make_move(self, coordinates, player):
        print("Making move at", coordinates)
        x, y = coordinates
        opponent = BLACK if player == WHITE else WHITE
        print("Player is", player, "Opponent is", opponent)
        if player == WHITE:
            self.pieces[x + (y * WIDTH)].set_white()
            self.pieces[x + (y * WIDTH)].set_flipped()
        else:
            self.pieces[x + (y * WIDTH)].set_black()
            self.pieces[x + (y * WIDTH)].set_flipped()
        for d in DIRECTIONS:
            tile = x + (y * WIDTH) + d
            if self.pieces[tile].get_state() == opponent:
                while self.pieces[tile].get_state() == opponent:
                    print("Flipping piece: ", tile % WIDTH, int(tile / WIDTH))
                    self.pieces[tile].flip()
                    tile += d


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
        if self.state == 'BLACK':
            self.state = 'WHITE'
        elif self.state == 'WHITE':
            self.state = 'BLACK'
        self.flipped = True

    def move(self):
        self.state = 'MOVE'

    def get_position(self):
        return self.x, self.y

    def get_state(self):
        return self.state

    def set_flipped(self):
        self.flipped = True


def main():
    """ Reversi game with human player vs AI player """

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Action timeout for the AI, in ms (default=5000 ms).", type=int, default=5000)
    parser.add_argument('--colour', help="The colour you want to play as (default=white).", type=str, default='BLACK')
    parser.add_argument('--display-moves', help="Whether legal moves should be displayed or not.", action='store_true')
    args = parser.parse_args()

    if args.timeout < 0: exit()

    print("EDA132> Reversi")

    # Initialize game
    # Begin game loop

    game = Game(args.timeout, args.colour, args.display_moves)
    game.run()


if __name__ == "__main__":
    main()
