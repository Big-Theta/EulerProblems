#!/usr/bin/python

from mr import *

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
    #print factors

def iterate(factors, which_f, pows):
    

def p47():
    primes = get_primes(10000)
    factors = get_factors(primes)
    ans = [0, 0, 0, 0]

    which_f = [0, 1, 2, 3]
    done = false
    while which_f[3] < len(factors) || not done:
        ans = ans[1:] + [1]
        for i in which_f:
            ans[3] *= factors[which_f[i]]

        iterate(factors, which_f, pows)
        if (ans[0] + 1 == ans[1] && ans[1] + 1 == ans[2] and ans[2] + 1 == ans[3]):
            done = True
    print ans[0]

    #ans2 = mult_total([primes[index2[i]] ** pow2[i] for i in range(4)])
    print pows
    print ans
    #print ans2

if __name__ == "__main__":
    p47()
