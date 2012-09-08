#!/usr/bin/python

from mr import *
from decbingray import *

def mult_total(arr):
    return_val = 1
    for i in arr:
        return_val *= i
    return return_val

def get_primes(total_primes):
    prime_test_num = 3
    primes = []
    while len(primes) < total_primes:
        if is_probable_prime(prime_test_num):
            primes += [prime_test_num]
        prime_test_num += 2
    return primes

def get_factors(primes):
    factors = []
    for p in primes:
        power = 1
        f = p
        while f < primes[-1]:
            factors += [f]
            power += 1
            f = p ** power
    factors.sort()
    return factors
    #print factors

def bit_count(num):
    count = 0
    while (num):
        num &= num - 1
        count += 1
    return count

def factor_indexes(which_f):
    a, b = divmod(which_f, 2)
    i = 0
    indexes = []
    while a:
        if b:
            indexes += [i]
        i += 1
        a, b = divmod(a, 2)
    indexes += [i]
    print indexes
    return indexes

def valid_ans(factors, which_f):
    return True

def get_next_ans(factors, which_f):
    which_f += 1
    while bit_count(which_f) != 4 or not valid_ans(factors, which_f):
        which_f += 1
    ans = 1
    #print bin(which_f)
    indexes = factor_indexes(which_f)
    for i in indexes:
        ans *= factors[i]
    return [ans, which_f]

def p47():
    primes = get_primes(10000)
    factors = get_factors(primes)
    ans = [0, 0, 0, 0]

    which_f = 0b10111
    print "num_bits = %i" % bit_count(which_f)
    done = False
    while not done and which_f != 0b1111:
        #print which_f
        next_ans, which_f = get_next_ans(factors, which_f)
        ans = ans[1:] + [next_ans]
        if (ans[0] + 1 == ans[1] and ans[1] + 1 == ans[2] and ans[2] + 1 == ans[3]):
            done = True
    print ans[0]

if __name__ == "__main__":
    p47()
