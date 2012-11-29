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
        all_sudoku[2].display()
        all_sudoku[2].get_euler_number()
        all_sudoku[2].display()
        """
        for s in all_sudoku:
            ans += s.get_euler_number()
        print ans
        """

class Sudoku:
    def is_solved(self):
        if self._valid():
            for g in self.rows:
                for n in g:
                    if n.get_state()[0] == 0:
                        return False
            return True
        else:
            return False

    def _takens(self, group): #return taken numbers in the group
        takens = []
        for n in group:
            takens += [n.get_state()[0]]
        return set(takens)

    def _valid(self):
        for g_collection in [self.rows, self.cols, self.sectors]:
            for g in g_collection:
                if not self._valid_group(g):
                    return False
        return True

    def _valid_group(self, group):
        takens = []
        for n in group:
            n_state = n.get_state()[0]
            if n_state not in takens:
                takens += [n_state]
            elif n_state != 0:
                #print "invalid group found", takens
                return False
        #print "valid group", takens
        return True

    def _narrow_possibles(self):
        possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for row in self.rows:
            for n in row:
                if n.get_state()[0] == 0:
                    row_takens = self._takens(self.rows[n.get_row_i()])
                    col_takens = self._takens(self.cols[n.get_col_i()])
                    sect_takens = self._takens(self.sectors[n.get_sect_i()])
                    prev_state = n.get_state()
                    n.set_state(list((row_takens | col_takens | sect_takens) ^ set(possibles)))
                    if n.get_col_i() == 4 and n.get_row_i() == 2:
                        print n.get_state(), "is this ever 6?"
                    if len(n.get_state()) == 1 and n.get_state()[0] == 0:
                        n.set_state(prev_state)
                        return False
                    if len(n.get_state()) == 2:
                        prev_state = n.get_state()
                        n.set_state([n.get_state()[1]])
                        if n.get_col_i() == 4 and n.get_row_i() == 2:
                            print n.get_state(), "is this ever 6?"
                        if self._valid() and self._narrow_possibles():
                            return True
                        else:
                            n.set_state(prev_state)
                            if n.get_col_i() == 4 and n.get_row_i() == 2:
                                print self._valid()
                                print n.get_state(), "is this ever unset?"
                            return False
        if not self.is_solved():
            self.display()
            return self._guess()
        else:
            return True

    def _guess(self):
        absurd_node = Node(0, 0, 0, 0)
        absurd_node.set_state([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        best_guess = absurd_node
        best_guess_len = len(absurd_node.get_state())
        for g in self.rows:
            for n in g:
                n_state_len = len(n.get_state())
                if n_state_len > 2 and n_state_len < best_guess_len:
                    best_guess = n
                    best_guess_len = n_state_len
        if best_guess == absurd_node:
            if self._valid() and self.is_solved():
                print "it's solved"
                return True
            else:
                return False
        prev_state = best_guess.get_state()
        the_guess_is_good = False
        for guess in prev_state[1:]:
            best_guess.set_state([guess])
            the_guess_is_good = self._narrow_possibles()
            if the_guess_is_good:
                print "good guess", best_guess.get_state()
                break
            #else:
                #print "bad move at ", n.get_col_i(), n.get_row_i(), "guess", n.get_state(), prev_state
        print "hmm", best_guess.get_state(), best_guess.get_col_i(), best_guess.get_row_i()


    def get_euler_number(self):
        #while not self.is_solved():
        self._narrow_possibles()
        """
        while not self.is_solved():
            print "didn't solve"
            #self._guess():
            
            """
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
