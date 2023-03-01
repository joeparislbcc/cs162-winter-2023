#!/usr/bin/env python3

# pylint: disable=no-else-return,missing-function-docstring


def reverse1(s: str):
    if s == "":
        return s
    else:
        head = s[0]
        tail = s[1:]
        return reverse1(tail) + head


def reverse2(s: str):
    if len(s) <= 1:
        return s
    else:
        head = s[0]
        tail = s[1:]
        return reverse2(tail) + head


def reverse3(s: str, idx: int):
    if idx < 0:
        # return False
        return ""
    elif idx == 0:
        return s[0]
    else:
        return s[idx] + reverse3(s, idx - 1)


def reverse4(s: str) -> str:
    if len(s) in (0, 1):
        return s

    head = s[0]
    tail = s[1:]
    return reverse4(tail) + head


if __name__ == "__main__":
    # assert reverse("") == ""
    # assert reverse("X") == "X"
    # assert reverse("abcdef") == "fedcba"
    # assert reverse("Joe") == "eoJ"

    # print(reverse(""))
    # print(reverse("X"))
    # print(reverse("abcdef"))
    # print(reverse("Joe"))

    print(reverse3("", len("") - 1))
    print(reverse3("X", len("X") - 1))
    print(reverse3("abcdef", len("abcdef") - 1))
    print(reverse3("Joe", len("Joe") - 1))
