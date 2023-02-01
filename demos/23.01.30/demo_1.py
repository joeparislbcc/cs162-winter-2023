#!/usr/bin/env python3
"""Simple class inheritance demo."""

#%%
class Person:
    """Model a person."""

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"{self._name}"

    def __repr__(self) -> str:
        return f"Person(name={self._name})"


#%%
class Student(Person):
    """Model a student.

    A Student is-a Person.
    """

    def __init__(self, name: str, major: str) -> None:
        super().__init__(name)
        self._major = major

    def __str__(self) -> str:
        return f"{self._name} is a(n) {self._major} major."

    def __repr__(self) -> str:
        return f"Student(name={self._name}, major={self._major})"


#%%
joe = Student("Joe", "Computer Science")
sarah = Student("Sarah", "Psychology")

print(joe)
print(sarah)

# %%
