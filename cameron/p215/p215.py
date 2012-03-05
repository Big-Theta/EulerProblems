#!/usr/bin/python

from brick import *

def p215(width, height):
    wall = []
    build_wall(width, [0], wall)
    print wall[0]
    print wall[-1]
    for row in wall:
        

def build_wall(width, breaks, rows):
    if breaks[-1] < width:
        build_wall(width, breaks + [breaks[-1] + 2], rows)
        build_wall(width, breaks + [breaks[-1] + 3], rows)
    elif breaks[-1] == width:
        rows.append(breaks[1:-1])

if __name__ == "__main__":
    p215(32, 10)
