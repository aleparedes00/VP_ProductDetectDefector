#!/usr/bin/env python3
from pprint import pprint
import os
import json

root = './data/'

def json_path(root):
    ext = '.json'
    list_json_data = []
    for file in os.listdir(root):
        if file.endswith(ext):
            list_json_data.append(os.path.join(root, file))
        else:
            print('file not json')
    return list_json_data
pass


def open_json_array(list_data):
    for json_path in list_data:
        print(json.load(open(json_path)))
pass


list_data = json_path(root)

open_json_array(list_data)
