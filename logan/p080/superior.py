import math

def is_sqrt_irrational(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return False
    else:
        return True


def next_char(c):
    return str(int(c) + 1)


def char_sum(val):
    my_sum = 0
    while val:
        my_sum += int(val[0])
        val = val[1:]
    return my_sum


def sqrt100(n, digits=100):
    tar = int(str(n) + (2 * digits) * '0')

    leng = 1
    val = ['1']
    while 1:
        if int(''.join(val)) ** 2 > tar:
            break
        else:
            val += ['0']
    val = val[:-1]
    length = len(val)

    for i in range(length):
        char_prev = val[i]
        char_tmp = char_prev
        while next_char(char_tmp) != '10':
            char_tmp = next_char(char_tmp)
            val[i] = char_tmp
            test = int(str(int(''.join(val)) ** 2))
            if test > tar:
                val[i] = char_prev
                break
            else:
                char_prev = char_tmp

    retval = ''.join(val)[0:digits]
    return retval

if __name__ == '__main__':
    my_sum = 0
    print char_sum(sqrt100(2))
    for x in range(100):
        if is_sqrt_irrational(x):
            my_sum += char_sum(sqrt100(x))
    print my_sum
