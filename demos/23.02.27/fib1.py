#!/usr/bin/env python3

# pylint: disable=no-else-return,consider-using-in


def fibonacci(n: int) -> int:
    """Compute the nth number in the Fibonacci sequence."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    number = fibonacci(5)
    print(number)
