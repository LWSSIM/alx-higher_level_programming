#!/usr/bin/python3
# print an int with error msg exceptions
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
