# Job 12 : Traitement d’un fichier 2.0

# Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
# le nombre de mots (sans caractère spéciaux) qui s’y trouvent.


import re

with open('data.txt', 'r') as f:
    text = f.read()

    # supprimer les caractères spéciaux
count = len(re.findall(r'\b\w+\b', text))
print(f"Le fichier contient {count} mots.")
