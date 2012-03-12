from binlab import *
import sys
#sys.setrecursionlimit(40)

"""
a = ComplimentBinary(7)
b = ComplimentBinary(10)
j = ComplimentBinary(-1)
"""

a = SignedBinary(7)
b = ComplimentBinary(-10)
j = SignedBinary(-1)

a + b
a - b
a * b
a & b
a ^ b
a | b

a.xnor(b)
-a
+a
abs(a)
~a
