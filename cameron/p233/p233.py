#!/usr/bin/python

from num_tools import *
from math import *

def p233():
    p = gen_prime()
    print p.next()

def p233_old(n):
    ans = 0
    for x in xrange(10**11):
        a = get_ans(x * 2)
        if a == 420:
            ans += x
            print x, ans
        elif x % 10000 == 0:
            print x

def get_ans(n):
    n *= 2
    i = 0
    tot = [0, 0]
    c = [int(sqrt((((n * 1.0) / 2) ** 2) * 2)), 0]
    target = ((n / 2) ** 2) * 2
    while c[0] > n / 2:
        projection = (c[0] ** 2) + c[1] ** 2
        if projection == target:
            if c[0] % 2 == 0 and c[1] % 2 == 0:
                tot[0] += 1
            elif c[0] % 2 == 1 and c[1] % 2 == 1:
                tot[1] += 1
            c[1] += 1
        elif projection < target:
            c[1] += 1
        else:
            c[0] -= 1
    return tot[(n / 2) % 2] * 8 + 4

if __name__ == "__main__":
    print get_ans(10075)
    #p233_old()
