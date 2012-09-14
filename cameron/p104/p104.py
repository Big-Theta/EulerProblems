#!/usr/bin/python

def is_pandoginal(x):
    compare = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    x = sorted(x)
    return compare == x


def p104():
    fa = 1
    fb = 1
    n = 2
    done = False
    big_enough = False
    while True:
        fa, fb, n = fb, fa + fb, n + 1
        if not big_enough:
            if len(str(fb)) >= 9:
                big_enough = True
        else:
            if is_pandoginal(str(fb % 1000000000)[-9:]) and is_pandoginal(str(fb)[:9]):
                return n



if __name__ == "__main__":
    print p104()
