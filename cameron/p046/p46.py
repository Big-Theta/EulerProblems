#!/usr/bin/python


from num_tools import *

def gen_square():
    i = 1
    while True:
        yield i * i
        i += 1

def p46(roof):
    squares = [gen_squares()]
    primes = get_n_primes(roof)
    print primes[-1]
    print "Happy"
    test_num = 3
    

if __name__ == "__main__":
    print x2squares_upto(100)
    #p46(10000)
