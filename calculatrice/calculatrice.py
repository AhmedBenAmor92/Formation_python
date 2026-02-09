a = input("Entrez un premier nombre : ")

b = input("Entrez un deuxième nombre : ")

while not a.isdigit() or not b.isdigit() :

    print("Veuillez entrer deux nombres valides")

    a = input("Entrez un premier nombre : ")

    b = input("Entrez un deuxième nombre : ")

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")