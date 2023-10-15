#!/usr/bin/python3
'''Module for the add_item program'''


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arg = list(sys.argv[1:])

try:
    ls = load_from_json_file('add_item.json')
except Exception:
    ls = []

ls.extend(args)
save_to_json_file(ls, 'add_item.json')
