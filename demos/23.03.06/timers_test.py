#!/usr/bin/env python3
"""Test utilities for timing Python code execution."""
import random
import time

from timers import Timer


def get_random_words(filename: str, count: int) -> list[str]:
    """Get count random words from the source file.

    Args:
        word_list (str): File containing newline separated words.
        count (int): The number of words to be read.

    Returns:
        list[str]: List of words randomly selected from the provided file.
    """
    with open(filename, mode="r", encoding="utf-8") as in_file:
        word_list = random.choices(in_file.read().splitlines(), k=count)

    return word_list


def loop():
    """Demo timing only what is important in a loop.

    Time the execution of the sort ignoring the time required to get 1000 random
    words from the input file each time the loop is executed.
    """

    timer = Timer("loop")
    for _ in range(10):
        words = get_random_words(filename="english_words.txt", count=1000)
        timer.start()
        words.sort()
        timer.stop()

    print(f"Total elapsed time: {Timer.timers['loop']:0.4f} seconds")


def loop2():
    """Demo using multiple timers."""
    loop_timer = Timer("loop_timer")
    sort_timer = Timer("sort_timer")

    loop_timer.start()
    for _ in range(10):
        words = get_random_words(filename="english_words.txt", count=1000)
        sort_timer.start()
        words.sort()
        sort_timer.stop()
    loop_timer.stop()

    print(f"Total time spent in the loop: {Timer.timers['loop_timer']:0.4f} seconds")
    print(f"Total time spent sorting: {Timer.timers['sort_timer']:0.4f} seconds")


def accumulate():
    """Demo getting instance and accumulated elapsed time."""
    timer = Timer("accumulate")
    timer.start()
    time.sleep(1.2)
    elapsed_time = timer.stop()
    print(f"elapsed time = {elapsed_time:0.4f} seconds")

    timer.start()
    time.sleep(0.5)
    elapsed_time = timer.stop()
    print(f"elapsed time = {elapsed_time:0.4f} seconds")

    print(f"total elapsed time = {Timer.timers['accumulate']:0.4f} seconds")


if __name__ == "__main__":
    loop()
    print()

    loop2()
    print()

    accumulate()
    print()
