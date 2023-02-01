#!/usr/bin/env python3
def special_sum(a: int, b: int) -> int:
    """Sum two ints.

    Sum two integers converting the arguments if necessary. Return 0 if
    conversion fails.

        Args:
        a (int): The first addend.
        b (int): The second addend.

    Returns:
        int: The sum of a and b.
    """
    if isinstance(a, int) and isinstance(b, int):
        result = a + b
    else:
        try:
            result = int(a) + int(b)
        except ValueError:
            result = 0
    return result
