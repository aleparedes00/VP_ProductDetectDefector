import json

# Ouverture du fichier JSON
json_data=open('data/MANOUSH4.json', encoding='utf-8').read()
data = json.loads(json_data)['fts']

# Mode de récupération des valeurs. Pour le debug, je l'initialise à "text"
# Dans la pratique, il sera fixé à "id"
# C'est ce qui définit si l'on récupère le contenu de la colonne "text" ou "id" pour chaque valeur
mode = "text"

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
l_data = []
l_targets = []
for i in range(len(data)):
    l_data.append([])
    for j in range(len(data[i]['attributes'])):
        if data[i]['attributes'][j]['value'] is not None and data[i]['attributes'][j]['value'][mode] is not None:
            val = data[i]['attributes'][j]['value'][mode]
        else:
            val = ""
        l_data[i].append(val)

    last_class_col = len(data[i]['classification']) - 1
    l_targets.append(data[i]['classification'][last_class_col][mode])

print(l_data)
print(l_targets)