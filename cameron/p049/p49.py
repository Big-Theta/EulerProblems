#!/usr/bin/python

from primes import *

def problem49():
    prime_list = primes_upto(10000)
    remove_small_vals(prime_list)
    permutations = []
    perm_sets = []
    for p in prime_list:
        permutations = get_permutations(p)
        perm_set = []
        for perm in permutations:
            if perm in prime_list:
                perm_set.append(perm)
        if len(perm_set) > 2:
            perm_sets.append(perm_set)
    possibles = []
    for s in perm_sets:
        dif_c = []
        dif_v = []
        for i, x in enumerate(s):
            for y in s[i + 1:]:
                if y - x in dif_v:
                    dif_c[dif_v.index(y - x)] += 1
                else:
                    dif_c.append(1)
                    dif_v.append(y - x)
        for p in s:
            seq_c = 0 #how many are in the sequence
            for i, x in enumerate(dif_c):
                if x > 1:
                    if p in s and p + dif_v[i] in s and p + (2 * dif_v[i]) in s:
                        print "%i%i%i" % (p, p + dif_v[i], p + (2 * dif_v[i]))
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
    problem49()
