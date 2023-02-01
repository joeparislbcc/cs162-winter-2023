#!/usr/bin/env python3


def plus(first, second):
    return first + second


plus(2, 3)
int(2).__add__(3)

plus("Hello ", "world!")
str("Hello ").__add__("world!")

len("Joe")  # 3
len(["Joe"])  # 1


class Person:
    """Model a person."""

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"{self._name}"

    @classmethod
    def display_person(cls, person_to_display):
        return str(person_to_display)


class Student(Person):
    """Model a student.

    A Student is-a Person.
    """

    def __init__(self, name: str, major: str) -> None:
        super().__init__(name)
        self.major = major

    def __str__(self) -> str:
        return f"{self._name} is a(n) {self.major} major."


joe = Student("Joe", "Computer Science")
print(Person.display_person(joe))
