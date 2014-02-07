from collections import deque
from game.board import Board
from game.controllers import PlayerController, AiController
from game.settings import *

__author__ = 'bengt'


class Game(object):
    """Game ties everything together. It has a board,
    two controllers, and can draw to the screen."""

    def __init__(self, timeout=1000, start_colour='BLACK', display_moves=True, players=['player', 'ai'], colour=False):
        self.board = Board(colour)
        self.timeout = timeout
        self.ai_counter = 0

        self.player = start_colour
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
        while True:
            #os.system('clear')
            print("Playing as:       " + self.player)
            print("Displaying moves: " + str(self.display_moves))
            print("Current turn:     " + str(self.controllers[0]))
            player = self.controllers[0].get_colour()
            self.board.mark_moves(player)
            print(self.board.draw())
            moves = [self.to_board_coordinates(piece.get_position()) for piece in self.board.get_moves(player)]
            print("Possible moves are: ", moves)
            self.board.clear_moves()

            next_move = self.controllers[0].next_move(self.board)
            self.board.make_move(next_move, self.controllers[0].get_colour())

            self.controllers.rotate()

    def to_board_coordinates(self, coordinate):
        x, y = coordinate
        return '{0}{1}'.format(chr(ord('a') + x), y + 1)