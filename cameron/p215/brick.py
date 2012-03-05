#!/usr/bin/python

class Brick:
    def __init__(self, width):
        self.width = width

    def next_brick(self, width):
        self.left = Brick(2)
        self.right = Brick(3)


class Row:
    def __init__(self, width):
        self.width = width
        self.top = Brick(0)
        self
