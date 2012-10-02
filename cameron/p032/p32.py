#!/usr/bin/python

from num_tools import *
from itertools import *

def digits(x):
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
    

def p32():
    answers = []
    for i in range(1000):
        for j in range(5000):
            if j >= i:
                possible_ans = i * j
                dig_i = digits(i)
                dig_j = digits(j)
                dig_p = digits(possible_ans)
                if dig_i + dig_j + dig_p == 9:

if __name__ == "__main__":
    p32()
