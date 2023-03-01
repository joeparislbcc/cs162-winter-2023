#!/usr/bin/env python3
# pylint: disable=no-else-return
"""Using the head-tail technique, create a recursive product() function that is
passed an array of integers and returns the total multiplied product of them.
This code will be almost identical to the sum_list() example we worked on in
class. However, note that the base case of a list with just one integer returns
the integer, and the base case of an empty list returns 1. Save your program in
a file named lastname_firstname_product.py"""


def product(nums: list[int]) -> int:
    if len(nums) == 0:  # base case 1
        return 1
    elif len(nums) == 1:  # base case 2
        return nums[0]
    else:  # recursive case
        head = nums[0]
        tail = nums[1:]
        return head * product(tail)


if __name__ == "__main__":
    product([5, 3])
    assert product([-2, -21]) == 42
    assert product([-2, 21]) == -42
    assert product([2, 21]) == 42
    assert product([3, 14]) == 42
    assert product([6, 7]) == 42
    assert product([7, 6]) == 42
    assert product([14, 3]) == 42
    assert product([21, 2]) == 42
    assert product([1, 37]) == 37
    assert product([37, 1]) == 37  # !!!
