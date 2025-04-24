########## DICTIONNARIES

## Dictionaries are unordered, changeable (mutable), and indexed collections of data.
# *In Python 3.6x dictionaries have become ordered by default.

## A dictionary is a set of key-value pairs
#  1- each key must be unique - it's not possible to have more than one key of the same value;
#  2- a key may be data of any type: it may be a number (integer or float), or even a string;
#  3- a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
#  4- the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
#  5- a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms,
# but not vice versa.
#  6- fully mutable meaning you can modify delete and add values


## create dictionaries

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict)
print(phoneNumbers)
print(emptyDictionary)
# {'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
# {'Suzy': 5557654321, 'boss': 5551234567}
# {}


## Penser à définir les variables au préalable avant de mettre dans la liste sinon error
myDictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3,
    }
# NameError: name 'key1' is not defined


## une paire clé/value peut etre une liste

colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
# white : (255, 255, 255)
# grey : (128, 128, 128)
# red : (255, 0, 0)
# green : (0, 128, 0)	


## retrouver des items : mentionner la clé

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict['cat'])
print(phoneNumbers['Suzy'])
# chat
# 22657854310


## creer un dictionnaire

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")
# cat -> chat
# lion is not in dictionary
# horse -> cheval


## printer par ordre alphabetique

dict = {"horse" : "cheval", "dog" : "chien", "cat" : "chat"}
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
# cat -> chat
# dog -> chien
# horse -> cheval


## modifier une value

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['cat'] = 'minou'
print(dict)
# {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}


# ajouter un item

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['swan'] = 'cygne'
print(dict)
# {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}


## deleter une key

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
del dict['dog']
print(dict)
# {'cat': 'chat', 'horse': 'cheval'}


## removes the dictionary

del polEngDict    


## Calculer la moyenne des eleves par ordre alphabetique

schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)
        
print (schoolClass)

for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)

# Enter the student's name (or type exit to stop): imane
# Enter the student's score (0-10): 8
# Enter the student's name (or type exit to stop): ouweys
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): soumaya
# Enter the student's score (0-10): 9
# Enter the student's name (or type exit to stop): imane
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): ouweys
# Enter the student's score (0-10): 10
# Enter the student's name (or type exit to stop): soumaya
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): exit
# {'imane': (8, 7), 'ouweys': (7, 10), 'soumaya': (9, 7)}
# imane : 7.5
# ouweys : 8.5
# soumaya : 8.0


## Creer une liste d anniversaire et mettre a jour si nom/date manquant

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays: 
        print(birthdays[name] + ' is the birthday of ' + name)    
    else:     
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')  
        bday = input() 
        birthdays[name] = bday 
        print('Birthday database updated.')
print (birthdays)


## Faire un inventaire des produits qu apportent les invites a un picnic

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},'Bob': {'ham sandwiches': 3, 'apples': 2},'Carol': {'cups': 3, 'apple pies': 1}}
def totalBrought(guests, item):
    numBrought = 0 
    for k, v in guests.items(): 
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups'))) 
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes'))) 
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches'))) 
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
# Number of things being brought:
#  - Apples         7
#  - Cups           3
#  - Cakes          0
#  - Ham Sandwiches 3
#  - Apple Pies     1


# dict.setdefault() + pprint.pprint() - pretty print
# classer et compter des items en ordre alaphabetique et 1 item par ligne

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
# {' ': 13,
#  ',': 1,
#  '.': 1,
#  'A': 1,
#  'I': 1,
#  'a': 4,
#  'b': 1,
#  'c': 3,
#  'd': 3,
#  'e': 5,
#  'g': 2,
#  'h': 3,
#  'i': 6,
#  'k': 2,
#  'l': 3,
#  'n': 4,
#  'o': 2,
#  'p': 1,
#  'r': 5,
#  's': 3,
#  't': 6,
#  'w': 2,
#  'y': 1}