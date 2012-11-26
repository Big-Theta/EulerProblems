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

def get_sectors(game):
    game_sectored = []
    for i in range(9):
        game_sectored += [[]]
    for row_i, row in enumerate(game):
        for elem_i, elem in enumerate(row):
            game_sectored[get_sector(elem_i, row_i)] += [elem]
    return game_sectored

def get_cols(game):
    cols = []
    for i in range(9):
        cols += [[]]
        for row in game:
            cols[-1] += [row[i]]
    return cols

"""
def fill_rows(game):
    for row in game:
        possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for elem in row:
            if elem in possibilities:
                possibilities.remove(elem)
        for elem in row:
            if type(elem) == list:
                elem += possibilities
"""

"""
def weed(game):
    for row_i, row in enumerate(game):
        taken = []
        free = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #find numbers not taken
        for elem_i, elem in enumerate(row):
            if type(elem) == int:
                taken += [elem]
            elif len(elem) == 1:
                row[elem_i] = elem[-1]
                taken += [elem[-1]]
        free = list(set(taken) ^ set(free))

        for elem_i, elem in enumerate(row):
            
        print "taken", taken
        print "free", free

        """

def intersect(a, b):
    return list(set(a) & set(b))

def display_game(game):
    for row_i, row in enumerate(game):
        possibles = []
        for elem_i, elem in enumerate(row):
            if type(elem) == int:
                print elem,
            else:
                print ' ',
                possibles += [elem]
            if elem_i % 3 == 2:
                print '|',
        print possibles,
        if row_i % 3 == 2:
            print "\n______________________",
        print ""

def valid(row):
    vrow = []
    for elem in row:
        if type(elem) == int:
            vrow += [elem]
    return set(vrow)

def valid_blanks(row):
    vrow = []
    for elem in row:
        if type(elem) == list:
            vrow += [elem]
    return set(vrow)

def weed(game):
    modified = False
    possibles = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    game_rotated = get_cols(game)
    game_sectored = get_sectors(game)
    for y, row in enumerate(game):
        for x, elem in enumerate(row):
            if type(elem) == list:
                xor = list(possibles ^ (set(row) | set(game_rotated[x]) | set(game_sectored[get_sector(x, y)])))
                if len(xor) == 1:
                    modified = True
                    row[y] = xor[-1]
                    game_rotated = get_cols(game)
                    game_sectored = get_sectors(game)
    return modified

def logic(game):
    modified = False
    for y, row in enumerate(game):
        for x, elem in enumerate(row):
            if type(elem) == list:
                if len(elem) == 


def elimination(game):
    possibles = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    game_rotated = get_cols(game)
    game_sectored = get_sectors(game)
    for y, row in enumerate(game):
        for x, elem in enumerate(row):
            if type(elem) == list:
                xor = list(possibles ^ (set(row) | set(game_rotated[x]) | set(game_sectored[get_sector(x, y)])))
                row[y] = xor

def guess(game):
    print "happy"

def p96():
    sudoku = build_sudoku_rows()
    sudoku = make_blanks(sudoku)
    sectors = sector_guide()
    game_num = 0
    #print sudoku[game_num]
    #print get_cols(sudoku[game_num])
    #weed(sudoku[game_num])
    #display_game(sudoku[game_num])
    #display_game(get_sectors(sudoku[game_num]))
    #while 0 in sudoku[game_num][0]:
    while weed(sudoku[game_num]) == True:
        print "happy"
        display_game(sudoku[game_num])
        print "\n\n\n"
    display_game(sudoku[game_num])


if __name__ == "__main__":
    p96()
