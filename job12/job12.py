# Job 12 : Traitement d’un fichier 2.0

# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre de mots (sans caractère spéciaux) qui s’y trouvent.


import re

with open('data.txt', 'r') as file:
    text = file.read()

    # supprimer les caractères spéciaux
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    count = len(words)
    print(f"Le fichier contient {count} mots.")
