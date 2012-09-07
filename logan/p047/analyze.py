import math as m

def T(n):
    return (2 * (n ** 2)) - 1

def count(val):
    my_count = 0
    for i in range(2, val):
        if is_probable_prime(T(i)):
            my_count += 1
    else:
        return my_count


#print(count(10000))
#print(len(create_primes_list(1000000)))


import random
_mrpt_num_trials = 5 # number of bases to test


def is_probable_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """

    assert n >= 2
    # special case 2
    if n == 2:
       return True
    # ensure n is odd
    if n % 2 == 0:
       return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
       quotient, remainder = divmod(d, 2)
       if remainder == 1:
           break
       s += 1
       d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite
