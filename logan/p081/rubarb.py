m = [[131, 673, 234, 103, 18 ],
     [201, 96,  342, 965, 150],
     [630, 803, 746, 422, 111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37,  331]]


def parse():
    '''This parses the matrix.txt file into a 2D matrix.'''

    matrix = []
    row = 0

    with open('./matrix.txt', 'r') as fin:
        for line in fin.readlines():
            matrix.append([])
            for cell in line.split(','):
                matrix[row].append(int(cell.strip()))
            row += 1

    return matrix


def redux(matrix):
    '''Starts at the top left of the matrix. It replaces every
    entry there with the minimum path to that location. Then, on
    the next row, it does the same... dito dito... at the end it has
    the result in m[79][79]'''

    for r, row in enumerate(matrix):
        for l, loc in enumerate(row):
            if r > 0:
                up = matrix[r][l] + matrix[r - 1][l]
            else:
                # left
                up = matrix[r][l] + matrix[r][l - 1]

            if l > 0:
                left = matrix[r][l] + matrix[r][l - 1]
            else:
                left = up

            if r == l == 0:
                left = up = matrix[0][0]

            matrix[r][l] = min(left, up)

    return matrix[-1][-1]


def run():
    print redux(parse())

    '''
    for l in m:
        for x in l:
            print x,
        print

    print redux(m)
    '''


if __name__ == '__main__':
    run()
