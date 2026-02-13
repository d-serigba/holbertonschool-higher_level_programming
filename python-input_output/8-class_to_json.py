#!/usr/bin/python3
"""
Function that returns a dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Args:
        obj: an instance of a class
    Returns:
        dictionary of all serializable attributes (instance + class)
    """
    result = {}
    for key in dir(obj):
        # Ignore private attributes et méthodes
        if key.startswith('__'):
            continue
        value = getattr(obj, key)
        # Garde seulement les types simples pour JSON
        if isinstance(value, (int, float, str, bool, list, dict)):
            result[key] = value
    return result
