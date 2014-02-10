from game.board import Board
from game.controllers import AiController
from game.settings import *

__author__ = 'bengt'

import unittest


class TestAi(unittest.TestCase):
    def setUp(self):
        pass

    def testAi(self):
        b = Board(False)

        b.set_white(4, 0)
        b.set_white(5, 0)
        b.set_white(6, 0)
        b.set_white(7, 0)
        b.set_white(3, 4)
        b.set_white(4, 4)
        b.set_white(4, 3)
        b.set_white(5, 3)
        b.set_white(5, 1)
        b.set_white(6, 1)

        b.set_black(1, 5)
        b.set_black(2, 0)
        b.set_black(2, 3)
        b.set_black(2, 4)
        b.set_black(3, 1)
        b.set_black(3, 2)
        b.set_black(3, 3)
        b.set_black(4, 1)
        b.set_black(4, 2)
        b.set_black(5, 2)
        b.set_black(6, 2)
        b.set_black(7, 1)
        b.set_black(7, 2)

        print(b.draw())

        ai = AiController(0, WHITE)
        move = ai.next_move(b)

        #self.assertEqual(, )
        self.assertIn(move, [p.get_position() for p in b.get_move_pieces(WHITE)])

if __name__ == '__main__':
    unittest.main()
