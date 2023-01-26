#!/usr/bin/env python3
"""Example of a class with an attribute and a method.

Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
"""


from datetime import datetime


class Student:
    """Simple Student class."""

    def __init__(self, first: str = "", last: str = "", id: int = 0, dob: str = "") -> None:
        """Initialize a Student.

        Args:
            first (str, optional): Student first name. Defaults to "".
            last (str, optional): Student last name. Defaults to "".
            id (int, optional): Student ID. Defaults to 0.
        """
        self.__first_name = first
        self.__last_name = last
        self.__id = id
        self.__dob = datetime.strptime(dob, "%m/%d/%Y")

    def __str__(self) -> str:
        """Return a string representation of the Student object."""
        return f"{self.__first_name} {self.__last_name}, ID: {self.__id}, DOB: {self.__dob}"

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        # sanity checks
        if not isinstance(value, str):
            return
        if not value:
            return

        self.__first_name = str.capitalize(value)

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        # sanity checks
        if not isinstance(value, str):
            return
        if not value:
            return

        self.__last_name = str.capitalize(value)

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        # sanity checks
        if not isinstance(value, int):
            return
        if not value >= 0:
            return
        # test that new id is not already used...

        self.__id = value

    @property
    def age(self) -> str:
        delta = datetime.today() - self.__dob
        return str(delta.days // 365)


def main():
    s1 = Student("Joe", "Paris", 37, "2/5/1974")
    print(s1)
    print(s1.age)


if __name__ == "__main__":
    main()
