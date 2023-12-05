#!/usr/bin/python3
"""Module: fn convert data to json
"""

import json


def to_json_string(my_obj):
    """json serialization using dumps

    Args:
        my_obj: object to serialize

    Return:
        JSON rep. of the passed obj
    """
    return json.dumps(my_obj)
