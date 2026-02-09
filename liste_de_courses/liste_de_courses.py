liste_des_courses = []
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
        liste_des_courses.append(demande)
        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
    
    elif choix == "2" :
        demande = input("Retirer un élément de la liste de courses : ")
        liste_des_courses = [x for x in liste_des_courses if x != demande]
        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    elif choix == "3" :
        for x, valeur in enumerate(liste_des_courses, start=1) :
            print(x, valeur)
        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    elif choix == "4" :
        liste_des_courses.clear()
        for i, element in enumerate(liste_des_choix, start=1) :
            print(i, element)
        choix = input("Votre choix : ")
        
    else :
        print("A bientôt !")
        a = False