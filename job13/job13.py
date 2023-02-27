# Job 13 : Traitement d’un fichier 3.0

# Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre
# entier. Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
# nombre de mots de la taille renseignée qui s’y trouvent.


import re

nombre = int(input("Entrez un nombre entier : "))
with open('data.txt', 'r') as fichier:
    text = fichier.read()

count = len([word for word in re.findall(
    r'\b\w+\b', text) if len(word) == nombre])

print('Le fichier contient', count, 'mots de taille', nombre, '.')
