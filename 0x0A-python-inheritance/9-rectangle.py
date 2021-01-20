#!/usr/bin/python3
"""
This module holds a class name Rectangle
and validates the entries
"""


bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(bg):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle class
        Instances:
        width (int): width of the rectangle
        height (int) height of the rectangle
        """
        bg.integer_validator(self, "width", width)
        self.__width = width
        bg.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """
        Return the area of a rectangle class
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns str representation of the class square
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
