#!/usr/bin/python
from math import sqrt

def problem50():
    prime_list = [2]
    num = 3
    while num < 100:
        check_prime(num, prime_list)
        num += 2
        #if (num - 1) % 10000 == 0:
            #print num
    print "done computing primes"
    print max_prime_sum(prime_list)


def check_prime(num, prime_list):
    biggest_to_check = int(sqrt(num)) + 1
    #print "biggest to check is %i" % biggest_to_check
    for prime in prime_list:
        if num % prime == 0:
            return False
        elif prime > biggest_to_check:
            break
    #print "%i is a prime" % num
    prime_list.append(num)
    return True

def max_prime_sum(prime_list):
    x = 1
    while x < prime_list.__len__():
        target = prime_list[-x]
        i_left = 0
        i_right = 1
        current = prime_list[0]
        while prime_list[i_right] < target:
            if current < target:
                current += prime_list[i_right]
                i_right += 1
            elif current > target:
                current -= prime_list[i_left]
                i_left += 1
            else:
                for y in range(i_
                return current
        x += 1
problem50()
