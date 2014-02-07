from game.board import Board
from game.settings import *

__author__ = 'bengt'

import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        b = Board(False)
        self.assertEqual(len(b.get_moves(WHITE)), 0)
        self.assertEqual(len(b.get_moves(BLACK)), 0)

    def test_outside(self):
        b = Board(False)
        self.assertEqual(b.outside_board(0, NORTH), True)
        self.assertEqual(b.outside_board(0, NORTHEAST), True)
        self.assertEqual(b.outside_board(0, NORTHWEST), True)
        self.assertEqual(b.outside_board(0, WEST), True)
        self.assertEqual(b.outside_board(0, SOUTHWEST), True)
        self.assertEqual(b.outside_board(0, EAST), False)
        self.assertEqual(b.outside_board(0, SOUTHEAST), False)
        self.assertEqual(b.outside_board(0, SOUTH), False)

        self.assertEqual(b.outside_board(1, NORTH), True)
        self.assertEqual(b.outside_board(1, NORTHEAST), True)
        self.assertEqual(b.outside_board(1, NORTHWEST), True)
        self.assertEqual(b.outside_board(1, WEST), False)
        self.assertEqual(b.outside_board(1, SOUTHWEST), False)
        self.assertEqual(b.outside_board(1, EAST), False)
        self.assertEqual(b.outside_board(1, SOUTHEAST), False)
        self.assertEqual(b.outside_board(1, SOUTH), False)

        self.assertEqual(b.outside_board(63, NORTH), False)
        self.assertEqual(b.outside_board(63, NORTHEAST), True)
        self.assertEqual(b.outside_board(63, NORTHWEST), False)
        self.assertEqual(b.outside_board(63, WEST), False)
        self.assertEqual(b.outside_board(63, SOUTHWEST), True)
        self.assertEqual(b.outside_board(63, EAST), True)
        self.assertEqual(b.outside_board(63, SOUTHEAST), True)
        self.assertEqual(b.outside_board(63, SOUTH), True)

        self.assertEqual(b.outside_board(23, NORTH), False)
        self.assertEqual(b.outside_board(23, NORTHEAST), True)
        self.assertEqual(b.outside_board(23, NORTHWEST), False)
        self.assertEqual(b.outside_board(23, WEST), False)
        self.assertEqual(b.outside_board(23, SOUTHWEST), False)
        self.assertEqual(b.outside_board(23, EAST), True)
        self.assertEqual(b.outside_board(23, SOUTHEAST), True)
        self.assertEqual(b.outside_board(23, SOUTH), False)

        self.assertEqual(b.outside_board(24, NORTH), False)
        self.assertEqual(b.outside_board(24, NORTHEAST), False)
        self.assertEqual(b.outside_board(24, NORTHWEST), True)
        self.assertEqual(b.outside_board(24, WEST), True)
        self.assertEqual(b.outside_board(24, SOUTHWEST), True)
        self.assertEqual(b.outside_board(24, EAST), False)
        self.assertEqual(b.outside_board(24, SOUTHEAST), False)
        self.assertEqual(b.outside_board(24, SOUTH), False)


    def test_draw(self):
        b = Board(False)

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
        b = Board(False)
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

        b = Board(False)
        b.set_white(3, 3)
        b.set_white(4, 4)
        b.set_black(3, 4)
        b.set_black(4, 3)

        b.mark_moves(BLACK)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 ................1
2 ................2
3 ......MM........3
4 ....MMWWBB......4
5 ......BBWWMM....5
6 ........MM......6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        b.clear_moves()
        b.make_move((3, 2), BLACK)
        b.mark_moves(WHITE)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 ................1
2 ................2
3 ....MMBBMM......3
4 ......BBBB......4
5 ....MMBBWW......5
6 ................6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        b.clear_moves()
        b.make_move((2, 2), WHITE)
        b.mark_moves(BLACK)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 ................1
2 ................2
3 ..MMWWBB........3
4 ....MMWWBB......4
5 ......BBWWMM....5
6 ........MM......6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        b = Board(False)
        b.set_white(6, 0)
        b.set_white(5, 1)
        b.set_white(3, 1)
        b.set_white(3, 2)
        b.set_white(4, 2)
        b.set_white(5, 2)
        b.set_white(3, 3)
        b.set_white(4, 3)

        b.set_black(2, 3)
        b.set_black(2, 4)
        b.set_black(3, 4)
        b.set_black(4, 4)
        b.set_black(1, 5)
        b.set_black(4, 5)
        b.mark_moves(BLACK)
        result = b.draw()
        canvas = """  a.b.c.d.e.f.g.h.
1 ......MM....WW..1
2 ......WWMMWWMM..2
3 ....MMWWWWWW....3
4 ....BBWWWWMM....4
5 ....BBBBBB......5
6 ..BB....BB......6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)

        b = Board(False)
        b.set_white(3, 4)
        b.set_white(4, 0)
        b.set_white(4, 3)
        b.set_white(4, 4)
        b.set_white(5, 0)
        b.set_white(5, 1)
        b.set_white(5, 3)
        b.set_white(6, 0)
        b.set_white(6, 1)
        b.set_white(7, 0)

        b.set_black(2, 0)
        b.set_black(3, 1)
        b.set_black(4, 1)
        b.set_black(7, 1)
        b.set_black(3, 2)
        b.set_black(4, 2)
        b.set_black(5, 2)
        b.set_black(6, 2)
        b.set_black(7, 2)
        b.set_black(3, 3)
        b.set_black(2, 3)
        b.set_black(2, 4)
        b.set_black(1, 5)

        b.mark_moves(BLACK)

        result = b.draw()
        #0 1 2 3 4 5 6 7
        canvas = """  a.b.c.d.e.f.g.h.
1 ....BB..WWWWWWWW1
2 ......BBBBWWWWBB2
3 ......BBBBBBBBBB3
4 ....BBBBWWWWMM..4
5 ....BBWWWWMMMM..5
6 ..BBMMMMMMMM....6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)


if __name__ == '__main__':
    unittest.main()
