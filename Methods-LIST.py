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


## list.index()
# ~ list.remove 
# donne l'index correspondant à une variable de la list
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.index("cherry")
print(x)
# 2

# si plusieurs occureces identiques, ne prend en compte que le premier
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.index("cherry")
print(x)
# 2


## list.insert(index,"string")
# insère une variable à l'index spécifié
spam = ['cat', 'dog', 'bat'] 
spam.insert(1, 'chicken') 
print (spam)
# ['cat', 'chicken', 'dog', 'bat']

 
## list.pop()
# supprime l'index spécifié
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# ['apple', 'cherry']


## list.remove 
# ~ list.index()
# supprime l'élément spécifié
spam = ['cat', 'bat', 'rat', 'elephant'] 
spam.remove('bat') 
print (spam)
['cat', 'rat', 'elephant']

# if same value many times in a list, ONLY the first is taken in account
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
spam.remove('cat')
print (spam)
# ['bat', 'rat', 'cat', 'hat', 'cat']
# pour contourner il faudra faire une boucle
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
for cat in spam:
    spam.remove('cat')
print (spam)
# ['bat', 'rat', 'hat']


## list.reverse()
# inverse l'ordre de la list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# ['cherry', 'banana', 'apple']


## list.sort
# sort the list alphabetically
# classe les elem en ordre croissant par defaut

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# ['BMW', 'Ford', 'Volvo']
# ou en decroissant avec sort(reverse=True)
spam = ['cat', 'rat', 'cat', 'cat'] 
spam.sort(reverse=True)
print (spam)
# ['rat', 'cat', 'cat', 'cat']

# on ne peut pas mélanger int et str
cars = ['Ford', 23, 'BMW', 4, 'Volvo']
cars.sort()
print(cars)
# Traceback (most recent call last):
#  File "c:\PythonLearning\bac-à-sable.py", line 2, in <module>
#    cars.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
# PS C:\PythonLearning> 
# PYTHON2
si list contient str et int, les int seront avant les str
spam = ['cat', 1, 'rat', 2,'cat',3,  'cat'] 
spam.sort()
print (spam)
[1, 2, 3, 'cat', 'cat', 'cat', 'rat']
# NE MARCHE PAS EN PYTHON3 !!!

# les str en MAJ sont avant les str en min
spam = ['a', 'z', 'A', 'Z'] 
spam.sort() 
print(spam) 
['A', 'Z', 'a', 'z']

# list.sort(key=?)
# Ex1
# UTILISER key=str.lower pour classer par ordre alphabetique, min/MAJ
spam = ['a', 'z', 'A', 'Z'] 
spam.sort(key=str.lower) 
print(spam)
# ['a', 'A', 'z', 'Z']
# Ex2
# .sort les éléments d'une list en fonction de la length
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
# ['VW', 'BMW', 'Ford', 'Mitsubishi']