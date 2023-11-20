#!/usr/bin/python3
# safely excecute a passed function
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as E:
        print("Exception: {}".format(E), file=sys.stderr)
        return None
