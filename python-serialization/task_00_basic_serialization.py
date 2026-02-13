#!/usr/bin/env python3
"""
Module for basic serialization and deserialization of Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the JSON file to save the data in.

    If the file already exists, it will be overwritten.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r') as file:
        return json.load(file)
