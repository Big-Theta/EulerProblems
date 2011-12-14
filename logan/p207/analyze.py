#Was the problem stated correctly?

def has_partition(val):
    index = 0
    if val == 0:
        return False

    while 1:
        fp = 4 ** index
        tp = 2 ** index
        tmp = tp + val
        print(fp, tp, val, index, tmp)
        if fp == tmp:
            return True
        elif fp > tmp:
            return False
        else:
            index += 1

def P(val):
    numerator = 0
    denominator = 0
    for i in range(val):
        if has_partition(i):
            numerator += 1
        denominator += 1
    return (numerator, denominator)

'''
for i in range(10):
    print(i, has_partition(i))
    print(P(i))
    '''

print(has_partition(2))
