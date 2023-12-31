#!/usr/bin/python3
"""Module:script that adds all arguments to a Python list,
and save them to a file
"""

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    arg_list = load_from_json_file("add_item.json")
except Exception:
    arg_list = []

for i in range(1, len(argv)):
    arg_list.append(argv[i])

save_to_json_file(arg_list, "add_item.json")
