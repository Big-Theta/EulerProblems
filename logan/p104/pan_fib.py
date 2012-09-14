def is_pandigital(segment):
    if len(segment) != 9:
        return False

    numbers = set()
    for c in segment:
        numbers.add(c)

    if len(numbers) != 9:
        return False
    if '0' in numbers:
        return False
    else:
        return True


def gen_fib():
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b

def first_is_pandigital(fib):
    test_str = str(fib)[0:9]
    if is_pandigital(test_str):
        return True
    else:
        return False

def last_is_pandigital(fib):
    test_str = str(fib % 1000000000)[-9:]
    if is_pandigital(test_str):
        return True
    else:
        return False

def find_last_pandigital():
    counter = 1
    for fib in gen_fib():
        if last_is_pandigital(fib):
            return counter
        else:
            counter += 1

def find_first_pandigital():
    counter = 1
    for fib in gen_fib():
        if first_is_pandigital(fib):
            return counter
        else:
            counter += 1

def find_both_pandigital():
    counter = 1
    for fib in gen_fib():
        if last_is_pandigital(fib):
            if first_is_pandigital(fib):
                return counter
        counter += 1

if __name__ == '__main__':
    print find_both_pandigital()

