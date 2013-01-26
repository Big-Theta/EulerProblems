import abc
from spot import *

def construct_path_list(start, stop):
    path = [stop]
    prev = stop.prev_spot
    while prev and prev != start:
        path.append(prev)
        prev = prev.prev_spot
    path.append(start)
    return path


class IllegalSpotException(Exception):
    pass


class BaseSearch(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, maze_file):
        self.read_maze_file(maze_file)
        self.open_spots = []
        self.closed_spots = []
        self.stats_steps = 0
        self.stats_max_open = 0
        self.stats_max_closed = 0
        self.add_to_open(self.start)

    def display_maze(self, final_spot=None):
        if not final_spot:
            try:
                final_spot = self.final
            except:
                final_spot = self.start
        path = construct_path_list(self.start, final_spot)

        print "|==================================="
        print "| Evaluation steps taken:       ", self.stats_steps
        print "| Maximum num open possitions:  ", self.stats_max_open
        print "| Final num open possitions:    ", len(self.open_spots)
        print "| Maximum num closed possitions:", self.stats_max_closed
        print "| Length of final solution:     ", final_spot.steps
        print "| Cost of final solution:       ", final_spot.cost
        print "|==================================="

        for y, row in enumerate(self.maze):
            for x, terrain in enumerate(row):
                candidate = Spot(x, y)
                if candidate == self.start:
                    # green
                    to_print = "\033[1;32m{0}\033[0m".format(terrain)
                elif candidate == self.goal:
                    # yellow
                    to_print = "\033[1;33m{0}\033[0m".format(terrain)
                elif spot_is_in_list(candidate, path):
                    # blue
                    to_print = "\033[1;34m{0}\033[0m".format(terrain)
                elif spot_is_in_list(candidate, self.closed_spots):
                    # red
                    to_print = "\033[1;31m{0}\033[0m".format(terrain)
                elif spot_is_in_list(candidate, self.open_spots):
                    # magenta
                    to_print = "\033[1;35m{0}\033[0m".format(terrain)
                else:
                    # black/gray
                    to_print = "\033[1;30m{0}\033[0m".format(terrain)
                print to_print,
            print

    def read_maze_file(self, maze_file):
        with open(maze_file, 'r') as fin:
            self.width, self.height = fin.readline().split()
            self.width = int(self.width)
            self.height = int(self.height)

            self.start = Spot(*fin.readline().split())
            self.start.cost = 0
            self.start.steps = 0
            self.goal = Spot(*fin.readline().split())

            self.maze = []
            for line in fin.readlines():
                self.maze.append(line.split()[0])

    def get_enter_cost(self, spot):
        """Returns the cost of moving into the indicated spot.

        Raises IllegalSpotException

        """
        if (spot.X < 0 or spot.X >= self.width or
            spot.Y < 0 or spot.Y >= self.height):
            raise IllegalSpotException(
                    "spot ({spot.X}, {spot.Y}) is out of bounds.".format(spot=spot))

        terrain = self.maze[spot.Y][spot.X]
        if terrain == 'R':
            return 1
        elif terrain == 'f':
            return 2
        elif terrain == 'F':
            return 4
        elif terrain == 'h':
            return 5
        elif terrain == 'r':
            return 7
        elif terrain == 'M':
            return 10
        elif terrain == 'W':
            raise IllegalSpotException("The terrain 'W' cannot be entered.")
        else:
            raise IllegalSpotException("The terrain '{0}' is not recognized.".format(terrain))

    @abc.abstractmethod
    def add_to_closed(self, to_add):
        new_size = len(self.closed_spots)
        if new_size > self.stats_max_closed:
            self.stats_max_closed = new_size

    @abc.abstractmethod
    def add_to_open(self, to_add):
        """Indicates that to_add needs to be evaulated.

        If to_add is in the closed list, it is the responsibility of this method
        to recognize that fact and deal with it appropriately.

        """
        new_size = len(self.open_spots)
        if new_size > self.stats_max_open:
            self.stats_max_open = new_size

    @abc.abstractmethod
    def get_next_open(self):
        """Removes the next spot that needs to be evaluated and returns it."""
        pass

    def get_all_adjacent(self, spot):
        """Returns a list of all adjacent spots to spot.

        These spots will all be legal, but they may appear in the closed list.

        """
        retlist = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            try:
                new_spot = Spot(spot.X + x, spot.Y + y)
                new_spot.cost = spot.cost + self.get_enter_cost(new_spot)
                new_spot.steps = spot.steps + 1
                new_spot.prev_spot = spot
                retlist.append(new_spot)
            except IllegalSpotException:
                pass
        return retlist

    def single_step(self):
        self.stats_steps += 1
        to_evaluate = self.get_next_open()
        if self.is_goal(to_evaluate):
            return to_evaluate

        self.add_to_closed(to_evaluate)
        for adjacent in self.get_all_adjacent(to_evaluate):
            self.add_to_open(adjacent)

        return False

    def process(self):
        final = self.single_step()
        while not final:
            final = self.single_step()
        self.final = final

    def is_goal(self, spot):
        if self.goal == spot:
            return True
        else:
            return False

def main():
    BaseSearch((0, 0), (0, 0), 'map.txt')

if __name__ == '__main__':
    main()

