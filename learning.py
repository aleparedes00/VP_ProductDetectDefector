#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
from sklearn import tree

# initialistion liste de données global
features = []
targets = []
test_data = []
check_data = []
class_dict = dict()

# Chargement de la liste des fichiers
json_files = json_path('data')

# Parcours des fichiers
for file in json_files:

    # Construction des listes de données
    tmp_features, tmp_targets = make_training_data(file)
    tmp_test_data, tmp_check_data = make_test_data(file)

    # Construction du dictionnaire des classifications
    tmp_class_dict = make_dico_target(file)

    # update des liste de donnée global
    features.extend(tmp_features)
    targets.extend(tmp_targets)
    test_data.extend(tmp_test_data)
    check_data.extend(tmp_check_data)
    class_dict.update(tmp_class_dict)

# Uniformisation des listes (pour que les lignes aient toutes la même longueur)
features, test_data = uniformise_features(features, test_data)

# Construction de l'arbre de décision
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, targets)

nb_error = 0

# Évaluation des données de test
for i in range(len(test_data)):
    answer = clf.predict([test_data[i]])[0]
    check = check_data[i]
    if answer != check:
        print("Je pense que ce produit a pour catégorie... " + class_dict[answer])
        print("Le produit est en réalité dans la catégorie... " + class_dict[check])
        print("\033[91mERROR\033[0m")
        print("")
        nb_error = nb_error + 1

# Pourcentage de précision de la machine
raw_precision = ((len(test_data) - nb_error) / len(test_data))*100
precision = format(raw_precision, '.2f')
print("Le pourcentage de précision est de \033[92m" + str(precision) + "%.\033[0m")