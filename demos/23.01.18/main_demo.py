#!/usr/bin/env python3
import sys


def say_hello(name: str = "world") -> None:
    print(f"Hello {name}!")


def foobar():
    say_hello("Joe")


if __name__ == "__main__":
    foobar()

print(f"Inside main_demo.py, main_demo.__name__ = {sys.modules[__name__]}")
print(f"Inside main_demo.py, main_demo.__name__ = {sys.modules['main_demo']}")
