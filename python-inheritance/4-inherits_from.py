#!/usr/bin/python3
"""
    This module defines a function to check if
    an object is an instance of a class that
    inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
        Check if the object is an instance of
        a class that inherited from a_class.

        Args:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
