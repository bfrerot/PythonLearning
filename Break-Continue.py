##########  break  ##########







##########  continue  ##########

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