#!/usr/bin/python3
"""
This module contains a class
with the attribure size validating their entrys
"""


class Square:
    """This is a square class"""
    def __init__(self, size=0):
        """
        Takes in size and validates it is a number and >= 0
        Args:
        size (int): size of the square, must be int
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
