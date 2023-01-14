# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
    def __radd__(self,param):
        """ Add two Rationals (reversed)"""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to f
        print("in radd")
        # mapping is already reversed so self will be Rational; call __add__
        return self.__add__(param)
