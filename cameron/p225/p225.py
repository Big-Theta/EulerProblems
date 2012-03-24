#!/usr/bin/python

from primes import *

def p225(depth):
    seqs = [[1, 1, 1]]
    for x in range(depth):
        seqs.append([0] * 3)

    for _ in range(40):
        next_term = seqs[0][0] + seqs[0][1] + seqs[0][2]
        seqs[0] = seqs[0][1:] + [next_term]
        print ("%11i" % seqs[0][-1]),
        print ("%4i" % (seqs[0][-1] % 27)),
        for i, s in enumerate(seqs[1:]):
            i += 1
            seqs[i] = seqs[i][1:] + [seqs[i - 1][-1] - seqs[i - 1][-2]]
            print ("%11i" % seqs[i][-1]),
        print ""
        #divs = divisors(next_term)
        #print seq[-1],
        #print seq[-1] - seq[-2]
        #print divs

def fib():
    seq = [0, 1]
    for _ in range(20):
        seq = seq[1:] + [seq[0] + seq[1]]
        print seq[1]

def p225_maybe():
    primes = first_n_primes(124)
    primes = primes[1:]
    cubes = [x**3 for x in primes]
    answer = []
    for i, x in enumerate(cubes):
        for y in range(1, 124):
            answer.append(x * ((y * 2) - 1))
    answer = list(set(answer))
    answer.sort()
    for x in answer:
        if x % 2 == 0:
            print "You fucked up"
    print answer[0]
    print answer[0:126]
    print answer[0:10]

def divisors(x):
    ans = []
    i = 2
    while x > 1:
        if x % i != 0:
            #print x, i
            i += 1
        else:
            ans.append(i)
            x /= i
    return ans


if __name__ == "__main__":
    p225(2)
    #fib()
