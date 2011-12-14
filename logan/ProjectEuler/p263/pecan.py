from analyze import is_probable_prime as pprime

def _factor(n):
    if n == 1: return [1]

    i = 2
    limit = n**0.5

    while i <= limit:
        if n % i == 0:
            ret = _factor(n/i)
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
    if a[0] > b[0] : return 1


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


def divisor_gen(n):
    factors = factor_multiplicity(n)
    nfactors = len(factors)
    f = [0] * nfactors

    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)

        i = 0

        while True:
            f[i] += 1

            if f[i] <= factors[i][1]:
                break

            f[i] = 0
            i += 1

            if i >= nfactors:
                return


def divisors(n):
    divisors_ = list(divisor_gen(n))
    divisors_.sort()
    return divisors_


def is_pos_expressible(n, divisors_):
    x = 1

    while x < n:
        x *= 2

    if len(divisors_) >= len(divisors(x)):
        return True
    else:
        return False
    '''
    if not divisors:
        return False
    elif n < 1:
        return False
    elif n in divisors:
        return True
    else:
        for item in divisors:
            unique_divisors = divisors[:]
            unique_divisors.remove(item)
            if is_expressible(n - item, unique_divisors):
                return True
        else:
            return False
            '''



def is_practical(n):
    divisors_ = divisors(n)
    if not is_pos_expressible(n, divisors_):
        return False

    factors = factor(n)
    last = 1

    for i, fact in enumerate(factors):
        if last == fact:
            continue
        else:
            last = fact

        x = reduce(lambda x, y: x * y, factors[:i], 1)
        if fact > 1 + sum(divisors(x)):
            return False
    else:
        return True


def is_practical_foursome(n):
    tests = [n - 8, n - 4, n, n + 4, n + 8]
    for test in tests:
        if not is_practical(test):
            return False
    else:
        return True


def next_sexy_foursome(begin):
    n = begin
    done = False

    while not done:
        tests = [n - 9, n - 3, n + 3, n + 9]
        for test in tests:
            if not pprime(test):
                n += 1
                break
        else:
            done = True

        if done:
            new_tests = [n - 7, n - 5, n - 1, n + 1, n + 5, n + 7]
            for test in new_tests:
                if pprime(test):
                    done = False
                    n += 1
                    break

    return n


def next_paradise(begin):
    n = next_sexy_foursome(begin)

    while 1:
        if not is_practical_foursome(n):
            n = next_sexy_foursome(n + 1)
        else:
            return n

        '''
        for test in tests:
            if not is_practical(test):
                break
        else:
            return n
        '''
        #n = next_sexy_foursome(n + 1)

def answer():
    import time
    start = time.time()
    my_sum = 0
    x = 0
    for _ in range(4):
        x = next_paradise(x)
        my_sum += x
        print
        print "Found paradise {0} after {1} seconds...".format(x, time.time() - start)
        print "Sum so far: " + str(my_sum)
        x += 1
    print "Execution of answer() took {0} seconds.".format(time.time() - start)
    return my_sum

def print_paradises():
    n = 0
    while 1:
        n = next_paradise(n)
        print "Paradise? " + str(n)
        n += 1


if __name__ == '__main__':
    '''
    #print list(divisorGen(next_sexy_foursome(1)))
    print is_practical_foursome(5390)
    #print is_practical_foursome(260)
    print divisors(264)
    print divisors(268)
    print is_expressible(267, divisors(268))
    '''
    #print next_paradise(5)
    print answer()
    #print_paradises()
    #print is_practical(429606)
