from base_search import *

class IterativeShorteningByStepsSearch(BaseSearch):
    def __init__(self, maze_file):
        self.current_max_depth = 0
        self.last_solution = None
        BaseSearch.__init__(self, maze_file)

    def shorten_iteration(self, final_spot):
        self.open_spots = []
        self.closed_spots = []
        self.add_to_open(self.start)
        self.current_max_depth -= 1

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

        if self.current_max_depth and to_add.steps > self.current_max_depth:
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
        if self.open_spots:
            spot = self.open_spots[-1]
            self.open_spots = self.open_spots[:-1]
            return spot
        else:
            self.display_maze(self.last_solution)
            exit()
            return False

    def is_goal(self, spot):
        if BaseSearch.is_goal(self, spot):
            self.last_solution = spot
            if self.current_max_depth == 0 or spot.steps < self.current_max_depth:
                self.current_max_depth = spot.steps
            self.shorten_iteration(spot)
            return self.get_next_open()
        else:
            return spot

    def single_step(self):
        self.stats_steps += 1
        to_evaluate = self.get_next_open()
        if not isinstance(to_evaluate, bool):
            to_evaluate = self.is_goal(to_evaluate)

        self.add_to_closed(to_evaluate)
        for adjacent in self.get_all_adjacent(to_evaluate):
            self.add_to_open(adjacent)

        return False


def main():
    search = IterativeShorteningByStepsSearch('new_map.txt')
    search.process()
    search.display_maze()

if __name__ == '__main__':
    main()

