#!/usr/bin/python3
"""
This module will print the str representation of a square
using char "#", validates if size is int or raises error
"""


def print_square(size):
    """
    Prints str representation of a square
    Args:
    size (int): size of the square to print
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()

