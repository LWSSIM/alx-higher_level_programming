#!/usr/bin/python3
"""Module: fn to write to a file
"""


def write_file(filename="", text=""):
    """Write text to a file
    Note:
        create file if not existant

    Args:
        filename:str
        text:str

    Return: nb of written chars
    """
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
        return num
