#!/usr/bin/env python3
"""Example of a class with an attribute and a method.

Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
"""


class Student:
    """Simple Student class."""

    def __init__(self, first: str = "", last: str = "", id: int = 0) -> None:
        """Initialize a Student.

        Args:
            first (str, optional): Student first name. Defaults to "".
            last (str, optional): Student last name. Defaults to "".
            id (int, optional): Student ID. Defaults to 0.
        """
        self.first_name = first
        self.last_name = last
        self.id = id

    def update(self, first: str = "", last: str = "", id: int = 0) -> None:
        if first:
            self.first_name = first
        if last:
            self.last_name = last
        if id:
            self.id = id

    def __str__(self):
        """Return a string representation of the Student object."""
        return f"{self.first_name} {self.last_name}, ID:{self.id}"


s1 = Student("Joe", "Paris", 37)
s1.update(first="Joseph")
# NOTE: we are able to modify the data from outside the class
s1.first_name = "Fred"

print(s1)
