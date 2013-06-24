from fractions import Fraction
from pprint import pprint

#D = 8
D = 1000000
TARGET = Fraction(3, 7)

def get_all(d=8):
    fracs = set()
    for out_dex in range(d + 1):
        if out_dex % 100 == 0:
            print str(out_dex) + '\r'
        for in_dex in range(out_dex):
            fracs.add(Fraction(in_dex, out_dex))
    return fracs

def find_frac_for(denom):
    return Fraction(int(TARGET * denom), denom)

def get_left_of(x, d=8):
    cand = set()
    for i in range(1, D + 1):
        if i % 1000 == 0:
            print i
        cand.add(find_frac_for(i))
    cand = sorted(list(cand))
    return cand[cand.index(x) - 1]


if __name__ == '__main__':
    #pprint(sorted(get_all()))
    print get_left_of(Fraction(3, 7), 1000000)

