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
        self.__first_name = first
        self.__last_name = last
        self.__id = id

    def __str__(self):
        """Return a string representation of the Student object."""
        return f"{self.__first_name} {self.__last_name}, ID:{self.__id}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        # sanity checks
        if not isinstance(value, str):
            return
        if not value:
            return

        self.__first_name = str.capitalize(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        # sanity checks
        if not isinstance(value, str):
            return
        if not value:
            return

        self.__last_name = str.capitalize(value)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        # sanity checks
        if not isinstance(value, int):
            return
        if not value >= 0:
            return
        # tests that new id is not already used

        self.__id = value


s1 = Student("Joe", "Paris", 37)
print(s1.first_name)
print(s1.last_name)
print(s1.id)

# import code_listing_11_3b as cl3b
