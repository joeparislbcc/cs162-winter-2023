#!/usr/bin/env python3
"""Demo using a custom error from another file.

MyCustomError was defined as an inner class inside foo.Foo.
"""
from foo import Foo


def bat():
    """Raises an exception.

    What a life.
    """
    raise Foo.MyCustomError


if __name__ == "__main__":
    bat()  # make it go
