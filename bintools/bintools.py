# Bintools
#
# Author: Greg Donohoe
# Start Date: March 3, 2011
#
# Purpose: A tool to facilitate design of fixed point data processing applications
# such as digital signal and image processing and automatic control.
#
# Personal Goal: Learn to program in Python
#
# These are all modules to serve either as top-level modules to be invoked from
# the Python command line, or as subordinate modules to be called by others.
#
"""
A tool to facilitate design of fixed point data processing applications
such as digital signal and image processing and automatic control.
"""
def isbin (binval):
    """
    Return True if binval is binary
    """
    if not type(binval) is str:
        return False
    for i in binval:
        if not i in set('01'): return False
    return True

def ishex (hexval):
    """
    Return True if hexval is hexadecimal
    """
    for i in hexval:
       if not i in set('0123456789ABCDEF'): return False
    return True

def isfixed(binval):
    """
    Return True if binval is fixed point (fraction or mixed)
    """
    if not type (binval) is str:
        return False
    for i in binval:
        fixedset = set("01.")
        for i in binval:
            if not i in fixedset: return False
    return True

def isint(binval):
    """
    Return True if binval is integer
    """
    if '.' in binval:
        return False
    else:
        return True

# Determine whether the data is positive
    """
    Return True if binval is positive or zero
    """
def ispos(binval):
    if binval[0] == '0':
        return True
    else:
        return False

def isneg(binval):
    """
    Return True if binval is negative
    """
    if binval[0] == '1':
        return True
    else:
        return False

def int2bin(intval):
    """
    Convert decimal value intval to binary
    """
    if intval < 0:
        negative = True
        intval = -intval
    else:
        negative = False
    binval = ""
    while intval > 0:
        if intval % 2 == 0:
           bit = '0'
        else:
           bit = '1'
        binval = bit + binval
        intval = intval/2
    if negative:
        if binval[0] == '1':	 
            binval = '0' + binval   
        binval = binneg(binval)
    return binval

def bin2int(binval):			# Binary to integer. Incorporate sign.
    """
    Convert binval to decimal integer
    """
    if binval[0] == '1':		# Negative number
        negative = True
        binval = binneg(binval)		# Invert it
    else:
        negative = False
    intval = 0
    pwr = len(binval)-1
    for i in range(len(binval)):
        if binval[i] == '1':
            intval = intval + 2**pwr
        pwr = pwr - 1
    if negative:			# Input was negative, so negate result
        intval = -intval
    return intval

def bin2frac(binval):
    """
    Convert binval to a decimal fraction
    """
    fracval = 0
    pwr = -1
    for i in binval:
        if i == '1':
            fracval = fracval + 2**pwr
        pwr = pwr-1
    return fracval

def fp2dec(fpval):
    """
    Convert fixed point fpval to decimal
    """
    decval = 0.0
    [left, right] = fpval.split('.')
    decval = decval + bin2int(left) + bin2frac(right)
    return(decval)

def int2sif(binval):
    """
    Return the Sign-Integer-Fraction (SIF) representation of a binary  integer
    """
    S = I = F = 0
    sign = binval[0]
    for i in binval:
       if i == sign:
           S += 1
       else:
           break
    I = len(binval) - S
    return([S, I, F])

# Convert fixed point number to SIF represn
def fp2sif(binval):
    """
    Return the Sign-Integer-Fraction (SIF) representation of binval
    should check to see that this is a fp number (has '.')
    """
    [left, right] = binval.split('.')
    S = I = F = 0
    sign = binval[0]
    for i in binval:
        if i == sign:
            S += 1
        else:
            break
    I = len(left) - S
    F = len(right)
    return([S, I, F])
    
def fpalign(fpval1, fpval2):
    """
    Align fixed point numbers for addition
    """
    [left1, right1] = fpval1.split('.')
    [left2, right2] = fpval2.split('.')

    if len(left1) > len(left2):
        left2 = binsext(left2,len(left1))

    if len(left2) > len(left1):
        left1 = binsext(left1,len(left2))
 
    if len(right1) > len(right2):
        right2 = binpadright(right2,len(right1))

    if len(right2) > len(right1):
        right1 = binpadright(right1,len(right2))

    fpval1 = left1 + '.' + right1
    fpval2 = left2 + '.' + right2
 
    return([fpval1, fpval2])

def fpadd(fpval1, fpval2):
    """
    Return fpval1 + fpval2 (binary fixed point numbers)
    """
    sum = ""
    carry = "0"
    retval = ""
    [tempval1, tempval2] = fpalign(fpval1, fpval2)
    n = len(tempval1)
    for i in range(n):
        j = n-i-1
        if not tempval1[j] == '.':
            retval = bitsum(tempval1[j],tempval2[j],carry) + retval
            carry = bitcarry(tempval1[j],tempval2[j],carry)
        else:
            retval = '.' + retval
    return retval
   
def binadd(binval1, binval2):
    """
    Return binval1 + binval2 (binary integers)
    """
    sum = ""
    carry = "0"
    retval = ""
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    for i in range(n):
        j = n-i-1
        retval = bitsum(binval1[j],binval2[j],carry) + retval
        carry = bitcarry(binval1[j],binval2[j],carry)
    if carry == "1":
        retval = carry + retval
    return retval

def binsub(binval1, binval2):
    """
    Return binval1 - binval 2 (binary integers)
    """
    return binadd(binval1,binneg(binval2))

def binoflows(binval1, binval2):
    """
    Return True if binval1 + binval2 would cause overflow
    """
    sum = ""
    carry = "0"
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    for i in range(n):
        j = n-i-1
        sum = bitsum(binval1[j],binval2[j],carry) + sum
        carry = bitcarry(binval1[j],binval2[j],carry)
    if ispos(binval1) and isneg(binval2): return False
    if isneg(binval1) and ispos(binval2): return False
    if ispos(binval1) and ispos(binval2) and isneg(sum): return True
    if isneg(binval1) and isneg(binval2) and ispos(sum): return True
    return False 


def binpadleft(binval,n,padval='0'):
    """
    Padd (extend) a binary number on the left
    n is the number of bits we want to pad to
    """
    if not isbin(binval): return
    dif = n - len(binval)
    if dif <= 0: return binval
    newval = binval
    for i in range(dif):
        newval = padval + newval
    return newval 

def binpadright(binval,n,padval='0'):
    """
    Pad (extend) a binary number on the right
    """
    if not isbin(binval): return
    dif = n - len(binval)
    if dif < 0: return binval
    newval = binval
    for i in range(dif):
        newval = newval + padval
    return newval 

# Sign extend a binary number
def binsext(binval, n):
    """
    Sign extend binvalue to a lenght of n bits
    """
    return binpadleft(binval,n,binval[0])

def bitsum (ain, bin, cin):
    """
    Return the sum bit of full adder operation abin+bin+cin
    """
    if ain != bin:
       temp = '1'
    else: 
       temp = '0'   
   
    if cin != temp:
        return '1'
    else:
        return '0'

def bitcarry(ain, bin, cin):
    """
    Return the carry bit of full adder operation abin+bin+cin
    """
    if (ain=='1' and bin=='1') or (ain=='1' and cin=='1') or (bin=='1' and cin=='1'):
        return '1'
    else:
        return '0'

# Invert a binary number
def binnot(binval):
    """
    Return not binval, i.e., bitwise inverse
    """
    retval = ""
    for i in binval:
        if i == '0':
            retval += '1'
        else:
            retval += '0'
    return retval 

def binneg(binval):
    """
    Return -binval
    """
    temp = binnot(binval)
    retval = binadd(temp,'1')
    return retval

def binand(binval1,binval2):
    """
    Return binval1 and binval2
    """
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    retval = ""
    for i in range(n):
        if (binval1[i] == '1') and (binval2[i] == '1'):
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binor(binval1,binval2):
    """
    Return binval1 nor binval2
    """
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    retval = ""
    for i in range(n):
        if (binval1[i] == '1') or (binval2[i] == '1'):
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binxor(binval1,binval2):
    """
    Return binval1 xor binval2
    """
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    retval = ""
    for i in range(n):
        if binval1[i] == binval2[i]:
            retval = retval + '0'
        else:
            retval = retval + '1'
    return retval

def binxnor(binval1,binval2):
    """
    Return binval1 xnor binval2
    """
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0")
    binval2=binpadleft(binval2,n,"0")
    retval = ""
    for i in range(n):
        if binval1[i] == binval2[i]:
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binprint(binval):
    """
    'Pretty print' binary number binval, in 4-bit groups
    """
    retval = ""
    n = len(binval)
    for i in range(n):
        j = n-i-1
        retval = binval[j] + retval
        if i % 4 == 3:
            retval = ' ' + retval
    return retval

def bin2hex(binval):
    """
    Return hex value of binval
    """
    if not isbin(binval): return
    import binhexdict
    retval = ""
    tempval = ""
    n = len(binval)
    for i in range(n):
        j = n-i-1
        tempval = binval[j] + tempval
        if i % 4 == 3:
            retval = binhexdict.binhex[tempval] + retval
            tempval = ""
    if not tempval == "":
        retval = binhexdict.binhex[tempval] + retval
    return retval

def hex2bin(hexval):
    """
    Return binary value of hexval
    """
    if not ishex(hexval): return
    import binhexdict
    retval = ""
    for i in hexval:
        retval = retval + binhexdict.hexbin[i]
    return retval            
