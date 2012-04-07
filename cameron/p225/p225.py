#!/usr/bin/python

from primes import *

def p225(answers_needed):
    rems = [1, 1, 3]
    cur_divisor = 17
    answers_found = 0

    while answers_found < answers_needed:
        cur_divisor += 2
        rems = [1, 1, 3]
        i = 0
        while not 0 in rems:
            rems[i] = (rems[0] + rems[1] + rems[2]) % cur_divisor
            i = (i + 1) % 3
            if rems == [1, 1, 1]:
                rems = [0, 0, 0]
                answers_found += 1
                if answers_found == answers_needed:
                    print cur_divisor


if __name__ == "__main__":
    p225(124)
