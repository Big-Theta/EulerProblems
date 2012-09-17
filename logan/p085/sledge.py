import sys
sys.setrecursionlimit(2100)

def memoize(func):
    cache = {}
    def memoized(width, height):
        retval = cache.get((width, height))
        if not retval:
            retval = func(width, height)
            cache[(width, height)] = retval
        return retval
    return memoized

@memoize
def rect(width, height):
    # The sum of 1 + 2 + 3 + ... + height
    if width == 1:
        return (height * height + height) / 2
    # Calculate how many rectangles do not have a bottom right
    # corner in the last row...
    acc = rect(width - 1, height)
    # Calculate how many have a corner in the bottom right row.
    for i in range(1, height + 1):
        acc += i * width
    return acc

def binary_search(x, height, lo=1, hi=2048):
    while lo < hi:
        mid = (lo + hi) // 2
        midval = rect(mid, height)
        if midval < x:
            lo = mid + 1
        elif midval > x:
            hi = mid
        else:
            assert False
    if mid < x:
        return mid, mid + 1
    else:
        return mid - 1, mid


if __name__ == "__main__":
    x = 2000000
    best = [0, x]

    for h in range(1, 1002):
        if h % 10 == 0:
            print h
        a, b = binary_search(x, h)
        for v in [a, b]:
            if abs(x - rect(v, h)) < abs(best[1]):
                best = [[v, h], x - rect(v, h)]

    print best
    print best[0][0] * best[0][1]

