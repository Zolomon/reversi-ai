#!/usr/bin/python3

import argparse
from game.game import Game


def main():
    """ Reversi game with human player vs AI player """

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Action timeout for the AI, in ms (default=5000 ms).", type=int, default=5000)
    parser.add_argument('--start-colour', help="The colour you want to play as (default=white).", type=str, default='BLACK')
    parser.add_argument('--display-moves', help="Whether legal moves should be displayed or not.", action='store_true')
    parser.add_argument('--colour', help="Display the game in 256 colours.", action='store_true')
    args = parser.parse_args()

    if args.timeout < 0:
        exit()

    print("EDA132> Reversi")

    # Initialize game
    # Begin game loop

    game = Game(timeout=args.timeout, start_colour=args.start_colour, display_moves=args.display_moves, colour=args.colour)
    game.run()


if __name__ == "__main__":
    main()
