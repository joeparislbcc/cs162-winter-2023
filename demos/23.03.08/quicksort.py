#!/usr/bin/env python3
"""Quicksort."""
# pylint: disable

import random


def quicksort(data):
    # If the input array contains fewer than two elements, return it
    if len(data) < 2:
        return data

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = data[random.randint(0, len(data) - 1)]

    for item in data:
        # Elements that are smaller than the `pivot` go to the `low` list.
        # Elements that are larger than `pivot` go to the `high` list. Elements
        # that are equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list with the `same` list and
    # the sorted `high` list
    return quicksort(low) + same + quicksort(high)


if __name__ == "__main__":
    nums = [8, 2, 6, 4, 5]

    sorted_nums = quicksort(nums)

    print(sorted_nums)
