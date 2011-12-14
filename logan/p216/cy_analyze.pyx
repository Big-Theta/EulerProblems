# cython: language_level=3

import math as m
import time
cdef long long int PRIMES[50000000]
cdef long P_INIT = 0

cpdef int get_P_INIT():
    return P_INIT

def memoize(long long limit):
    global P_INIT
    cdef long index
    cdef long long int x
    cdef long i
    cdef long prime
    cdef long range_limit = P_INIT
    PRIMES[0] = 2
    PRIMES[1] = 3
    range_limit = 2
    for x in range(5, limit, 2):
        if x % 1000000 == 1:
            print(' =>', x, limit, range_limit)
        for i in range(range_limit):
            prime = PRIMES[i]
            if x % prime == 0:
                break

            if prime * prime > x:
                PRIMES[range_limit] = x
                range_limit += 1
                break
    P_INIT = range_limit


cpdef int get_prime(int index):
    return int(PRIMES[index])


cpdef int is_prime(val):
    global P_INIT
    cdef long long int my_val = <long long int>val
    cdef long int i
    cdef long long int my_sqrt = <long long int>(val ** .5 + 1)
    for i in range(P_INIT):
        prime = PRIMES[i]
        if my_val % prime == 0:
            return 0
        if prime > my_sqrt:
            return 1
    else:
        return 1


cpdef inline long int T(int n):
    return (2 * (n ** 2)) - 1

def count(val):
    cdef long int my_count, i
    start = time.time()
    my_count = 0
    print('Start:')
    memoize((T(val) ** .5) + 1)
    print('Begin the count! {0} {1:.2} minutes elapsed.'.format(val, (time.time() - start) / 60))
    print(P_INIT)
    for i in range(2, val):
        if i % 10000 == 0:
            print(' >', i, '{0:.2} minutes elapsed.'.format((time.time() - start) / 60))
        if is_prime(T(i)):
            my_count += 1
    else:
        return my_count
