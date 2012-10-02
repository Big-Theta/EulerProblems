from analyze import pprime

def gen_tsquare():
    i = 1
    while True:
        yield 2 * (i ** 2)
        i += 1

def is_goldbach(num):
    for tsquare in gen_tsquare():
        if tsquare > num:
            break
        if pprime(num - tsquare):
            return True
    else:
        return False

if __name__ == '__main__':
    i = 3
    while True:
        if not pprime(i) and not is_goldbach(i):
            print i
            break
        i += 2

