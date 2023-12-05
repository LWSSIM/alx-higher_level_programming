#!/usr/bin/python3
"""Module: fn to read and print file content
"""


def read_file(filename=""):
    """Read file and print content

    Note:
        encoding-uft8
    """
    with open(filename, "r") as f:
        content = f.read()
        print(content)
