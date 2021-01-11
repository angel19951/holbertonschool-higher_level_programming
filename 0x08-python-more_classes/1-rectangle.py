#!/usr/bin/python3
"""
This module contains a class named Rectangle
and attributes width and height.
Validating the entries given.
"""


class Rectangle:
    """This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        Takes attrbutes width and height.
        Attributes:
        width (int): width of the rectangle; must be int
        height (int): height of the rectangle; must be int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns width
        """
        return self.__width
    @width.setter
    def width(self, width_set):
        if type(width_set) is not int:
            raise TypeError("width must be an integer")
        elif width_set < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width_set
    @property
    def height(self):
        """
        Returns height
        """
        return self.__height
    @height.setter
    def height(self, height_set):
        if type(height_set) is not int:
            raise TypeError("height must be an integer")
        elif height_set < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height_set
