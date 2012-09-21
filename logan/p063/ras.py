def gen_nth_powers(n):
    i = 1
    while True:
        val = i ** n
        length = len(str(val))

        if length == n:
            yield val
        elif length > n:
            break
        yield val
        i += 1


def binary_search(length, power, lo=0, hi=16384):
    while lo < hi:
        mid = (lo + hi) // 2
        midval = len(str(mid ** power))
        midval_down = len(str((mid - 1) ** power))
        if midval < length:
            lo = mid + 1
        elif midval_down >= length:
            hi = mid
        elif midval_down == length - 1 and midval == length:
            return mid


def count_for_n(n):
    low = binary_search(n, n)
    high = binary_search(n + 1, n)
    if not low:
        low = 0
    return high - low


if __name__ == '__main__':
    count = 0
    passes = 5
    i = 1
    while True:
        flag = False
        in_range = count_for_n(i)
        count += in_range
        print i, in_range, count
        if not in_range:
            passes -= 1
            if passes == 0:
                break
        in_range = 0
        i += 1
    print count

