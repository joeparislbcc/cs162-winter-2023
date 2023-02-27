#!/usr/bin/env python3

# pylint: disable=no-else-return


def factorial(number: int) -> int:
    if number == 1:  # base case
        return 1
    else:  # recursive case
        return number * factorial(number - 1)


print(factorial(4))
