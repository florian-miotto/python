# Créer un programme job23.py qui demandera à l’utilisateur de renseigner un mot et un
# seul, sans espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent
# ni majuscule).

# Votre programme devra modifier ce mot, en y changeant de place certains caractères
# (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
# renseigné par l'utilisateur.
# Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
# alphabétique, du mot original !

def input_word():
    word = input("Entrez un mot sans espaces ni caractères spéciaux : ")
    if not word.isalpha() or not word.islower():
        print("Le mot doit être composé uniquement de lettres de l'alphabet sans accent ni majuscules.")
        return input_word()
    else:
        return word


def rearrange_word(word):
    letters = list(word)
    for i in range(len(letters)-1, 0, -1):

        if letters[i] != letters[i-1]:

            old_ascii = ord(letters[i])
            new_ascii = old_ascii
            while new_ascii == old_ascii:
                new_ascii += 1
            letters[i] = chr(new_ascii)
            letters[i:] = sorted(letters[i:])
            break
    new_word = ''.join(letters)
    return new_word


word = input_word()
new_word = rearrange_word(word)
print(f"Le mot '{word}' réarrangé est '{new_word}'.")
