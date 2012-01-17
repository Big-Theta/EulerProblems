#!/usr/bin/python

def problem2():
    x = 1
    y = 2
    total = 2
    while y < 4000000:
        x, y = y, x
        y += x
        if y % 2 == 0:
            total += y
    print total



if __name__ == '__main__':
    problem2()
