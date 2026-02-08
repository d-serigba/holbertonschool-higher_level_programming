#!/usr/bin/python3
"""
    This module defines a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry. """
    def __init__(self, width, height):
        """
            Initializes a new Rectangle instance.

            Args:
                width (int): Width of the rectangle.
                height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
            Computes and returns the area of the rectangle.

            Returns:
                int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
            Returns a string representation of the rectangle.

            Returns:
                str: String representation in
                the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
