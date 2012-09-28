#!/usr/bin/python

from mr import *


"""
returns list of first n primes
ex: get_n_primes(5) --> [2, 3, 5, 7, 11]
"""
def get_n_primes(total_primes):
    prime_test_num = 2
    primes = []
    while len(primes) < total_primes:
        if is_probable_prime(prime_test_num):
            primes += [prime_test_num]
        prime_test_num += 1
    return primes


"""
returns graycode of given num
"""
def bin2gray(num):
    return num ^ (num >> 1)

"""
returns True if all digits are unique
"""
def is_pandigital(num):
    digits = [0] * 10
    while num > 0:
        num, r = divmod(num, 10)
        digits[r] += 1
        if digits[r] > 1 or digits[0] > 0:
            return False
    return True


"""
returns list of factors of given num
ex: get_factors(63) --> [3, 3, 7]
"""
def get_factors(num, primes):
    i = 0
    ans = []
    if len(primes) == 0:
        primes += get_n_primes(1)
    while num > primes[-1]:
        print "extending primes list"
        primes = get_n_primes(len(primes) * 2)[len(primes):]
    while num and i < len(primes):
        test_num, r = divmod(num, primes[i])
        if r:
            i += 1
        else:
            num = test_num
            ans += [primes[i]]
    return ans
