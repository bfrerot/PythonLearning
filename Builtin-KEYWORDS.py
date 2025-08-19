########## PYTHON KEY WORDS ##########


### and 
# opérateur logique

a = 5
b = 10
if a > 0 and b > 0:
    print("Les deux sont positifs")
# Les deux sont positifs



### as 
# pour créer un alias

import math as m
print(m.sqrt(16))



### assert
# pour déboguer

x = 10
assert x > 5 # x doit être supérieur à 5



### break 
# pour sortir d'une boucle

for i in range(5):
    if i == 3:
        break
    print(i)



### class 
# pour définir une class

class Person:
    def __init__(self, name):
        self.name = name



### continue 
# pour passer à l'itération suivante

for i in range(5):
    if i == 2:
        continue
    print(i)



### def 
# pour définir une fonction

def add(a, b):
    return a + b



### del 
# pour supprimer un objet

x = [1, 2, 3]
del x
x = [1, 2, 3]
del x[0]
print(x)
# [2, 3]

x = "string"
del x
x = "string"
del x[0]
# TypeError: 'str' object doesn't support item deletion

x = {1,2,3}
del x[0]
# TypeError: 'set' object doesn't support item deletion
x = {1,2,3}
del x

x = {1:"a",2:"b",3:"c"}
del x
x = {1:"a",2:"b",3:"c"}
del x[2]
print(x)
{1: 'a', 3: 'c'}

x = (1,2,3)
del x
x = (1,2,3)
del x[1]
# TypeError: 'tuple' object doesn't support item deletion



### elif 
# condition supplémentaire

x = 10
if x > 0:
    print("Positif")
elif x == 0:
    print("Zéro")



### else 
# condition alternative

x = -1
if x > 0:
    print("Positif")
else:
    print("Négatif ou zéro")



### except 
# gérer une exception

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division par zéro détectée")



### False 
# valeur booléenne

print(3 > 5)  # False



### finally 
# exécuter du code après try...except
# RAPPEL, s'excute avant le return si return dans try ou except car dans un try, rien ne se passe plus après un return

try:
    print(10 / 0)
    
except ZeroDivisionError:
    print("Erreur")
    
finally:
    print("Fin du traitement")
# Erreur
# Fin du traitement



### for 
# boucle for

for i in range(3):
    print(i)



### from 
# importer une partie d’un module

from math import pi
print(pi)



### global 
# déclarer une variable globale

x = 5
def test():
    global x
    x = 10
test()
print(x)



### if

x = 7
if x > 5:
    print("x est supérieur à 5")



### import

import math
print(math.sqrt(9))



### in 
# vérifier la présence dans une collection

list = [1, 2, 3]
print(2 in list)  
# True



### is
# To test if two variables are equal
p = 10
q = 10
print (p is q) # égal à (p==q)
# True

# cas des list
lst1 = [2,4,6]
lst2 = [2,4,6]
print(lst1 is lst2)
print(lst1 == lst2)
False
True



## lambda 
# fonction anonyme

square = lambda x: x * x
print(square(4))



### None 
# valeur nulle

x = None
print(x)



### nonlocal 
# déclarer une variable non locale

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)
outer()



### not 
# opérateur logique

x = True
print(not x)  # False



### or 
# opérateur logique

a = False
b = True
if a or b:
    print("Au moins un est vrai")



### pass 
# ne rien faire

def fonction_vide():
    pass



### raise 
# lancer une exception

def verifier_age(age):
    if age < 18:
        raise ValueError("Âge insuffisant")
verifier_age(16)



### return 
# renvoyer une valeur depuis une fonction

def double(x):
    return x * 2
print(double(3))



### True 
# valeur booléenne

print(4 > 2)  # True



### try 
# gestion d’erreur

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Erreur capturée")



### while 
# boucle while

i = 0
while i < 3:
    print(i)
    i += 1



### with 
# gestion automatique des ressources

with open('fichier.txt', 'r') as fichier:
    contenu = fichier.read()



### yield 
# générateur

def compteur():
    for i in range(3):
        yield i
for nombre in compteur():
    print(nombre)