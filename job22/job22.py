# Job 22 : Chaîne de caractères

# Créer un programme job22.py. Il devra prendre un premier input qui sera une chaine de
# caractère, puis un deuxième. Si le deuxième input est :
# - “upper” : une fonction “myUper” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en majuscule.
# - “lower” : une fonction “myLower” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en minuscule.
# - “title” : une fonction “myTitle” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne avec une majuscule
# au début de chaque mot.
# - “clean” : une fonction “myClean” devra être appellée. Cette fonction prend en
# paramètre une chaine de caractère, et retourne cette chaîne en enlevant tous les
# espaces inutiles (en début et en fin de chaine de caractère, et les doubles
# espaces).
# Aucune fonction system n’est autorisée. Vous pouvez cependant les tester afin d’étudier
# leur fonctionnement.
# A la fin de votre programme, la chaine de caractère retournée par la fonction devra être
# affichée sur le terminal.

str = input("Entrez une chaine de caractère : ")
f = input("choix de fonction (upper,lower,title,clean) : ")


# -------------------------------Majususcule------------------------------->
def myUper(str):
    # str = input("Enter the String(Upper case):")
    i = 0
    ch2 = ''

    while str[i:]:
        ch = ord(str[i])
        if ch > 96 and ch < 123:
            ch2 += chr(ch-32)
        else:
            ch2 += chr(ch)
        i += 1
    print("en MMajuscule:", ch2)
# -------------------------------Minuscule------------------------------->


def myLower(str):
   # str = input("Enter the String(Upper case):")
    i = 0
    ch2 = ''

    while str[i:]:
        ch = ord(str[i])
        if ch > 64 and ch < 91:
            ch2 += chr(ch+32)
        else:
            ch2 += chr(ch)
        i += 1
    print("en minuscule:", ch2)

# -------------------------------TITLE------------------------------->


def myTitle(str):
    words = str.split()
    titleString = ""
    for word in words:
        titleWord = word[0].upper() + word[1:]
        titleString += titleWord + " "
    return titleString.strip()
# -------------------------------CLEAN------------------------------->


def myClean(str):
    return str.replace(" ", "")


if f == "upper":
    print(myUper(str))
elif f == "lower":
    print(myLower(str))

elif f == "title":
    print(myTitle(str))

elif f == "clean":
    print(myClean(str))


else:
    print("fonction invalide")
