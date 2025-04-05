### METHODS LISTS ###

# lister les methodes dispo pour une list
dir(interfaces)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
'sort']

## list.index

spam = ['hello', 'hi', 'howdy', 'heyas'] 
print (spam.index('hello'))
0

# if same value many times in a list, ONLY the first is taken in account

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka'] 
spam.index('Pooka')
1


## list.append()
# ajoute un element a la fin de la list

list=[777, 2, 3, 4, 5, 6]
list.append(7)
new_list
print(list)
# [777, 2, 3, 4, 5, 6, 7]

spam = ['cat', 'dog', 'bat'] 
spam.append('moose')
print (spam)
['cat', 'dog', 'bat', 'moose']


## list.clear()
# supprime tous les éléments d'une liste
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# []


## list.copy()
# copie les éléments d'une liste dans une autre
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
# ["apple", "banana", "cherry"]


## list.count()
# compte le nombre d'occurence dans la liste de la variable spécifiée
fruits = ["apple", "banana", "cherry"]
x = fruits.count("apple")
print(x)
# 1
# OBLIGATOIRE de spécifier une variable
fruits = ["apple", "banana", "cherry"]
x = fruits.count()
print(x)
# Traceback (most recent call last):
#  File "./prog.py", line 3, in <module>
# TypeError: list.count() takes exactly one argument (0 given)


## list.extend()
# rajoute des valeurs en fin de list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
# ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']





## list.insert(index,"string")

spam = ['cat', 'dog', 'bat'] 
spam.insert(1, 'chicken') 
print (spam)
['cat', 'chicken', 'dog', 'bat']

 
#Note the spam = spam.insert() or spam>append() value is None


## list.remove

spam = ['cat', 'bat', 'rat', 'elephant'] 
spam.remove('bat') 
print (spam)
['cat', 'rat', 'elephant']

# if same value many times in a list, ONLY the first is taken in account

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
for cat in spam:
    spam.remove('cat')
print (spam)
['bat', 'rat', 'hat']


## list.sort

classer les elem en ordre croissant

PYTHON2
si list contient str et int, les int seront avant les str
spam = ['cat', 1, 'rat', 2,'cat',3,  'cat'] 
spam.sort()
print (spam)
[1, 2, 3, 'cat', 'cat', 'cat', 'rat']
NE MARCHE PAS EN PYTHON3 !!!

ou en decroissant avec sort(reverse=True)
spam = ['cat', 'rat', 'cat', 'cat'] 
spam.sort(reverse=True)
print (spam)
['rat', 'cat', 'cat', 'cat']

les str en MAJ sont avant les str en min
spam = ['a', 'z', 'A', 'Z'] 
spam.sort() 
print(spam) 
['A', 'Z', 'a', 'z']

UTILISER key=str.lower pour classer par ordre alphabetique, min/MAJ

spam = ['a', 'z', 'A', 'Z'] 
spam.sort(key=str.lower) 
print(spam)
['a', 'A', 'z', 'Z']


# Convertir en list

list(('cat', 'dog', 5)) # tuple en list
['cat', 'dog', 5] 

list('hello') # string en list
['h', 'e', 'l', 'l', 'o']



