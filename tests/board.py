from game.board import Board
from game.settings import *

__author__ = 'bengt'

import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        b = Board()
        self.assertEqual(len(b.get_moves(WHITE)), 0)
        self.assertEqual(len(b.get_moves(BLACK)), 0)

    def test_draw(self):
        b = Board()

        b.set_black(0, 0)
        b.set_black(1, 0)
        b.set_white(1, 1)
        b.set_move(0, 1)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 BBBB............1
2 MMWW............2
3 ................3
4 ................4
5 ................5
6 ................6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)

        b.clear_moves()
        b.mark_moves(BLACK)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 BBBB............1
2 ..WW............2
3 ..MMMM..........3
4 ................4
5 ................5
6 ................6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""
        self.assertEqual(result, canvas)

        b.clear_moves()
        b = Board()
        b.set_white(3, 3)
        b.set_white(3, 4)
        b.set_white(4, 4)
        b.set_white(4, 3)
        b.set_black(2, 2)
        b.set_black(3, 2)
        b.set_black(4, 2)
        b.set_black(5, 2)
        b.set_black(2, 3)
        b.set_black(5, 3)
        b.set_black(2, 4)
        b.set_black(5, 4)
        b.set_black(2, 5)
        b.set_black(3, 5)
        b.set_black(4, 5)
        b.set_black(5, 5)

        b.clear_moves()
        b.mark_moves(WHITE)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 ................1
2 ..MMMMMMMMMMMM..2
3 ..MMBBBBBBBBMM..3
4 ..MMBBWWWWBBMM..4
5 ..MMBBWWWWBBMM..5
6 ..MMBBBBBBBBMM..6
7 ..MMMMMMMMMMMM..7
8 ................8
  a.b.c.d.e.f.g.h."""
        self.assertEqual(result, canvas)


if __name__ == '__main__':
    unittest.main()
