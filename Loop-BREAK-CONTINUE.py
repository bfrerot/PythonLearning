##########  BREAK ##########

# pour sortir TOUT D SUITE ET COMPLETEMENT de la boucle

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    if letter == " ":
        letter = "_"
    print(letter, end="")
#OpenEDG_



##########  CONTINUE  ##########

# pour IGNORER l'occurence si elle matche le if

user_word = input("Give me a word: ") # Benoit
user_word = user_word.upper()  # Benoit ==> BENOIT
forbidden_letter = ['I', 'O', 'U', 'E', 'A']  # Liste des lettres interdites

result = ""  # Variable pour stocker le mot sans les lettres interdites

for letter in user_word: 
    if letter not in forbidden_letter:  # On garde les lettres non interdites
        result += letter
    else:
        continue # ici rien après donc on repart à la prochaine occurence "letter"

print(result)
# BNT