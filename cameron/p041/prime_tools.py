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
