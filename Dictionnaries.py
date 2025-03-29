#  ------- DICTIONNARIES -------

# Dictionaries are unordered, changeable (mutable), and indexed collections of data.
# *In Python 3.6x dictionaries have become ordered by default.

# A dictionary is a set of key-value pairs
#  1- each key must be unique - it's not possible to have more than one key of the same value;
#  2- a key may be data of any type: it may be a number (integer or float), or even a string;
#  3- a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values;
#  4- the len() function works for dictionaries, too - it returns the numbers of key-value elements in the dictionary;
#  5- a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms,
# but not vice versa.
#  6- fully mutable meaning you can modify and add values


# create dictionaries

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict)
print(phoneNumbers)
print(emptyDictionary)
{'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
{'Suzy': 5557654321, 'boss': 5551234567}
{}

OU 

##### ne marche pas, key1 is undefined #####
myDictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3,
    }
#################


# !! une value peut etre une liste

colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
white : (255, 255, 255)
grey : (128, 128, 128)
red : (255, 0, 0)
green : (0, 128, 0)	

# retrouver des items
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict['cat'])
print(phoneNumbers['Suzy'])
chat
22657854310


# creer un dictionnaire
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")
cat -> chat
lion is not in dictionary
horse -> cheval


# printer par ordre alphabetique
dict = {"horse" : "cheval", "dog" : "chien", "cat" : "chat"}
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
cat -> chat
dog -> chien
horse -> cheval


# methods .values et items
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for english, french in dict.items(): # item = pair key/value
    print(english, "->", french)
cat -> chat
dog -> chien
horse -> cheval

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for english, french in dict.values(): # value = 1 - NE MARCHE PAS si on donne un couple (item)
    print(english, "->", french)
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    for english, french in dict.values(): 
ValueError: too many values to unpack (expected 2

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for french in dict.values():
    print(french)
cheval
chien
chat


# modifier une value
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['cat'] = 'minou'
print(dict)
{'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}


# ajouter un item
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['swan'] = 'cygne'
print(dict)
{'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}


# update()

polEngDict = {"kwiat" : "flower"}
polEngDict.update("gleba" : "soil") # ERROR avec les :  ne marche pas
print(polEngDict)    

polEngDict = {"kwiat" : "flower"}
add = {"gleba" : "soil"}
polEngDict.update(add) 
print(polEngDict)
{'kwiat': 'flower', 'gleba': 'soil'}

OU

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}
for item in (d1, d2):
    d3.update (item)
print(d3)
{'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}


# deleter une key
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
del dict['dog']
print(dict)
{'cat': 'chat', 'horse': 'cheval'}

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict.popitem() # delete le dernier item MAIS AVANT PYTHON 3.6.7, REMOVE UN AU HASARD !!!!
print(dict)  
{'cat' : 'chat', 'dog' : 'chien'}


# delete tous les items
polEngDict.clear() 


# removes the dictionary
del polEngDict    


# Copier un dictionnaire -- !!! Contrairement aux list, les dictionnaires seront independants entre eux apres avoir ete copies
copyDict = polEngDict.copy()

myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()
print(copyMyDict)
{'A': 1, 'B': 2}


# Calculer la moyenne des eleves par ordre alphabetique

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

Enter the student's name (or type exit to stop): imane
Enter the student's score (0-10): 8
Enter the student's name (or type exit to stop): ouweys
Enter the student's score (0-10): 7
Enter the student's name (or type exit to stop): soumaya
Enter the student's score (0-10): 9
Enter the student's name (or type exit to stop): imane
Enter the student's score (0-10): 7
Enter the student's name (or type exit to stop): ouweys
Enter the student's score (0-10): 10
Enter the student's name (or type exit to stop): soumaya
Enter the student's score (0-10): 7
Enter the student's name (or type exit to stop): exit
{'imane': (8, 7), 'ouweys': (7, 10), 'soumaya': (9, 7)}
imane : 7.5
ouweys : 8.5
soumaya : 8.0



# Associer une value a une variable

polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"] # indexation
print(item1)    
soil
item2 = polEngDict.get("woda") # get() method
print(item2)    
water


# Creer une liste d anniversaire et mettre a jour si nom/date manquant

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


# Creer un TicTacToe - mais bug = on peut ecraser les cases 0 et X entre elles..

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',            
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']) 
turn = 'X' 
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?') 
    move = input()
    theBoard[move] = turn 
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X' 
printBoard(theBoard)
| | 
-+-+-
 | | 
-+-+-
 | | 
Turn for X. Move on which space?
top-L
X| | 
-+-+-
 | | 
-+-+-
 | | 
Turn for O. Move on which space?
top-L
O| | 
-+-+-
 | | 
-+-+-
 | | 
Turn for X. Move on which space?
#etc


# Faire un inventaire des produits qu apportent les invites a un picnic

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
Number of things being brought:
 - Apples 7
 - Cups 3
 - Cakes 0
 - Ham Sandwiches 3
 - Apple Pies     1


 ### METHODS DICTIONARIES ###

# dict.values()

spam = {'color': 'red', 'age': 42} 
for v in spam.values():       
   print(v)
red 
42


# dict.keys()

spam = {'color': 'red', 'age': 42}
for k in spam.keys():    
    print(k)
color
age 


#dict.items()
spam = {'color': 'red', 'age': 42}
for i in spam.items():    
    print(i)
('color', 'red') 
('age', 42)


# dict.get

picnicItems = {'apples': 5, 'cups': 2} 
print ('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') 
print ('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
I am bringing 2 cups.
I am bringing 0 eggs. # comme eggs n est pas dans le dictionnaire, le get reourne un 0 par defaut


# dict.setdefault()

## compter le nombre de caracteres dans un string ou phrase
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
s': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}


# pprint.pprint() - pretty print

permet de classer la date en ordre alaphabetique et 1 item par ligne


import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.print(count)
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}


# Pour afficher tous les couples key/value
device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
device.pop('os') # on enlève "os" et sa valeur du dictionnaire --> device = {'hostname': 'router1', 'vendor': 'juniper'}
oper = dict(cpu='5%', memory='10%') # on créée un dictionnaire --> oper = {'cpu': '5%', 'memory': '10%'}
print(oper)
device.update(oper) # on ajoute des données au dictionnaire --> device = {'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}
print(device)
for key, value in device.items():
    print(key + ': ' + value)
#{'cpu': '5%', 'memory': '10%'}
#{'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}
#hostname: router1
#vendor: juniper
#cpu: 5%
#memory: 10%

