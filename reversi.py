#!/usr/bin/python3

import os
import argparse
import sys
from string import ascii_lowercase, digits
from collections import deque

import color as clr

class Controller(object):
    def next_move(self, pieces):
        pass

class PlayerController(Controller):
    def __init__(self):
        pass

    def next_move(self, board):
        result = None
        while result is None:
            
            event = input('')
            if event[0] == '/':
                if event[1:] == 'quit' or event[1:] == 'q': 
                    print('Quitting. Thank you for playing.')
                    exit()                    
            else: 
                try:
                    coords = list(map(lambda x: x.lower(), event.split()))
                    result = self._parse_coords(coords)
                except:
                    print("Invalid coordinates, retry.")
        return result      

    def _parse_coords(self, data):
        src = (abs(ord(data[0][0]) - ord('h')), abs(ord(data[0][1])))
        dst = (abs(ord(data[1][0]) - ord('h')), abs(ord(data[1][1])))
        return (src, dst)

    def __str__(self):
        return "Player"
    
    def __repr__(self):
        return "PlayerController"

class AiController(Controller):
    def __init__(self, id):
        self.id = id

    def next_move(self, board):
        pass

    def __str__(self):
        return "Ai"

    def __repr__(self):
        return "AiController["+self.id+"]"

class AlphaBetaPruner(object):
    """Alpha-Beta Pruning algorithm."""
    def __init__(self):
        pass

    def alpha_beta_search(self, state):
        """Returns an action"""
        #value = self.max_value(state, sys.minint, sys.maxint)
        #return 
        pass

    def max_value(self, state, alpha, beta):
        """Returns a utility value"""
        pass

    def min_value(self, state, alphaa, beta):
        """Returns a utility value"""
        pass
    

class Game(object):
    """Game ties everything together. It has a board, 
    two controllers, and can draw to the screen."""
    def __init__(self, timeout=1000, colour='WHITE', display_moves=True, players=['player', 'ai']):
        self.board         = Board()
        self.timeout       = timeout
        self.aicounter     = 0

        self.player        = colour
        self.players       = players
        self.display_moves = display_moves
        
        self.controllers   = deque([self._make_controller(p) for p in players])

        self.board.set_black(4,3)
        self.board.set_black(3,4)
        self.board.set_black(3,5)
        self.board.set_white(3,3)
        self.board.set_white(4,4)

        self.board.mark_moves(self.player)       
        

    def _make_controller(self, ctrltype):
        if ctrltype == 'player':
            return PlayerController()
        else:
            self.aicounter += 1
            return AiController(self.aicounter)
    

    def run(self):       
        turn = 'player'
        while True:
            os.system('clear')
            print("Playing as:       " + self.player)
            print("Displaying moves: " + str(self.display_moves))
            print("Current turn:     " + str(self.controllers[0]))
            self.board.draw()            

            self.board.make_move(self.controllers[0].next_move(self.board))

            self.controllers.rotate()

BOARD, WHITE, BLACK, MOVE = 'BOARD', 'WHITE', 'BLACK', 'MOVE'
WIDTH, HEIGHT = 8, 8
NORTH     = -HEIGHT
NORTHEAST = -HEIGHT  + 1
EAST      =            1
SOUTHEAST =  HEIGHT  + 1
SOUTH     =  HEIGHT
SOUTHWEST =  HEIGHT  - 1
WEST      =          - 1
NORTHWEST = -HEIGHT  - 1

DIRECTIONS = (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST)

class Board(object):
    """Board represents the current state of the Reversi board."""
    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = list((Piece(x, y) 
                       for x in range(0, self.width) 
                       for y in range(0, self.height)))
        
    def draw(self):
        labels = "  a b c d e f g h"
        print(labels)
                
        size = self.width * self.height
        i = 0
        for p in self.pieces:
            if i == 0:
                print(str(int(i/8)+1), end=' ')
            elif (i) % 8 == 0:                 
                print('', str(int(i/8)))
                print(str(int(i/8)+1), end=' ')
                
            p.draw()

            i += 1
        print('', 8)
        print(labels)

    def set_white(self, x, y):
        self.pieces[x + (y*self.width)].set_white()

    def set_black(self, x, y):
        self.pieces[x + (y*self.width)].set_black()

    def flip(self, x, y):
        self.pieces[x + (y*self.width)].flip()
        
    def move(self, x, y):
        self.pieces[x + (y*self.width)].move()

    def mark_moves(self, player):
        """ 
        Marks all 'BOARD' pieces that are valid moves as 'MOVE' pieces 
        for the current player. 
        """        
        for p in self.pieces:
            if p.get_state() == player:
                #for d in DIRECTIONS:
                #    self.mark_move(player, p, d)
                [self.mark_move(player, p, d) for d in DIRECTIONS]

    def mark_move(self, player, piece, direction):
        x, y = piece.get_position()
        opponent = BLACK if player == WHITE else WHITE
        tile = (x + (y * WIDTH)) + direction      
        if self.pieces[tile].get_state() == opponent:
            while self.pieces[tile].get_state() == opponent:
                tile += direction
            if self.pieces[tile].get_state() == BOARD:
                self.pieces[tile].move()      

    def make_move(self, coordinates):
        print(coordinates)
            

class Piece(object):
    """Pieces are laid out on the board on an 8x8 grid."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 'BOARD'
        self.flipped = False

        self.drawing = {
            "WHITE":self.draw_white, 
            "BLACK":self.draw_black, 
            "BOARD":self.draw_board, 
            "MOVE" :self.draw_move}

    def draw(self):        
        if self.state in self.drawing:
            self.drawing[self.state]()
            
        self.flipped = False

    def draw_white(self):
        if self.flipped:
            sys.stdout.write(
                clr.format_color('><', fg=clr.rgb(4,4,4), bg=clr.rgb(5,5,5)))
        else:
            sys.stdout.write(clr.format_color('  ', bg=clr.rgb(5,5,5)))


    def draw_black(self):
        if self.flipped:
            sys.stdout.write(
                clr.format_color('><', fg=clr.rgb(2,2,2), bg=clr.rgb(1,1,1)))
        else:
            sys.stdout.write(clr.format_color('  ', bg=clr.rgb(1,1,1)))

    def draw_board(self):
        sys.stdout.write(clr.format_color('  ', bg=clr.rgb(0,3,0)))

    def draw_move(self):
        sys.stdout.write(
            clr.format_color('><', fg=clr.rgb(5,0,0), bg=clr.rgb(0,3,0)))

    def set_black(self):
        self.state = 'BLACK'
    
    def set_white(self):
        self.state = 'WHITE'

    def flip(self):
        if self.state == 'BLACK': 
            self.state = 'WHITE'
        elif self.state == 'WHITE': 
            self.state = 'BLACK'
        self.flipped = True

    def move(self):
        self.state = 'MOVE'

    def get_position(self):
        return (self.x, self.y)

    def get_state(self):
        return self.state  

def main():
    """ Reversi game with human player vs AI player """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Action timeout for the AI, in ms (default=5000 ms).", type=int, default=5000)
    parser.add_argument('--colour', help="The colour you want to play as (default=white).", type=str, default='WHITE')
    parser.add_argument('--display-moves', help="Whether legal moves should be displayed or not.", action='store_true')
    args = parser.parse_args()

    if args.timeout < 0: exit()

    print("EDA132> Reversi")
    
    # Initialize game
    # Begin game loop 
        
    game = Game(args.timeout, args.colour, args.display_moves)
    game.run()
    

if __name__ == "__main__":
    main()
