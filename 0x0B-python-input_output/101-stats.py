#!/usr/bin/python3
"""Module: script reads stdin line by line and computes metrics
"""


import sys


def print_stat(size, status):
    """print stat with desired format


    Args:
        size: file size
        status: code:number
    """
    print(f"File size: {size}")
    for key in status:
        if status[key] > 0:
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
    for line in sys.stdin:
        if line_nb == 10:
            print_stat(size, status)
            line_nb = 0
        else:
            line_nb += 1
        lines = line.split()
        size += int(line[-1])

        for key in status:
            if key == lines[-2]:
                status[key] += 1

    print_stat(size, status)
except KeyboardInterrupt:
    print_stat(size, status)
