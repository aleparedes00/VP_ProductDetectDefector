#!/usr/bin/env python3

from open_json import json_path
import json

"""
faire un dictionner qui lit chaque ID a un TEXT a partir de fichier json

"""
def make_dico_target(path):
    dico = dict()
    file = open(path, encoding='utf-8').read()
    json_file = json.loads(file)['fts']
    for i in range(0, len(json_file)):
        for j in range(0, len(json_file[i]['classification'])):
            dico[json_file[i]['classification'][j]['id']] =  json_file[i]['classification'][j]['text']
        pass
    pass
    return dico
pass

def make_dico_feature(path):
    dico = dict()
    file = open(path, encoding='utf-8').read()
    json_file = json.loads(file)['fts']
    for i in range(0, len(json_file)):
        for j in range(0, len(json_file[i]['attributes'])):
            dico[json_file[i]['attributes'][j]['id']] =  json_file[i]['attributes'][j]['text']
        pass
    pass
    return dico
pass

def make_dico_target_last(path):
    dico = dict()
    file = open(path, encoding='utf-8').read()
    json_file = json.loads(file)['fts']
    for i in range(0, len(json_file)):
        j = len(json_file[i]['classification']) - 1
        dico[json_file[i]['classification'][j]['id']] =  json_file[i]['classification'][j]['text']
    pass
    return dico
pass
