from game.settings import *
from game.piece import Piece

__author__ = 'bengt'

import unittest


class TestPiece(unittest.TestCase):
    def setUp(self):
        pass

    def test_positions(self):
        p1 = Piece(0, 0)
        p2 = Piece(2, 2)
        self.assertEqual(p1.get_position(), (0, 0))
        self.assertEqual(p2.get_position(), (2, 2))

    def test_state(self):
        p1 = Piece(0, 0)
        p1.set_black()
        self.assertEqual(p1.get_state(), BLACK)

        p2 = Piece(1, 1)
        p2.set_white()
        self.assertEqual(p2.get_state(), WHITE)

        p3 = Piece(3, 3)
        p3.set_move()
        self.assertEqual(p3.get_state(), MOVE)

        p1.flip()
        self.assertEqual(p1.get_state(), WHITE)
        self.assertEqual(p1.is_flipped(), True)

        p4 = Piece(4,4)
        p4.set_board()
        self.assertEqual(p4.get_state(), BOARD)

if __name__ == '__main__':
    unittest.main()