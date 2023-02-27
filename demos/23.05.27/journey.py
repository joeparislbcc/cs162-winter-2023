#!/usr/bin/env python3

# pylint: disable=no-else-return


def take_step(n: int) -> str:
    """The journey of 1000 miles begins with a single step."""
    if n == 1:  # base case
        return "First step"
    else:  # recursive case
        this_step = f"step {n}"
        previous_steps = take_step(n - 1)
        return f"{previous_steps}\n{this_step}"


if __name__ == "__main__":
    print(take_step(5))
