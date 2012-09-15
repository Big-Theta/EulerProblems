import math
import numpy as np

def find_angle(p, q):
    opp = q[1] - p[1]
    adj = q[0] - p[0]
    if adj == 0:
        return np.pi / 2
    return np.arctan(float(opp) / float(adj))

def is_same_side(p, q, trial_a, trial_b=[0, 0]):
    threshhold = find_angle(p, q)
    a_is_top = None
    b_is_top = None
    if (((find_angle(p, trial_a) >= threshhold and (p > trial_a))) or
        ((find_angle(p, trial_a) < threshhold) and (p < trial_a))):
        a_is_top = True
    else:
        a_is_top = False

    if (((find_angle(p, trial_b) >= threshhold and (p > trial_b))) or
        ((find_angle(p, trial_b) < threshhold) and (p < trial_b))):
        b_is_top = True
    else:
        b_is_top = False

    if a_is_top == b_is_top:
        return True
    else:
        return False

def contains_origin(triangle):
    p, q, r = triangle
    if (is_same_side(p, q, r) and
        is_same_side(p, r, q) and
        is_same_side(r, q, p)):
        return True
    else:
        return False

def create_list():
    triangles = []
    with open("triangles.txt", "r") as infile:
        for line in infile.readlines():
            line = line.strip()
            points = line.split(',')
            points = [int(x) for x in points]
            triangles.append([[points[0], points[1]],
                              [points[2], points[3]],
                              [points[4], points[5]]])
    return triangles


if __name__ == '__main__':
    counter = 0
    for triangle in create_list():
        if contains_origin(triangle):
            counter += 1
    print counter

