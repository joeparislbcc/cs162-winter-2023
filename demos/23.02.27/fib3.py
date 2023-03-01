#!/usr/bin/env python3
"""Compute numbers in the Fibonacci sequence.

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

Use memoization to make the overall algorithm more better.
"""

# pylint: disable=no-else-return,consider-using-in
cache: dict[int, int] = {}


def recursive_fibonacci(n: int) -> int:
    if n in cache:  # value was already computed, return early
        return cache[n]

    if n == 0 or n == 1:  # base case
        cache[n] = n
        return n
    else:  # recursive case
        cache[n] = recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
        return cache[n]


if __name__ == "__main__":
    r = recursive_fibonacci(5)
    print(r)
