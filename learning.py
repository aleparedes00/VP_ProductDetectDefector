#!/usr/bin/env python3
from open_json import *
from jsonreader import *
from make_dico import *
from sklearn import tree

json_files = json_path('data')
for file in json_files:
    print("Opening file " + file)
    features, targets, test_data, check_data = make_test_data(file)

    #class_dict = make_dico(file)
    #print(class_dict)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, targets)

    for i in range(len(test_data)):
        answer = clf.predict([test_data[i]])[0]
        check = check_data[i]
        print("I think that this product is a... " + str(answer))#class_dict[answer])
        print("The product is actually a... " + str(check))#class_dict[check])
        if answer != check:
            print("ERROR")