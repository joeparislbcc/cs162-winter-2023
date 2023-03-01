#!/usr/bin/env python3
"""Compute numbers in the Fibonacci sequence.

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
"""

# pylint: disable=no-else-return,consider-using-in


def recursive_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci_1(n: int) -> int:
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a


def iterative_fibonacci_2(n: int) -> int:
    fibonacci_numbers = [0, 1, 1]
    for _ in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    return fibonacci_numbers[n]


if __name__ == "__main__":
    r = recursive_fibonacci(5)
    print(r)

    i1 = iterative_fibonacci_1(5)
    print(i1)

    i2 = iterative_fibonacci_2(5)
    print(i2)
