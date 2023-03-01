#!/usr/bin/env python3

"""Using the head-tail technique, create a recursive concat() function that when
passed a list of strings returns the strings concatenated together into a single
string. For example, concat(['Hello', 'World']) should return HelloWorld. Save
your program in a file named lastname_firstname_concat.py"""


def concat(lst: list[str]) -> str:
    if len(lst) == 0:
        return ""

    head = lst[0]
    tail = lst[1:]
    return head + str(concat(tail))


if __name__ == "__main__":
    print(concat(["Hello", "World"]))

    menu = [
        "Egg and bacon",
        "Egg, sausage and bacon",
        "Egg and spam",
        "Egg, bacon and spam",
        "Egg, bacon, sausage and spam",
        "Spam, bacon, sausage and spam",
        "Spam, egg, spam, spam, bacon and spam",
        "Spam, spam, spam, egg and spam",
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, spam and spam",
        "Lobster thermidor aux crevettes with a mornay sauce garnished with truffle paté, brandy and a fried egg on top and spam",
    ]

    print(concat(menu))

    guard = [
        "I",
        " don't",
        " want",
        " to",
        " talk",
        " to",
        " you",
        " anymore",
        " you",
        " empty-headed",
        " animal",
        " food",
        " trough",
        " whopper.",
    ]
    print(concat(guard))
