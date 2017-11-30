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
percentage = 0.8


# Uniformise une liste si toutes les lignes n'ont pas le même nombre de cases
def uniformise_features(fts, test):

    # Obtenir la taille maximum
    size = len(fts[0])
    for i in range(1, len(fts)):
        if size < len(fts[i]):
            size = len(fts[i])
    for i in range(1, len(test)):
        if size < len(test[i]):
            size = len(test[i])

    # Remplir les lignes trop courtes
    for i in range(len(fts)):
        while len(fts[i]) < size:
            fts[i].append(default)
    for i in range(len(test)):
        while len(test[i]) < size:
            test[i].append(default)

    return fts, test


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
def make_training_data(json_file):

    data = get_data(json_file)
    # Construction de la liste des attributs et targets
    l_features = []
    l_targets = []
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

    return l_features, l_targets


# AP Divide make_test_data in a second fc to separate test data and training data
def make_test_data(json_file):

    data = get_data(json_file)
    limit = int(percentage * len(data))
    # Construction des données de test
    l_test_features = []
    l_test_targets = []
    added_values = []
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

    return l_test_features, l_test_targets
