#!/usr/bin/python

from primes import *

def problem49():
    prime_list = primes_upto(10000)
    remove_small_vals(prime_list)
    permutations = []
    for p in prime_list:
        permutations = get_permutations(p)
        matches = []
        for perm in permutations:
            if perm in prime_list:
                matches.append(perm)
        if len(matches) > 4:
            difference_count = []
            differences = []
            for i, x in enumerate(matches):
                if i < len(matches) + 1:
                    for y in matches[i:len(matches)]:
                        dif = y - x
                        if dif in differences:
                            difference_count[differences.index(dif)] += 1
                        else:
                            differences.append(dif)
                            difference_count.append(1)
            for i, x in enumerate(difference_count):
                if x < 3:
                    difference_count.pop(i)
                    differences.pop(i)
            if len(differences) > 0:
                print ("anser is %i" % differences[0])

    return True


def get_permutations(x):
    permutations = []
    x, d0 = divmod(x, 10)
    x, d1 = divmod(x, 10)
    x, d2 = divmod(x, 10)
    x, d3 = divmod(x, 10)
    digits = [d0, d1, d2, d3]
    for a in range(4):
        l = digits.pop(a)
        for b in range(3):
            m = digits.pop(b)
            for c in range(2):
                n = digits.pop(c)
                permutations += [(l * 1000) + (m * 100) + (n * 10) + digits[0]]
                digits.insert(c, n)
            digits.insert(b, m)
        digits.insert(a, l)
    return sorted(list(set(permutations)))


def remove_small_vals(prime_list):
    while prime_list[0] < 1000:
        prime_list.pop(0)

if __name__ == "__main__":
    #print get_permutations(1234)
    problem49()
