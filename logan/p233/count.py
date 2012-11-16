import math as m
import itertools
import analyze


gPrimes1 = []
gPrimes3 = [2]
gMultiples = []
MAX = 4733728
#MAX = 100
LIM = int(1E11)

def init_primes():
    for i in xrange(3, MAX, 2):
        if analyze.pprime(i):
            if i % 4 == 1:
                gPrimes1.append(i)
            else:
                gPrimes3.append(i)


def construct_base_sol():
    for a in range(len(gPrimes1)):
        if gPrimes1[a] ** 3 > LIM:
            break
        for b in range(a + 1, len(gPrimes1)):
            if gPrimes1[a] ** 3 * gPrimes1[b] ** 2 > LIM:
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
                    if p < LIM:
                        yield p

    for a in range(len(gPrimes1)):
        if gPrimes1[a] ** 7 > LIM:
            break
        for b in range(a + 1, len(gPrimes1)):
            if gPrimes1[a] ** 7 * gPrimes1[b] ** 3 > LIM:
                break
            pos = [
                    gPrimes1[a] ** 7 * gPrimes1[b] ** 3,
                    gPrimes1[a] ** 3 * gPrimes1[b] ** 7
                ]
            for p in pos:
                if p < LIM:
                    yield p


def construct_multiples():
    pass



def get_radius(N):
    """
    x^2 + y^2 = z^2  # Pythagorus
    2 * z = N * sqrt(2)  # N * sqrt(2) is diameter
    z = (N * sqrt(2)) / 2

    """
    #return m.sqrt(2 * ((N / 2.0) ** 2))
    return (N * m.sqrt(2.0)) / 2.0


def is_inside(N, x, y):
    h_dist = x - N / 2.0
    v_dist = y - N / 2.0
    cond = h_dist ** 2 + v_dist ** 2
    other = (N ** 2.0) / 2.0

    if cond < other:
        return -1
    elif cond > other:
        return 1
    else:
        return 0


def f(N):
    count = 0
    cond = None
    x = int(m.floor((N + 1) // 2 + get_radius(N)))
    y = (N - 1) // 2

    while x > N // 2:
        cond = is_inside(N, x, y)
        if cond == 0:
            count += 1
            x -= 1
            y += 1
        elif cond == -1:
            y += 1
        else:
            x -= 1

    final = count * 4

    #final = count * 8 - 4
    return final


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


def h(N):
    c_1 = c_3 = 0
    for divisor in gen_odd_divisors(N):
        if divisor % 4 == 1:
            c_1 += 1
        else:
            c_3 += 1
    print 'c_1', c_1
    print 'c_3', c_3
    return 4 * (c_1 - c_3)


def gen_base():
    """Find primes p congruent to 1 mod 4.
    The basic solutions are:
    p_1 ** 3 * p_2 ** 7
    p_1 ** 1 * p_2 ** 2 * p_3 ** 3

    Multiply this quantity by any number that does not have one
    of these special p's as a factor, and the resultant number will
    have the same property.

    """
    p_3 = 5
    p_2 = 13
    p_1 = 17
    for p in gen_primes_con(1):
        if p * (p_2 ** 2) * (p_3 ** 3) > 1E11:
            break
        p_1 = p
    print p_1



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

    init_primes()
    print len(gPrimes1)
    print len(gPrimes3)
    acc = 0
    for x in construct_base_sol():
        acc += 1
    print acc

