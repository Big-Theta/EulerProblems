from base_search import *

class BredthFirstSearch(BaseSearch):
    def add_to_closed(self, to_add):
        BaseSearch.add_to_closed(self, to_add)
        self.closed_spots.append(to_add)

    def add_to_open(self, to_add):
        """Indicates that to_add needs to be evaulated.

        If to_add is in the closed list, it is the responsibility of this method
        to recognize that fact and deal with it appropriately.

        """
        BaseSearch.add_to_open(self, to_add)
        if (spot_is_in_list(to_add, self.closed_spots) or
            spot_is_in_list(to_add, self.open_spots)):
            return
        else:
            self.open_spots.append(to_add)

    def get_next_open(self):
        """Removes the next spot that needs to be evaluated and returns it."""
        if self.open_spots:
            spot = self.open_spots[0]
            self.open_spots = self.open_spots[1:]
            return spot
        else:
            return False


def main():
    bfs = BredthFirstSearch('new_map.txt')
    bfs.process()
    bfs.display_maze()

if __name__ == '__main__':
    main()

