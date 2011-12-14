import math as m

cpdef int is_prime(the_val):
    cdef int i
    cdef val = the_val
    if val < 2:
        return False
    else:
        for i in range(2, int(val ** .5)):
            if int(val / i) == (val / i):
                break
        else:
            return True
        return False

def quad(n, b, c):
    return int( n ** 2 + b * n + c)

def evaluator():
    cdef int max_seq = 0
    cdef int i, j, k
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            k = 0
            while is_prime(quad(k, i, j)):
                k += 1
            if k > max_seq:
                ref = (i, j, k)
                max_seq = max(max_seq, k)
    print(max_seq, ref)

#evaluator()
