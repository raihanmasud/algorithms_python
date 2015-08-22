__author__ = 'raihan'

from Node import Node

class Queue:

    def __init__(self):
        self.queue = []
        self.front = 0
        self.back = 0

    def enqueue(self, item):
        self.queue.insert(self.back, item)
        self.back += 1

    def deque(self):
        self.queue.pop(self.front)
        # self.front -= 1 ; for non pythonic implementation

    def peek(self):
        return self.queue[self.front]

    def is_empty(self):
        return len(self.queue) == 0


#test queue
