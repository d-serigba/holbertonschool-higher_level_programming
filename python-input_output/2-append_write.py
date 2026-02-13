#!/usr/bin/python3
"""
Function that appends a string to a UTF8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends text to end of file and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
