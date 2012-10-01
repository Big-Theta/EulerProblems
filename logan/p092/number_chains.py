def memoize(func):
    cache = {}
    def decorated(num):
        ret = cache.get(num)
        if not ret:
            ret = func(num)
        return ret
    return decorated

def next_number(num):
    acc = 0
    while num:
        num, res = divmod(num, 10)
        acc += (res * res)
    return acc


@memoize
def chain(num):
    if num in [1, 89]:
        return num
    else:
        return chain(next_number(num))


def count():
    counter = 0
    for i in xrange(1, 10000000):
        if i % 100000 == 0:
            print i, counter
        if chain(i) == 89:
            counter += 1
    return counter


if __name__ == '__main__':
    import time
    start = time.time()
    print count()
    print "time:", time.time() - start

