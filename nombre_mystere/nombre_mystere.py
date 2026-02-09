import random

nombre_mystere = random.randint(0, 100)
essais = list(range(5, 0, -1))
print("Devine le nombre entre 0 et 100 !")

for i in essais :
    print(f"Il te reste {i} essais")
    nombre = input("Devine le nombre : ")
    while not nombre.isdigit() or int(nombre) not in range(0, 101) :
        print("Veuillez entrer un nombre valide.")
        print(f"Il te reste {i} essais")
        nombre = input("Devine le nombre : ")
    if int(nombre) == int(nombre_mystere) :
        print(f"Bravo ! Le nombre mystère était {nombre_mystere}")
        break
    else :
        if int(nombre_mystere) > int(nombre) :
            print(f"Le nombre mystère est plus grand que {nombre}")
        else :
            print(f"Le nombre mystère est plus petit que {nombre}")
else :
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")
print("Fin de jeu.")