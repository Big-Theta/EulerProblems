from __future__ import print_function


class BaseBinary(object):
    def __init__(self, val=0, bits=8, encoding="compliment"):
        '''
        @param val (int or str)
            If str, use base 10.
        @param bits (int)
            The number of bits to use in the representation.
        @param encoding (str)
            Use one of ['compliment', 'signed', 'inverse']
        '''
        self.val = int(val)
        self.encoding = encoding
        self.set_bits(bits)

        # Not yet used
        self.endian = 'little'

    def set_bits(self, bits):
        '''The alternative to this is to import abc and then set __metaclass__
        to abcmeta, or something like that.'''

        raise NotImplementedError()

    def __str__(self):
        '''
        TODO This should not have a read definition here, but instead
        should be described in all inheriting classes.
        '''

        str_val = []
        str_val += ["val (base 10): {self.val}"]
        str_val += ["encoding: {self.encoding}"]
        str_val += ["bits: {self.bits}"]
        str_val = '\n'.join(str_val)
        return str_val.format(self=self)


class ComplimentBinary(BaseBinary):
    def __init__(self, *args):
        BaseBinary.__init__(self, *args)

    def sign(self):
        return '0' if self.val >= 0 else '1'

    def set_bits(self, bits):
        self.bits = bits

    def __str__(self):
        return "{rep:{sign}>{self.bits}}".format(rep=bin(self.val).lstrip('0b'),
                                                 self=self, sign=self.sign())


if __name__ == '__main__':
    x = ComplimentBinary(10)
    x.set_bits(2)
    print(x)
