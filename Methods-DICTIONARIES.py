### METHODS DICTIONARIES ###


# lister les methodes dispo pour les dictionaries
device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}

dir(device)
['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys',
'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values',
'viewitems', 'viewkeys', 'viewvalues']


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


# .pop() & .update() 
device = {'hostname': 'router1', 'vendor': 'juniper', 'os': '12.1'}
device.pop('os')
oper = dict(cpu='5%', memory='10%')
print(oper)
device.update(oper)
print(device)

{'cpu': '5%', 'memory': '10%'}
{'hostname': 'router1', 'vendor': 'juniper', 'cpu': '5%', 'memory': '10%'}