#!/usr/bin/env python3
"""Demonstrate formatting output."""


def main():
    print("foo\tbar")
    for num in range(1, 101):
        # print numbers 1 through 100 in a column 3 chars wide
        # print(f"{num:3}{num/2:20.2}")
        # print("{:3d}".format(num), "{:20.2f}".format(num / 2))
        print(f"{num}\t{num/2}")


if __name__ == "__main__":
    main()
