#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
from sklearn import tree

# initialistion liste de données global
features = []
targets = []
eval_features = []
eval_targets = []
eval_info = []

# Chargement du modèle sauvegardé
# TODO...

# Chargement du dictionnaire sauvegardé
# TODO...
class_dict = dict()

# Chargement de la liste des nouveaux fichiers référence (dossier data)
json_files = json_path('data2')

# Parcours des fichiers
for file in json_files:

    # Construction des listes de données
    tmp_features, tmp_targets, tmp_info = make_data(file)
    # Debug/dev mode: décommenter pour créer les listes d'évaluation à partir des mêmes fichiers
    # Note: penser à changer la valeur de percentage dans jsonreader.py (ex: 0.8 pour un ratio 80-20)
    # tmp_eval_features, tmp_eval_targets, tmp_eval_info = make_eval_features(file)

    # Construction du dictionnaire des classifications
    tmp_class_dict = make_dico_target_last(file)

    # update des liste de donnée global
    features.extend(tmp_features)
    targets.extend(tmp_targets)
    # Décommenter si debug/dev mode
    # eval_features.extend(tmp_eval_features)
    # eval_targets.extend(tmp_eval_targets)
    class_dict.update(tmp_class_dict)

# Uniformisation des listes (pour que les lignes aient toutes la même longueur)
# TODO... Récupérer la taille max de ma liste précédente (sauvegardée)
features, eval_features = uniformise_features(features, eval_features) #indiquer la taille en paramètre
# TODO... Uniformiser aussi LA LISTE PRÉCÉDENTE !


# Construction de l'arbre de décision
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, targets)
print(clf.get_params)

nb_error = 0

# Évaluation des données de test
for i in range(len(eval_features)):
    answer = clf.predict([eval_features[i]])[0]
    check = eval_targets[i]
    if answer != check:
        print("Je pense que ce produit a pour catégorie... " + class_dict[answer])
        print("Le produit est en réalité dans la catégorie... " + class_dict[check])
        print("\033[91mERROR\033[0m")
        print("")
        nb_error = nb_error + 1

# Pourcentage de précision de la machine
raw_precision = ((len(eval_features) - nb_error) / len(eval_features))*100
precision = format(raw_precision, '.2f')
print("Le pourcentage de précision est de \033[92m" + str(precision) + "%.\033[0m")
print("Nombre d'erreurs : " + str(nb_error))