# btfw - acronym for "bintools, fixed width"
#        Where "bintools" allows the word width to grow, btfw
#        fixes word width.

#import "../bintools/bintools"
import bintools

#width = 16	# default word width. Can be changed.

def init:
    
def btfwadd(binval1, binval2):
    if binval1[0] == binval2[0]:
        sameSign = True;
        print "Same sign"
    else:
        sameSign =  False;
    retval = bintools.binadd(binval1,binval2)
    print "return = ", len(retval),
    print "datapath width ", width
    if (len(retval) > width) and (sameSign):
      print "Overflow"
    return(retval)

