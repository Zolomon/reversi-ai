from game.piece import Piece
from game.settings import *

__author__ = 'bengt'


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
        p = self.pieces[x + (y * WIDTH)]
        if player == WHITE:
            p.set_white()
            p.set_flipped()
        else:
            p.set_black()
            p.set_flipped()
        for d in DIRECTIONS:
            tile = x + (y * WIDTH) + d
            #if self.pieces[tile].get_state() == opponent:
            to_flip = []
            while self.pieces[tile].get_state() != BOARD:
                if self.pieces[tile].get_state() == opponent:
                    #print("Flipping piece: ", tile % WIDTH, int(tile / WIDTH))
                    #self.pieces[tile].flip()
                    to_flip.append(self.pieces[tile])
                tile += d

            if self.pieces[tile-d].get_state() == player:
                [x.flip() for x in to_flip]




    def clear_moves(self):
        [x.set_board() for x in self.pieces if x.get_state() == MOVE]