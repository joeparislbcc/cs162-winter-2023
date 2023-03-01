#!/usr/bin/env python3

# pylint: disable=no-else-return,missing-function-docstring


def sum_list(lst: list[int]) -> int:
    if len(lst) == 0:  # base case
        return 0
    else:  # recursive case
        head = lst[0]
        tail = lst[1:]
        return head + sum_list(tail)


if __name__ == "__main__":
    nums = []
    print(f"The sum of {nums} is {sum_list(nums)}")

    nums = [1, 2, 3, 4, 5]
    print(f"The sum of {nums} is {sum_list(nums)}")

    nums = [5, 2, 4, 8]
    print(f"The sum of {nums} is {sum_list(nums)}")

    nums = [1, 10, 100, 1000]
    print(f"The sum of {nums} is {sum_list(nums)}")
