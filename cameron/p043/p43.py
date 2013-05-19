#!/usr/bin/python

def p43():
  i17 = 17



def isUnique(i_arr):
  taken = []
  for i in i_arr:
    while i > 0:
      i, r = divmod(i, 10)
      if r in taken:
        return False
      else:
        taken += [r]
  return True

def m(x):
  cur = 987
  while True:
    if cur == 0:
      yield 0
      cur = 987
    elif cur % x == 0 and len(set([cur % 10, (cur % 100) / 10, cur / 100])) > 2:
      yield cur
    cur -= 1

if __name__ == "__main__":
  p43();
