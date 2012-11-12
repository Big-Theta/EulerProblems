import math as m
import itertools

def get_radius(N):
    return m.sqrt(2 * ((N / 2.0) ** 2))


def is_inside(N, radius, x, y):
    h_dist = x - N / 2.0
    v_dist = y - N / 2.0
    cond = m.sqrt(h_dist ** 2 + v_dist ** 2)

    if cond < radius:
        return -1
    elif cond > radius:
        return 1
    else:
        return 0


def f(N):
    """Assumes case where N is even. If it is not, then
    there is a possibility of overcounting by 4.

    """

    count = 0
    cond = None
    x = int(m.floor((N + 1) // 2 + get_radius(N)))
    y = (N - 1) // 2
    radius = get_radius(N)

    #while x >= N // 2:
    while x > y:
        cond = is_inside(N, radius, x, y)
        if cond == 0:
            #print x, y
            count += 1
            x -= 1
            y += 1
        elif cond == -1:
            y += 1
        else:
            x -= 1

    final = count * 8 + 4
    if (N % 2 == 1 and
        int(N / 2.0 - radius) == m.floor(N / 2.0 - radius)):
        final -= 4

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

if __name__ == '__main__':
    acc = 0
    for i in xrange(int(1E6)):
    #for i in xrange(int(1E11), 1, -1):
        #val = f(i)
        val_2 = g(i)
        if i % 1000 == 0:
            print i, val_2
        if val_2 == 420:
            print 'here'
            acc += i

