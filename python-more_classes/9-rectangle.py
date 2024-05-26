#!/usr/bin/python3
"""Contains an empty class definition of 'Rectangle'"""


class Rectangle:
    """definition of 'Rectangle'"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif not type(height) is int:
            raise TypeError("height must be an integer")
        if int(width) < 0:
            raise ValueError("width must be >= 0")
        if int(height) < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        self.__class__.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        string += "{}".format(
            "\n".join([str(self.print_symbol) * self.__width] * self.__height)
        )
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
