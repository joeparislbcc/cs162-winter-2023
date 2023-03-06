#!/usr/bin/env python3
import random


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


if __name__ == "__main__":
    words = get_random_words("english_words.txt", 10)

    print(words)

    print(sorted(words))  # returns a new, sorted Iterable
    print(words)

    print(words.sort())  # returns None - sorts in place
    print(words)
