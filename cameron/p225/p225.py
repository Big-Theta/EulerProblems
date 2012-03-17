#!/usr/bin/python

def p225():
    seq = [1, 1, 1]

    for _ in range(100):
        x = seq[0] + seq[1] + seq[2]
        seq = seq[1:] + [x]
        print ("%i" % x),
        print divisors(x)

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
    p225()
