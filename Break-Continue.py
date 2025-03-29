##########  break  ##########

# pour sortir complètement de la boucle

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    if letter == " ":
        letter = "_"
    print(letter, end="")
#OpenEDG_





##########  continue  ##########

# pour ignorer l'occurence si elle match le if

user_word = input("Give me a word: ")
user_word = user_word.upper()  # Convertir en majuscules
forbidden_letter = ['I', 'O', 'U', 'E', 'A']  # Liste des lettres interdites

result = ""  # Variable pour stocker le mot sans les lettres interdites

for letter in user_word: 
    if letter not in forbidden_letter:  # On garde les lettres non interdites
        result += letter
    else:
        continue # ici rien après donc on repart à la prochaine occurence "letter"

print(result)