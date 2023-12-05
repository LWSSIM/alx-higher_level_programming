#!/usr/bin/python3

import sys

sys.path.insert(0, "..")

append_after = __import__("100-append_after").append_after

append_after("append_after_100.txt", "Python", '"C is fun!"\n')
