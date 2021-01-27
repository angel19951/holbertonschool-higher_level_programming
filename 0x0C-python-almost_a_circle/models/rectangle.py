#!/usr/bin/python3
"""
This module containes a class name Rectangle
and attributes width, height, x and y
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Rectangle class
    Args:
    width (int): width of the rectangle
    height (int): height of the rectangle
    x (int): position of the rectangle x axis
    y (int): position of the rectangle y axis
    id (int): is number for class inherited
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inititalizes a Rectangle class
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): position in x axis of rectangle
        y (int): position in y axis of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Prints information of the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    @property
    def width(self):
        """
        Returns width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines and validates the value of width
        Args:
        value (int): width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Defines and validates the value of height
        Args:
        value (int): height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Returns x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Defines and validates the value of x
        Args:
        value (int): x position of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Returns y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Defines and validates the value of y
        Args:
        value (int): y position of the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints str representation of a rectangle
        """
        for y_skip in range(self.y):
            print()
        spaces = " " * self.x
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for row in range(self.height):
                print(spaces, end="")
                for col in range(self.width):
                    print("#", end="")
                print()

    def update(self, *args, **kwargs):
        """
        Updates the values inside the rectangle
        using args
        """
        if len(args):
            for arg, value in enumerate(args):
                if arg == 0:
                    self.id = value
                elif arg == 1:
                    self.width = value
                elif arg == 2:
                    self.height = value
                elif arg == 3:
                    self.x = value
                elif arg == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Return dict representation of a class
        """
        rectangle = Rectangle(self.id, self.width, self.height, self.x, self.y)
        return dict(rectangle.__dict__)
