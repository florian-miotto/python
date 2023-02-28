# Job 16 : Fonctions et paramètres 2.0

# Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini.
# La fonction écrira tous les paramètres dans le terminal.


def fonctionInd(*params):
    for p in params:
        print(p)


# Exemple d'utilisation de la fonction
fonctionInd("Bonjour", "j'ai ", 4, "paramètres", True)
