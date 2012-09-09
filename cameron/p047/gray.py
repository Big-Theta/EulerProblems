#!/usr/bin/python

def bin2gray32(num):
    ans = num ^ (num >> 1)
