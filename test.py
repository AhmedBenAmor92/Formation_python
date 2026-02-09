import random
 
vie_joueur = 50
vie_ennemi = 50
potion = 3
 
while vie_joueur > 0 and vie_ennemi > 0:
    vie = random.randint(15, 50)
    degat_joueur = random.randint(5, 10)
    degat_ennemi = random.randint(5, 15)
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ")
    while not choix.isdigit() or int(choix) not in range(1, 3):
        choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ")
    if int(choix) == 1 :
        print(f"Vous avez infligé {degat_joueur} points de dégats à l'ennemi")
        print(f"L'ennemi vous a infligé {degat_ennemi} points de dégats")
        print(f"Il vous reste {vie_joueur - degat_ennemi} points de vie")
        print(f"Il reste {vie_ennemi - degat_joueur} points de vie à l'ennemi")
        vie_joueur = vie_joueur - degat_ennemi
        vie_ennemi = vie_ennemi - degat_joueur
        print("---------------------------------------------------------------------------")
    else :
        if (potion - 1) >= 0 :
            if (potion - 1) > 1 :
                print(f"Vous récupérez {vie} points de vie ({potion - 1} potions restantes)")
            else :
                print(f"Vous récupérez {vie} points de vie ({potion - 1} potion restantes)")
            vie_joueur = vie_joueur + vie
            potion -= 1
            print(f"L'ennemi vous a infligé {degat_ennemi} points de dégats")
            print(f"Il vous reste {vie_joueur - degat_ennemi} points de vie")
            print(f"Il reste {vie_ennemi} points de vie à l'ennemi")
            vie_joueur = vie_joueur - degat_ennemi
            print("---------------------------------------------------------------------------")
            print("Vous passez votre tour ...")
            degat_ennemi = random.randint(5, 15)
            print(f"L'ennemi vous a infligé {degat_ennemi} points de dégats")
            print(f"Il vous reste {vie_joueur - degat_ennemi} points de vie")
            print(f"Il reste {vie_ennemi} points de vie à l'ennemi")
            vie_joueur = vie_joueur - degat_ennemi
            print("---------------------------------------------------------------------------")
        else :
            print("Vous n'avez plus de potions ...")
    if vie_joueur <= 0 :
        print("Tu as perdu :'(")
        break
    elif vie_ennemi <= 0 :
        print("Vous avez gagné :D")
        break
print("Fin de jeu.")