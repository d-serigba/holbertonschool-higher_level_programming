#!/usr/bin/python3
"""
Function that reads a UTF8 text file and prints it to stdout.
"""


def read_file(filename=""):
    """Reads and prints the content of a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
