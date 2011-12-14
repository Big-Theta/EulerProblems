grid = {}
points = 21

for i in range(points):
    for j in range(points):
        if i is points - 1 or j is points - 1:
            grid[(i, j)] = (1, True)
        else:
            grid[(i, j)] = (0, False)

grid[(points - 1, points - 1)] = (1, True)
'''
print()
for i in range(points):
    print()
    for j in range(points):
        print('\t', end='')
        print(grid[(i, j)], end='')
        '''

flag = False
while not flag:

    '''
    print()
    for i in range(points):
        print()
        for j in range(points):
            print('\t', end='')
            print(i, j, grid[(i, j)], end='')
            '''
    flag = True
    for i in range(points):
        for j in range(points):
            if grid[(i, j)][1] is True:
                continue
            elif grid[(i + 1, j)][1] is True and grid[(i, j + 1)][1] is True:
                grid[(i, j)] = (grid[(i+1, j)][0] + grid[(i, j+1)][0], True)
            else:
                flag = False


'''
print()
for i in range(points):
    print()
    for j in range(points):
        print('\t', end='')
        print(grid[(i, j)], end='')
print()
'''
print(grid[(0, 0)])
