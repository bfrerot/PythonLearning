wordwithoutvowel=''
userword = input('Please enter any word: ')
print (userword)
userword = userword.upper()
print (userword)
for letter in userword:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordwithoutvowel = wordwithoutvowel + letter
        # ou print letter si on veut les afficher une par une en sautant un eligne à chaque fois

print (wordwithoutvowel)