from game.piece import Piece
from game.settings import *

__author__ = 'bengt'


class Board(object):
    """Board represents the current state of the Reversi board."""

    def __init__(self, colour):
        self.width = 8
        self.height = 8
        self.pieces = list((Piece(x, y, colour)
                            for y in range(0, self.height)
                            for x in range(0, self.width)))

    def draw(self):
        """ Returns a representation of the board in monochrome or 256 RGB colour.
        """
        labels = "  a.b.c.d.e.f.g.h."

        grid = ''
        i = 0
        for row_of_pieces in chunks(self.pieces, 8):
            row = ''
            for p in row_of_pieces:
                row += p.draw()

            grid += '{0} {1}{0}\n'.format(str(i + 1), row)

            i += 1

        output = '{0}\n{1}{0}'.format(labels, grid)
        return output

    def set_white(self, x, y):
        """ Sets the specified piece's state to WHITE.
        """
        self.pieces[x + (y * self.width)].set_white()

    def set_black(self, x, y):
        """ Sets the specified piece's state to BLACK.
        """
        self.pieces[x + (y * self.width)].set_black()

    def set_move(self, x, y):
        """ Sets the specified piece's state to MOVE.
        """
        self.pieces[x + (y * self.width)].set_move()

    def flip(self, x, y):
        """ Flips the specified piece's state from WHITE<->BLACK.
        """
        self.pieces[x + (y * self.width)].flip()

    def set_flipped(self, x, y):
        """ Sets the specified piece as flipped.
        """
        self.pieces[x + (y * self.width)].set_flipped()

    def get_move_pieces(self, player):
        """ Returns a list of moves for the specified player.
        """
        self.mark_moves(player)
        moves = [piece for piece in self.pieces if piece.get_state() == MOVE]
        self.clear_moves()
        return moves

    def mark_moves(self, player):
        """ Marks all 'BOARD' pieces that are valid moves as 'MOVE' pieces
            for the current player.

            Returns: void
        """
        [self.mark_move(player, p, d)
         for p in self.pieces
         for d in DIRECTIONS
         if p.get_state() == player]

    def mark_move(self, player, piece, direction):
        """ Will mark moves from the current 'piece' in 'direction'.
        """
        x, y = piece.get_position()
        opponent = get_opponent(player)
        if outside_board(x + (y * WIDTH), direction):
            return

        tile = (x + (y * WIDTH)) + direction

        if self.pieces[tile].get_state() == opponent:
            while self.pieces[tile].get_state() == opponent:
                if outside_board(tile, direction):
                    break
                else:
                    tile += direction

            if self.pieces[tile].get_state() == BOARD:
                self.pieces[tile].set_move()

    def make_move(self, coordinates, player):
        """ Will modify the internal state to represent performing the
            specified move for the specified player.
        """
        moves = [piece.get_position() for piece in self.get_move_pieces(player)]
        if coordinates not in moves:
            raise ValueError

        placed = coordinates[0] + (coordinates[1] * WIDTH)

        p = self.pieces[placed]
        if player == WHITE:
            p.set_white()
        else:
            p.set_black()

        for d in DIRECTIONS:
            if outside_board(placed, d):
                continue

            tile = start = placed + d

            to_flip = []
            while self.pieces[tile].get_state() != BOARD:
                if self.pieces[tile].get_state() == player or outside_board(tile, d):
                    break
                else:
                    to_flip.append(self.pieces[tile])
                    tile += d

            if self.pieces[tile].get_state() == player:
                for pp in to_flip:
                    if player == WHITE:
                        pp.set_white()
                    else:
                        pp.set_black()

            self.pieces[start].reset_flipped()

    def clear_moves(self):
        """ Sets all move pieces to board pieces.
        """
        [x.set_board() for x in self.pieces if x.get_state() == MOVE]

    def __repr__(self):
        return self.draw()
