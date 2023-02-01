#!/usr/bin/env python3
"""Simple composition demo."""


class Person:
    """Model a person."""

    def __init__(self, name: str, street: str, city: str, state: str, zip_code: str) -> None:
        self.name = name
        self.address = Address(street, city, state, zip_code)

    def __str__(self) -> str:
        return f"{self.name} who lives at:\n{self.address}"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, \
            street={self.address.street}, \
            city={self.address.city}, \
            state={self.address.state}, \
            zip_code={self.address.zip_code})"


class Student(Person):
    """Model a student.

    A Student is-a Person.
    """

    def __init__(
        self, name: str, major: str, street: str, city: str, state: str, zip_code: str
    ) -> None:
        super().__init__(name, street, city, state, zip_code)
        self.major = major

    def __str__(self) -> str:
        return f"{self.name} is a(n) {self.major} major who lives at:\n{self.address}"

    def __repr__(self) -> str:
        return f"Student(name={self.name}, \
            major={self.major}\
            street={self.address.street}, \
            city={self.address.city}, \
            state={self.address.state}, \
            zip_code={self.address.zip_code})"


class Address:
    """A US address."""

    def __init__(self, street: str, city: str, state: str, zip_code: str) -> None:
        """Initialize the address."""
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code

    def __str__(self) -> str:
        return f"{self.street}\n{self.city}, {self.state} {self.zip_code}"


#%%
izzy = Person("Izzy", "123 Main St NE", "Salem", "OR", "97304")
joe = Student("Joe", "Computer Science", "6500 SW Pacific Blvd", "Albany", "OR", "97321")

# %%
