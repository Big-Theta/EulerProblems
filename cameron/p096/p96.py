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
        all_sudoku[1].display()
        for s in all_sudoku:
            ans += s.get_euler_number()
        print ans

class Sudoku:
    def _takens(self, group): #return taken numbers in the group
        takens = []
        for n in group:
            takens += [n.get_state()[0]]
        return set(takens)

    def _replace_zeros(self):
        modified = False
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in self.rows:
            for n in row:
                if n.get_state()[0] == 0:
                    row_takens = self._takens(self.rows[n.get_row_i()])
                    col_takens = self._takens(self.cols[n.get_col_i()])
                    sect_takens = self._takens(self.sectors[n.get_sect_i()])
                    n.set_state(list((row_takens | col_takens | sect_takens) ^ set(possibles)))
                    if len(n.get_state()) == 2:
                        n.set_state([n.get_state()[1]])
                        modified = True
        if modified:
            self._replace_zeros()

    #def _eliminate(self):

    def get_euler_number(self):
        while not self.solved:
            self.solved = True
        #self.display()
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
        #self.display()

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

    def set_state(self, state):
        self.state = state

    def __init__(self, row_i, col_i, sect_i, state):
        self.row_i = row_i
        self.col_i = col_i
        self.sect_i = sect_i
        self.state = [state]

if __name__ == "__main__":
    p = Euler96()
