#!/usr/bin/env python3
"""A simple student class.

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

    def __str__(self) -> str:
        """String representation, e.g. for printing.

        Returns:
            str: A string representation of the object.
        """
        return f"{self.first_name} {self.last_name}, {self.id}"
