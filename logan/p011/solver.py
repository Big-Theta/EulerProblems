nums = {}

with open('grid.txt') as grid:
    for i in range(20):
        line = grid.readline()
        line = line.split()
        for j in range(20):
            nums[(i, j)] = int(line[j])

m_max = 0

for i in range(21):
    for j in range(21):
        for k in range(-1, 2, 1):
            for l in range(-1, 2, 1):
                tmp_prod = 1
                for m in range(4):
                    if not k == l == 0:
                        try:
                            tmp_prod *= nums[(i + (m * k), j + (m * l))]
                        except KeyError:
                            continue
                m_max = max(m_max, tmp_prod)
print(m_max)
