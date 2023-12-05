#!/usr/bin/python3
"""Module: fn write json str rep to file
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: py_object
        filename: file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
