#!/usr/bin/env python3
"""Insertion sort."""
# pylint: disable


def insertion_sort(data):
    """Insertion sort.

    Insertion sort iterates, consuming one input element each repetition, and
    grows a sorted output list. At each iteration, insertion sort removes one
    element from the input data, finds the location it belongs within the sorted
    list, and inserts it there. It repeats until no input elements remain.

    Sorting is typically done in-place, by iterating up the array, growing the
    sorted list behind it. At each array-position, it checks the value there
    against the largest value in the sorted list (which happens to be next to
    it, in the previous array-position checked). If larger, it leaves the
    element in place and moves to the next. If smaller, it finds the correct
    position within the sorted list, shifts all the larger values up to make a
    space, and inserts into that correct position.

    The resulting array after k iterations has the property where the first
    k + 1 entries are sorted ("+1" because the first entry is skipped). In each
    iteration the first remaining entry of the input is removed, and inserted
    into the result at the correct position, thus extending the result:

     sorted
     partial                 unsorted
     result                  data
    -------------------------------------
    |   <=x   |   > x   | x |    ...    |
    -------------------------------------

    becomes

     sorted
     partial                 unsorted
     result                  data
    -------------------------------------
    |   <=x   | x |   > x   |    ...    |
    -------------------------------------

    with each element greater than x copied to the right as it is compared
    against x.

    Args:
        data: The data to be sorted.

    Returns:
        The data in sorted order.
    """
    # Loop from the second element of the array until the last element
    for i in range(1, len(data)):
        # This is the element we want to position in its correct place
        key_item = data[i]

        # Initialize the variable that will be used to find the correct position
        # of `key_item`
        j = i - 1

        # Run through the list of items (the left portion of the array) and find
        # the correct position of `key_item`; do this only if `key_item` is
        # smaller than its adjacent values
        while j >= 0 and data[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            data[j + 1] = data[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        data[j + 1] = key_item

    return data


if __name__ == "__main__":
    nums = [8, 2, 6, 4, 5]

    sorted_nums = insertion_sort(nums)

    print(sorted_nums)
