#!/usr/bin/env python3


def factorial(number):
    product = 1

    for i in range(1, number + 1):
        product = product * i

    return product


print(f"{factorial(52):,}")
