#!/usr/bin/python

def problem16():
    x = pow(2, 1000)
    ans = 0
    while x > 0:
        x, c = divmod(x, 10)
        ans += c
    print ans

if __name__ == "__main__":
    problem16()
