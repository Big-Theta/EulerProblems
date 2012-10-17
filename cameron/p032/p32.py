#!/usr/bin/python

from num_tools import *
from itertools import *

def digit_count(x):
    if x != 0:
        total = 0
        x = abs(x)
        while x > 0:
            x /= 10
            total += 1
        return total
    else:
        return 0

def is_pandigital_product(x, y, z):
    total = z
    while x > 0:
        x, r = divmod(x, 10)
        total = (total * 10) + r
    while y > 0:
        y, r = divmod(y, 10)
        total = (total * 10) + r
    if is_pandigital(total):
        return True
    else:
        return False

def p32():
    answers = []
    for i in range(1000):
        for j in range(5000):
            if j >= i:
                possible_ans = i * j
                dig_i = digit_count(i)
                dig_j = digit_count(j)
                dig_p = digit_count(possible_ans)
                if dig_i + dig_j + dig_p == 9:
                    if is_pandigital_product(i, j, possible_ans):
                        answers += [possible_ans]
    answers = list(set(answers))
    final_ans = 0
    for a in answers:
        final_ans += a
    print final_ans

if __name__ == "__main__":
    p32()
