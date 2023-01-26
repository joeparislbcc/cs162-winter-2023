#!/usr/bin/env python3
from datetime import date


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        return cls(name, date.today().year - birth_year)

    @classmethod
    def newborn(cls, name: str):
        return cls(name, 0)

    @staticmethod
    def is_adult(age):
        return age >= 18


def main():
    person1 = Person("Susan", 28)
    print(person1)

    person2 = Person.from_birth_year("Sarah", 1992)
    print(person2)
    print(type(person2))

    baby = Person.newborn("Albert")
    print(baby)
    print(type(baby))

    print(Person.is_adult(person1.age))
    print(Person.is_adult(person2.age))
    print(Person.is_adult(baby.age))


if __name__ == "__main__":
    main()
