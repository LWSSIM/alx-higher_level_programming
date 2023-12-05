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

    found = False
    for i, line in enumerate(lines):
        if search_string in line:
            found = True
            lines.insert(i + 1, new_string + "\n")

    if found:
        with open(filename, "w") as f:
            f.writelines(lines)
