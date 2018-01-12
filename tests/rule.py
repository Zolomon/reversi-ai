from game.game import Game
from game.settings import BLACK, WHITE

__author__ = 'yuessiah'

import unittest


class TestRule(unittest.TestCase):
    def setUp(self):
        pass

    def test_player_cant_move(self):
        b = Game(colour=True, players=['player', 'player'])

        b.board.make_move(parse_coordinates("e6"), BLACK)
        b.board.make_move(parse_coordinates("f6"), WHITE)
        b.board.make_move(parse_coordinates("c4"), BLACK)
        b.board.make_move(parse_coordinates("c5"), WHITE)
        b.board.make_move(parse_coordinates("c6"), BLACK)
        b.board.make_move(parse_coordinates("d6"), WHITE)
        b.board.make_move(parse_coordinates("g7"), BLACK)
        b.board.make_move(parse_coordinates("f4"), WHITE)
        b.board.make_move(parse_coordinates("g4"), BLACK)
        b.board.make_move(parse_coordinates("g6"), WHITE)
        b.board.make_move(parse_coordinates("e7"), BLACK)
        b.board.make_move(parse_coordinates("h8"), WHITE)
        b.board.make_move(parse_coordinates("h6"), BLACK)
        b.board.make_move(parse_coordinates("g5"), WHITE)
        b.board.make_move(parse_coordinates("g8"), BLACK)
        b.board.make_move(parse_coordinates("f8"), WHITE)

        b.run() #BLACK round is present


def parse_coordinates(move):
    """ Parses board coordinates into (x, y) coordinates.
    """
    return ord(move[0]) - ord('a'), ord(move[1]) - ord('0') - 1


if __name__ == '__main__':
    unittest.main()
