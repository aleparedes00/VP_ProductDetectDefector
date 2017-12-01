#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
import pickle
import os
from sklearn import tree

eval_root = 'eval'

if os.path.isdir(eval_root):
    try:
        # AP creating all list for features, targets and info that will be submit at test
        features = pickle.load(open('model/features.sav', 'rb'))
        targets = pickle.load(open('model/targets.sav', 'rb'))
        class_dict = pickle.load(open('model/class_dict.sav', 'rb'))
        eval_features = []
        eval_targets = []
        eval_info = []

        json_files = json_path(eval_root)

        if len(json_files) == 0:
            print("No files to evaluate.")
        else:
            for file in json_files:

                # creating the data lists
                tmp_eval_features, tmp_eval_targets, tmp_eval_info = make_data(file)

                # Construction du dictionnaire des classifications
                tmp_class_dict = make_dico_target_last(file)

                eval_features.extend(tmp_eval_features)
                eval_targets.extend(tmp_eval_targets)
                eval_info.extend(tmp_eval_info)
                class_dict.update(tmp_class_dict)

            # Uniformisation des listes (pour que les lignes aient toutes la même longueur)
            features, eval_features = uniformise_features(features, eval_features)

            # Construction de l'arbre de décision
            model = tree.DecisionTreeClassifier()
            model = model.fit(features, targets)

            # Évaluation des données de test
            nb_error = 0
            log = open("error_log.txt", "w+", encoding="UTF-8")
            for i in range(len(eval_features)):
                answer = model.predict([eval_features[i]])[0]
                check = eval_targets[i]
                if answer != check:
                    log.write("Expected [" + class_dict[answer] + "], found [" + class_dict[check] + "] for product [" +
                              str(eval_info[i]['id']) + " - " + str(eval_info[i]['file']) + "]\n")
                    nb_error = nb_error + 1
            log.close()

            if nb_error > 0:
                print("Found " + str(nb_error) + " errors. Check error_log.txt for more info.")
            else:
                os.remove("error_log.txt")
                print("No error found.")

    except FileNotFoundError:
        print("Classification model undefined. Please run learning.py script first.")
else:
    print("No eval directory found.")