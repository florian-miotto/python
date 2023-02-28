# Job 20 : Valeur de retour

# Créer un programme job20.py. Le programme devra contenir une seule fonction
# nommée myAddition qui prend en paramètres deux nombres et qui retourne le résultat
# de leur addition.
# Vous devrez appeler cette fonction et assigner à une variable le résultat qu’elle retourne.

input1 = int(input("Entrez un nombre : "))
input2 = int(input("Entrez un nombre : "))


def myAddition(a, b):
    c = a+b
    return (c)


print(myAddition(input1, input2))
