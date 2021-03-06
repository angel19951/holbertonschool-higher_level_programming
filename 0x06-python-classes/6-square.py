#!/usr/bin/python3
"""
This module contains a class
with the attribure size validating their entrys
"""


class Square:
    """This is a sqaure class."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Takes in size variable
        Attributes:
        size (int): size of the square, must be int
        position (tuple): position of the square
        """
        self.size = size
        self.position = position

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
        if self.__size is 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for row in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or \
           len(value) is not 2 or \
           any(map(lambda x: type(x) is not int or x < 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
