#!/usr/bin/python3
"""
Returns True if the object is an instance of, or inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is instance or inherited from a_class."""
    return isinstance(obj, a_class)
