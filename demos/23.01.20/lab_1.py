#!/usr/bin/env python3
"""Module docstring."""


import csv
import os


def open_file(s):
    """Insert Docstring"""
    pass  # replace this line with your code


def build_dictionary(file: os.PathLike):
    """Insert Docstring"""
    pass  # replace this line with your code


def get_ingredients(D, L):
    """Insert Docstring"""
    pass  # replace this line with your code


def get_useful_and_missing_ingredients(D, foods, pantry):
    """Insert Docstring"""
    pass  # replace this line with your code


def get_list_of_foods(D, L):
    """Insert Docstring"""
    pass  # replace this line with your code


def get_food_by_preference(D, preferences):
    """Insert Docstring"""
    pass  # replace this line with your code


def main():
    print("Indian Foods & Ingredients.\n")
    MENU = """
        A. Input various foods and get the ingredients needed to make them!
        B. Input various ingredients and get all the foods you can make with them!
        C. Input various foods and ingredients and get the useful and missing ingredients!
        D. Input various foods and preferences and get only the foods specified by your preference!
        Q. Quit
        : """

    print("Thanks for playing!")

    with open("indian_food.csv") as in_file:
        text = in_file.read()
        print(text)


if __name__ == "__main__":
    main()
