m_ = [[131,673,234,103,18],
     [201,96 ,342,965,150],
     [630,803,746,422,111],
     [537,699,497,121,956],
     [805,732,524,37 ,331]]

m = {}
for _y, _line in enumerate(m_):
    for _x, _cell in enumerate(_line):
        m[_x, _y] = _cell


class tentry(object):
    '''Tree entry.
    Indecies are as follows:
    obj[0] is x, y tuple for location in matrix
    obj[1] is current sum (sort on this)
    obj[2] is matrix object'''

    def __init__(self, obj):
        self.ident = obj[:]

    def gen(self):
        x, y = self.ident[0]
        ret = []

        for (x_, y_) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            try:
                ret.append(tentry([(x_, y_), self.ident[1] + self.ident[2][(x_, y_)], self.ident[2]]))
            #    print self.ident[1], ret[0][1]
            except KeyError:
                pass
        return ret

    def __getitem__(self, val):
        return self.ident[val]


def parse():
    '''This parses the matrix.txt file into a 2D matrix.'''

    matrix = {}

    with open('./matrix.txt', 'r') as fin:
        for y, line in enumerate(fin.readlines()):
            for x, cell in enumerate(line.split(',')):
                matrix[x, y] = int(cell.strip())

    return matrix


def redux(matrix, target):

    tree = []
    marked = {}

    tree.append(tentry([(0, 0), matrix[0, 0], matrix]))

    while 1:
        tree.sort(key=lambda x: x[1], reverse=True)

        tmp = tree.pop()
        marked[tmp[0]] = True

        for item in tree:
            if marked.get(item[0]):
                tree.remove(item)

        if tmp[0] == target:
            return tmp
        else:
            for item in tmp.gen():
                tree.append(item)


def run():

    #print redux(m, (4, 4))[1]
    p = parse()
    size_x, size_y = 0, 0

    for x_, y_ in p.keys():
        if x_ > size_x:
            size_x = x_

        if y_ > size_y:
            size_y = y_

    print redux(parse(), (size_x, size_y))[1]


if __name__ == '__main__':
    #print m
    #parse()
    import time
    start = time.time()
    run()
    print "This took %lf seconds." % float(time.time() - start)
