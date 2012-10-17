#!/usr/bin/python


from num_tools import *

def gen_square():
    i = 1
    while True:
        yield i * i
        i += 1

def p46():
    sg = gen_square()
    pg = gen_prime()
    squares = [sg.next()]
    primes = [2]
    test_num = 1
    found = True
    while found:
        test_num += 2
        found = False
        while test_num > squares[-1]:
            squares += [sg.next()]
        if is_probable_prime(test_num):
            primes += [test_num]
            found = True
        else:
            for s in squares:
                if (test_num - (2 * s)) in primes:
                    found = True
                    break
    return test_num

if __name__ == "__main__":
    print p46()
