#!/usr/bin/env python3
import string

test_string = "Race car # 42."


translation_table = str.maketrans(
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits + string.punctuation + string.whitespace,
)

print(test_string.translate(translation_table))
