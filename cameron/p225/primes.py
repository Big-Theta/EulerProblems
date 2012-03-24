#!/usr/bin/python
from math import sqrt

def first_n_primes(x):
    prime_list = [2]
    num = 3
    while len(prime_list) < x:
        check_prime(num, prime_list)
        num += 2
    return prime_list

def nth_prime(x):
    return first_n_primes(x)[-1]

def primes_upto(x):
    prime_list = [2]
    num = 3
    while num <= x:
        check_prime(num, prime_list)
        num += 2
    return prime_list


def check_prime(num, prime_list):
    biggest_to_check = int(sqrt(num)) + 1
    #print "biggest to check is %i" % biggest_to_check
    for prime in prime_list:
        if num % prime == 0:
            return False
        elif prime > biggest_to_check:
            break
    #print "%i is a prime" % num
    #print ("%i is prime" % num)
    prime_list.append(num)
    return True
