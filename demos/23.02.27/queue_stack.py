#!/usr/bin/env python3

from queue import LifoQueue

stack: LifoQueue[str] = LifoQueue()

stack.put("a")
stack.put("b")
stack.put("c")

print(stack)

print(stack.get())
print(stack.get())
print(stack.get())
# print(stack.get())
