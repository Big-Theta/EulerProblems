from __future__ import print_function
from abc import ABCMeta, abstractmethod, abstractproperty
import re
import inspect

BITSDEFAULT = 8

class BinLabError(Exception):
    """Generic error for illegal operations."""
    pass


def bincast(obj, new_type, bits=BITSDEFAULT):
    """Takes the obj and casts is as an object of type new_type.

    This will modify the underlying value of the returned value. For example,
    int(bincast(UnsignedBinary('1100'), ComplimentBinary)) -> -4
    @param obj (BaseBinary obj)
        Object to cast
    @param new_type (BaseBinary obj or str)
        if BaseBinary obj, this is the return type of the case. If str, then
        the str must specify the desired type.
    """

    type_map = {'ComplimentBinary' : ComplimentBinary,
                'UnsignedBinary' : UnsignedBinary,
                'GrayCode' : GrayCode,
                'SIFBinary' : SIFBinary}

    assert isinstance(obj, BaseBinary) or isinstance(obj, int)

    if isinstance(new_type, BaseBinary):
        new_type = new_type.obj_type

    if new_type in type_map.keys():
        return type_map[new_type](int(obj), bits=bits)
    elif new_type in type_map.values():
        return new_type(int(obj), bits=bits)
    else:
        raise BinLabError("Could not cast {0} "
                          "as type {1}.".format(type(obj), type(new_type)))


def binfactory(val, new_type, bits=None):
    """
    @param val (str or int)
        The new value. If str, then this is assumed to be encoded in the
        new_type encoding.
    @param new_type (BaseBinary obj or str)
        if BaseBinary obj, this is the return type of the case. If str, then
        the str must specify the desired type.
    @param bits
        If val is a str and bits is None, bits defaults to the length of the
        str. If val is an int and bits is NONE, bits defaults to BITSDEFAULT.
    """

    type_map = {'ComplimentBinary' : ComplimentBinary,
                'UnsignedBinary' : UnsignedBinary,
                'GrayCode' : GrayCode,
                'SIFBinary' : SIFBinary}

    if not bits:
        if type(val) == str:
            bits = len(val)
        elif type(val) == int:
            bits = BITSDEFAULT

    if new_type in type_map.keys():
        return type_map[new_type](val, bits=bits)
    elif new_type in type_map.values():
        return new_type(val, bits=bits)
    else:
        raise BinLabError()


def my_coerce(func):
    def decorated(self, other):
        return func(self, bincast(other, self, bits=self.bits))

    # Without this, the func_name would show up as decorated. However, in
    # the _display decorator, we check for the function name.
    decorated.func_name = func.func_name
    return decorated


def _print_binary_op(op_a, op_b, func_symbol, retval):
    # Well... this is a pretty terrible solution... I'm making certain that
    # the module that initiated this call is NOT binlab.py. So, this makes the
    # assumption that all paths that should be printed are short.
    if re.search('binlab.py', inspect.stack()[2][1]):
        return

    fmt_str = []
    fmt_str += ["{0:>20}{1:>20}{2:>20}{3:>20}{4:>20}".format(
            'Encoding |', 'Binary Value |', 'Int Value |', 'Hex Value |',
            'Oct Value |')]
    fmt_str += ["{a[type_of]:<20}|{a[bin_of]:>20}{a[int_of]:>20}"
                "{a[hex_of]:>20}{a[oct_of]:>20}"]
    fmt_str += ["{b[type_of]:<20}{func_symbol:>2}{b[bin_of]:>17}"
                "{func_symbol:>2}{b[int_of]:>17}"
                "{func_symbol:>2}{b[hex_of]:>17}"
                "{func_symbol:>2}{b[oct_of]:>17}"]
    fmt_str += ["-" * 100]  # This could be separated out to individual
                            # equal bars
    fmt_str += ["{res[type_of]:>20}{res[bin_of]:>20}{res[int_of]:>20}"
                "{res[hex_of]:>20}{res[oct_of]:>20}"]
    fmt_str = '\n'.join(fmt_str)

    a = {}
    b = {}
    res = {}

    for dict_, operand in [[a, op_a], [b, op_b], [res, retval]]:
        dict_['type_of'] = operand.obj_type
        dict_['bin_of'] = str(operand)
        dict_['int_of'] = operand.val
        dict_['hex_of'] = hex(operand.val)
        dict_['oct_of'] = oct(operand.val)

    print(fmt_str.format(a=a, b=b, res=res, func_symbol=func_symbol))


def _display(func):
    """This is a decorator for binary operations.

    It will display the
    operands in their native binary, decimal, and hexadecimal. It will show
    the results, and the operation performed."""

    def decorated(self, *other):
        """self is expected because this will only decorate methods. other,
        however, might or might not exist."""

        retval = func(self, *other)
        op = re.search("(?P<operation>__\w+__)", func.func_name)
        if not op:
            raise BinLabError('"{0}" is not a recognized BinLab '
                              'function.'.format(func.func_name))
        else:
            if op.group('operation') in self._unary_func_names:
                _print_unary_op(self, retval)
            elif op.group('operation') in self._binary_func_names:
                #other = bincast(other[0], self, bits=self.bits)
                #other = other[0]
                _print_binary_op(self, other[0],
                                 self._binary_func_names[func.func_name],
                                 retval)
            elif op.group('operation') in self._comparison_func_names.keys():
                _print
            else:
                raise BinLabError('"{0}" is not a recognized BinLab '
                                  'operation.'.format(op.group('operation')))

        return retval

    return decorated


class BaseBinary(object):
    """This base class defines all of the arithmatic operations for the
    inheriting classes.

    Note: I'm not metaclassing because the syntax is different
    between python2 and python3.

    This class needs to define operations for quite a number of
    operators. Each of these operators must first coerce the operands to
    a common type, then must be able to display the operations, and then must
    return the correct values. For all of them, the operations are the same:

    1) Coerce the second operand into the datatype of the first.
    2) Perform the operation using obj1.val OP obj2.val
    3) Report the display type, operators, and return value to a display
       function.
    4) Return the correct value.

    This could plausibly be done with some metaclass shenatigans. First, it
    would probably be pragmatic to remove the ABCMeta definition and instead
    use a Python 2.5 style abstract base class. Second, we would define a
    metaclass that automatically applies 2 decorators to the methods named
    in the _(\w+)_func_names lists below. The first would coerce the second
    argument into the datatype of the first (using bincast), and the second
    decorator would decorate the operator with the appropriate _print function.

    Instead, I'm going to manually apply these decorators, because that
    syntax should be the same for python2 and python3.
    """

    __metaclass__ = ABCMeta

    # These names are used to switch on the correct display mechanism.
    # TODO: None of the unary or comparison functions have stubs yet.
    _unary_func_names = ['__nonzero__', '__neg__', '__pos__', '__abs__',
                         '__invert__', '__oct__', '__hex__']
    _binary_func_names = {'__add__' : '+', '__sub__' : '-', '__mul__' : '*',
                          '__and__' : '&', '__xor__' : '^', '__or__' : '|'}
    #  '__lshift__', '__rshift__', 
    _comparison_func_names = ['__cmp__']
    #['__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__']
    _boolean_func_names = ['__nonzero__']


    @abstractmethod
    def __init__(self, val=0, bits=BITSDEFAULT):
        """
        @param val (int or str)
            If str, use base 10.
        @param bits (int)
            The number of bits to use in the representation.
        @param encoding (str)
            Use one of ['compliment', 'signed', 'inverse']
        """

        self.val = int(val)
        self.bits = bits
        # FIXME
        # I'm INTENDING for this to call the method obj_type.setter. I sorta
        # doubt that that this is what is happening, however. Use the __dict__
        # or __setattr__ method instead? At the very least, confirm that
        # I'm not overwritting the method.
        self.obj_type = "BaseBinary"

        # Not yet used
        self.endian = 'little'

    def sign(self):
        return '0' if self.val >= 0 else '1'

    @abstractproperty
    def obj_type(self):
        return self._obj_type

    @obj_type.setter
    def obj_type(self, new_val):
        self._obj_type = new_val

    @abstractproperty
    def bits(self):
        """The alternative to this is to import abc and then set __metaclass__
        to abcmeta, or something like that."""

        return self._bits

    @bits.setter
    def bits(self, bits):
        """This method  is the reason for the properties. When we set the bits,
        we want to automatically truncate or extend the binary number."""

        self._bits = bits

    @bits.deleter
    def bits(self):
        del self._bits

    @abstractmethod
    def _truncate(self):
        """Called by bits.setter after the bits have been shortened."""
        pass

    @abstractmethod
    def _extend(self):
        """Called by bits.setter after the bits have been lengthened."""
        pass

    @abstractmethod
    def __str__(self):
        str_val = []
        str_val += ["val (base 10): {self.val}"]
        str_val += ["bits: {self.bits}"]
        str_val = '\n'.join(str_val)
        return str_val.format(self=self)

    def inverse(self):
        """Returns the inverse.

        I would use (self ^ 0), but I don't have a 0 or 1 easily defined."""

        new_str = []
        for c in str(self):
            new_str.append('1' if str(c) == '0' else '0')

        new_str = ''.join(new_str)
        return binfactory(new_str, self.obj_type)

    def __int__(self):
        return self.val

    @_display
    @my_coerce
    def __add__(self, other):
        # The int branch is used in a situation where I use (self + 1) to
        # find the negative representation of some numbers. It's nice to be
        # able to increment easily. I don't think that an int needs be
        # supported in any other operation, except maybe __sub__?
        if type(other) == int:
            op_b = binfactory(val=other, new_type=self.obj_type)
        else:
            op_b = bincast(obj=other, new_type=self.obj_type,
                           bits=self.bits)
        retval = binfactory(val=int(self) + int(op_b),
                            new_type=self.obj_type,
                            bits=self.bits)
        return retval

    def __sub__(self, other):
        op_b = bincast(obj=other, new_type=self.obj_type, bits=self.bits)
        retval = binfactory(val=int(self) - int(op_b),
                            new_type=self.obj_type,
                            bits=self.bits)
        return retval

    def __mul__(self, other):
        op_b = bincast(obj=other, new_type=self.obj_type, bits=self.bits)
        # Omitting the bits param and using a str for val so that auto
        # bits sizing will take place.
        retval = binfactory(val=bin(int(self) * int(op_b)),
                            new_type=self.obj_type)
        return retval

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == '1' and str(other)[i] == '1':
                new_str.append('1')
            else:
                new_str.append('0')

        new_str = ''.join(new_str)
        return binfactory(new_str, self.obj_type)

    def __xor__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == str(other)[i]:
                new_str.append('0')
            else:
                new_str.append('1')

        new_str = ''.join(new_str)
        return binfactory(new_str, self.obj_type)

    def __or__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == '1' or str(other)[i] == '1':
                new_str.append('1')
            else:
                new_str.append('0')

        new_str = ''.join(new_str)
        return binfactory(new_str, self.obj_type)


class ComplimentBinary(BaseBinary):
    def __init__(self, val=0, bits=8):
        BaseBinary.__init__(self, val=0, bits=8)
        self.obj_type = 'ComplimentBinary'

        if type(val) == int:
            self.val = val
        # TODO This doesn't handle hex strings.
        elif type(val) == str:
            self.val = int(val, 2)
            """
            if val.startswith('0b') or val.startswith('-0b'):
                val = int(val, 2)
            elif val.startswith('0x') or val.startswith('-0x'):
                val = int(val, 16)
            else:
                val = int(val)
            """
        else:
            raise BinLabError()

        self.bits = bits  # This is done in super, but it will trigger a
                          # possible resize

    @property
    def obj_type(self):
        #BaseBinary.obj_type(self)
        return self._obj_type

    @obj_type.setter
    def obj_type(self, new_val):
        #BaseBinary.obj_type(self, new_val)
        self._obj_type = new_val

    @property
    def bits(self):
        #BaseBinary.bits(self)
        return self._bits

    @bits.setter
    def bits(self, bits):
        #BaseBinary.bits(self, bits)
        self._bits = bits
        if bits > len(str(self)):
            self._extend()
        elif bits < len(str(self)):
            self._truncate()

    @bits.deleter
    def bits(self):
        BaseBinary.bits(self)

    def _truncate(self):
        """Should be called ONLY from bits.setter. This takes the rightmost
        bits and creates a new object using these. It then sets the self.val
        to this new value."""

        BaseBinary._truncate(self)
        self.val = int(binfactory(val=str(self)[-self.bits:],
                                  new_type=self.obj_type))

    def _extend(self):
        """Should only be called from bits.setter."""

        pass

    def __str__(self):
        if self.sign() == '0':
            rep = bin(self.val).lstrip('0b')
        else:
            rep = bin(self.val).lstrip('-0b')
            rep = binfactory(val=rep, new_type=self.obj_type)
            rep = rep.inverse()
            rep = rep + 1

        return "{rep:{sign}>{self.bits}}".format(rep=rep,
                                                 self=self, sign=self.sign())



class SignedBinary(BaseBinary):
    pass


class UnsignedBinary(BaseBinary):
    pass


class GrayCode(BaseBinary):
    pass


class SIFBinary(BaseBinary):
    pass


def main():
    """I'm using a main function instead of placing all of this in the
    __name__ == '__main__' conditional because it reduces parse times for
    imports."""

    a = ComplimentBinary(10)
    b = ComplimentBinary(7)
    j = ComplimentBinary(-1)
    print(a + b)
    """
    k = ComplimentBinary(-7)
    """
    """
    x = ComplimentBinary(10)
    y = ComplimentBinary(10010012011)
    z = ComplimentBinary(10010012011, bits=16)
    """

    """
    print('a    : ' + str(a))
    print('b    : ' + str(b))
    print('--- a OP b ---')
    print('add  : ' + str(a + b))
    print('minus: ' + str(a - b))
    print('times: ' + str(a * b))
    print('and  : ' + str(a & b))
    print('xor  : ' + str(a ^ b))
    print('or   : ' + str(a | b))
    print()
    print('--- b OP a ---')
    print('add  : ' + str(b + a))
    print('minus: ' + str(b - a))
    print('times: ' + str(a * b))
    print('and  : ' + str(b & a))
    print('xor  : ' + str(b ^ a))
    print('or   : ' + str(b | a))
    print('--------------')
    print(j)
    print(k)
    """
    """
    print(a.__add__)
    print(dir(a.__add__))
    print(a.__add__.__func__)
    """

    """
    print(x)
    print(y)
    print(z)
    """

if __name__ == '__main__':
    main()
