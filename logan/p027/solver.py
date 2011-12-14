import math as m

def is_prime(val):
    val = int(val)
    if val < 2:
        return False
    else:
        for i in range(2, m.floor(m.sqrt(val)) + 1):
            if m.floor(val / i) == (val / i):
                break
        else:
            return True
        return False

def quad(n, b, c):
    return int( n ** 2 + b * n + c)

def evaluator():
    max_seq = 0
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
