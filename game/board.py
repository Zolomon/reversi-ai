from game.piece import Piece
from game.settings import *

__author__ = 'bengt'


class Board(object):
    """Board represents the current state of the Reversi board."""

    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = list((Piece(x, y)
                            for y in range(0, self.height)
                            for x in range(0, self.width)))

    def draw(self):
        labels = "  a.b.c.d.e.f.g.h."
        #labels = "  0 1 2 3 4 5 6 7"
        #print(labels)

        grid = ''
        size = self.width * self.height
        i = 0
        for row_of_pieces in chunks(self.pieces, 8):
            #if i == 0:
            #    print(str(int(i / 8) + 1), end=' ')
                #print(str(int(i / 8)), end=' ')
            #elif (i) % 8 == 0:
            #    print('', str(int(i / 8)))
            #    print(str(int(i / 8) + 1), end=' ')
                #print(str(int(i / 8)), end=' ')
            row = ''
            for p in row_of_pieces:
                row += p.draw()

            grid += '{0} {1}{0}\n'.format(str(i+1), row)

            i += 1
        #print('', 8)
        #print(labels)

        output = '{0}\n{1}{0}'.format(labels, grid)
        return output

    def set_white(self, x, y):
        self.pieces[x + (y * self.width)].set_white()

    def set_black(self, x, y):
        self.pieces[x + (y * self.width)].set_black()

    def flip(self, x, y):
        self.pieces[x + (y * self.width)].flip()

    def set_move(self, x, y):
        self.pieces[x + (y * self.width)].set_move()

    def set_flipped(self, x, y):
        self.pieces[x + (y * self.width)].set_flipped()

    def get_moves(self, player):
        self.mark_moves(player)
        moves = [piece for piece in self.pieces if piece.get_state() == MOVE]
        self.clear_moves()
        return moves

    def mark_moves(self, player):
        """
        Marks all 'BOARD' pieces that are valid moves as 'MOVE' pieces
        for the current player.

        Returns: void
        """
        # for p in self.pieces:
        #     if p.get_state() == player:
        [self.mark_move(player, p, d)
         for p in self.pieces
         for d in DIRECTIONS
         if p.get_state() == player]

    def mark_move(self, player, piece, direction):
        """
        Will mark moves from the current 'piece' in 'direction'
        """
        x, y = piece.get_position()
        opponent = get_opponent(player)
        tile = (x + (y * WIDTH)) + direction
        if tile < 0 or tile >= WIDTH*HEIGHT:
            return

        if self.pieces[tile].get_state() == opponent:
            while self.pieces[tile].get_state() == opponent:
                tile += direction
            if self.pieces[tile].get_state() == BOARD:
                self.pieces[tile].set_move()

    def make_move(self, coordinates, player):
        print("Making move at", coordinates)
        x, y = coordinates
        opponent = get_opponent(player)
        print("Player is", player, "Opponent is", opponent)
        p = self.pieces[x + (y * WIDTH)]
        if player == WHITE:
            p.set_white()
            p.set_flipped()
        else:
            p.set_black()
            p.set_flipped()
        for d in DIRECTIONS:
            start = x + (y * WIDTH) + d
            tile = start
            #if self.pieces[tile].get_state() == opponent:

            to_flip = []
            #to_flip = []
            while self.pieces[tile].get_state() != BOARD:
                #if self.pieces[tile].get_state() == opponent:
                    #print("Flipping piece: ", tile % WIDTH, int(tile / WIDTH))
                    #self.pieces[tile].flip()
                    #to_flip.append(self.pieces[tile])
                #if self.pieces[tile].get_state() == opponent:
                #    opponent_pieces.append(self.pieces[tile])
                to_flip.append(self.pieces[tile])
                tile += d

            start_flipping = False
            for pp in reversed(to_flip):
                if not start_flipping:
                    if pp.get_state() == opponent:
                        continue
                start_flipping = True

                if player == WHITE:
                    pp.set_white()
                    pp.set_flipped()
                else:
                    pp.set_black()
                    pp.set_flipped()

            self.pieces[start].reset_flipped()

    def clear_moves(self):
        [x.set_board() for x in self.pieces if x.get_state() == MOVE]