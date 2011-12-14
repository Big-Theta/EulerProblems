def is_increasing(num):
    tmp = str(num)
    last_num = 0
    while tmp:
        first = tmp[0]
        tmp = tmp[1:]
        if int(first) < last_num:
            return False
        else:
            last_num = int(first)
    else:
        return True

def is_decreasing(num):
    tmp = str(num)
    last_num = 9
    while tmp:
        first = tmp[0]
        tmp = tmp[1:]
        if int(first) > last_num:
            return False
        else:
            last_num = int(first)
    else:
        return True

def return_bouncy(ratio):
    bouncy = 0

    i = 1
    while True:
        if (bouncy / i) < ratio:
            i += 1
            if not (is_increasing(i) or is_decreasing(i)):
                bouncy += 1
        else:
            break

    return i
