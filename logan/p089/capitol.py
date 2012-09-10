def compare(left, right):
    vals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    return cmp(vals.index(left), vals.index(right))

def parser(numerals):
    parsed = []
    while len(numerals) > 1:
        if compare(numerals[0], numerals[1]) == -1:
            parsed.append(numerals[0:2])
            numerals = numerals[2:]
        else:
            parsed.append(numerals[0])
            numerals = numerals[1:]
    if numerals:
        parsed.append(numerals)
    return parsed

def value(numeral):
    vals = {'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000}
    v = vals[numeral[-1]]
    if len(numeral) == 2:
        v = v - vals[numeral[0]]
    return v

def to_i(numerals):
    parsed = parser(numerals)
    acc = 0
    for numeral in parsed:
        acc += value(numeral)
    return acc

def to_num(i_val):
    numeral_rep = []
    vals = [['I', 1],
            ['IV', 4],
            ['V', 5],
            ['IX', 9],
            ['X', 10],
            ['XL', 40],
            ['L', 50],
            ['XC', 90],
            ['C', 100],
            ['CD', 400],
            ['D', 500],
            ['CM', 900],
            ['M', 1000]]
    vals.sort(key=lambda pair: pair[1], reverse=True)
    while i_val:
        for num, val in vals:
            if i_val >= val:
                i_val -= val
                numeral_rep.append(num)
                break

    return ''.join(numeral_rep)

def compress(numeral):
    return to_num(to_i(numeral))


if __name__ == '__main__':
    acc = 0
    with open("roman.txt", 'r') as infile:
        for line in infile.readlines():
            a = len(line.strip())
            b = len(compress(line.strip()))
            acc += a - b
    print acc


