# Job 18 : Trier avec sort

# Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Trier par ordre croissant la liste à l’aide de la fonction sort
# - Afficher la liste dans un terminal


def fonctionInd(*nbr):
    myList = list(nbr)
    myList.sort()
    print(myList)


fonctionInd(1, 28, 3, 4, 5, 6, 7)
