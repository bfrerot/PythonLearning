########## METHODS DICTIONARIES ##########


## .clear()
# delete tous les items

polEngDict.clear() 


## .copy() 
# Copier un dictionnaire -- 
# !!! Contrairement aux list, les dictionnaires seront independants entre eux apres avoir ete copiés

copyDict = polEngDict.copy()

myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()
print(copyMyDict)
# {'A': 1, 'B': 2}


## .fromkeys()

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
# {'key1': 0, 'key2': 0, 'key3': 0}


## .get

picnicItems = {'apples': 5, 'cups': 2} 
print ('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') 
print ('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
# I am bringing 2 cups.
# I am bringing 0 eggs. # comme eggs n est pas dans le dictionnaire, le get reourne un 0 par defaut


## .items()

spam = {'color': 'red', 'age': 42}
for i in spam.items():    
    print(i)
('color', 'red') 
('age', 42)


## .keys()

spam = {'color': 'red', 'age': 42}
for k in spam.keys():    
    print(k)
# color
# age 


## .pop()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print (car)
car.pop("model")
print(car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# {'brand': 'Ford', 'year': 1964}


## .popitem()

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict.popitem() # delete le dernier item MAIS AVANT PYTHON 3.6.7, REMOVE UN AU HASARD !!!!
print(dict)  
# {'cat' : 'chat', 'dog' : 'chien'}


## setdefault()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
# Mustang

## compter le nombre de caracteres dans un string ou phrase
message = 'It was a bright cold day in April, and the clocks were striking thirteen.' 
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
# {'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}


## .update()

polEngDict = {"kwiat" : "flower"}
polEngDict.update("gleba" : "soil") # ERROR avec les :  ne marche pas

polEngDict = {"kwiat" : "flower"}
add = {"gleba" : "soil"}
polEngDict.update(add) 
print(polEngDict)
# {'kwiat': 'flower', 'gleba': 'soil'}

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}
for item in (d1, d2):
    d3.update (item)
print(d3)
# {'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}


## .values()

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for english, french in dict.values(): # value = 1 - NE MARCHE PAS si on donne un couple (item)
    print(english, "->", french)
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     for english, french in dict.values(): 
# ValueError: too many values to unpack (expected 2

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for french in dict.values():
    print(french)
# chat
# chien
# cheval