import re
import copy
import time
import sys


gBoards = []

class Board(object):
    def __init__(self, number, text_arr):
        self.number = number
        # Configure constraints (no processing yet)
        self.row_pos = [set(range(1, 10)) for _ in range(9)]
        self.col_pos = [set(range(1, 10)) for _ in range(9)]
        self.nan_pos = [set(range(1, 10)) for _ in range(9)]

        self.grid = [[] for _ in range(9)]

        # Initialize the grid
        for i, line in enumerate(text_arr):
            for ch in line:
                ch = int(ch)
                if ch:
                    self.grid[i].append(set())
                    self.grid[i][-1].add(ch)
                else:
                    self.grid[i].append(set(range(1, 10)))


    def nantile(self, x, y):
        if 0 <= x <= 2 and 0 <= y <= 2:
            return self.nan_pos[0]
        elif 3 <= x <= 5 and 0 <= y <= 2:
            return self.nan_pos[1]
        elif 6 <= x <= 8 and 0 <= y <= 2:
            return self.nan_pos[2]
        if 0 <= x <= 2 and 3 <= y <= 5:
            return self.nan_pos[3]
        elif 3 <= x <= 5 and 3 <= y <= 5:
            return self.nan_pos[4]
        elif 6 <= x <= 8 and 3 <= y <= 5:
            return self.nan_pos[5]
        if 0 <= x <= 2 and 6 <= y <= 8:
            return self.nan_pos[6]
        elif 3 <= x <= 5 and 6 <= y <= 8:
            return self.nan_pos[7]
        elif 6 <= x <= 8 and 6 <= y <= 8:
            return self.nan_pos[8]

    def nantile_index(self, x, y):
        if 0 <= x <= 2 and 0 <= y <= 2:
            return 0
        elif 3 <= x <= 5 and 0 <= y <= 2:
            return 1
        elif 6 <= x <= 8 and 0 <= y <= 2:
            return 2
        if 0 <= x <= 2 and 3 <= y <= 5:
            return 3
        elif 3 <= x <= 5 and 3 <= y <= 5:
            return 4
        elif 6 <= x <= 8 and 3 <= y <= 5:
            return 5
        if 0 <= x <= 2 and 6 <= y <= 8:
            return 6
        elif 3 <= x <= 5 and 6 <= y <= 8:
            return 7
        elif 6 <= x <= 8 and 6 <= y <= 8:
            return 8


    def nantile_other_indecies(self, x, y):
        index = self.nantile_index(x, y)
        for i in range(9):
            for j in range(9):
                if (self.nantile_index(i, j) == index and
                    not (x == i and y == j)):
                    yield [i, j]


    def eliminate(self):
        while self._eliminate_update_constraints():
            for i in range(9):
                for j in range(9):
                    # Cell is not known
                    if len(self.grid[i][j]) != 1:
                        basic_eliminate = (self.grid[i][j] &
                                           self.col_pos[i] &
                                           self.row_pos[j] &
                                           self.nantile(i, j))

                        # XXX
                        self.grid[i][j] = basic_eliminate
                        continue

                        pos_elsewhere_col = set()
                        for offset in range(9):
                            if offset != i:
                                if len(self.grid[offset][j]) == 1:
                                    pos_elsewhere_col ^= self.grid[offset][j]
                        other_eliminate_col = set(range(1, 10)) - pos_elsewhere_col
                        pos_elsewhere_row = set()
                        for offset in range(9):
                            if offset != j:
                                if len(self.grid[i][offset]) == 1:
                                    pos_elsewhere_row ^= self.grid[i][offset]
                        other_eliminate_row = set(range(1, 10)) - pos_elsewhere_row

                        pos_elsewhere_nan = set()
                        for a, b in self.nantile_other_indecies(i, j):
                            if len(self.grid[a][b]) == 1:
                                pos_elsewhere_nan ^= self.grid[a][b]
                        other_eliminate_nan = set(range(1, 10)) - pos_elsewhere_nan

                        self.grid[i][j] = (basic_eliminate &
                                           other_eliminate_col &
                                           other_eliminate_row &
                                           other_eliminate_nan)


    def _eliminate_update_constraints(self):
        updated = False
        for i in range(9):
            for j in range(9):
                if len(self.grid[i][j]) == 1:
                    size_col = len(self.col_pos[i])
                    size_row = len(self.row_pos[j])
                    size_nan = len(self.nantile(i, j))
                    self.col_pos[i] -= self.grid[i][j]
                    self.row_pos[j] -= self.grid[i][j]
                    self.nan_pos[self.nantile_index(i, j)] -= self.grid[i][j]
                    if size_col != len(self.col_pos[i]):
                        updated = True
                    if size_row != len(self.row_pos[j]):
                        updated = True
                    if size_nan != len(self.nantile(i, j)):
                        updated = True
        return updated


    def grid_hash(self):
        return (self.grid[0][0] * 100 +
                self.grid[0][1] * 10 +
                self.grid[0][2])

    def board_copy(self):
        return copy.deepcopy(self)

    def is_solved(self):
        for x in range(9):
            for y in range(9):
                if len(self.grid[x][y]) != 1:
                    return False
        return True

    def view(self):
        print
        print "==========="
        print "Grid", self.number
        for i in range(9):
            if i % 3 == 0:
                print "========================="
            for j in range(9):
                if j % 3 == 0:
                    print "|",
                if len(self.grid[i][j]) == 1:
                    store = self.grid[i][j].pop()
                    print store,
                    self.grid[i][j].add(store)
                else:
                    print '.',
            print "|"
        print "========================="

    def view_num_pos(self):
        print
        print "==========="
        print "Grid", self.number, "num possible"
        for i in range(9):
            if i % 3 == 0:
                print "========================="
            for j in range(9):
                if j % 3 == 0:
                    print "|",
                print len(self.grid[i][j]),
            print "|"
        print "========================="


def gen_text_arrs():
    with open('./sudoku.txt', 'r') as fin:
        for _ in range(50):
            line = fin.readline()
            match = re.match(r"Grid (?P<number>\d+)$", line)
            lines = []
            if match:
                number = int(match.group('number'))
            for _ in range(9):
                lines.append(fin.readline().strip())

            yield Board(number, lines)


def test_gen_text_arr():
    yield Board(0, ['003020600',
                    '900305001',
                    '001806400',
                    '008102900',
                    '700000008',
                    '006708200',
                    '002609500',
                    '800203009',
                    '005010300'])


def populate_gBoards(board_gen):
    for board in board_gen:
        gBoards.append(board)


def backtrack(board, depth=0):
    copy = board.board_copy()
    copy.reduce_grid()
    if not copy.is_reduced():
        for i in range(9):
            for j in range(9):
                if isinstance(copy.grid[i][j], set):
                    for val in copy.grid[i][j]:
                        new_copy = copy.board_copy()
                        new_copy.grid[i][j] = val
                        new_copy.reduce_grid()
                        if new_copy.is_reduced():
                            return new_copy

        # single lookahead didn't work. Try double
        for size in range(2, 3):
            #print size
            for i in range(9):
                for j in range(9):
                    #copy.print_grid()
                    if (isinstance(copy.grid[i][j], set) and
                        len(copy.grid[i][j]) == size and
                        depth < 2):
                        for val in copy.grid[i][j]:
                            new_copy = copy.board_copy()
                            new_copy.grid[i][j] = val
                            new_copy = backtrack(new_copy, depth + 1)
                            if new_copy.is_reduced():
                                return new_copy

    return copy


def main():
    populate_gBoards(gen_text_arrs())
    count = 0
    for board in gBoards:
        board.eliminate()
        if board.is_solved():
            count += 1
    b = gBoards[6]
    #b.view_num_pos()
    '''
    b.view_num_pos()
    '''
    b.eliminate()
    '''
    b.view_num_pos()
    '''
    b.view()
    #b.view_num_pos()

    print count

if __name__ == '__main__':
    main()
    '''
    gen_text_arrs()
    #test_gen_text_arr()
    new_boards = []
    for board in gBoards:
        start = time.time()
        print "Starting", board.number, "...",
        new_boards.append(backtrack(board))
        if new_boards[-1].is_reduced():
            print "solved", new_boards[-1].grid_hash(), time.time() - start
        else:
            print "failed"
    gBoards = new_boards

    count = 0
    hash_total = 0
    for board in gBoards:
        if board.is_reduced():
            count += 1
            hash_total += board.grid_hash()

    print count
    print hash_total
    '''

