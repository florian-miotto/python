# Écrire un programme job10.py qui demande à l’utilisateur d’entrer un texte. Le
# programme devra récupérer ce texte, et l’écrire dans un fichier “output.txt”.
# Écrire un programme qui lit le contenu de fichier “output.txt”, et qui l’écrit dans le
# terminal.

text = input("Entrez un texte : ")
fichier = open("output.txt", "w")
fichier.write(text)
fichier.close()
print("Le texte a été écrit dans le fichier output.txt")
f = open("output.txt", "r")
print(f.read())
