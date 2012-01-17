#!/usr/local/bin/python

import math
from mr import *

def p263():
  print "hello p263"
  primes = [3]
  testnum = 5
  found = 0
  total = 0
  while found < 4:
    if is_probable_prime(testnum):
      if primes[-1] != testnum - 6:
        primes = [testnum]
      else:
        primes.append(testnum)
      
      if len(primes) >= 4 and test_practicality(primes[-1] - 9):
        found += 1
        print "found a paradise!"
        print "paradise at %i" % primes[-1] - 9
        total += primes[-1] - 9
    testnum += 2
  print "total is " + total

def test_practicality(n):
  for i in range(-8, 9, 4):
    div_sum = 0
    current = n + i
    for d in range(1, current):
      if current % d == 0:
        if d > div_sum + 1:
          return False
        div_sum += d
  return True

p263()
