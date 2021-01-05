#!/usr/bin/python3
"""
This module contains a class
with the attribure size validating their entrys
"""


class Square:
    """This is a sqaure class."""

    def __init__(self, size=0):
        """
        Takes in size variable
        Attributes:
        size (int): size of the square, must be int
        """
        self.__size = size

    def area(self):
        """
        Return the multiplication of size by itself
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Defines the value of size
        and validates if is a num and >= 0
        Attributes:
        value (int): size of the square, must be int
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints to stdout a are square of the given size
        """
        if self.__size == 0:
            print()
        else:
            for row in range(0, self.__size):
                for col in range(0, self.__size):
                    print("#", end="")
                print()
