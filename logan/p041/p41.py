from analyze import pprime
from itertools import permutations

def get_in_range(length):
    numbers = []
    for i in range(1, length + 1):
        numbers.append(i)
    for perm in permutations(numbers):
        joined = ''.join([str(x) for x in perm])
        if pprime(int(joined)):
            yield joined


if __name__ == '__main__':
    vals = []
    for i in range(9, 0, -1):
        for x in get_in_range(i):
            vals.append(x)
    vals.sort()
    print vals[-1]

