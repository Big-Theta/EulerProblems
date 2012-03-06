nums = {}
for i, line in enumerate(open('triangle.txt', 'r').readlines()):
    nums[i] = line.split()
for x in range(i - 2, -1, -1):
    for y in range(len(nums[x])):
        nums[x][y] = int(nums[x][y]) + max(int(nums[x + 1][y]), int(nums[x + 1][y + 1]))
print(nums[0][0])
