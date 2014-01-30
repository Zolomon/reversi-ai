#!/usr/bin/python3

import os
import argparse
import sys

import color as clr

class Game(object):
    def __init__(self, timeout=1000, colour='WHITE', display_moves=True):
        self.board = Board()
        self.timeout = timeout

        self.player = colour
        self.display_moves = display_moves

        self.board.set_black(4,3)
        self.board.set_black(3,4)
        self.board.set_black(3,5)
        self.board.set_white(3,3)
        self.board.set_white(4,4)

        #self.board.move(5,5)
        self.board.mark_moves(self.player)

    def run(self):
        while True:
            os.system('clear')
            print("Playing as:       " + self.player)
            print("Displaying moves: " + str(self.display_moves))
            self.board.draw()
            event = input('')
            
            if event == 'quit': 
                break
            else: 
                pass
    

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
                for d in DIRECTIONS:
                    self.mark_move(player, p, d)

    def mark_move(self, player, piece, direction):
        x, y = piece.get_position()
        opponent = BLACK if player == WHITE else WHITE
        tile = (x + (y * WIDTH)) + direction      
        if self.pieces[tile].get_state() == opponent:
            while self.pieces[tile].get_state() == opponent:
                tile += direction
            if self.pieces[tile].get_state() == BOARD:
                self.pieces[tile].move()      
            

class Piece(object):
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
