#!/usr/bin/python

def problem8():
    f = open('number.txt')
    number = int(f.read())
    top5 = [0] * 5
    pos = 0
    biggest = 0
    while number > 0:
        number, top5[pos] = divmod(number, 10)
        y = 1
        for x in top5:
            y *= x
        biggest = max([biggest, y])
        pos = (pos + 1) % 5
    print biggest
problem8()
