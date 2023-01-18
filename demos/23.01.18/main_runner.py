#!/usr/bin/env python3
import sys

import main_demo as m_demo

print(f"Inside main_runner.py, main_runner.__name__ = {sys.modules[__name__]}")
print(f"Inside main_runner.py, main_demo.__name__ = {sys.modules['main_demo']}")
