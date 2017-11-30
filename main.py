#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
import pickle
from sklearn import tree

# AP creating all list for features, targets and info that will be submit at test
features = []
targets = []
eval_features = []
eval_targets = []
eval_info = []
class_dict = dict()

json_files = json_path(eval)

for file in json_files:

    # creating the data lists
    tmp_eval_features, tmp_eval_targets, tmp_eval_info = make_data(file)

    # Construction du dictionnaire des classifications
    tmp_class_dict = make_dico_target_last(file)

    eval_features.extend(tmp_eval_features)
    eval_targets.extend(tmp_eval_targets)
    eval_info.extend(tmp_eval_info)
    class_dict.update(tmp_class_dict)

model = pickle.load(open('ProductDefectDetector.sav', 'rb'))
nb_error = 0

# Évaluation des données de test
for i in range(len(eval_features)):
    answer = model.predict([eval_features[i]])[0]
    check = eval_targets[i]
    if answer != check:
        print("Je pense que ce produit a pour catégorie... " + class_dict[answer])
        print("Le produit est en réalité dans la catégorie... " + class_dict[check])
        print("Le objet est l'id =" + eval_info[i]['id'] + "dans le fichier " + eval_info[i]['file'] + "\n")
        print("\033[91mERROR\033[0m\n")
        nb_error = nb_error + 1

