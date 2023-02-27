#!/usr/bin/env python3
"""A simple stack implementation."""

from collections import deque
from typing import Any


class Stack:
    """A stack is a LIFO data structure that offers constant time insertion and
    removal of data elements."""

    def __init__(self) -> None:
        """Create a stack.

        Args:
            max_length (int | None): If provided sets the maximum number of
            elements the stack can hold.
        """
        self.__data: deque[Any] = deque()

    def __str__(self) -> str:
        return f"{list(self.__data)}"

    def __repr__(self) -> str:
        raise NotImplementedError()

    def is_empty(self) -> bool:
        """Returns whether or not the stack is empty."""
        return len(self.__data) == 0

    def size(self) -> int:
        """Returns the number of elements in the stack."""
        return len(self.__data)

    def peek(self) -> Any:
        """Returns but does not remove the element at the top of the stack."""
        return self.__data[-1]

    def pop(self) -> Any:
        """Removes and returns the element at the top of the stack."""
        return self.__data.pop()

    def push(self, element: Any) -> None:
        """Insert element at the top of the stack."""
        self.__data.append(element)


if __name__ == "__main__":
    stack = Stack()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())
