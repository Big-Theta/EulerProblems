import re
import copy
import time


gBoards = []

class Board(object):
    def __init__(self, number, text_arr):
        self.number = number
        self.grid = [[] for _ in range(9)]

        for i, line in enumerate(text_arr):
            for ch in line:
                if ch == '0':
                    illegals = set()
                    for x in range(1, 10):
                        illegals.add(x)

                    self.grid[i].append(illegals)
                else:
                    self.grid[i].append(int(ch))

    def grid_hash(self):
        return self.grid[0][0] * 100 + self.grid[0][1] * 10 + self.grid[0][2]

    def board_copy(self):
        return copy.deepcopy(self)

    def is_reduced(self):
        for x in range(9):
            for y in range(9):
                if isinstance(self.grid[x][y], set):
                    return False
        return True

    def reduce_grid(self):
        reduced_f = True
        while reduced_f:
            reduced_f = False
            for x in range(9):
                for y in range(9):
                    if self.reduce_spot(x, y):
                        reduced_f = True
                    if (isinstance(self.grid[x][y], set) and
                        len(self.grid[x][y]) == 1):
                        self.grid[x][y] = int(self.grid[x][y].pop())
                        reduced_f = True


    def reduce_spot(self, x, y):
        if isinstance(self.grid[x][y], int):
            return False
        pre_reduced_size = len(self.grid[x][y])

        # Row
        for i in range(9):
            if i != y and isinstance(self.grid[x][i], int):
                self.grid[x][y].discard(self.grid[x][i])

        # Col
        for i in range(9):
            if i != x and isinstance(self.grid[i][y], int):
                self.grid[x][y].discard(self.grid[i][y])

        # Square
        if 0 <= x <= 2:
            x_range = range(0, 3)
        elif 3 <= x <= 5:
            x_range = range(3, 6)
        else:
            x_range = range(6, 9)

        if 0 <= y <= 2:
            y_range = range(0, 3)
        elif 3 <= y <= 5:
            y_range = range(3, 6)
        else:
            y_range = range(6, 9)

        for i in x_range:
            for j in y_range:
                if i == x and j == y:
                    continue
                if isinstance(self.grid[i][j], int):
                    self.grid[x][y].discard(self.grid[i][j])

        if pre_reduced_size == len(self.grid[x][y]):
            return False
        else:
            return True


    def view(self):
        print
        print '==========='
        print self.number
        for l in self.grid:
            print l

    def print_grid(self):
        time.sleep(0.01)
        print
        print "==========="
        print self.number
        for i in range(9):
            if i % 3 == 0:
                print "========================="
            for j in range(9):
                if j % 3 == 0:
                    print "|",
                if isinstance(self.grid[i][j], int):
                    print self.grid[i][j],
                else:
                    print '.',
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

            gBoards.append(Board(number, lines))


def test_gen_text_arr():
    gBoards.append(Board(
            0,
            [
                '003020600',
                '900305001',
                '001806400',
                '008102900',
                '700000008',
                '006708200',
                '002609500',
                '800203009',
                '005010300']
        ))


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


if __name__ == '__main__':
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

