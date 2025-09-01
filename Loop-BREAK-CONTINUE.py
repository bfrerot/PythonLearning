##########  BREAK ##########

# to exit the loop once for all, definitively

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    if letter == " ":
        letter = "_"
    print(letter, end="")
#OpenEDG_



##########  CONTINUE  ##########

# to ignore the iteration and go to the next

user_word = input("Give me a word: ") # Benoit
user_word = user_word.upper()  # Benoit ==> BENOIT
forbidden_letter = ['I', 'O', 'U', 'E', 'A']  # forbidden letters in a list

result = ""  # to store the final value

for letter in user_word: 
    if letter not in forbidden_letter:  # we keep only non-forbidden letters
        result += letter
    else:
        continue # if letter is a forbidden one, we ignore it

print(result)
# BNT