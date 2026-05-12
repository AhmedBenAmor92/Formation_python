"""Module générateur d'utilisateurs"""
from faker import Faker
from pathlib import Path
import logging

base_dir = Path(__file__).resolve().parent
fake = Faker(locale="fr_FR")
logging.basicConfig(level=logging.INFO,
                    filename=base_dir / 'user.log',
                    filemode="a", # mode d'ajout, ça nous permet d'ajouter le message d'erreur dans le fichier
                    format='%(asctime)s - %(levelname)s - %(message)s')
def get_user() :
    """générateur d'un utilisateur
    cette fonction va nous génrer un nom (prénom nom)
    Returns:
        str : utilisateur
    """
    logging.info("Generation d'un utilisateur.")
    nom = fake.name()
    return nom


def get_users(nb_users) :
    """générateur d'une liste d'utilisateur

    Args:
        nb_users (int): nombre d'utilisateurs qu'on veut générer

    Returns:
        list[str] : utilisateurs
    """
    logging.info(f"Generation de {nb_users} utilisateurs.")
    noms = []
    for _ in range(nb_users):
        noms.append(get_user())
    return noms

if __name__ == "__main__" :
    user = get_users(5)
    print(user)