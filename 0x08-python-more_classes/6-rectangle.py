#!/usr/bin/python3
"""
This module containes a class named Rectangle
and attributes width and height

Calculates the area and perimeter.

validating the entries given.
"""


class Rectangle:
    """
    This is a Rectangle class
    Attributes:
    number_of_instance (int): counts the ammount of 
    intances created
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Takes attributes width and height.
        Attributes:
        width (int): width of the rectangle; must be int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns width
        """
        return self.__width

    @width.setter
    def width(self, width_set):
        """
        Defines the value of width
        and validates if is an int and >= 0
        Attributes:
        width_set (int): width of the rectangle
        """
        if type(width_set) is not int:
            raise TypeError("width must be an integer")
        elif width_set < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width_set

    @property
    def height(self):
        """
        Retrurns height
        """
        return self.__height

    @height.setter
    def height(self, height_set):
        """
        Defines the value of width
        and validates if is an int and >= 0
        Attributes:
        height_set (int): height of the rectangle
        """
        if type(height_set) is not int:
            raise TypeError("height must be an integer")
        elif height_set < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height_set

    def area(self):
        """
        Returns the are of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of a rectangle
        """
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (int(self.width) * 2) + (int(self.height) * 2)

    def __str__(self):
        """
        Prints # in the area of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = ""
            rectangle = ("#" * self.width + '\n') * self.height
            rectangle = rectangle[:-1]
            return rectangle

    def __repr__(self):
        """
        Returns the representation of a rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Deletes an instance and prints bye message
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
