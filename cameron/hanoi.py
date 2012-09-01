#!/usr/bin/python

def move(dx, towers):
    done = False
    while not done:
        print towers
        if dx in towers[2]:
            done = True
            print "here0"
        elif dx in towers[1]:
            print "here1"
            towers = move(dx, [towers[1], towers[0], towers[2]])
            towers = [towers[1], towers[0], towers[2]]
        else:
            if towers[0][0] != dx:
                print "here3"
                towers = move(towers[0][towers[0].index(dx) - 1], [towers[0], towers[2], towers[1]])
                towers = [towers[0], towers[2], towers[1]]
            elif len(towers[2]) > 0 and towers[2][0] > dx:
                for i in range(1, 5):
                    if dx + i in towers[2]:
                        towers = move(dx + i, [towers[2], towers[0], towers[1]])
                        towers = [towers[1], towers[2], towers[0]]
            else:
                print "here4"
                towers[2] = [dx] + towers[2]
                towers[0] = towers[0][1:]
                done = True
    return towers

def hanoi(x):
    t0 = []
    for i in range(0, x):
        t0 = [i] + t0
    towers = [t0, [], []]
    for i in range(0, x):
        towers = move(i, towers)
        print towers
    print towers

if __name__ == "__main__":
    hanoi(5)
