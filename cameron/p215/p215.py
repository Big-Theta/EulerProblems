#!/usr/bin/python

from brick import *

def p215(width, height):
    wall = []
    build_wall(width, [0], wall)
    print wall[0]
    print wall[-1]
    print "wall length is %i" % len(wall)
    adj = {}
    for i, row in enumerate(wall):
        adj[i] = []
        for j, possible_row in enumerate(wall):
            if not intersect(row, possible_row):
                adj[i] = adj[i] + [j]
                """
                print "Match"
                print row
                print possible_row
                print ""
                """
        print str(i) + " " + str(adj[i])

def build_wall(width, breaks, rows):
    if breaks[-1] < width:
        build_wall(width, breaks + [breaks[-1] + 2], rows)
        build_wall(width, breaks + [breaks[-1] + 3], rows)
    elif breaks[-1] == width:
        rows.append(breaks[1:-1])

def intersect(a, b):
    for x in a:
        if x in b:
            return True
    return False

if __name__ == "__main__":
    p215(9, 3)
