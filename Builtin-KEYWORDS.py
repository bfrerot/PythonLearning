########## PYTHON KEY WORDS ##########


### and 

a = 5
b = 10
if a > 0 and b > 0:
    print("Les deux sont positifs")
# Les deux sont positifs



### as 
# to create an alias

import math as m
print(m.sqrt(16))



### assert
# assertion

x = 10
assert x > 5 # x doit être supérieur à 5



### break 
# to exit completely from a loop

for i in range(5):
    if i == 3:
        break
    print(i)



### class 
# to create a class

class Person:
    def __init__(self, name):
        self.name = name



### continue 
# to go to next iteration

for i in range(5):
    if i == 2:
        continue
    print(i)
0
1 
#   if i == 2 means here we do not print it
3
4


### def 
# to create a function

def add(a, b):
    return a + b



### del 
# to delete an object, or an index when iterable + support for index manipulation

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
# conditionning

x = 10
if x > 0:
    print("Positif")
elif x == 0:
    print("Zéro")



### else 
# conditionning

x = -1
if x > 0:
    print("Positif")
else:
    print("Négatif ou zéro")



### except 
# exception management

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division par zéro détectée")



### False 
# boolean
# False = 0

print(3 > 5)  # False



### finally 
# excepetion managment, final action
# REMINDER, applies BEFORE any return which would be present in try ou except, because nothing occurs after a return

try:
    print(10 / 0)
    
except ZeroDivisionError:
    print("Error")
    
finally:
    print("The end")
# Error
# The end



### for 
# loop

for i in range(3):
    print(i)
0
1
2
print(i) # REMINDER: i will keep its last invoked value
2


### from 
# module management

from math import pi
print(pi)



### global 
# declare a variable in global scope

x = 5
def test():
    global x
    x = 10
test()
print(x)



### if

x = 7
if x > 5:
    print("x i greater than 5")
# x i greater than 5



### import

import math
print(math.sqrt(9))
3



### in 
# check item presence into a collection

list = [1, 2, 3]
print(2 in list)  
# True



### is
# To test if two variables are equal
p = 10
q = 10
print (p is q) # equal to (p==q) if str, number, tuple BUT NOT EQUAL if LIST,SET,DICT
# True

# list
lst1 = [2,4,6]
lst2 = [2,4,6]
print(lst1 is lst2)
print(lst1 == lst2)
False
True



### lambda 
# anonymous function

square = lambda x: x * x
print(square(4))



### None 
# null value

x = None
print(x)



### nonlocal 
# declare a non-local variable

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)
outer()



### not 

x = True
print(not x)  # False



### or 

a = False
b = True
if a or b:
    print("Au moins un est vrai")



### pass 
# do nothing

def fonction_vide():
    pass



### raise 
# force an exception to occur

def check_age(age):
    if age < 18:
        raise ValueError("You are not old enough")
check_age(16)



### return 
# send back a output from a function

def double(x):
    return x * 2
print(double(3))



### True 
# bool
# True = 1

print(4 > 2)  # True



### try 
# exception management

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Matched error")



### while 
# loop

i = 0
while i < 3:
    print(i)
    i += 1
0
1
2



### with 

with open('fichier.txt', 'r') as fichier:
    contenu = fichier.read()



### yield 
# iterator

def counter():
    for i in range(3):
        yield i
for number in counter():
    print(number)