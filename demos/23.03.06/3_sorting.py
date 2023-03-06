#!/usr/bin/env python3

import random
from timeit import repeat

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

FILENAME = "english_words.txt"
COUNT = 10_000


def run_sorting_algorithm(algorithm: str, data: list, r: int = 3, n: int = 5) -> None:
    """Run the specified sorting algorithm on the supplied list of inputs.

    Args:
        algorithm (str): The sorting algorithm to run.
        array (list): The data to be sorted.
        r (int): The number of times to call timeit.timeit.
        n (int): The number of times to timeit.timeit will run the algorithm.
    """
    # Set up the context and prepare the call to the specified algorithm using
    # the supplied list; only import the algorithm function if it's not the
    # built-in `sorted()`
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({data})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=r, number=n)
    print(times)

    print(f"Algorithm: {algorithm} - Minimum execution time: {min(times):0.5f} seconds")


if __name__ == "__main__":
    # numbers = [random.randint(0, 1000) for i in range(COUNT)]
    with open(FILENAME, mode="r", encoding="utf-8") as in_file:
        words = random.choices(in_file.read().splitlines(), k=COUNT)

    # run_sorting_algorithm(algorithm="sorted", data=words)
    # run_sorting_algorithm(algorithm="bubble_sort", data=words)
    # run_sorting_algorithm(algorithm="insertion_sort", data=words)
    run_sorting_algorithm(algorithm="merge_sort", data=words)
