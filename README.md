# VP_ProductDefectDetector #

## REQUIREMENTS ##
*python3*  
*pip3* (python3-pip)  
*numpy*  
*pandas*  
*scikit-learn*  
*scipy*  
    ___
## INSTALL ##
_'sudo pip3 install -r requirements.txt'_  
_'chmod +x ./learning.py'_  
_'chmod +x ./main.py'_  
    ___
## USAGE ##
- learning :
    Placer les données à apprendre dans le dossier data.  
    Pour tester le modèle, changer la valeur de percentage dans jsonreader.py.  
    Exemples : 0.8 pour un ratio 80% à apprendre, 20% à évaluer ; 0 pour ne rien apprendre et tout évaluer.  
    Pour apprendre tout le contenu de data et sauvegarder le modèle, mettre à 1.  
    Exécuter le fichier learning.py soit en _'python3 ./learning.py'_ soit _'./learning.py'_  

- main :
    Placer les données à évaluer dans le dossier eval.  
    Exécuter le fichier main.py soit en _'python3 ./main.py'_ soit _'./main.py'_  
