#!/usr/bin/python3
"""
    This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle. """
    def __init__(self, size):
        """
            Initializes a new Square instance.

            Args:
                size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
            Computes and returns the area of the square.

            Returns:
                int: The area of the square.
        """
        return super().area()
