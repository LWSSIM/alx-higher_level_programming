#!/usr/bin/python3
"""Module: fn convert data from json str
"""

import json


def from_json_string(my_str):
    """json deserialization using load

    Args:
        my_str: object to deserialize

    Return:
        JSON rep. of the passed obj
    """
    return json.loads(my_str)
