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

    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"Student(first = {self.first_name}, last = {self.last_name}, id = {self.id})"


student_1 = Student("Joe", "Paris", 37)  # Python calls __init__ here
# print(student_1)  # Python calls __str__ here
# print(repr(student_1))  # ???
# print(hex(id(student_1)))

student_2 = Student("Sarah", "Jeller", 42)

print(student_1 == student_2)
