map_a = {
        0 : '',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six', 
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10: 'ten', 
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

map_b = {
        0 : '',
        1 : '',
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty', 
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety'
    }

map_c = {
        0 : '',
        1 : 'hundred'
    }

total = []
for i in range(1, 1000):
    phrase = ''
    c = i // 100
    b = (i // 10) % 10
    a = i % 10
    if c:
        phrase += map_a[c]
        phrase += 'hundred'
        if b or a:
            phrase += 'and'

    if b >= 2:
        phrase += map_b[b]
    elif b == 1:
        phrase += map_a[10*b + a]

    if a and b != 1:
        phrase += map_a[a]
    total += [phrase]
total += ['onethousand']
total = ''.join(total)

m_sum = 0
for x in total:
    if (x is not ' ') and (x is not '\n'):
#        print(x, end='')
        m_sum += 1

print(m_sum)
