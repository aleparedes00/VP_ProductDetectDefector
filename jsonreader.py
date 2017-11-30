#!/usr/bin/env python3
import json
import random

# Mode de récupération des valeurs. Pour le debug, je l'initialise à "text"
# Dans la pratique, il sera fixé à "id"
# C'est ce qui définit si l'on récupère le contenu de la colonne "text" ou "id" pour chaque valeur
mode = "id"
# Valeur par défaut. Les cases vides (null) de la table seront remplacées par cette valeur
default = -1
# AP this represent the percentage of the data we'll take for the training step
percentage = 1


# Uniformise une liste si toutes les lignes n'ont pas le même nombre de cases
def uniformise_features(features, eval_features):

    # Obtenir la taille maximum si pas définie en paramètre
    size = len(features[0])
    for i in range(1, len(features)):
        if size < len(features[i]):
            size = len(features[i])
    for i in range(1, len(eval_features)):
        if size < len(eval_features[i]):
            size = len(eval_features[i])

    # Remplir les lignes trop courtes
    for i in range(len(features)):
        while len(features[i]) < size:
            features[i].append(default)
    for i in range(len(eval_features)):
        while len(eval_features[i]) < size:
            eval_features[i].append(default)

    return features, eval_features


# Retourne un indice aléatoire dans la liste
def get_value(i, first_line, last_line, added_values):

    # Sans aléatoire (décommenter)
    # return i

    # Valeur aléatoire
    r = random.randint(first_line, last_line - 1)
    while r in added_values:
        r = random.randint(first_line, last_line - 1)
    # Stockage de la valeur dans la liste des valeurs ajoutées
    added_values.append(r)
    # Renvoi de la valeur
    return r


# AP Function to open de file
def get_data(json_file):

    # Ouverture du fichier JSON
    json_data = open(json_file, encoding='utf-8').read()
    data = json.loads(json_data)['fts']
    return data


# Crée les données d'apprentissage et de test à partir d'un JSON donné
# AP Function called make_test_data before. Now will only create the training data
def make_data(json_file):

    data = get_data(json_file)
    # Construction de la liste des attributs et targets AP adding the id of the product
    l_features = []
    l_targets = []
    l_info = []
    limit = int(percentage * len(data))
    added_values = []
    for i in range(limit):
        l_features.append([])
        r = get_value(i, 0, limit, added_values)
        for j in range(len(data[r]['attributes'])):
            if data[r]['attributes'][j]['value'] is not None and data[r]['attributes'][j]['value'][mode] is not None:
                val = data[r]['attributes'][j]['value'][mode]
            else:
                val = default
            l_features[i].append(val)
        last_class_col = len(data[r]['classification']) - 1
        l_targets.append(data[r]['classification'][last_class_col][mode])
        product_info = dict()
        product_info['id'] = data[r]['id']
        product_info['file'] = data[r]['operationCode']
        l_info.append(product_info)

    return l_features, l_targets, l_info


# AP Divide make_test_data in a second fc to separate test data and training data
# Note: only for debug/dev
def make_test_data(json_file):

    data = get_data(json_file)
    limit = int(percentage * len(data))
    # Construction des données de test
    l_test_features = []
    l_test_targets = []
    added_values = []
    l_info = []
    for i in range(limit, len(data)):
        l_test_features.append([])
        r = get_value(i, limit, len(data), added_values)
        for j in range(len(data[r]['attributes'])):
            if data[r]['attributes'][j]['value'] is not None and data[r]['attributes'][j]['value'][mode] is not None:
                val = data[r]['attributes'][j]['value'][mode]
            else:
                val = default
            l_test_features[i - limit].append(val)
        last_class_col = len(data[r]['classification']) - 1
        l_test_targets.append(data[r]['classification'][last_class_col][mode])
        product_info = dict()
        product_info['id'] = data[r]['id']
        product_info['file'] = data[r]['operationCode']
        l_info.append(product_info)

    return l_test_features, l_test_targets, l_info
