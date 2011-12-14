sum = 0

for line in open('numbers.txt', 'r'):
    sum += int(line)

sum = str(sum)
sum = sum[:10]
print(sum)
