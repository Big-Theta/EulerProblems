from depth_first_search import *

class MemorylessDepthFirstSearch(DepthFirstSearch):
    def add_to_open(self, to_add):
        """Indicates that to_add needs to be evaulated.

        If to_add is in the closed list, it is the responsibility of this method
        to recognize that fact and deal with it appropriately.

        """
        BaseSearch.add_to_open(self, to_add)
        if spot_is_in_list(to_add, self.closed_spots):
            return
        else:
            self.open_spots.append(to_add)


def main():
    mdfs = MemorylessDepthFirstSearch('map.txt')
    mdfs.process()
    mdfs.display_maze()

if __name__ == '__main__':
    main()

