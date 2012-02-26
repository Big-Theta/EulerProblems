#!/usr/bin/python

from primes import primes_upto

def problem49():
    prime_list = primes_upto(10000)
    remove_small_vals(prime_list)
    permutations = []
    for p in prime_list:
        permutations = get_permutations(p)

    return True


def get_permutations(x):
    permutations = []
    x, d0 = x.divmod(10)
    x, d1 = x.divmod(10)
    x, d2 = x.divmod(10)
    x, d3 = x.divmod(10)
    digits = [d0, d1, d2, d3]
    
    return list(set(permutations))


def remove_small_vals(prime_list):
    while prime_list[0] < 1000:
        prime_list.pop(0)

if __name__ == "__main__":
    problem49()
