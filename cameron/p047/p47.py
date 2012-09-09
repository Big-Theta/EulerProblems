#!/usr/bin/python

#anwer is 134043

from num_tools import *

def test_gray_upto(x):
    for i in range(x):
        gray = bin2gray(i)
        if bit_count(gray) == 4:
            print bin(gray)
    #print gray2bin("1010101010101")


def mult_total(arr):
    return_val = 1
    for i in arr:
        return_val *= i
    return return_val

def get_all_factors(primes):
    factors = []
    for p in primes:
        power = 1
        f = p
        while f < primes[-1]:
            factors += [f]
            power += 1
            f = p ** power
    factors.sort()
    return factors
    #print factors

def bit_count(num):
    count = 0
    while (num):
        num &= num - 1
        count += 1
    return count

def factor_indexes(which_f):
    a, b = divmod(which_f, 2)
    i = 0
    indexes = []
    while a:
        if b:
            indexes += [i]
        i += 1
        a, b = divmod(a, 2)
    indexes += [i]
    print indexes
    return indexes

def valid_ans(factors, which_f):
    return True

def get_next_ans(factors, which_f):
    which_f += 1
    while bit_count(which_f) != 4 or not valid_ans(factors, which_f):
        which_f += 1
    ans = 1
    #print bin(which_f)
    indexes = factor_indexes(which_f)
    for i in indexes:
        ans *= factors[i]
    return [ans, which_f]

def p47():
    primes = get_n_primes(10000)
    factors = get_all_factors(primes)
    ans = [0, 0, 0, 0]

    which_f = 0b10111
    print "num_bits = %i" % bit_count(which_f)
    done = False
    while not done and which_f != 0b1111:
        #print which_f
        next_ans, which_f = get_next_ans(factors, which_f)
        ans = ans[1:] + [next_ans]
        if (ans[0] + 1 == ans[1] and ans[1] + 1 == ans[2] and ans[2] + 1 == ans[3]):
            done = True
    print ans[0]

def get_factors_47(num, primes):
    i = 0
    ans = []
    if len(primes) == 0:
        primes += get_n_primes(1)
    while num > primes[-1]:
        print "extending primes list"
        primes = get_n_primes(len(primes) * 2)[len(primes):]
    while num > 0 and i < len(primes) and len(ans) < 5:
        test_num, r = divmod(num, primes[i])
        if r:
            i += 1
        else:
            num = test_num
            if not primes[i] in ans:
                ans += [primes[i]]
    return ans

def p47_easy():
    primes = get_n_primes(100000)
    ans = 0
    in_a_row = 0
    while in_a_row < 4:
        if len(get_factors_47(ans, primes)) == 4:
            in_a_row += 1
            print ans
        else:
            in_a_row = 0
        ans += 1
    print ans - 4



if __name__ == "__main__":
    p47_easy()
    #print get_all_factors(get_n_primes(40))
    #p47()
