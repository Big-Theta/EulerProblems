#! /usr/bin/env python

"""decbingray.py -- A collection of coding conversion functions.

The functions convert between Python numbers (integers and longs)
and their binary and Gray code representations, which are implemen-
ted as Python strings containing only '1' and '0' (without leading 
zeros). The converting functions do handle leading zeros correctly,
though. 

    >>> from decbingray import *
    >>> bin2dec('0')
    0
    >>> bin2dec('0001')
    1

A function to pad bit strings with leading zeros is not provided 
as this is very simple to do in Python using the zfill function 
in the string module, e.g.:

    >>> from string import zfill
    >>> zfill("1010", 8)
    '00001010'

A block grouping function, rgroup(), is provided, though, in
order to aid in the tedious procedure of manually counting bits
(unfortunately the standard string module does not contain a 
grouping function):

    >>> from decbingray import *
    >>> import sys, string
    >>> rgroup(dec2bin(sys.maxint), 8)
    '1111111 11111111 11111111 11111111'
    >>> bin = '1111 1111   ' * 4
    >>> bin = string.replace(bin, ' ', '')
    >>> bin
    '11111111111111111111111111111111'
    >>> bin2dec(bin)
    4294967295L
    >>> 2L**32-1
    4294967295L
    
When Python numbers (integers or longs) are involved as in- or 
output, there is a potential overflow issue. One solution is to 
provide two (almost identical) versions of the same funtion,
like bin2int() and bin2long(). The second is to provide only
one function, like bin2dec() that will return the 'appropriate' 
type or that can handle both number types as input. This is the 
one that has been implemented.

   >>> import sys
   >>> mi = sys.maxint
   >>> mi1 = sys.maxint + 1L
   >>> mi
   2147483647
   >>> mi1
   2147483648L
   >>> from decbingray import *
   >>> bmi, bmi1 = dec2bin(mi), dec2bin(mi1)
   >>> rgroup(bmi)
   '111 1111 1111 1111 1111 1111 1111 1111'
   >>> rgroup(bmi1)
   '1000 0000 0000 0000 0000 0000 0000 0000'
   >>> bin2dec(bmi)
   2147483647
   >>> bin2dec(bmi1)
   2147483648L

Dinu Gherman
"""


import sys, random


# Utility functions.

# This one is actually not needed anymore, 
# but might still be considered useful.
def stringXOR(a, b):
    """Perform XOR function on two strings of same length.

    E.g. stringXOR('1010', '1111') ==> '0101'.
    Works also for non-binary string, like:
    stringXOR('ACCABC', 'ABBAAC') ==> '011010'."""

    msg = "Strings do not have same length: %d, %d!"
    assert len(a) == len(b), msg % (len(a), len(b))
    
    # Set counter.
    cnt = len(a) - 1

    result = ''
    # Iterate until cnt < 0.
    while cnt + 1:
        # Do XOR.
        result = `(a[cnt] != b[cnt])` + result
        # `...` returns '0' or '1'
        cnt = cnt - 1

    return result


def rgroup(str, size=4, sep=' '):
    """Group a string into blocks (starting at the right).

    E.g. rgroup('11000', 4) ==> '1 1000'."""
    
    # The dual function lgroup() is not interesting in this
    # context and, hence, is left as an exercize...
    
    assert len(sep) == 1, "Seperator string must have length 1!"
    
    if str == '':
        return ''
        
    if len(str) <= size:
        return str
    else:
        res = ''
        s = str[:]
        while s:
            res = sep + s[-size:] + res
            s = s[:-size]
        if res[0] == sep:
            res = res[1:]
        return res


# Conversion functions between strings. (No numbers involved.)

def gray2bin(gray):
    """Convert gray string to binary string.
    
    E.g. gray2bin('1111') ==> '1010' and gray2bin('') ==> '0."""

    # Gracefully handle degenerate case.
    if not gray:
        return '0'
    
    # Set counter.
    cnt = 0
    
    # Copy first 'bit'.
    bin = gray[0]

    # Iterate.
    while cnt < len(gray)-1:
        # Do XOR.
        bin = bin + `bin[cnt] != gray[cnt+1]`
        # `...` returns '0' or '1'
        cnt = cnt + 1

    # Return binary representation.
    return bin


def bin2gray(bin):
    """Convert binary string to gray string.
    
    E.g. bin2gray('1010') ==> '1111' and  bin2gray('') ==> '0'."""

    # Gracefully handle degenerate case.
    if not bin:
        return '0'
    
    # Set counter.
    cnt = 0
    
    # Copy first 'bit'.
    gray = bin[0]

    # Iterate.
    while cnt < len(bin)-1:
        # Do XOR.
        gray = gray + `bin[cnt] != bin[cnt+1]`
        # `...` returns '0' or '1'
        cnt = cnt + 1

    # Return gray representation.
    return gray
    

# Conversion functions with numbers as in- or output.

def dec2bin(num):
    """Convert long/integer number to binary string.

    E.g. dec2bin(12) ==> '1100'."""

    assert num >= 0, "Decimal number must be >= 0!"

    # Gracefully handle degenerate case.
    # (Not really needed, but anyway.)    
    if num == 0:
        return '0'

    # Find highest value bit.
    val, j = 1L, 1L
    while val < num:
        val, j = val*2L, j+1L

    # Convert.
    bin = '' 
    i = j - 1
    while i + 1L:
        k = pow(2L, i)
        if num >= k:
            bin = bin + '1'
            num = num - k
        else:
            if len(bin) > 0:
                bin = bin + '0'
        i = i - 1L

    return bin


def dec2gray(num):
    """Convert integer/long to gray string.
    
    E.g. dec2gray(8) ==> '1100'."""

    assert num >= 0, "Decimal number must be >= 0!"
    
    # Gracefully handle degenerate case.
    # (Not really needed, but anyway.)    
    if num == 0:
        return '0'
        
    bin = dec2bin(num)
    gray = bin2gray(bin)
    return gray
    

def bin2dec(bin):
    """Convert binary string to integer/long.

    E.g. bin2dec('1100') ==> 12."""

    # Gracefully handle degenerate case.
    # (Not really needed, but anyway.)    
    if bin in ('0', ''):
        return 0

    # Find highest value bit.
    val, j = 1L, 1L
    while j < len(bin):
        val, j = val*2, j+1L

    # Convert.
    num = 0L
    for j in range(len(bin)):
        if bin[j] == '1':
            num = num+val
        val = val/2

    # Return integer if possible, long otherwise.
    try:
        return int(num)
    except OverflowError:
        return num
    

def gray2dec(gray):
    """Convert gray string to integer/long.
    
    E.g. gray2dec('1100') ==> 10."""
    
    # Gracefully handle degenerate case.
    # (Not really needed, but anyway.)    
    if gray in ('0', ''):
        return 0
        
    bin = gray2bin(gray)
    return bin2dec(bin)
    

# Test functions.

def randomBitString(length, msb1=1):
    "Return a random bit string of a specified length."

    assert length > 0
    
    # If length should be one, we return a random bit...
    if length == 1:
        b = str(random.randint(0, 1))
    # ... else we return a random bit string ...
    else:
        # ... starting with most significant bit = '1', 
        # if desired ...
        if msb1:
            b = '1'
            for i in xrange(length-1):
                b = b + str(random.randint(0, 1))
        # ... or with a random bit.
        else:
            b = ''
            for i in xrange(length):
                b = b + str(random.randint(0, 1))
        
    return b


def testLongVsInt():
    print "Testing long vs. int\n"
    maxint = sys.maxint
    bmi = rgroup(dec2bin(maxint), 8)
    bmi1 = rgroup(dec2bin(maxint+1L), 8)
    print "maxint", maxint, bmi
    print "maxint + 1L", maxint+1L, bmi1
    print
    # maxint
    b = '1111111111111111111111111111111'
    print bin2dec(b)
    # maxint + 1, should not raise OverflowError
    b = '10000000000000000000000000000000'
    print bin2dec(b)


def printTable(numbers, converters):
    "Print a conversion table for a list of numbers and functions."

    print "Conversion table\n"
    
    # Find max. column with for bit strings.
    if type(numbers[0]) == type(0):
        m = len(dec2bin(max(numbers)))
    elif type(numbers[0]) == type('0'):
        m = len(numbers[0])
    format = '%' + str(m) + 's '
    
    # Print the column titles (with shortened function names).
    titleMap = {dec2bin:'d2b', dec2gray:'d2g', 
        gray2dec:'g2d', gray2bin:'g2b',
        bin2gray:'b2g', bin2dec:'b2d'}
    titles = ['']
    for conv in converters:
        titles.append(titleMap[conv])
    print format*len(titles) % tuple(titles) + '\n'
    
    # Print one row of converted values, derived from the first.
    values = []
    for i in numbers:
        values = [i]
        for conv in converters:
            values.append(conv(values[-1]))
        print format*len(values) % tuple(values)


def test():
    # testLongVsInt()
    # print
    
    maxint = sys.maxint
    printTable(range(16), # +[maxint-1, maxint, maxint+1L], 
               [dec2bin, bin2gray, gray2bin, bin2dec, dec2gray, gray2dec])
    print
    
    list = []
    for i in range(16):
        list.append(randomBitString(4))
    printTable(list, [bin2gray, gray2bin, bin2dec, dec2gray, gray2dec])
    print
    
    list = []
    for i in range(16):
        list.append(randomBitString(4, msb1=0))
    printTable(list, [bin2gray, gray2bin, bin2dec, dec2gray, gray2dec])
    print
    

if __name__ == '__main__':
    test()
    
