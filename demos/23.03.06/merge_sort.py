#!/usr/bin/env python3
"""Merge sort."""
# pylint: disable


def merge(left, right):
    """Merge the two parts of the data together."""

    # If the first half is empty, then nothing needs to be merged, and you can
    # return the second half as the result
    if len(left) == 0:
        return right

    # If the second half is empty, then nothing needs to be merged, and you can
    # return the first half as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Go through both lists until all the elements make it into the resultant
    # list
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the resultant list, so
        # you need to decide whether to get the next element from the first or
        # the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can add the remaining
        # elements from the other array to the result and break
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(data):
    """Merge sort.

    Merge sort is an efficient, general-purpose, and comparison-based sorting
    algorithm. Most implementations produce a stable sort, which means that the
    order of equal elements is the same in the input and output. Merge sort is a
    divide-and-conquer algorithm that was invented by John von Neumann in 1945.
    A detailed description and analysis of bottom-up merge sort appeared in a
    report by Goldstine and von Neumann as early as 1948.

    Merge sort recursively splits the list into sublists until sublist size is
    1, then merges those sublists to produce a sorted list.

    Args:
        data: The data to be sorted.

    Returns:
        The data in sorted order.
    """
    if len(data) < 2:
        return data

    midpoint = len(data) // 2

    # Sort the data by recursively
    return merge(left=merge_sort(data[:midpoint]), right=merge_sort(data[midpoint:]))


if __name__ == "__main__":
    nums = [8, 2, 6, 4, 5]

    sorted_nums = merge_sort(nums)

    print(sorted_nums)
