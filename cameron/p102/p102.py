#!/usr/bin/python

def p102():
    f = open("triangles.txt")
    f = f.readlines()
    for line in f:
        tri = line.strip().split(',')
        for i, x in enumerate(tri):
            tri[i] = int(x)
        print tri

def contains_origin(p1, p2, p3):
    

if __name__ == "__main__":
    p102()
