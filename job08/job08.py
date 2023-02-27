# Écrire un programme rectangle.py qui attend deux inputs : la largeur puis la hauteur.
# Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
# - des “|” pour dessiner les côtés droite et gauche
# - des “-” pour dessiner le haut et le bas
# - des espaces pour remplir le rectangle

# version turtle.py 1.0.0
# import turtle
# largeur = int(input("Largeur : "))
# hauteur = int(input("Hauteur : "))

# # Programme pour dessiner un carré avec turtle
# tur = turtle.Turtle()

# tur.forward(largeur)  # Forward turtle de 100 unités
# tur.left(90)  # rotation de turtle de 90 degrés
# tur.forward(hauteur)
# tur.left(90)
# tur.forward(largeur)
# tur.left(90)
# tur.forward(hauteur)
# tur.left(90)

largeur = int(input("Entrez la largeur du rectangle : "))
hauteur = int(input("Entrez la hauteur du rectangle : "))

# Dessiner la première ligne
print("+" + "-" * (largeur - 2) + "+")

# Dessiner les lignes intermédiaires
for i in range(hauteur - 2):
    print("|" + " " * (largeur - 2) + "|")

# Dessiner la dernière ligne
print("+" + "-" * (largeur - 2) + "+")
