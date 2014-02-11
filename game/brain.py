import datetime
import threading

__author__ = 'bengt'


class Brain(threading.Thread):
    def __init__(self, mutex, q, duration, board, colour):
        self.mutex = mutex
        self.q = q
        self.duration = duration
        threading.Thread.__init__(self)
        self.has_started = False
        self.lifetime = None

    def run(self):
        pruner = AlphaBetaPruner()

    def process_data(self):
        pass