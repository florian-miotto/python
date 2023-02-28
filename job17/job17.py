# Job 17 : Listes

# Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.


def fonctionInd(*nbr):
    for n in nbr:
        if n % 2 == 0:
            list = []
            list.append(n)
            print(list)


fonctionInd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)
