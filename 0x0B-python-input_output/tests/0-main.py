#!/usr/bin/python3

import sys

sys.path.insert(0, "..")

read_file = __import__("0-read_file").read_file

read_file("my_file_0.txt")