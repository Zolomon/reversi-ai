from game.board import Board
from game.settings import *

__author__ = 'bengt'

import unittest


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        b = Board(False)
        self.assertEqual(len(b.get_move_pieces(WHITE)), 0)
        self.assertEqual(len(b.get_move_pieces(BLACK)), 0)

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

        b = Board(False)
        b.set_white(3, 2)
        b.set_white(4, 1)
        b.set_white(4, 2)
        b.set_white(5, 1)
        b.set_white(5, 2)
        b.set_white(6, 0)
        b.set_white(6, 1)
        b.set_white(6, 2)
        b.set_white(6, 3)

        b.set_black(1, 3)
        b.set_black(1, 5)
        b.set_black(2, 0)
        b.set_black(2, 3)
        b.set_black(2, 4)
        b.set_black(3, 1)
        b.set_black(3, 3)
        b.set_black(3, 4)
        b.set_black(3, 5)
        b.set_black(4, 3)
        b.set_black(4, 4)
        b.set_black(5, 3)
        b.set_black(5, 5)
        b.set_black(6, 4)
        b.set_black(7, 0)

        b.mark_moves(BLACK)

        result = b.draw()
        #0 1 2 3 4 5 6 7
        canvas = """  a.b.c.d.e.f.g.h.
1 ....BB..MMMMWWBB1
2 ....MMBBWWWWWWMM2
3 ......WWWWWWWW..3
4 ..BBBBBBBBBBWWMM4
5 ....BBBBBB..BB..5
6 ..BB..BB..BB....6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)

        b.clear_moves()
        b.mark_moves(WHITE)
        result = b.draw()

        canvas = """  a.b.c.d.e.f.g.h.
1 ....BBMM....WWBB1
2 ....MMBBWWWWWW..2
3 ......WWWWWWWW..3
4 MMBBBBBBBBBBWW..4
5 ..MMBBBBBBMMBB..5
6 ..BBMMBBMMBBMMMM6
7 MM..MMMM........7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)

        ##b.clear_moves()
        ##b.mark_moves(WHITE)
        b.clear_moves()
        b.make_move((0, 3), WHITE)
        
        result = b.draw()
        #0 1 2 3 4 5 6 7
        canvas = """  a.b.c.d.e.f.g.h.
1 ....BB......WWBB1
2 ......BBWWWWWW..2
3 ......WWWWWWWW..3
4 WWWWWWWWWWWWWW..4
5 ....BBBBBB..BB..5
6 ..BB..BB..BB....6
7 ................7
8 ................8
  a.b.c.d.e.f.g.h."""

        self.assertEqual(result, canvas)

    def test_ai(self):
        b = Board(False)

        b.set_black(4, 3)
        b.set_black(3, 4)
        b.set_white(4, 4)
        b.set_white(3, 3)

        b.clear_moves()
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
        self.assertEqual(result, canvas)

        #b.make_move()

if __name__ == '__main__':
    unittest.main()
