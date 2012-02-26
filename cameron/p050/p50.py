#!/usr/bin/python
from math import sqrt

def problem50():
    prime_list = [2]
    num = 3
    while num < 1000000:
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
    #print ("%i is prime" % num)
    prime_list.append(num)
    return True

def max_prime_sum(prime_list):
    x = 1
    max_length = 0
    answer = 0
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
            elif i_right - i_left > max_length:
                max_length = i_right - i_left
                answer = current
            else:
                break
        x += 1
    return answer

if __name__ == "__main__":
    problem50()
