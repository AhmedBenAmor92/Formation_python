from pathlib import Path


chemin_script = Path(__file__).parent

chemin_file_source = chemin_script / "prenoms.txt"
chemin_file_clean = chemin_script / "prenoms_clean.txt"
chemin_file_clean.touch(exist_ok=True)
contenu_clean = []
with open(chemin_file_source, "r") as f :
    # mettre le contenu du fichier dans une liste
    contenu = f.read().splitlines()
# nettoyer la liste contneu (remplacer les . par , et spliter pour séparer les chaines qui cotiennents plusieurs chaines)
for i in contenu :
    element = i.replace(".", ",").split(",")
    for y in element :  
        if y != '' :
            # ajouter les chaine dans une nouvelle liste en supprimant les espaces
            contenu_clean.append(y.strip())
# écrire les les chaine de la liste contenu_clean dans le fichier chemin_file_clean
contenu_clean.sort()
with open(chemin_file_clean, "w") as f :
    for i in contenu_clean :
        f.write(i + "\n")