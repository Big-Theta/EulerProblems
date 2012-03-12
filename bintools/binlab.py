from __future__ import print_function
from abc import ABCMeta, abstractmethod, abstractproperty
import re
import inspect

BITSDEFAULT = 8
DISPLAY = True

class BinLabError(Exception):
    """Generic error for illegal operations."""
    pass


def toggle_display(set_value=None):
    """Toggles automatic display of operations.

    This exists so that a user who has used "from binlab import *" can still
    modify the value."""

    global DISPLAY
    if set_value:
        DISPLAY = set_value
    else:
        DISPLAY = not DISPLAY


def bincast(val, new_type, bits=None):
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
                'SignedBinary' : SignedBinary,
                'GrayCode' : GrayCode,
                'SIFBinary' : SIFBinary,
                'InverseBinary' : InverseBinary}

    assert (isinstance(val, BaseBinary) or isinstance(val, int) or
            isinstance(val, str))

    if not bits:
        if isinstance(val, BaseBinary):
            bits = val.bits
        elif isinstance(val, str):
            bits = len(val)
        else:
            bits = BITSDEFAULT

    # If an int or str is passed, we can't access an obj_type attr
    if isinstance(new_type, BaseBinary):
        new_type = new_type.obj_type

    # This is the case where we are performing mixed arithmatic.
    if isinstance(val, BaseBinary) and val.obj_type != new_type:
        return type_map[new_type](str(val), bits=bits)
    elif new_type in type_map.keys():
        if isinstance(val, BaseBinary):
            return type_map[new_type](int(val), bits=bits)
        else:
            return type_map[new_type](val, bits=bits)
    elif new_type in type_map.values():
        if isinstance(val, BaseBinary):
            return new_type(int(val), bits=bits)
        else:
            return new_type(val, bits=bits)
    else:
        raise BinLabError("Could not cast {0} "
                          "as type {1}.".format(type(val), type(new_type)))


def binlab_deco(func):
    return my_coerce(_display(func))
    #return _display(my_coerce(func))


def my_coerce(func):
    def decorated(self, *other):
        if other:
            return func(self, bincast(other[0], self, bits=self.bits))
        else:
            return func(self)

    # Without this, the func_name would show up as decorated. However, in
    # the _display decorator, we check for the function name.
    decorated.func_name = func.func_name
    return decorated


def _print_unary_op(operand, func_symbol, retval):
    fmt_str = ['-' * 100]
    fmt_str += ["| {0:<16} |{1:>18} |{2:>18} |{3:>18} |{4:>18} |".format(
            'Encoding', 'Binary Value', 'Integer Value', 'Hexadecimal Value',
            'Octal Value')]
    fmt_str += ["|" + "-" * 18 + "|" + ("-" * 19 + "|") * 4]
    fmt_str += ["| {a[type_of]:<16} |"
                "{func_symbol:>3}{a[bin_of]:>15} |"
                "{func_symbol:>3}{a[int_of]:>15} |"
                "{func_symbol:>3}{a[hex_of]:>15} |"
                "{func_symbol:>3}{a[oct_of]:>15} |"]
    fmt_str += ["|" + "-" * 18 + "|" + ("-" * 19 + "|") * 4]
    fmt_str += ["| {res[type_of]:<16} |{res[bin_of]:>18} |{res[int_of]:>18} |"
                "{res[hex_of]:>18} |{res[oct_of]:>18} |"]
    fmt_str += ['-' * 100]

    fmt_str = '\n'.join(fmt_str)
    a = {}
    res = {}

    for dict_, operand in [[a, operand], [res, retval]]:
        dict_['type_of'] = operand.obj_type
        dict_['bin_of'] = str(operand)
        dict_['int_of'] = operand.val
        dict_['hex_of'] = hex(operand.val)
        dict_['oct_of'] = oct(operand.val)

    print(fmt_str.format(a=a, res=res, func_symbol=func_symbol))

def _print_binary_op(op_a, op_b, func_symbol, retval):
    fmt_str = ['-' * 100]
    fmt_str += ["| {0:<16} |{1:>18} |{2:>18} |{3:>18} |{4:>18} |".format(
            'Encoding', 'Binary Value', 'Integer Value', 'Hexadecimal Value',
            'Octal Value')]
    fmt_str += ["|" + "-" * 18 + "|" + ("-" * 19 + "|") * 4]
    fmt_str += ["| {a[type_of]:<16} |{a[bin_of]:>18} |{a[int_of]:>18} |"
                "{a[hex_of]:>18} |{a[oct_of]:>18} |"]
    fmt_str += ["| {b[type_of]:<16} |"
                "{func_symbol:>2}{b[bin_of]:>16} |"
                "{func_symbol:>2}{b[int_of]:>16} |"
                "{func_symbol:>2}{b[hex_of]:>16} |"
                "{func_symbol:>2}{b[oct_of]:>16} |"]
    fmt_str += ["|" + "-" * 18 + "|" + ("-" * 19 + "|") * 4]
    fmt_str += ["| {res[type_of]:<16} |{res[bin_of]:>18} |{res[int_of]:>18} |"
                "{res[hex_of]:>18} |{res[oct_of]:>18} |"]
    fmt_str += ['-' * 100]
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
        # Well... this is a pretty terrible solution... I'm making certain that
        # the module that initiated this call is NOT binlab.py. So, this makes
        # the assumption that all paths that should be printed are short.

        if not DISPLAY or re.search('binlab.py', inspect.stack()[2][1]):
            return retval

        op = func.func_name
        if not op:
            raise BinLabError('"{0}" is not a recognized BinLab '
                              'function.'.format(func.func_name))
        else:
            if op in self._unary_func_names:
                _print_unary_op(self, self._unary_func_names[func.func_name],
                                retval)
            elif op in self._binary_func_names:
                _print_binary_op(self, other[0],
                                 self._binary_func_names[func.func_name],
                                 retval)
            else:
                raise BinLabError('"{0}" is not a recognized BinLab '
                                  'operation.'.format(op))

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
    _unary_func_names = {'__neg__' : '-', '__pos__' : '+',
                         '__abs__' : 'abs', '__invert__' : '~'}
    # xnor doesn't really exist, but it is discussed a lot in digital logic
    # classes.
    _binary_func_names = {'__add__' : '+', '__sub__' : '-', '__mul__' : '*',
                          '__and__' : '&', '__xor__' : '^', '__or__' : '|',
                          'xnor' : '!^'}
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
            Use one of ['compliment', 'signed', 'invert']
        """

        self.obj_type = "BaseBinary"

        if isinstance(val, int):
            self.val = val
        elif isinstance(val, str):
            self.val = int(val, 2)
        else:
            raise BinLabError()

        # Not yet used
        self.endian = 'little'

    @property
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

    def invert(self):
        """Returns the invert.

        I would use (self ^ 0), but I don't have a 0 or 1 easily defined."""

        new_str = []
        for c in str(self):
            new_str.append('1' if str(c) == '0' else '0')

        new_str = ''.join(new_str)
        return bincast(new_str, self.obj_type)

    def __int__(self):
        return self.val

    @binlab_deco
    def __neg__(self):
        return bincast(val= - int(self), new_type=self.obj_type,
                       bits=self.bits)

    @binlab_deco
    def __pos__(self):
        return bincast(val=int(self), new_type=self.obj_type, bits=self.bits)

    @binlab_deco
    def __abs__(self):
        return bincast(val=abs(int(self)), new_type=self.obj_type,
                       bits=self.bits)

    @binlab_deco
    def __invert__(self):
        new_rep = ''.join(['0' if x == '1' else '1' for x in str(self)])
        return bincast(val=new_rep, new_type=self.obj_type, bits=self.bits)

    @binlab_deco
    def __add__(self, other):
        # The int branch is used in a situation where I use (self + 1) to
        # find the negative representation of some numbers. It's nice to be
        # able to increment easily. I don't think that an int needs be
        # supported in any other operation, except maybe __sub__?
        if type(other) == int:
            op_b = bincast(val=other, new_type=self.obj_type)
        else:
            op_b = bincast(val=other, new_type=self.obj_type,
                           bits=self.bits)
        retval = bincast(val=int(self) + int(op_b),
                            new_type=self.obj_type,
                            bits=self.bits)
        return retval

    @binlab_deco
    def __sub__(self, other):
        op_b = bincast(val=other, new_type=self.obj_type, bits=self.bits)
        retval = bincast(val=int(self) - int(op_b),
                            new_type=self.obj_type,
                            bits=self.bits)
        return retval

    @binlab_deco
    def __mul__(self, other):
        op_b = bincast(val=other, new_type=self.obj_type, bits=self.bits)
        # Omitting the bits param and using a str for val so that auto
        # bits sizing will take place.
        retval = bincast(val=bin(int(self) * int(op_b)),
                            new_type=self.obj_type)
        return retval

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    @binlab_deco
    def __and__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == '1' and str(other)[i] == '1':
                new_str.append('1')
            else:
                new_str.append('0')

        new_str = ''.join(new_str)
        return bincast(new_str, self.obj_type)

    @binlab_deco
    def __xor__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == str(other)[i]:
                new_str.append('0')
            else:
                new_str.append('1')

        new_str = ''.join(new_str)
        return bincast(new_str, self.obj_type)

    @binlab_deco
    def __or__(self, other):
        new_str = []
        for i in range(len(str(self))):
            if str(self)[i] == '1' or str(other)[i] == '1':
                new_str.append('1')
            else:
                new_str.append('0')

        new_str = ''.join(new_str)
        return bincast(new_str, self.obj_type)

    @binlab_deco
    def xnor(self, other):
        return ~ (self ^ other)


class ComplimentBinary(BaseBinary):
    def __init__(self, val=0, bits=BITSDEFAULT):
        BaseBinary.__init__(self, val=val, bits=bits)
        self.obj_type = 'ComplimentBinary'

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
        bit_len = len(str(self))
        if bits > bit_len:
            self._extend()
        elif bits < bit_len:
            self._truncate()

    @bits.deleter
    def bits(self):
        del self._bits

    def _truncate(self):
        """Should be called ONLY from bits.setter. This takes the rightmost
        bits and creates a new object using these. It then sets the self.val
        to this new value."""

        BaseBinary._truncate(self)
        self.val = int(bincast(val=str(self)[-self.bits:],
                               new_type=self.obj_type))

    def _extend(self):
        """This might not be needed. While the typical approach is to sign
        extend a value, I'm keeping track of everything with a base integer,
        so finding the binary representation in a more permissive base doesn't
        modify the integer at all."""
        BaseBinary._extend(self)

    def __str__(self):
        if self.sign == '0':
            rep = bin(self.val).lstrip('0b')
        else:
            rep = bin(self.val).lstrip('-0b')
            rep = bincast(val=rep, new_type=self.obj_type)
            rep = rep.invert()
            rep = rep + 1

        return "{rep:{self.sign}>{self.bits}}".format(rep=rep, self=self)


class SignedBinary(BaseBinary):
    def __init__(self, val=0, bits=BITSDEFAULT):
        BaseBinary.__init__(self, val=val, bits=bits)
        self.obj_type = "SignedBinary"

        if isinstance(val, int):
            self.val = val
        elif isinstance(val, str):
            # The default int() converter won't pick up on the fact that a
            # value that starts with '1' is negative.
            if len(val) == bits and val[0] == '1':
                self.val = - int(val, 2)
            else:
                self.val = int(val, 2)
        else:
            raise BinLabError()

        self.bits = bits

    @property
    def obj_type(self):
        return self._obj_type

    @obj_type.setter
    def obj_type(self, new_val):
        self._obj_type = new_val

    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, bits):
        self._bits = bits
        bit_len = len(str(self))
        if bits > bit_len:
            self._extend()
        elif bits < bit_len:
            self._truncate()

    @bits.deleter
    def bits(self):
        del self._bits

    def _truncate(self):
        BaseBinary._truncate(self)
        if self.val >= 0:
            new_str_val = self.sign + str(self)[-self.bits + 1:]
        else:
            new_str_val = self.sign + (~ self)[-self.bits + 1:]

        self.val = int(bincast(val=new_str_val, new_type=self.obj_type,
                               bits=self.bits))

    def _extend(self):
        BaseBinary._extend(self)

    def __str__(self):
        if self.sign == '0':
            rep = bin(self.val).lstrip('0b')[-self.bits + 1:]
        else:
            rep = bin(self.val).lstrip('-0b')[-self.bits + 1:]

        return "{self.sign}{rep:0>{bits}}".format(rep=rep, self=self,
                                                  bits=self.bits - 1)


class InverseBinary(BaseBinary):
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

    pass


if __name__ == '__main__':
    main()
