#!/usr/bin/env python3
"""
Module that defines a CustomObject class
with methods to serialize and deserialize using pickle.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object with name, age, and is_student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass  # Silently ignore exceptions as per instructions

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject or None: The deserialized object,
            or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
