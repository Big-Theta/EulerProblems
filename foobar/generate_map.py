#!/usr/bin/env python2

import argparse
from random import randint

def gen_map(outfile_name, width, height):
    maze = [[None for _ in range(width)] for _ in range(height)]

    for w_dex in range(0, width):
        for h_dex in range(0, height):
            my_rand = randint(0, 6)
            if my_rand == 0:
                terrain = 'R'
            elif my_rand == 1:
                terrain = 'f'
            elif my_rand == 2:
                terrain = 'F'
            elif my_rand == 3:
                terrain = 'h'
            elif my_rand == 4:
                terrain = 'r'
            elif my_rand == 5:
                terrain = 'M'
            else:
                terrain = 'W'

            maze[h_dex][w_dex] = terrain

    with open(outfile_name, 'w') as outfile:
        print >> outfile, width, height
        while True:
            start_x, start_y = randint(0, width - 1), randint(0, height - 1)
            if maze[start_y][start_x] != 'W':
                break
        print >> outfile, start_x, start_y
        while True:
            goal_x, goal_y = randint(0, width - 1), randint(0, height - 1)
            if maze[goal_y][goal_x] != 'W':
                break
        print >> outfile, goal_x, goal_y
        for row in maze:
            print >> outfile, ''.join(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CS 570 -- Project one -- maze generator")
    parser.add_argument("-o", "--output", type=str,
                        help="The output maze filename.")
    parser.add_argument("-W", "--width", type=int, default=0,
                        help="The maze width.")
    parser.add_argument("-H", "--height", type=int, default=0,
                        help="The maze height.")

    args = parser.parse_args()

    if not args.width:
        args.width = randint(20, 50)
    if not args.height:
        args.height = randint(20, 50)
    gen_map(args.output, args.width, args.height)

