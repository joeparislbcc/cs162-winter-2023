#!/usr/bin/env python3

from collections import deque

stack: deque[str] = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
