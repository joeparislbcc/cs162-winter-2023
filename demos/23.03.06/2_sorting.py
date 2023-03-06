#!/usr/bin/env python3
import random
import timeit

# python -m timeit "import random; in_file=open('english_words.txt'); words=random.choices(in_file.read().splitlines(),k=1000); in_file.close(); words.sort()"


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
    SETUP = """\
import random;
in_file=open('english_words.txt');
words=random.choices(in_file.read().splitlines(),k=1000);
in_file.close()"""

    STMT = "words.sort()"

    print(globals())

    print(timeit.timeit(stmt=STMT, setup=SETUP, number=1_000_000, globals=globals()))
