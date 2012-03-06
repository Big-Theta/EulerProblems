def isbin (binval):
    if not type(binval) is str:
        return False
    for i in binval:
        binset = set("01")
        if not i in binset: return False
    return True

def isfixed(binval):
    if not type (binval) is str:
        return False
    for i in binval:
        fixedset = set("01.")
        for i in binval:
            if not i in fixedset: return False
    return True

def ispos(binval):
    if binval[0] == '0':
        return True
    else:
        return False

def isneg(binval):
    if binval[0] == '1':
        return True
    else:
        return False

def int2bin(intval):
    binval = ""
    while intval > 0:
        if intval % 2 == 0:
           bit = '0'
        else:
            bit = '1'
        binval = binval + bit
        intval = intval/2
    return binval

def bin2int(binval):
    intval = 0
    pwr = len(binval)-1
    for i in range(len(binval)):
        if binval[i] == '1':
            intval = intval + 2**pwr
        pwr = pwr - 1
    return intval

def bin2frac(binval):
    fracval = 0
    pwr = -1
    for i in binval:
        if i == '1':
            fracval = fracval + 2**pwr
        pwr = pwr-1
    return fracval

def fp2dec(fpval):
    decval = 0.0
    [left, right] = fpval.split('.')
    decval = decval + bin2int(left) + bin2frac(right)
    return(decval)

def int2sif(binval):
    S = I = F = 0
    sign = binval[0]
    for i in binval:
       if i == sign:
           S += 1
       else:
           break
    I = len(binval) - S
    return([S, I, F])

def fp2sif(binval):
   # should check to see that this is a fp number (has '.')
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
    sum = ""
    carry = "0"
    retval = ""
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    for i in range(n):
        j = n-i-1
        retval = bitsum(binval1[j],binval2[j],carry) + retval
        carry = bitcarry(binval1[j],binval2[j],carry)
    if carry == "1":
        retval = carry + retval;
    return retval

def binsub(binval1, binval2):
    return binadd(binval1,binneg(binval2))

def binoflows(binval1, binval2):
    sum = ""
    carry = "0"
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    for i in range(n):
        j = n-i-1
        sum = bitsum(binval1[j],binval2[j],carry) + sum
        carry = bitcarry(binval1[j],binval2[j],carry)
    if ispos(binval1) and isneg(binval2): return False
    if isneg(binval1) and ispos(binval2): return False
    if ispos(binval1) and ispos(binval2) and isneg(sum): return True
    if isneg(binval1) and isneg(binval2) and ispos(sum): return True
    return False 


# n is the number of bits we want to pad to
def binpadleft(binval,n,padval='0'):
    if not isbin(binval): return
    dif = n - len(binval)
    if dif <= 0: return binval
    newval = binval
    for i in range(dif):
        newval = padval + newval
    return newval 

def binpadright(binval,n,padval='0'):
    if not isbin(binval): return
    dif = n - len(binval)
    if dif < 0: return binval
    newval = binval
    for i in range(dif):
        newval = newval + padval
    return newval 

def binsext(binval, n):
    return binpadleft(binval,n,binval[0])

def bitsum (ain, bin, carry):
    if ain != bin:
       temp = '1'
    else: 
       temp = '0'   
   
    if carry != temp:
        return '1'
    else:
        return '0'

def bitcarry(ain, bin, cin):
    if (ain=='1' and bin=='1') or (ain=='1' and cin=='1') or (bin=='1' and cin=='1'):
        return '1'
    else:
        return '0'

def binnot(binval):
    retval = ""
    for i in binval:
        if i == '0':
            retval += '1'
        else:
            retval += '0'
    return retval 

def binneg(binval):
    temp = binnot(binval);
    retval = binadd(temp,'1')
    return retval

def binand(binval1,binval2):
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    retval = ""
    for i in range(n):
        if (binval1[i] == '1') and (binval2[i] == '1'):
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binor(binval1,binval2):
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    retval = ""
    for i in range(n):
        if (binval1[i] == '1') or (binval2[i] == '1'):
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binxor(binval1,binval2):
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    retval = ""
    for i in range(n):
        if binval1[i] == binval2[i]:
            retval = retval + '0'
        else:
            retval = retval + '1'
    return retval

def binxnor(binval1,binval2):
    n = max(len(binval1),len(binval2))
    binval1=binpadleft(binval1,n,"0");
    binval2=binpadleft(binval2,n,"0");
    retval = ""
    for i in range(n):
        if binval1[i] == binval2[i]:
            retval = retval + '1'
        else:
            retval = retval + '0'
    return retval

def binprint(binval):
    retval = ""
    n = len(binval)
    for i in range(n):
        j = n-i-1
        retval = binval[j] + retval;
        if i % 4 == 3:
            retval = ' ' + retval;
    return retval


