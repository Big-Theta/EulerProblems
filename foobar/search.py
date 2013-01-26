#!/usr/bin/env python2

import argparse
import os

import bredth_first_search
import depth_first_search
import iterative_deepening_by_steps
import iterative_shortening_by_steps
import memoryless_depth_first_search
import lowest_cost_search


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description=("CS 570 -- Project one -- searcher\n"
                         "Search algorithms:\n"
                         "bfs -- bredth first search\n"
                         "dfs -- depth first search\n"
                         "idbs -- iterative deepening by steps\n"
                         "isbs -- iterative shortening by steps\n"
                         "lcs -- lowest cost search\n"
                         "mdfs -- memoryless depth first search\n"))
    parser.add_argument("-m", "--maze", type=str, default="random",
                        help="The input maze filename.")
    parser.add_argument("-s", "--search", type=str,
                        help="The search algorithm. E.g. -s lcs")
    parser.add_argument("-d", "--display", type=str, default="full",
                        help="Display options: full, stats")

    args = parser.parse_args()

    if args.search == 'bfs':
        Search = bredth_first_search.BredthFirstSearch
    elif args.search == 'dfs':
        Search = depth_first_search.DepthFirstSearch
    elif args.search == 'idbs':
        Search = iterative_deepening_by_steps.IterativeDeepeningByStepsSearch
    elif args.search == 'isbs':
        Search = iterative_shortening_by_steps.IterativeShorteningByStepsSearch
    elif args.search == 'lcs':
        Search = lowest_cost_search.LowestCostSearch
    elif args.search == 'mdfs':
        Search = memoryless_depth_first_search.MemorylessDepthFirstSearch
    else:
        print 'Search ' + args.search + ' not recognized.'

    if args.maze == 'random':
        args.maze = 'random_maze.txt'
        os.system("./generate_map.py -o " + args.maze)

    search = Search(args.maze)
    search.process()

    # TODO Fix display options
    search.display_maze()

