#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
from sklearn import tree

# Chargement de la liste des fichiers
json_files = json_path('data')

# Parcours des fichiers
for file in json_files:

    # Construction des listes de données
    features, targets, test_data, check_data = make_test_data(file)

    # Construction du dictionnaire des classifications
    class_dict = make_dico(file)

    # Construction de l'arbre de décision
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, targets)

    # Évaluation des données de test
    for i in range(len(test_data)):
        answer = clf.predict([test_data[i]])[0]
        check = check_data[i]
        print("Je pense que ce produit a pour catégorie... " + class_dict[answer])
        print("Le produit est en réalité dans la catégorie... " + class_dict[check])
        if answer != check:
            print("\033[91mERROR\033[0m")