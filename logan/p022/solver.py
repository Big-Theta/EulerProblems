f = open('names.txt', 'r')

f = str(f.readlines()).strip()
f = f[2:len(f) - 4]
f = f.split(',')

new_list = []

for item in f:
    item = item.strip('\n').strip('"')
    new_list.append(item)

new_list.sort()
print(f)

total = 0
index = 0
for name in new_list:
    index += 1
    letter_sum = 0
    for letter in name:
        if letter.isalpha():
            letter_sum += ord(letter) - ord('A') + 1
    total += letter_sum * index
    if index < 10:
        print(name, letter_sum * index)

print(total)
