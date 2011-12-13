matrix = []
row = 0

with open('./matrix.txt', 'r') as fin:
    print "here"
    for line in fin.readlines():
        matrix.append([])
        for cell in line.split(','):
            matrix[row].append(int(cell.strip()))
        row += 1

print matrix
