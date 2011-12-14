import time
dur = 2

def timeit(func=None):
    start = time.time()
    i = 0
    while i < 1000000:
        i += 1

    return time.time() - start


if __name__ == '__main__':
    print(timeit())
