#!/usr/bin/python3
"""
This module holds a class name Square
and valiadte the entries
"""


rec = __import__('9-rectangle').Rectangle


class Square(rec):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a square class
        Instances:
        size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Return the area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
