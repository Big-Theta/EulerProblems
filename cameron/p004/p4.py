#!/usr/bin/python

def problem4():
    x, y = 999, 999
    min_y = 0
    check = 0
    cur = 0
    while y > min_y:
        x = y
        while x > 0:
            check = x * y
            if check > cur and is_palindrome(check):
                cur = check
                if x > min_y:
                    min_y = x
                x = 0
            x -= 1
        y -= 1
    print cur

def is_palindrome(s):
    s = str(s)
    saved_s = s
    s = list(s)
    s.reverse()
    s = ''.join(s)
    return s == saved_s


"""
i
str(i)
list(string)
l.reverse()
string = ''.join(l)
string == stringb
"""


if __name__ == '__main__':
    problem4()
