#!/usr/bin/python3
""" Student module with JSON serialization and reloading """

class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the student.

        If attrs is a list of strings, only return those attributes.
        Otherwise, return all attributes.
        """
        if attrs is None:
            return self.__dict__.copy()
        filtered = {}
        for key in attrs:
            if key in self.__dict__:
                filtered[key] = self.__dict__[key]
        return filtered

    def reload_from_json(self, json):
        """Replace all attributes of the student with the dictionary values."""
        for key, value in json.items():
            setattr(self, key, value)
