def parse():
    matrix = []
    row = 0
    with open('./matrix.txt', 'r') as fin:
        for line in fin.readlines():
            matrix.append([])
            for cell in line.split(','):
                matrix[row].append(int(cell.strip()))
            row += 1

    return matrix


if __name__ == '__main__':
    parse()
