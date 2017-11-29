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

    # Test d'affichage de la liste des attributs (première ligne uniquement)
    # Décommentez si vous voulez tester
    # for i in range(len(data[0]['attributes'])):
    #     att = data[0]['attributes'][i][mode]
    #     if data[0]['attributes'][i]['value'] is not None and data[0]['attributes'][i]['value'][mode] is not None:
    #         val = data[0]['attributes'][i]['value'][mode]
    #     else:
    #         val = ""
    #     print(att + " : " + val)

    # Construction de la liste des attributs et targets
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
            print()
        l_check.append(data[i]['classification'][last_class_col][mode])

    # print("features: " + str(l_features))
    l_features, l_test = uniformise_features(l_features, l_test)
    # print("features (fixed): " + str(l_features))
    # print("targets: " + str(l_targets))
    # print(l_test)
    # print(l_check)
    return l_features, l_targets, l_test, l_check

make_test_data('data/MANOUSH4.json')