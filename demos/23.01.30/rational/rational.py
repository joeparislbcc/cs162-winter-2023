#!/usr/bin/env python3
from __future__ import annotations

from gcd import gcd
from lcm import lcm


class Rational:
    """Rational with numerator and denominator."""

    def __init__(self, numerator: int, denominator: int = 1):
        """Initialize Rational object.

        Args:
            numerator (_type_): The numerator.
            denominator (int, optional): The denominator. Defaults to 1.
        """
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """String representation for printing."""
        return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self):
        """String representation for debugging."""
        return f"Rational(numerator={self.numerator}, denominator={self.denominator})"

    def __add__(self, other: Rational | int) -> Rational:
        """Add two Rationals. Allows int as a parameter."""
        if isinstance(other, int):
            other = Rational(other)

        if isinstance(other, Rational):
            # find a common denominator (lcm)
            the_lcm = lcm(self.denominator, other.denominator)

            # multiply each by the lcm, then add
            numerator_sum = (the_lcm * self.numerator / self.denominator) + (
                the_lcm * other.numerator / other.denominator
            )

            return Rational(int(numerator_sum), the_lcm)

        raise TypeError

    def __radd__(self, other: Rational):
        """Add two Rationals (reversed)."""
        # mapping is reversed: if "1 + x", x maps to self, and 1 maps to other
        # mapping is already reversed so self will be Rational; call __add__
        return self.__add__(other)

    def __sub__(self, other: Rational | int) -> Rational:
        """Subtract two Rationals."""
        # subtraction is the same but with '-' instead of '+'
        if isinstance(other, int):
            other = Rational(other)

        if isinstance(other, Rational):
            # find a common denominator (lcm)
            the_lcm = lcm(self.denominator, other.denominator)

            # multiply each by the lcm, then add
            numerator_sum = (the_lcm * self.numerator / self.denominator) - (
                the_lcm * other.numerator / other.denominator
            )

            return Rational(int(numerator_sum), the_lcm)

        raise TypeError

    def __rsub__(self, other: int) -> Rational:
        """Subtract two Rationals (reversed)."""
        # mapping is reversed: if "1 - x", x maps to self, and 1 maps to other
        # mapping is already reversed so self will be Rational; call __sub__
        return self.__sub__(other)

    def reduce_rational(self) -> Rational:
        """Return the reduced fractional value as a Rational."""
        # find the gcd and then divide numerator and denominator by gcd
        the_gcd = gcd(self.numerator, self.denominator)

        return Rational(self.numerator // the_gcd, self.denominator // the_gcd)

    def __eq__(self, other: Rational) -> bool:
        """Compare two Rationals for equality."""
        # reduce both; then check that numerators and denominators are equal
        reduced_self = self.reduce_rational()
        reduced_param = other.reduce_rational()
        return (
            reduced_self.numerator == reduced_param.numerator
            and reduced_self.denominator == reduced_param.denominator
        )


def main():
    # r1 = Rational(1, 2)
    # r2 = Rational(1, 3)
    # r3 = Rational(3)
    # r4 = r1 + r3
    # r5 = r1 - r3

    # print(r1)
    # print(r2)
    # print(r3)
    # print(r4)
    # print(r5)

    r6 = Rational(3, 1)
    r7 = Rational(6, 2)

    print(r6)
    print(r7)

    print(r6 == r7)

    print(r6 + 1)
    print(1 + r6)


if __name__ == "__main__":
    main()
