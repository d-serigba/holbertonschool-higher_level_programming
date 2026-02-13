#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and saves them in a JSON file
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

my_list = []
if os.path.exists(filename):
    my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
