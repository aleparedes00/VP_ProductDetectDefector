#!/usr/bin/env python3

from open_json import json_path
from pprint import pprint
import json

"""
faire un dictionner qui lit chaque ID a un TEXT a partir de fichier json

"""
def make_dico(path):
    col = ('id', 'text')
    dico = dict.fromkeys(col)
    file = open(path, encoding='utf-8').read()
    json_file = json.loads(file)['fts']
    for i in range(0, len(json_file)):
        for j in range(0, len(json_file[i]['classification'])):
            dico[json_file[i]['classification'][j]['id']] =  json_file[i]['classification'][j]['text']
        pass
    pass
    return dico
pass
