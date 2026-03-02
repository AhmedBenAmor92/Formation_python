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


#Méthode 2 :
# from pathlib import Path

# chemin = "/Users/thibh/dossier_test"

# d = {"Films": ["Le seigneur des anneaux",
#                "Harry Potter",
#                "Moon",
#                "Forrest Gump"],
#      "Employes": ["Paul",
#                   "Pierre",
#                   "Marie"],
#      "Exercices": ["les_variables",
#                    "les_fichiers",
#                    "les_boucles"]}


# for dossier_principal, sous_dossiers in d.items():
#     for dossier in sous_dossiers:
#         chemin_dossier = Path(chemin) / dossier_principal / dossier
#         chemin_dossier.mkdir(exist_ok=True, parents=True)