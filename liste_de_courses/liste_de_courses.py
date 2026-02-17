import json
import os

CUR_DIR = os.path.dirname(__file__)
chemin = os.path.join(CUR_DIR, "liste_des_courses.json")

if not os.path.exists(chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump([], f)


liste_des_choix = ["Ajouter un élément à la liste de courses",
                   "Retirer un élément de la liste de courses",
                   "Afficher les éléments de la liste de courses",
                   "Vider la liste de courses",
                   "Quitter le programme"]

for i, element in enumerate(liste_des_choix, start=1) :
    print(i, element)

choix = input("Votre choix : ")
a = True
while a :
    while not choix.isdigit() or int(choix) not in range(1,6) :
        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")

    if choix == "1" :
        demande = input("Ajouter un élément à la liste de courses : ")

        # récupération des données dans la variable donnees
        with open(chemin, "r", encoding='UTF-8') as f :
            donnees = json.load(f)
        # modifier les donnees dans la variable donnees
        donnees.append(demande)
        # réécrire les donnees dans notre dichier JSON
        with open(chemin, "w", encoding='UTF-8') as f :
            json.dump(donnees, f, indent=4)

        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
    
    elif choix == "2" :
        demande = input("Retirer un élément de la liste de courses : ")
        

        # récupération des données dans la variable donnees
        with open(chemin, "r", encoding='UTF-8') as f :
            donnees = json.load(f)
        # modifier les donnees dans la variable donnees
        donnees = [x for x in donnees if x != demande]
        # réécrire les donnees dans notre dichier JSON
        with open(chemin, "w", encoding='UTF-8') as f :
            json.dump(donnees, f, indent=4)

        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    elif choix == "3" :

        with open(chemin, "r", encoding='UTF-8') as f :
            contenu = json.load(f)
            
        print("--------------------------------------------------------------------------------")
        for i, element in enumerate(contenu, start=1) :
            print(f"{i}. {element}")
        print("--------------------------------------------------------------------------------")

        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    elif choix == "4" :
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump([], f)

        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    else :
        print("A bientôt !")
        a = False