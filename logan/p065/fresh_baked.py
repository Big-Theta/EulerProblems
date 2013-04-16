from fractions import *

class ICFrac(object):
    def __init__(self, arr):
        self.m_arr = arr

    def get_convergent(self, num):
        frac = Fraction(self.m_arr[num - 1])
        for i in range(num - 2, -1, -1):
            frac = self.m_arr[i] + Fraction(1, frac)
        return frac


def construct_e():
    i = 2
    arr = [2]
    for x in range(1000):
        arr += [1, i, 1]
        i += 2
    return arr


if __name__ == '__main__':
    x = ICFrac(construct_e())
    print sum([int(val) for val in str(x.get_convergent(100).numerator)])
    #print sum([int(val) for val in str(x.get_convergent(10).numerator)])

