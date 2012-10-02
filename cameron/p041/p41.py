#!/usr/bin/python


from mr import *
from num_tools import *
from itertools import *

def p41():
    num = "7654321"
    perms = permutations(num)
    nums = []
    for p in perms:
        nums += [int(''.join(p))]
    new_nums = []
    for n in nums:
        for i in range(9):
            new_nums += [n / (10 ** i)]
    nums += new_nums
    nums = sorted(list(set(nums)))
    nums.reverse()
    for n in nums:
        if is_probable_prime(n):
            return n

if __name__ == "__main__":
    print p41()
