import math as m
import itertools
import analyze
import time


gPrimes1 = []
gPrimes3 = []
gMultiples = [1]
LIM = int(1E11)
LIM = int(1E9)
MAX = LIM / (5 ** 3 * 13 ** 2)


def init_primes():
    for i in xrange(3, MAX, 2):
        if analyze.pprime(i):
            if i % 4 == 1:
                gPrimes1.append(i)
            else:
                gPrimes3.append(i)


def yield_base_sol():
    base_sol = set()
    def deapen(value, primes, exponents):
        for prime_index in range(len(primes)):
            for exp in exponents:
                prime = primes[prime_index]
                cand = value * prime ** exp
                if cand > LIM:
                    return
                deaper_exponents = list(exponents[:])
                deaper_exponents.remove(exp)
                deaper_primes = primes[prime_index + 1:]
                deapen(cand, deaper_primes, deaper_exponents)
                if len(exponents) == 1:
                    base_sol.add(cand)
    for exponents in find_base_exponents():
        print "\tUsing exponents:", exponents, "..."
        start = time.time()
        deapen(1, gPrimes1, exponents)
        print "\t\t\t\tdone --", time.time() - start, "seconds"


    for sol in base_sol:
        yield sol


def construct_safe_multiples():
    for i in xrange(MAX):
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


def find_base_exponents():
    base_sol = set()
    def deapen(value, level):
        my_exp = 1
        cand = value
        while cand <= LIM:
            cand = value * gPrimes1[level] ** my_exp
            my_exp += 1
            if g(cand) == 420:
                sol = []
                for f, m in factor_multiplicity(cand):
                    sol.append(m)
                sol.sort()
                base_sol.add(tuple(sol))
            deapen(cand, level + 1)
    deapen(1, 0)
    return base_sol


def g(N):
    c_1 = c_3 = 0
    for divisor in gen_odd_divisors(N ** 2):
        if divisor % 4 == 1:
            c_1 += 1
        else:
            c_3 += 1
    return 4 * (c_1 - c_3)



def acc_solutions():
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
    start = time.time()
    print "LIM:", LIM
    print "Initializing primes ..."
    start_init_primes = time.time()
    init_primes()
    print "\t\t\t\tdone --", time.time() - start_init_primes, "seconds"

    print "construct_safe_multiples() ..."
    start_construct = time.time()
    construct_safe_multiples()
    print "\t\t\t\tdone --", time.time() - start_construct, "seconds"

    sol = acc_solutions()
    print "Solution:", sol
    print "Time taken:", time.time() - start, "seconds"

