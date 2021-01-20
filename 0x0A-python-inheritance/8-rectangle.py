#!/usr/bin/python3
"""
This module holds a class named rectangle
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
        Intances:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        bg.integer_validator(self, "width", width)
        self.__width = width
        bg.integer_validator(self, "height", height)
        self.__height = height
