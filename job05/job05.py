# Job 05 : Les boucles For

# Créez un script job05.py
# L’utilisateur devra entrer deux valeurs en input.
# A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
# trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
# aller jusqu’à l’input 2.
# Si les deux sont égaux, le programme devra écrire “Valeurs égales”.

valeur1 = int(input("Valeur1 : "))
valeur2 = int(input("Valeur2 : "))
if valeur1 == valeur2:
    print("Valeurs égales")

else:
    for i in range(valeur1 and valeur2):

        print(i)
