#!/usr/bin/python

def problem6():
    su_sq = 0
    sq_su = 0
    for x in range(1, 101):
        su_sq += x * x
    for x in range(1, 101):
        sq_su += x
    sq_su *= sq_su
    print abs(su_sq - sq_su)


"""
i
str(i)
list(string)
l.reverse()
string = ''.join(l)
string == stringb
"""


if __name__ == '__main__':
    problem6()
