#!/usr/bin/python


"""
takes text file of unsolved sudoku and solves them.
"""
class Euler96:
    def build_sudoku_games(self):
        f = open("sudoku.txt", 'r')
        all_sudoku = []
        line_num = 1
        raw_data = []
        for line in f:
            if line_num % 10 != 1:
                for i in range(9):
                    raw_data += [int(line[i])]
            elif line_num != 1:
                s = Sudoku(raw_data)
                all_sudoku.append(s)
                raw_data = []
            line_num += 1
        return all_sudoku

    def __init__(self):
        ans = 0
        all_sudoku = self.build_sudoku_games()
        #all_sudoku[0].display()
        print all_sudoku[0].get_euler_number()
        #for s in all_sudoku:
        #    ans += s.get_euler_number()

class Sudoku:
    def _replace_zeros(self):
    """

    FINISH HERE

    """

    #def _eliminate(self):
        

    def get_euler_number(self):
        while not self.solved:
            self.solved = True
        en = self.rows[0][0].get_state()[0]
        en = (en * 10) + self.rows[0][1].get_state()[0]
        return (en * 10) + self.rows[0][2].get_state()[0]

    def _parse_data(self, raw_data):
        node_list = []
        for data_i, data in enumerate(raw_data):
            row_i, col_i = divmod(data_i, 9)
            sect_i = (col_i / 3) + (3 * ( row_i / 3))
            new_node = Node(row_i, col_i, sect_i, data)
            node_list += [new_node]

        for i in range(9):
            self.rows += [[]]
            self.cols += [[]]
            self.sectors += [[]]

        for n in node_list:
            self.solved = False
            self.rows[n.get_row_i()] += [n]
            self.cols[n.get_col_i()] += [n]
            self.sectors[n.get_sect_i()] += [n]

    def display(self):
        for row in self.rows:
            for n in row:
                print n.get_state()[0],
            print ""

        print "\n\n"


    def __init__(self, raw_data): #data should be list of 81 ints
        self.rows = [] #9 groups of nodes go here. Index matters.
        self.cols = [] #9 groups of nodes go here. Index matters.
        self.sectors = [] #9 groups of nodes go here. Index matters.

        self._parse_data(raw_data)
        self._replace_zeros()

"""
node of a sudoku game.
"""
class Node:
    def display(self):
        print "row %i, col %i: %i", (row_i, col_i, state)

    def get_row_i(self):
        return self.row_i

    def get_col_i(self):
        return self.col_i

    def get_sect_i(self):
        return self.sect_i

    def get_state(self):
        return self.state

    def __init__(self, row_i, col_i, sect_i, state):
        self.row_i = row_i
        self.col_i = col_i
        self.sect_i = sect_i
        self.state = [state]

if __name__ == "__main__":
    p = Euler96()
