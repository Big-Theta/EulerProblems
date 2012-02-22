#!/usr/bin/python

def problem67():
    f = open("triangle.txt", "r")
    arr = []
    for i, line in enumerate(f.readlines()):
        arr.append(line.strip().split())
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    arr.pop()
    for i, line in enumerate(arr):
        if i > 0:
            arr[i - 1] = [0] + arr[i - 1] + [0]
            for j in range(len(arr[i])):
                arr[i][j] += max(arr[i - 1][j], arr[i - 1][j + 1])

    print max(arr[len(arr) - 1])

