#!/usr/bin/env python3

import turtle


def sierpinski(length: float, depth: int) -> None:
    if depth > 1:  # base case
        turtle.dot()
    if depth == 0:  # base case
        turtle.stamp()
    else:
        turtle.forward(length)
        sierpinski(length / 2, depth - 1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinski(length / 2, depth - 1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinski(length / 2, depth - 1)
        turtle.backward(length)
        turtle.left(120)


if __name__ == "__main__":
    LENGTH = 200
    DEPTH = 7

    turtle.setup(width=900, height=900)
    turtle.colormode(255)
    turtle.bgcolor(216, 216, 216)
    turtle.pencolor(33, 148, 240)

    turtle.speed(0)
    if DEPTH > 5:
        turtle.tracer(10)
    sierpinski(LENGTH, DEPTH)

    turtle.hideturtle()
    turtle.exitonclick()
