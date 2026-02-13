#!/usr/bin/python3
"""
Defines a Student class with JSON serialization.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student instance.
        This mimics 8-class_to_json by returning only serializable attributes.
        """
        return {key: value for key, value in self.__dict__.items()}
