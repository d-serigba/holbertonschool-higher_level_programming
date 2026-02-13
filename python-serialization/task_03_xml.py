#!/usr/bin/env python3
"""
Module to serialize and deserialize a Python dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The reconstructed dictionary from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result
    except (ET.ParseError, FileNotFoundError):
        return {}
