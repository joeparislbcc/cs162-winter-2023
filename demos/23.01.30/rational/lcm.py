#!/usr/bin/env python3
from gcd import gcd


def lcm(a: int, b: int):
    """Calculate the least common multiple of two positive integers."""
    return (a * b) // gcd(a, b)


def main():
    print(lcm(5, 20))
    print(lcm(12, 36))
    print(lcm(1245, 3196))  # ??
    print(lcm(1245, 3195))  # ??


if __name__ == "__main__":
    main()
