#!/usr/bin/python

def get_length(x):
    digits = 0
    while x > 0:
        x /= 10
        digits += 1
    return digits


def p63():
    ans = 0
    p = 1
    n = 1
    test_n = n ** p
    length = get_length(test_n)
    done = False
    while n < 10:
        while length == p:
            ans += 1
            p += 1
            test_n = n ** p
            length = get_length(test_n)
        p = 1
        n += 1
        test_n = n ** p
        length = get_length(test_n)
    print ans


if __name__ == "__main__":
    p63()
