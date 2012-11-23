import math as m
import itertools
import analyze
import time


gPrimes1 = []
gPrimes3 = [2]
gMultiples = []
#MAX = 100
#LIM = int(1E11)
LIM = 38000000

MAX = LIM / (5 ** 6)
#MAX = 4733728

"""
30875234922 for n<=38000000
"""

def init_primes():
    for i in xrange(3, MAX, 2):
        if analyze.pprime(i):
            if i % 4 == 1:
                gPrimes1.append(i)
            else:
                gPrimes3.append(i)


def yield_base_sol():
    for a in range(len(gPrimes1)):
        if gPrimes1[a] ** 3 * 13 ** 2 * 17 > LIM:
            break
        for b in range(a + 1, len(gPrimes1)):
            if gPrimes1[a] ** 3 * gPrimes1[b] ** 2 * 17 > LIM:
                break
            for c in range(b + 1, len(gPrimes1)):
                if gPrimes1[a] ** 3 * gPrimes1[b] ** 2 * gPrimes1[c] > LIM:
                    break
                pos = [
                    gPrimes1[a] ** 3 * gPrimes1[b] ** 2 * gPrimes1[c],
                    gPrimes1[a] ** 3 * gPrimes1[b] * gPrimes1[c] ** 2,
                    gPrimes1[a] ** 2 * gPrimes1[b] ** 3 * gPrimes1[c],
                    gPrimes1[a] ** 2 * gPrimes1[b] * gPrimes1[c] ** 3,
                    gPrimes1[a] * gPrimes1[b] ** 3 * gPrimes1[c] ** 2,
                    gPrimes1[a] * gPrimes1[b] ** 2 * gPrimes1[c] ** 3,
                    ]
                for p in pos:
                    if p <= LIM:
                        yield p

    for a in range(len(gPrimes1)):
        if gPrimes1[a] ** 7 * 13 ** 3 > LIM:
            break
        for b in range(a + 1, len(gPrimes1)):
            if gPrimes1[a] ** 7 * gPrimes1[b] ** 3 > LIM:
                break
            pos = [
                    gPrimes1[a] ** 7 * gPrimes1[b] ** 3,
                    gPrimes1[a] ** 3 * gPrimes1[b] ** 7
                ]
            for p in pos:
                if p <= LIM:
                    yield p


def construct_safe_multiples():
    for i in xrange(278455):
        for f in factor(i):
            if f % 4 == 1:
                break
        else:  # for
            gMultiples.append(i)
def _factor(n):
    if n == 1: return [1] 

    i = 2
    limit = n ** 0.5

    while i <= limit:
        if n % i == 0:
            ret = _factor(n / i)
            ret.append(i)
            return ret
        i += 1

    return [n]


def factor(n):
    ret = _factor(n)
    ret.sort()
    return ret

def _cmp(a, b):
    if a[0] < b[0]: return -1
    if a[0] == b[0]: return 0
    if a[0] > b[0]: return 1


def factor_multiplicity(n):
    factors = factor(n)
    with_mult = {}
    for item in factors:
        if item not in with_mult:
            with_mult[item] = 0 
        with_mult[item] += 1
    new_list = [[fact, mult] for fact, mult in with_mult.items()]
    new_list.sort(_cmp)

    return new_list


def gen_divisors(n):
    fm = factor_multiplicity(n)
    exponents = []
    bases = [x for x, y in fm]
    for x, y in fm:
        exponents.append(range(0, y + 1))
    for x in itertools.product(*exponents):
        acc = 1
        for p, q in zip(bases, x):
            acc *= p ** q
        yield acc


def gen_primes(n):
    for i in range(1, n, 2):
        if analyze.pprime(i):
            yield i


def gen_primes_con(k):
    """Only yield if prime p = k mod 4"""
    i = 1
    while True:
        if i % 4 == k and analyze.pprime(i):
            yield i
        i += 1


def gen_num_primes_con(num, k):
    acc = []
    for i in gen_primes_con(k):
        if not num:
            break
        num -= 1
        acc.append(i)
    return acc


def gen_odd_divisors(n):
    fm = factor_multiplicity(n)
    exponents = []
    bases = [x for x, y in fm]

    for x, y in fm:
        exponents.append(range(0, y + 1))

    if bases[0] == 2:
        exponents = exponents[1:]
        bases = bases[1:]

    for x in itertools.product(*exponents):
        acc = 1
        for p, q in zip(bases, x):
            acc *= p ** q
        yield acc


def g(N):
    c_1 = c_3 = 0
    for divisor in gen_odd_divisors(N ** 2):
        if divisor % 4 == 1:
            c_1 += 1
        else:
            c_3 += 1
    return 4 * (c_1 - c_3)



def acc_solutions():
    print "init_primes()..."
    init_primes()
    print "construct_safe_multiples()..."
    construct_safe_multiples()
    acc = 0
    cand = None
    for sol in yield_base_sol():
        for p in gMultiples:
            cand = sol * p
            if cand <= LIM:
                acc += cand
            else:
                break
    return acc


if __name__ == '__main__':
    '''
    acc = 0
    #for i in xrange(10000, 20 * 10000, 10000):
    #for i in xrange(int(1E11), 1, -1):
    #for i in xrange(10000, 10001):
    for i in xrange(10000, 10100):
    #print g(48612265)
    #for i in xrange(359125, 359126):
        val = f(i)
        val_2 = g(i)
        print i, val, val_2
        if val_2 == 420:
            print 'here'
            acc += i

    x = 0
    i = 1
    acc = 0
    while True:
        i += 1
        y = gen_num_primes_con(i, 1)
        acc = 1
        for z in y:
            acc *= z

        if g(x) > 420:
            break
        else:
            x = acc

    primes = y
    print primes
    print acc
    print g(acc)
    print 5 ** 3 * 13 ** 2 * 17
    print 5 ** 7 * 13 ** 3
    print g(5 ** 3 * 13 ** 2 * 17)
    print g(5 ** 7 * 13 ** 3)
    '''

    '''
    start = time.time()
    print acc_solutions()
    print "Time taken:", time.time() - start
    '''
    acc = 0
    for i in xrange(LIM):
        if g(i) == 420:
            acc += i
    print acc

