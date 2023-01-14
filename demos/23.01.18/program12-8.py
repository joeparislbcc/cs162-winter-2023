# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
    def __add__(self, param):
        """ Add two Rationals. Allows int as a parameter"""
        print('in add')
        if type(param) == int:  # convert ints to Rationals
            param = Rational(param)
        if type(param) == Rational:
            # find a common denominator (lcm)
            the_lcm = lcm(self.denom, param.denom)
            # multiply each by the lcm, then add
            numerator_sum = (the_lcm * self.numer/self.denom) + \
                (the_lcm * param.numer/param.denom)
            return Rational(int(numerator_sum),the_lcm)
        else:
            print('wrong type')  # problem: some type we cannot handle
            raise(TypeError)
