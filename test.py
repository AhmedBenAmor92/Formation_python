from pathlib import Path
 
d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}
 
chemin = Path(r"C:\Users\bnamo\OneDrive\Bureau\workspace\FormationPython\dossier_test")

for i in d.keys():
    new_dir = chemin / i
    new_dir.mkdir(exist_ok=True)
    liste = d[i]
    for y in liste:
        sous_dossier = new_dir / y
        sous_dossier.mkdir(exist_ok=True)