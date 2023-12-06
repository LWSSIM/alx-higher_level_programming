#!/usr/bin/python3
"""Module: script reads stdin line by line and computes metrics
"""


from sys import stdin


def print_stat(size, status):
    """print stat with desired format


    Args:
        size: file size
        status: code:number
    """
    print(f"File size: {size}")
    for key in status:
        if status[key] != 0:
            print(f"{key}: {status[key]}")


size = 0
status = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_nb = 0
try:
    for line in stdin:
        if line_nb == 10:
            print_stat(size, status)
            line_nb = 0
        else:
            line_nb += 1
        lines = line.split()
        try:
            size += int(lines[-1])
        except (ValueError, IndexError):
            pass
        try:
            for key in status:
                if key == lines[-2]:
                    status[key] += 1
        except IndexError:
            pass
    print_stat(size, status)
except KeyboardInterrupt:
    print_stat(size, status)
    raise
