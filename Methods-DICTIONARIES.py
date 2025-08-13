########## METHODS DICTIONARIES ##########


## .clear()
# delete tous les items
polEngDict = {1:"imane",2:"ouweys",3:"soumaya"}
polEngDict.clear()
print(polEngDict)
# {}



## .copy() 
# Copier un dictionnaire
myDict = {"A":1, "B":2}
copyDict = myDict.copy()
print(copyDict)
# {'A': 1, 'B': 2}



## .fromkeys()

x = ('key1', 'key2', 'key3')
y = ["un", "deux","trois"]
thisdict = dict.fromkeys(x, y)
print(thisdict)
# {'key1': ['un', 'deux', 'trois'], 'key2': ['un', 'deux', 'trois'], 'key3': ['un', 'deux', 'trois']}

x = ('key1', 'key2', 'key3')
y = ("un", "deux","trois")
thisdict = dict.fromkeys(x, y)
print(thisdict)
# {'key1': ['un', 'deux', 'trois'], 'key2': ['un', 'deux', 'trois'], 'key3': ['un', 'deux', 'trois']}

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
# {'key1': 0, 'key2': 0, 'key3': 0}

# si on ne spécifie qu'un parameter, il sera utilisé pour les KEY et la VALUE sera None
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x)
print(thisdict)
# {'key1': None, 'key2': None, 'key3': None}



## .get(value, default si non existent)

picnicItems = {'apples': 5, 'cups': 2} 
print ('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.') # cups dans dict et = 2
# I am bringing 2 cups.
print ('I am bringing ' + str(picnicItems.get('eggs', 100)) + ' eggs.') # eggs absent donc par défaut = 100
# I am bringing 100 eggs.



## .items()
# par item on entend paire key/value

spam = {'color': 'red', 'age': 42}
for i in spam.items():    
    print(i)
# ('color', 'red') 
# ('age', 42)



## .keys()

spam = {'color': 'red', 'age': 42}
for k in spam.keys():    
    print(k)
# color
# age 

dict = {"horse" : "cheval", "dog" : "chien", "cat" : "chat"}
for key in sorted(dict.keys()):
    print(key, "->", dict[key])
# cat -> chat
# dog -> chien
# horse -> cheval



## .pop(value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print (car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
car.pop("model")
print(car)
# {'brand': 'Ford', 'year': 1964}



## .popitem()
# SANS parameter
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
dict.popitem() # delete le dernier item MAIS AVANT PYTHON 3.6.7, REMOVE UN AU HASARD !!!!
print(dict)  
# {'cat' : 'chat', 'dog' : 'chien'}

# on peut récupérer la valeur du popitem
ui_elements = dict([('radio_button', 2),('text_box', 3),('standard_button', 5)])
popped_element = ui_elements.popitem()
print(list(popped_element))
# ['standard_button', 5]



## setdefault()
# Si key existe, setdefault() retourne sa valeur sans modifier le dictionnaire, meme si VALEUR = None
# Si key n'existe pas, setdefault() ajoute key avec default_value et renvoie default_value

car = {
  "brand": "Ford",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
# Bronco
print(car)
{'brand': 'Ford', 'year': 1964, 'model': 'Bronco'}

car = {
  "brand": "Ford",
  "model": None,
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
None
print(car)
{'brand': 'Ford', 'model': None, 'year': 1964}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
# Mustang
print(car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



## .update()
# update un dict avec un autre
polEngDict = {"kwiat" : "flower"}
add = {"gleba" : "soil"}
polEngDict.update(add) 
print(polEngDict)
# {'kwiat': 'flower', 'gleba': 'soil'}



## .values()

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for english, french in dict.values(): # value = 1 - NE MARCHE PAS si on donne un couple (item)
    print(english, "->", french)
# ValueError: too many values to unpack (expected 2)

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
for french in dict.values():
    print(french)
# chat
# chien
# cheval