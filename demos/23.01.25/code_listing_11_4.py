#!/usr/bin/env python3
"""Example of a class with an attribute and a method.

Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
"""
import math


class Point:
    """A Cartesian point (x,y)."""

    def __init__(self, x=0.0, y=0.0):
        """Initialize a Point.

        Args:
            x (float, optional): The point's x coordinate. Defaults to 0.0.
            y (float, optional): The point's y coordinate. Defaults to 0.0.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.sum(other)

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def distance(self, other):
        """Compute the distance between two Points."""
        delta_x = self.x - other.x  # (x1 - x2)
        delta_y = self.y - other.y  # (y1 - y2)
        # standard distance formula: square differences, sum, and take sqrt
        return math.sqrt(delta_x**2 + delta_y**2)

    def sum(self, other):
        """Vector sum of self and a Point."""
        new_point = Point()
        new_point.x = self.x + other.x  # calculate x value sum from self and pt
        new_point.y = self.y + other.y

        return new_point


def main():
    p1 = Point()
    p2 = Point(3, 5)
    # p2.x = 3
    # p2.y = 5

    print(p1.distance(p2))
    print(p1.sum(p2))

    print(p1 + p2)


if __name__ == "__main__":
    main()
