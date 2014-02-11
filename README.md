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
```
$ mkdir reversi
$ cd reversi
$ wget https://github.com/Zolomon/reversi-ai/archive/master.zip
$ unzip master.zip 
$ cd reversi-ai-master/
$ chmod +x reversi.py
$ ./reversi.py --colour # or...
$ #python3 reversi.py --colour
```
###3. What is it?
`reversi-ai` is an implementation of the game Reversi where you can face the computer, or 
watch two artificial intelligences battle it out against each other. 

The game is implemented in Python (3.x) and consists of a few different components. 

At the top is the `reversi.py` file which contains the common "main" function which starts the application. 
This takes care of parsing command line arguments and constructing the `Game` object which handles the game 
specific parts of the application. 

The `Game` class exists inside the `game/game.py` file. 
