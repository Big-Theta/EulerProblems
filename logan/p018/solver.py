nums = {}
i = -1
for line in open('triangle.txt', 'r').readlines():
    i += 1
    nums[i] = line.split()

print(nums, sep='\n')
print(nums[0][0])

for x in range(i - 1, -1, -1):
    for y in range(len(nums[x])):
        print()
        print(x, y)
        nums[x][y] = int(nums[x][y]) + max(int(nums[x + 1][y]), int(nums[x + 1][y + 1]))

print(nums[0][0])
