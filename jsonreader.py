#!/usr/bin/env python3
import json

# Mode de récupération des valeurs. Pour le debug, je l'initialise à "text"
# Dans la pratique, il sera fixé à "id"
# C'est ce qui définit si l'on récupère le contenu de la colonne "text" ou "id" pour chaque valeur
mode = "id"
# Valeur par défaut. Les cases vides (null) de la table seront remplacées par cette valeur
default = -1

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


# Crée les données d'apprentissage et de test à partir d'un JSON donné
def make_test_data(json_file):

    # Ouverture du fichier JSON
    json_data = open(json_file, encoding='utf-8').read()
    data = json.loads(json_data)['fts']

    # Construction de la liste des attributs et targets
    # TODO: les données sont construites en mode 80 premiers % / 20 derniers %. Idéalement, il faudrait revoir cette fonction pour qu'il garde le ratio mais sélectionne les entrées AU HASARD.
    l_features = []
    l_targets = []
    limit = int(0.8 * len(data))
    for i in range(limit):
        l_features.append([])
        for j in range(len(data[i]['attributes'])):
            if data[i]['attributes'][j]['value'] is not None and data[i]['attributes'][j]['value'][mode] is not None:
                val = data[i]['attributes'][j]['value'][mode]
            else:
                val = default
            l_features[i].append(val)
        last_class_col = len(data[i]['classification']) - 1
        l_targets.append(data[i]['classification'][last_class_col][mode])

    # Construction des données de test
    l_test = []
    l_check = []
    for i in range(limit, len(data)):
        l_test.append([])
        for j in range(len(data[i]['attributes'])):
            if data[i]['attributes'][j]['value'] is not None and data[i]['attributes'][j]['value'][mode] is not None:
                val = data[i]['attributes'][j]['value'][mode]
            else:
                val = default
            l_test[i - limit].append(val)
        last_class_col = len(data[i]['classification']) - 1
        l_check.append(data[i]['classification'][last_class_col][mode])

    # Uniformisation des listes (pour que les lignes aient toutes la même longueur)
    l_features, l_test = uniformise_features(l_features, l_test)

    return l_features, l_targets, l_test, l_check