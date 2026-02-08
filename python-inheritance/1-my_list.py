#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""

class MyList(list):
    """
    A class that extends the built-in list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
