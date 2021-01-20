#!/usr/bin/python3
"""
This module containse a class named BaseGeometry
and validates the entries
"""


class BaseGeometry:
    """
    BaseGeometry empty class
    """
    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the entry,
        raising error if value is not int
        or value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
