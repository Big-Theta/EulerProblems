import random

_mrpt_num_trials = 5

def is_prime(n):
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

def factor(val):
    if val == 1:
        return set()
    if is_prime(val):
        return set([val])
    for i in xrange(2, val):
        if val % i == 0:
            factors = factor(val // i)
            factors.add(i)
            return factors

def solver():
    VALS = 3
    x = [[i, None] for i in range(VALS)]
    while 1:
        new_val = x[VALS - 1][0] + 1
        factors = len(factor(new_val))
        x = x[1:] + [[new_val, factors]]
        for i in range(VALS):
            if x[i][1] != VALS:
                break
        else:
            print x[0][0]
            break

if __name__ == "__main__":
    solver()

