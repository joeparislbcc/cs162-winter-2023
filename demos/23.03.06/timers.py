#!/usr/bin/env python3
"""Utilities for timing Python code execution."""
from __future__ import annotations

import functools
import time
from dataclasses import dataclass, field
from typing import Any, Callable, ClassVar, Hashable


class TimerError(Exception):
    """Custom exception to report errors in the Timer class."""


@dataclass
class Timer:
    """A simple pausable timer that can be used as a class, a context manager,
    or as a decorator.

    1.  As a class:

        t = timer()
        t.start()
        # code to be timed goes here
        t.stop()
        t.elapsed_time  # get the elapsed time

        Alternatively:

        t = timer()
        for _ in range(10):
            # code that should not be timed here
            t.start()
            # code to be timed goes here
            t.stop()
            # code that should not be timed here

    2.  As a context manager:

        with Timer() as timer:
            # code to be timed goes here

        elapsed_time = timer.elapsed_time

    3.  As a decorator (Note - when using Timer as a decorator you must provide a
        name for the timer in order to retrieve its value from Timer.timers):

        @Timer(name=some_timer)
        def func():
            # code to be timed goes here

        latest_tutorial()

        print(Timer.timers["some_timer"])

    Adapted from https://realpython.com/python-timer/
    """

    timers: ClassVar[dict[Any, float]] = {}
    name: Hashable = None
    text: str = "Elapsed time: {:0.4f} seconds"
    logger: Callable | None = None
    _start_time: float | None = field(default=None, init=False, repr=False)

    def __post_init__(self):
        if self.name:
            self.timers.setdefault(self.name, 0)

    def __call__(self, func: Callable, *args: Any, **kwargs: Any) -> Callable:
        """Make Timer callable.

        This is required to use it as a decorator.
        """

        @functools.wraps(func)
        def timer_wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return timer_wrapper

    def __enter__(self) -> Timer:
        """Start a new timer as a context manager."""
        self.start()
        return self

    def __exit__(self, *exec_info) -> None:
        """Stop the context manager timer."""
        self.stop()

    def start(self) -> None:
        """Start a new timer."""
        if self._start_time is not None:
            raise TimerError("Timer is running, use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer and return the elapsed time.

        Raises:
            TimerError: Custom exception type for reporting errors in using the
                Timer class

        Returns:
            float: The elapsed time.
        """
        if self._start_time is None:
            raise TimerError("Timer is not running, use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger is not None:
            self.logger(self.text.format(elapsed_time))

        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time
