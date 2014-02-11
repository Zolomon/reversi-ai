reversi-ai
==========
![](http://raw.github.com/Zolomon/reversi-ai/master/reversi.gif)

A text based python implementation of Reversi with an artificial intelligence as opponent.

Table of Contents
=================

1. Requirements
2. How to Install and Run
3. What is it? 


###1. Requirements
Requirements:
* Python 3.2

The application was only tested on Ubuntu 13.10 and Mac OS X 10.8.5 with successful results.

###2. How to Install and Run
`
$ mkdir reversi
$ cd reversi
$ wget https://github.com/Zolomon/reversi-ai/archive/master.zip
$ unzip master.zip 
$ cd reversi-ai-master/
$ chmod +x reversi.py
$ ./reversi.py --help
$ ./reversi.py --colour 
$ #python3 reversi.py --colour
`
###3. What is it?
`reversi-ai` is an implementation of the game Reversi where you can face the computer, or 
watch two artificial intelligences battle it out against each other. 

The game is implemented in Python (3.x) and consists of a few different components. 

At the top is the `reversi.py` file which contains the common "main" function which starts the application. 
This takes care of parsing command line arguments and constructing the `Game` object which handles the game 
specific parts of the application. 

The `Game` class exists inside the `game/game.py` file. The `Game` object creates the `Board` object which 
is used as the front-end for the game. `Game` also initializes the values needed for the game to be played. 
The essence of the `Game` object is its `run` function which mimics the common `REPL` (read-eval-print-loop). 
It will render the current game state, ask for user input, process the input and then repeat from the first step. 

The `Game` object holds information about the players in the shape of two controllers. A 
`Controller` (in `game/controllers.py`) can be either an `PlayerController` or an `AiController`. 
The `PlayerController` will parse input from the user through the console into a valid move command, or Ctrl+D to quit 
the game. The `AiController` will parse the current state and pass that information on to the `Brain` (in `game/brain.py`)
which in turn will create an instance of the `AlphaBetaPruner` (in `game/ai.py`) in a second thread. 

This allows the user to easily output extra information or capture user input while the `Brain` is performing its calculations. 
However, only simple output is done to signal that the application has not crashed. 

The `AlphaBetaPruner` (`ABP`) is an implementation of the Minimax algorithm with the Alpha-Beta Pruning optimization. 
The `ABP` is implemented using a list of integers to represent the board, a more optimized way would have been to just use 
three 64 bit integers and bitwise operators, but this was the first representation that came to mind so I went with this.  
In the implementation of the `ABP`, the most interesting function is the `evaluation` function. 

This is what can actually be considered the brain of the whole artificial intelligence, here is where the actual state evaluation is performed. The following evaluations are used; whether the player has more bricks than its opponent, how many player bricks are located on the edges (edge bricks are important in order to control flipping of the opponent's bricks), how many player bricks are in the corners which are also very important strategically. 
