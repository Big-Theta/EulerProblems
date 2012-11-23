#!/usr/bin/python


#all_sudoku = [[rowsof9, colsof9, squaresof9], ...]
def build_sudoku_rows():
    f = open("sudoku.txt", 'r')
    sudoku = []
    raw = []
    line_num = 1
    for line in f:
        if line_num % 10 != 1:
            raw += [line]
        line_num += 1

    for i, line in enumerate(raw):
        if i % 9 == 0:
            sudoku += [[]]
        sudoku[-1] += [[]]
        for c in range(9):
            sudoku[-1][-1] += [int(line[c])]
    return sudoku

#def build_soduku_cols(all_sudoku

def make_blanks(sudoku):
    for game in sudoku:
        for row in game:
            for i, col in enumerate(row):
                if col == 0:
                    row[i] = []
    return sudoku

def get_sector(x, y):
    return x / 3 + 3 * (y / 3)

def sector_guide():
    sectors = []
    for x in range(9):
        sectors += [[0] * 9]
        for y in range(9):
            sectors[x][y] = x / 3 + 3 * (y / 3)
    return sectors

def fill_rows(game):
    for row in game:
        possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for elem in row:
            if elem in possibilities:
                possibilities.remove(elem)
        for elem in row:
            if type(elem) == list:
                elem += possibilities
        for i, elem in enumerate(row):
            if type(elem) == list and len(elem) == 1:
                elem += possibilities

def intersect(a, b):
    return list(set(a) & set(b))

def p96():
    sudoku = build_sudoku_rows()
    sudoku = make_blanks(sudoku)
    sectors = sector_guide()
    game = 0
    sudoku[game]
    fill_rows(sudoku[game])
    print sudoku[game]


if __name__ == "__main__":
    p96()
