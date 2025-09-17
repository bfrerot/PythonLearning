########## DICTIONARY ##########


### Dictionaries are unordered, changeable (mutable), and indexed collections of data.
# In Python 3.6x dictionaries have become ordered by default.

## A dictionary is a set of key-value pairs
#  1- each key must be unique - it's not possible to have more than one key of the same value
#  2- a key may be data of any type: it may be a number (integer or float), or even a string
#  3- a dictionary is not a list - a list contains a set of numbered values, while a dictionary holds pairs of values
#  4- the len() function works for dictionaries, too - it returns the numbers of key-value pairs in the dictionary
#  5- a dictionary is a one-way tool - if you have an English-French dictionary, you can look for French equivalents of English terms
# but not vice versa
#  6- fully mutable meaning you can modify delete and add values


### create dictionaries

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict)
# {'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
print(phoneNumbers)
# {'Suzy': 5557654321, 'boss': 5551234567}
print(emptyDictionary)
# {}


### Penser à définir les variables au préalable avant de mettre dans la liste sinon NameError
# les keys doivent etre des strings ou numbers par exemple; si variable, il faut la définir avant
myDictionary = {
    key1 : value1,
    key2 : value2,
    key3 : value3,
    }
# NameError: name 'key1' is not defined
value1 = 1
value2 = 2
value3 = 3
myDictionary = {
    "key1" : value1,
    "key2" : value2,
    "key3" : value3,
    }
print(myDictionary)
# {'key1': 1, 'key2': 2, 'key3': 3}


### une paire key/value peut etre comparée à une liste

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


### retrouver des items : mentionner la clé

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}
print(dict['cat'])
# chat
print(phoneNumbers['Suzy'])
# 22657854310

# PAS d'indexation !
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
print(phoneNumbers[1])
# KeyError

# PAS PLUS D'1 KEY
data = {'a': 1, 'b': 2, 'c': 3}
print(data['a', 'b']) # les key a et b
# KeyError: ('a', 'b')


### for + dictionnaire

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


### modifier une value

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['cat'] = 'minou'
print(dict)
# {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}


### ajouter un item

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict['swan'] = 'cygne'
print(dict)
# {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'} # ajoute à la fin


### delete une key

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
del dict['dog']
print(dict)
# {'cat': 'chat', 'horse': 'cheval'}


## removes the dictionary
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
del dict
print(dict)
# NameError


## 1 = 1.0 =! "1"
data = {}
data[1] = 1
data['1'] = 2
data[1.0] = 4  # ici data[1] = data[1.0] donc 1 est écrasé par 4
print(data)
# {1: 4, '1': 2}
res = 0
for d in data:
    res += data[d]
print(res)
# 6


### copy between dictionaries

# SHALLOW copy

import copy

a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1964)', 'You Only Live Twice']
    }
b_dict = (a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
# Memory chunks: 2452251144960 2452251144960

print('Same memory chunk?', a_dict is b_dict)
# Same memory chunk? True

a_dict['movies'].append('Diamonds Are Forever (1971)')
print('a_dict movies:', a_dict['movies'])
# a_dict movies: ['Goldfinger (1964)', 'You Only Live Twice', 'Diamonds Are Forever (1971)']
print('b_dict movies:', b_dict['movies'])
# b_dict movies: ['Goldfinger (1964)', 'You Only Live Twice', 'Diamonds Are Forever (1971)'] 
 
# DEEP copy

import copy

a_dict = {
    'first name': 'James',
    'last name': 'Bond',
    'movies': ['Goldfinger (1964)', 'You Only Live Twice']
    }
b_dict = copy.deepcopy(a_dict)
print('Memory chunks:', id(a_dict), id(b_dict))
# Memory chunks: 2349147026176 2349144587520

print('Same memory chunk?', a_dict is b_dict)
# Same memory chunk? False

a_dict['movies'].append('Diamonds Are Forever (1971)')
print('a_dict movies:', a_dict['movies'])
# a_dict movies: ['Goldfinger (1964)', 'You Only Live Twice', 'Diamonds Are Forever (1971)']
print('b_dict movies:', b_dict['movies'])
# b_dict movies: ['Goldfinger (1964)', 'You Only Live Twice']

