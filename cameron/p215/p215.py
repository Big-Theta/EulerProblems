#!/usr/bin/python

from brick import *

def p215(width, height):
    wall = []
    build_wall(width, [0], wall)
    path_count = [1] * len(wall)
    print "Done building wall. %i possible rows" % len(wall)
    adj = {}
    for i, row in enumerate(wall):
        adj[i] = []
        for j, possible_row in enumerate(wall):
            if not intersect(row, possible_row):
                adj[i] = adj[i] + [j]
        #print str(i) + " " + str(adj[i])
    print "Done finding adjacencies."
    for x in range(1, height):
        path_count = add_routes(path_count, adj)
    total_paths = 0
    for x in path_count:
        total_paths += x
    print total_paths

def add_routes(current_count, adj):
    path_count = [0] * len(current_count)
    for key, adjacencies in adj.iteritems():
        for adjacency in adjacencies:
            path_count[key] += current_count[adjacency]
    return path_count

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
    p215(32, 10)
