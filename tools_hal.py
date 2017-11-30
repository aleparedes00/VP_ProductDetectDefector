#!/usr/bin/env python3

from make_dico import *

def remove_newline_dict(dico):
    for key, value in dico.items():
        dico[key] = remove_newline_str(value)
    pass
    return dict
pass

def remove_newline_str(str):
    if (str[len(str) - 1] == "\n"):
        return str[:-1]
    else:
        return str
pass