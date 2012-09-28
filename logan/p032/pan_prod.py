from __future__ import print_function
from itertools import *
import time

def gen_pandigital():
    seed = [x for x in range(1, 10)]
    for pan in permutations(seed):
        yield pan


def to_i(arr):
    '''
    if not arr:
        return 0
    return int(''.join([str(x) for x in arr]))
    '''
    acc = 0
    for val in arr:
        acc *= 10
        acc += val
    return acc


def try_split(pan):
    j = 5
    for i in range(1, j):
        first = to_i(pan[:i])
        middle = to_i(pan[i:j])
        last = to_i(pan[j:])
        if first * middle == last:
            return last


if __name__ == '__main__':
    x = gen_pandigital()
    acc = set()
    prods = set()
    for x in gen_pandigital():
        prod = try_split(x)
        if prod:
            prods.add(prod)
    print(sum(prods))

