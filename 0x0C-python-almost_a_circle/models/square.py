#!/usr/bin/python3
"""
This module contains a Square class
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square class that inherits from rectangle
        Args:
        size (int): size of the square
        x (int): position in x axis of the square
        y (int): position in y axis of the square
        """
        self.size = size
        super().__init__(size, size, x, y)

    def __str__(self):
        """
        Prints information of a square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.size)

    @property
    def size(self):
        """
        Returns size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Assings and validates the value of size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of a square
        """
        return self.size * self.size

    def display(self):
        """
        Prints str rep of a square
        """
        for y_skip in range(self.y):
            print()
        spaces = " " * self.x
        for row in range(self.size):
            print(spaces, end="")
            for col in range(self.size):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        if len(args):
            for key, arg in enumerate(args):
                if arg == 0:
                    self.id = arg
                elif arg == 1:
                    self.size = arg
                elif arg == 2:
                    self.x = arg
                elif arg == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return dict representation of a class
        """
        square = Square(self.id, self.size, self.x, self.y)
        return dict(square.__dict__)
