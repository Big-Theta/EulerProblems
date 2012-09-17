#!/usr/bin/python

def summation(x):
    return (x * (x + 1)) / 2



def p85():
    target = 2000000
    dims = []
    ans = []
    dim = summation(0)
    i = 1
    while dim < target:
        dims += [dim]
        dim = summation(i)
        i += 1


    ix, iy = 0, len(dims) - 1
    ans = [dims[0] * dims[-1], [ix, iy]]
    cur_difference = abs(target - ans[0])
    while ix < len(dims):
        iy = len(dims) -1
        while ix <= iy:
            test_ans = dims[ix] * dims[iy]
            if abs(target - test_ans) < cur_difference:
                ans[0] = test_ans
                ans[1] = [ix, iy]
                cur_difference = abs(target - test_ans)
            iy -= 1
        ix += 1
    print ans
    print ans[1][0] * ans[1][1]

if __name__ == "__main__":
    p85()
