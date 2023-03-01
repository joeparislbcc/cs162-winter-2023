#!/usr/bin/env python3

import turtle


def branch(length: float, level: int) -> None:
    # base case
    if level <= 0:
        return

    # recursive case
    turtle.forward(length)
    turtle.left(45)
    branch(0.6 * length, level - 1)
    turtle.right(90)
    branch(0.6 * length, level - 1)
    turtle.left(45)
    turtle.backward(length)


if __name__ == "__main__":
    turtle.setup(width=800, height=600)
    turtle.left(90)

    branch(100, 5)

    turtle.hideturtle()
    turtle.exitonclick()
