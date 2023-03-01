#!/usr/bin/env python3
"""Compute numbers in the Fibonacci sequence.

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
"""

# %%
def fib(n: int) -> int:
    if n in (0, 1):
        return n

    return fib(n - 1) + fib(n - 2)

%timeit -n 1_000_000 fib(8)

# %%
cache: dict[int, int] = {}


def dict_cached_fib(n: int) -> int:
    if n in cache:  # value was already computed, return early
        return cache[n]

    if n == 0 or n == 1:  # base case
        cache[n] = n
        return n
    else:  # recursive case
        cache[n] = dict_cached_fib(n - 1) + dict_cached_fib(n - 2)
        return cache[n]

%timeit -n 1_000_000 dict_cached_fib(8)

# %%
from functools import lru_cache

@lru_cache
def lru_cached_fib(n: int) -> int:
    if n in (0, 1):
        return n

    return lru_cached_fib(n - 1) + lru_cached_fib(n - 2)

%timeit -n 1_000_000 lru_cached_fib(8)

# %%
