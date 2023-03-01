#!/usr/bin/env python3

import turtle


def koch(size: float, order: int) -> None:
    if order > 0:
        for angle in (60, -120, 60, 0):
            koch(size / 3, order - 1)
            turtle.left(angle)
    else:
        turtle.forward(size)


if __name__ == "__main__":
    SIZE = 500
    ORDER = 5

    turtle.setup(width=800, height=600)
    turtle.color("white", "white")
    turtle.bgcolor("sky blue")

    turtle.penup()
    turtle.backward(SIZE / 1.732)
    turtle.left(30)
    turtle.pendown()

    turtle.speed(0)
    if ORDER >= 5:
        turtle.tracer(5)
    turtle.hideturtle()

    turtle.begin_fill()
    for i in range(3):
        koch(SIZE, ORDER)
        turtle.right(120)
    turtle.end_fill()

    turtle.exitonclick()
