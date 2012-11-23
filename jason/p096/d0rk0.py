#!/usr/bin/env python

class Board:
    def __init__(self, name, rows):
        self._name = name[:-1]
        self._rows = []
        for row in rows:
            self._rows.append([int(c) for c in row
              if c in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")])

    def __repr__(self):
        lines = []
        lines.append("%s" % self._name)
        lines.append("+---+---+---+")
        for j in xrange(len(self._rows)):
            row = self._rows[j]
            line = ""
            for i in xrange(len(row)):
                if i == 0:
                    line += "|"
                val = row[i]
                if val == 0:
                    line += "."
                else:
                    line += "%d" % val
                if i == 2 or i == 5 or i == 8:
                    line += "|"
            lines.append(line)
            if j == 2 or j == 5:
                lines.append("+---+---+---+")
        lines.append("+---+---+---+")
        return "\n".join(lines)

    def nunset(self):
        ret = 0
        for row in self._rows:
            for col in xrange(len(row)):
                if row[col] == 0:
                    ret += 1
        return ret

    def get(self, row, col):
        return self._rows[row][col]

    def set(self, row, col, val):
        valid = self.getValid(row, col)
        if valid == None:
            return True
        assert valid != None
        okay = False
        for v in valid:
            if v == val:
                okay = True
                break
        if not okay:
            return True
        self._rows[row][col] = val
        return False

    def unset(self, row, col):
        self._rows[row][col] = 0

    def getValid(self, row, col):
        if self._rows[row][col] != 0:
            return None
        valid = {i:True for i in xrange(1, 10)}
        # Check row.
        for i in xrange(9):
            val = self._rows[row][i]
            if val != 0:
                valid[val] = False
        # Check col.
        for j in xrange(9):
            val = self._rows[j][col]
            if val != 0:
                valid[val] = False
        # Check nontant.
        for j in xrange(3):
            rMin = row - (row % 3)
            for i in xrange(3):
                cMin = col - (col % 3)
                val = self._rows[rMin+j][cMin+i]
                if val != 0:
                    valid[val] = False
        ret = [i for i in xrange(1, 10) if valid[i]]
        return ret

    def prepSearch(self):
        tups = []
        for row in xrange(9):
            for col in xrange(9):
                valid = self.getValid(row, col)
                if valid != None:
                    tups.append((row, col, valid))
                    if len(valid) == 0:
                        return None
        decos = [(len(tup[2]), tup) for tup in tups]
        decos.sort()
        tups = [tup for key, tup in decos]
        return tups

    def reset(self, undoTups):
        for tup in undoTups:
            (row, col) = tup
            self.unset(row, col)

    def search(self, maxWidth=2, maxDepth=2, curDepth=0):
        if curDepth > maxDepth:
            return None
        # Fast-forward provable moves.
        tups = self.prepSearch()
        if tups == None:
            return None
        undoTups = [(row, col) for (row, col, valid) in tups]
        needRecalc = True
        while needRecalc:
            needRecalc = False
            for tup in tups:
                (row, col, valid) = tup
                if len(valid) == 1:
                    if self.set(row, col, valid[0]):
                        self.reset(undoTups)
                        return None
                    needRecalc = True
                else:
                    break
            if needRecalc:
                tups = self.prepSearch()
                if tups == None:
                    self.reset(undoTups)
                    return None
        # Search.
        if len(tups) == 0:
            print "Solved!",
            print "%r" % self
            return self
        for tup in tups:
            (row, col, valid) = tup
            if len(valid) > maxWidth:
                break
            for val in valid:
                self.set(row, col, val)
                ret = self.search(maxWidth, maxDepth, curDepth+1)
                if ret != None:
                    return ret
                self.unset(row, col)
        self.reset(undoTups)
        return None

    def tlc(self):
        row = self._rows[0]
        return (row[0]*100 + row[1]*10 + row[2])

def read_input(infile):
    boards = []
    f = open(infile)
    lines = f.readlines()
    i = 0
    while i < len(lines):
        name = lines[i]
        rows = lines[i+1:i+10]
        boards.append(Board(name, rows))
        i += 10
    return boards

boards = read_input("sudoku.txt")

solved = []
for board in boards:
    for maxWidth in xrange(2, 10):
        result = None
        for maxDepth in xrange(1, board.nunset()):
#            print "maxWidth=%d, maxDepth=%d" % (maxWidth, maxDepth)
            result = board.search(maxWidth, maxDepth)
            if result != None:
                solved.append(result)
                break
        if result != None:
            break

answer = 0
for board in solved:
    answer += board.tlc()
print answer
