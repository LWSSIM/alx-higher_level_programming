#!/usr/bin/python3
"""Module:fn special file insert
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename: file stream
        search_string: flag str
        new_string: input text
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(search_string)