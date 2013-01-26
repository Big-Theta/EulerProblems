from base_search import *

class IterativeDeepeningByStepsSearch(BaseSearch):
    def __init__(self, maze_file):
        self.current_max_depth = 1
        BaseSearch.__init__(self, maze_file)

    def depth_iteration(self):
        self.open_spots = []
        self.closed_spots = []
        self.add_to_open(self.start)
        self.current_max_depth += 1

    def add_to_closed(self, to_add):
        BaseSearch.add_to_closed(self, to_add)
        self.closed_spots.append(to_add)

    def add_to_open(self, to_add):
        """Indicates that to_add needs to be evaulated.

        If to_add is in the closed list, it is the responsibility of this method
        to recognize that fact and deal with it appropriately.

        """
        BaseSearch.add_to_open(self, to_add)
        element_open = spot_is_in_list(to_add, self.open_spots)
        element_closed = spot_is_in_list(to_add, self.closed_spots)

        if to_add.steps > self.current_max_depth:
            return
        elif element_open and to_add.steps < element_open.steps:
            self.open_spots.remove(element_open)
            self.open_spots.append(to_add)
        elif element_closed and to_add.steps < element_closed.steps:
            self.closed_spots.remove(element_closed)
            self.open_spots.append(to_add)
        elif not (element_open or element_closed):
            self.open_spots.append(to_add)

    def get_next_open(self):
        """Removes the next spot that needs to be evaluated and returns it."""
        if not self.open_spots:
            self.depth_iteration()
        spot = self.open_spots[-1]
        self.open_spots = self.open_spots[:-1]
        return spot


def main():
    idbs = IterativeDeepeningByStepsSearch('map.txt')
    idbs.process()
    idbs.display_maze()

if __name__ == '__main__':
    main()

