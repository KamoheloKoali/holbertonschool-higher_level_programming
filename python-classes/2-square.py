#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
2-square.py: is a class Square that defines a square
"""

class Square:
    """Represent a square.

    Attributes:
        attr1 (_Square_Size): private instance attribute size

    """

    def __init__(self, size=0):
        """Initializer _square_size"""
        if size.isdigit():
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size =  size
        else:
            raise TypeError("size must be an integer")
