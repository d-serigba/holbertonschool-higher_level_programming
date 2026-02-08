#!/usr/bin/python3
"""
This module defines a function that lists available attributes and methods.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
