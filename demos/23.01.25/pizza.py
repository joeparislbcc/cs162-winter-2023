#!/usr/bin/env python3


class Pizza:
    def __init__(self, ingredients: list[str]):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes", "basil"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])

    @classmethod
    def cheese(cls):
        return cls(["mozzarella"])
