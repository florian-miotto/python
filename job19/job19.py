# Job 19 : Trier avec sort

# Créer un programme job19.py. Le programme devra contenir une seule fonction qui
# prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Trier par ordre croissant la liste  (Donc sans la fonction sort)
#
# - Afficher la liste dans un terminal

def fonction_ind(*args):
    # convertir les arguments en liste
    lst = list(args)
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j = j-1
        lst[j] = x
    print(lst)


fonction_ind(1, 28, 3, 4, 5, 6, 7)
