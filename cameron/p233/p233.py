#!/usr/bin/python

from num_tools import *

def p233(target):
    p = gen_prime()
    print p.next()
    print p.next()

if __name__ == "__main__":
    print "happy"
    p233(52)
