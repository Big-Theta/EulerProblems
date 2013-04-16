def gen17():
    for x in range(0, 1000, 17):
        yield ('000' + str(x))[-3:]

def gen_for_num(str_input, num):
    for x in range(0, 10):
        new_string = str(x) + str_input
        if len(new_string) == len(set(new_string)) and int(new_string[:3]) % num == 0:
            yield new_string

def main():
    results = []
    for x17 in gen17():
        for x13 in gen_for_num(x17, 13):
            for x11 in gen_for_num(x13, 11):
                for x7 in gen_for_num(x11, 7):
                    for x5 in gen_for_num(x7, 5):
                        for x3 in gen_for_num(x5, 3):
                            for x2 in gen_for_num(x3, 2):
                                for x1 in gen_for_num(x2, 1):
                                    results += [x1]
    print sum([int(x) for x in results])


if __name__ == '__main__':
    main()

