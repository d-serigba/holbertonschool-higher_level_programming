#!/usr/bin/python3
"""
Defines a base geometry class.
"""


class BaseGeometry:
    """
    Base class for geometry objects.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.
        """
        raise Exception("area() is not implemented")
