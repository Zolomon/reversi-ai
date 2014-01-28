#!/usr/bin/python3

import os
import argparse
import sys

class Game(object):
    def __init__(self, timeout=1000):
        self.board = Board()
        self.timeout = timeout

    def run(self):
        while True:
            self.board.draw()
            event = input('')
            
            if event == 'quit': 
                break
            else: 
                pass

class Board(object):
    def __init__(self):
        self.width = 8
        self.height = 8

    def draw(self):
        os.system('clear')

        labels = "  a b c d e f g h\n"
        sys.stdout.write(labels)

        size = self.width * self.height
        for x in range(size+1):
            if x == (size): 
                sys.stdout.write('x\n')
            elif x % 8 == 0 and x != 0: 
                sys.stdout.write('x\n' + str(int(x / 8) + 1) + ' ')
            elif x == 0:
                sys.stdout.write('1 ')
            else: 
                sys.stdout.write('x ')

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
