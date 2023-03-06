#!/usr/bin/env python3
"""Bubble sort."""
# pylint: disable


def bubble_sort(data):
    """Bubble sort.

    The bubble sort algorithm works by stepping through the input data element
    by element, comparing the current element with the one after it, and
    swapping their values if needed. These passes through the list are repeated
    until no swaps had to be performed during a pass, meaning that the list has
    become fully sorted.

    Args:
        data: The data to be sorted.

    Returns:
        The data in sorted order.
    """
    n = len(data)

    for i in range(n):
        is_sorted = True  # optimistic optimization
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # swap

                is_sorted = False  # made a swap, go again

        if is_sorted:  # made no swaps, data is sorted
            break

    return data


if __name__ == "__main__":
    nums = [8, 2, 6, 4, 5]

    sorted_nums = bubble_sort(nums)

    print(sorted_nums)
