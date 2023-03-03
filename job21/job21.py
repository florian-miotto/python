# Créer un programme job21.py. Reprenez l’exercice 19, mais modifiez le de façon à
# utiliser deux fonctions :
# - Une fonction mySort, qui prendra en paramètre une liste. Elle retourne une liste
# avec les valeurs de celle passée en paramètre, triés par ordre croissant.
# - Une fonction myDisplay qui prendra en paramètre une liste. Elle affichera dans le
# terminal le contenu de cette liste.
def mySort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j = j-1
        lst[j] = x
    return lst


def myDisplay(lst):
    for element in lst:
        print(element, end=" ")
    print()


myList = [10, 7, 3, 9, 4, 1, 6, 8, 5, 2]

# trier la liste en utilisant la fonction mySort
print(mySort(myList))

# afficher la liste
myDisplay(myList)
