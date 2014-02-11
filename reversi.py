#!/usr/bin/env python3

import argparse
from game.game import Game


def main():
    """ Reversi game with human player vs AI player """

    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', help="Number of seconds the brain is allowed to think before making its move.",
                        type=int, default=20)
    parser.add_argument('--display-moves', help="Whether legal moves should be displayed or not.", action='store_true')
    parser.add_argument('--colour', help="Display the game in 256 colours.", action='store_true')

    args = parser.parse_args()

    if args.timeout < 0:
        exit()

    print("EDA132> Reversi")

    # Initialize game
    # Begin game loop

    game = Game(timeout=args.timeout,
                display_moves=args.display_moves,
                colour=args.colour)
    game.run()


if __name__ == "__main__":
    main()
