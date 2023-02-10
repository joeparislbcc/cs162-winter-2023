#!/usr/bin/env python3
"""Demoing inner classes."""


class Foo:
    def bar(self):
        """Example class.

        Exists only to raise our custom error."""
        raise Foo.MyCustomError

    class MyCustomError(Exception):
        """Custom exception type.

        Defined as an inner class (that is, a class inside another class) to
        prevent it from accidentally polluting the global namespace.
        """

        pass  # GNDN


def main():
    f = Foo()

    f.bar()


if __name__ == "__main__":
    main()
