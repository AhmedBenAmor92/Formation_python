from pathlib import Path


chemin_script = Path("/Users/rihabazzabi/Desktop/workspace/Formation_python/data_clean")

chemin_file_source = chemin_script / "prenoms.txt"
chemin_file_clean = chemin_script / "prenoms_clean.txt"
chemin_file_clean.touch(exist_ok=True)
contenu_clean = []
with open(chemin_file_source, "r") as f :
    contenu = f.read().splitlines()
for i in contenu :
    element = i.replace(".", ",").split(",")
    for y in element :  
        if y != '' :
            contenu_clean.append(y.strip())
for i in contenu_clean :
    print(i)
    with open(chemin_file_clean, "w") as f :
        f.write(i)