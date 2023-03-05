# Ouvrir le fichier contenant le dictionnaire
with open('dico_france.txt', 'r') as f:
    dictionary = [line.strip() for line in f]

# Définir les points pour chaque lettre
points = {
    letter: 1 for letter in 'AEINORSTUL'
}
points.update({
    letter: 2 for letter in 'DG'
})
points.update({
    letter: 3 for letter in 'BCP'
})
points.update({
    letter: 4 for letter in 'FHV'
})
points.update({
    letter: 8 for letter in 'JQ'
})
points.update({
    letter: 10 for letter in 'KWXYZ'
})

letters = input("Entrez les lettres (sans espaces ni caractères spéciaux) : ")
letters = letters.lower()

if not letters.isalpha():
    print("Erreur : l'entrée doit contenir uniquement des lettres.")
    exit()

# Chercher les mots possibles et calculer les points
word_scores = {}
for word in dictionary:
    if len(word) >= 2 and all(letter in letters for letter in word):
        score = sum(points[letter.upper()] for letter in word)
        word_scores[word] = score

# Afficher les mots par ordre décroissant de points
for word, score in sorted(word_scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{word} : {score} points")
    

