#!/usr/bin/python3
"""Module: fn to apppen txt to file
"""


def append_write(filename="", text=""):
    """append content to file
    Note:
        create if no file exist

    Args:
        filename: str
        text: str

    Return:
        nb of written chars
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
        return num
