#!/usr/bin/python3

import os
import argparse
import sys

import color as clr

class Game(object):
    def __init__(self, timeout=1000):
        self.board = Board()
        self.timeout = timeout

        self.board.set_black(4,3)
        self.board.set_black(3,4)
        self.board.set_white(3,3)
        self.board.set_white(4,4)
        self.board.flip(4,4)
        self.board.flip(3,4)

        self.board.move(5,5)

    def run(self):
        while True:
            self.board.draw()
            event = input('')
            
            if event == 'quit': 
                break
            else: 
                pass

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
            sys.stdout.write(clr.format_color('><', 
                                                  fg=clr.rgb(4,4,4), 
                                                  bg=clr.rgb(5,5,5)))
        else:
            sys.stdout.write(clr.format_color('  ', bg=clr.rgb(5,5,5)))


    def draw_black(self):
        if self.flipped:
            sys.stdout.write(clr.format_color('><', 
                                                  fg=clr.rgb(2,2,2), 
                                                  bg=clr.rgb(1,1,1)))
        else:
            sys.stdout.write(clr.format_color('  ', bg=clr.rgb(1,1,1)))

    def draw_board(self):
        sys.stdout.write(clr.format_color('  ', bg=clr.rgb(0,3,0)))

    def draw_move(self):
        sys.stdout.write(clr.format_color('><', 
                                                  fg=clr.rgb(5,0,0), 
                                                  bg=clr.rgb(0,3,0)))

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
    

class Board(object):
    def __init__(self):
        self.width = 8
        self.height = 8
        self.pieces = list((Piece(x, y) 
                       for x in range(0, self.width) 
                       for y in range(0, self.height)))

    def draw(self):
        os.system('clear')

        labels = "  a b c d e f g h"
        sys.stdout.write(labels)
                
        size = self.width * self.height
        i = 0
        for p in self.pieces:
            if i % 8 == 0:                 
                print()
                print(str(int(i/8)+1), end=' ')
                
            p.draw()

            i += 1
        print()

    def set_white(self, x, y):
        self.pieces[x + (y*self.width)].set_white()

    def set_black(self, x, y):
        self.pieces[x + (y*self.width)].set_black()

    def flip(self, x, y):
        self.pieces[x + (y*self.width)].flip()
        
    def move(self, x, y):
        self.pieces[x + (y*self.width)].move()

def main():
    """ Reversi game with human player vs AI player """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Action timeout for the AI, in ms (default=5000 ms).", type=int, default=5000)
    args = parser.parse_args()

    if args.timeout < 0: exit()

    print("EDA132> Reversi")
    
    # Initialize game
    # Begin game loop 
        
    game = Game(args.timeout)
    game.run()
    

if __name__ == "__main__":
    main()
