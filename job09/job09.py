# Job 09 : Triangle

# Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
# ‘\’ et des ‘/’
# en fonction de l’input entré, qui représentera la hauteur.


hauteur = int(input("Entrez la hauteur du triangle : "))


# Dessiner le triangle
for i in range(hauteur):
    print(" " * (hauteur - i - 1) + "/" + " " * (2 * i) + "\\")

print(hauteur)
