#!/usr/bin/python

from primes import *

def p225_old(answers_needed):
    seq = [1, 1, 1]
    cur_divisor = 17
    answers_found = 0

    remainders = [1, 1, 1]
    while answers_found < answers_needed:
        seq = get_seq((len(remainders) + 1) * 2, seq)
        remainders += [seq[len(remainders)] % cur_divisor]
        if remainders[-1] == 0:
            #print "found a dud %i" % cur_divisor
            cur_divisor += 2
            remainders = [1, 1, 1]
        elif remainders[-3:] == [1, 1, 1]:
            #print "gets here!"
            target = remainders[:-3]
            possible_match = [x % cur_divisor for x in seq[len(target):len(target) * 2]]
            #print target
            #print possible_match
            if target == possible_match:
                answers_found += 1
                print "Yay, found %i, divisor number %i" % (cur_divisor, answers_found)
                cur_divisor += 2
                remainders = [1, 1, 1]
    print cur_divisor

def p225(answers_needed):
    seq = [1, 1, 1]
    cur_divisor = 17
    answers_found = 0

    remainders = [1, 1, 1]
    cur_index = 3
    while answers_found < answers_needed:
        seq = get_seq(cur_index + 1, seq)
        remainders = remainders[1:] + [seq[cur_index] % cur_divisor]
        if remainders[-1] == 0:
            #print "found a dud %i" % cur_divisor
            cur_divisor += 2
            remainders = [1, 1, 1]
        elif remainders == [1, 1, 1] and cur_index > 3:
            answers_found += 1
            print "Yay, found %i, divisor number %i" % (cur_divisor, answers_found)
            cur_divisor += 2
            remainders = [1, 1, 1]
            cur_index = 2
        cur_index += 1
    print cur_divisor

def get_seq(length, seq):
    while len(seq) < length:
        seq += [seq[-3] + seq[-2] + seq[-1]]
        #print seq[-1]
    return seq

if __name__ == "__main__":
    p225(124)
