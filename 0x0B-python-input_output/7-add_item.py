#!/usr/bin/python3
'''
Collects all arguments into a Python list,
and subsequently stores them in a file
'''


import sys
fdumpJson = __import__('5-save_to_json_file').save_to_json_file
loadJson = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

try:
    pyData = loadJson('add_item.json')
except FileNotFoundError:
    pyData = []

pyData.extend(args)
dumpJson(pyData, 'add_item.json')