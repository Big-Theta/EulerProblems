import fractions as f

my_list = []

for i in range(100):
    for j in range(i, 100):
        try:
            '''
            print(i, j)
            print(str(i)[1], str(j)[0])
            print()
            '''
            num = int(str(i)[0]) / int(str(j)[1])
            if ((num == i / j) and (str(i)[1] == str(j)[0])) and (num < 1):
                my_list.append( f.Fraction(i, j))
        except (IndexError, ZeroDivisionError):
            continue

ag = f.Fraction(1, 1)
for item in my_list:
    ag *= item

print(ag.denominator)
