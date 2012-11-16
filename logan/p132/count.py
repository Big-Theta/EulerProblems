import math as m
import itertools
import analyze

def _factor(n):
    print n
    if n == 1: return [1]
    i = 2
    limit = n ** 0.5

    while i <= limit:
        if n % i == 0:
            ret = _factor(n / i)
            ret.append(i)
            print i
            return ret
        i += 1

    return [n]


def factor(n):
    ret = _factor(n)
    ret.sort()
    return ret


def _cmp(a, b):
    if a[0] < b[0]: return -1
    if a[0] == b[0]: return 0
    if a[0] > b[0]: return 1


def factor_multiplicity(n):
    factors = factor(n)
    with_mult = {}
    for item in factors:
        if item not in with_mult:
            with_mult[item] = 0 
        with_mult[item] += 1
    new_list = [[fact, mult] for fact, mult in with_mult.items()]
    new_list.sort(_cmp)

    return new_list


def R(x):
    return int('1' * x)


if __name__ == '__main__':
    print factor_multiplicity(R(10**9))

