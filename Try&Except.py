########## Error Handling ##########



# Error will occur wherever it is possible = Murphy law
# Syntax error = code's form not allowed in Python
# Runtime error = error not detectable before start of program

## when code does something wrong Python does stop the program and creates an exception
# = raising an exception    
# if exception is addressed --> program continues
# if nothing is done --> program stops and generate an error


### ERRORS REFs

# --> voir Python_error_tree.mmd pour voir le tree complet

ArithmeticError # any arithmetic error
# BaseException ← Exception ← ArithmeticError 
# including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain

AssertionError 
# BaseException ← Exception ← AssertionError
# concrete exception raised by the assert instruction when its argument evaluates to False,
# None, 0, or an empty string

AttributeError
# when you try to activate a method which doesn't exist in an item you're dealing with
short_list = [1]
short_list.append(2)
print(short_list)
# [1, 2]
short_list.depend(3)
# AttributeError: 'list' object has no attribute 'depend'. Did you mean: 'append'?

BaseException 
# BaseException
# = any error source tree

ImportError
# BaseException ← Exception ← StandardError ← ImportError
# raised when an import operation fails
# One of these imports will fail – which one?
try:
    import math
    import time
    import abracadabra: # will cause an issue
except:
    print('One of your imports has failed.')
# One of your imports has failed.

IndexError 
# BaseException ← Exception ← LookupError ← IndexError
# Lookup error, parent, peut suffir
# index introuvable,inexistant
list = []
x = list[0]
# Traceback (most recent call last):
# ""  File "main.py", line 2, in <module>
#    x = list[0]
# IndexError: list index out of range
##########
my_list = [10, 20, 30]
try:
    value = my_list[5] # Tentative d'accès à un index qui n'existe pas 
except IndexError:
    print("L'index est hors de portée.")
except LookupError:
    print("Erreur de recherche : un index est introuvable.")
#L'index est hors de portée.

KeyboardInterrupt 
# BaseException ← KeyboardInterrupt
# raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs)

KeyError 
# BaseException ← Exception ← LookupError ← KeyError
# when you try to access a collection's non-existent element
dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)
# b
# c
# d
# No such key: d

LookupError 
# BaseException ← Exception ← LookupError
# errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    # Tentative d'accès à une clé qui n'existe pas
    value = my_dict["d"]
except LookupError:
    print("Erreur de recherche : une clé est introuvable.")
# La clé n'existe pas dans le dictionnaire.

MemoryError 
# BaseException ← Exception ← MemoryError
# cannot be completed due to a lack of free memory
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

OverflowError
# BaseException ← Exception ← ArithmeticError ← OverflowError
# when an operation produces a number too big to be successfully stored
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...
from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')
2.718281828459045
7.38905609893065
54.598150033144236
2980.9579870417283
8886110.520507872
78962960182680.69
6.235149080811617e+27
3.8877084059945954e+55
1.5114276650041035e+111
2.2844135865397565e+222
# The number is too big.    

SyntaxError
# raised when the control reaches a line of code which violates Python's grammar
print("Bonjour tout le monde"
# SyntaxError: unexpected EOF while parsing


TypeError
# when you try to apply a data whose type cannot be accepted in the current context
short_list = [1]
one_value = short_list[0.5] # [0.5] cannot be

ValueError # with values which may be inappropriately used in some context
short_list = [1]
one_value = short_list[0.5]


ZeroDivisionError # you cannot divide by 0
# BaseException ← Exception ← ArithmeticError ← ZeroDivisionErro
# si on essaie  de mettre 0 en diviseur avec /, //, ou %
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     value /= 0
#  ZeroDivisionError: division by zero


### Summary of CONCRETE PYTHON EXCEPTIONS

ValueError # raised when a function gets an argument of the right type but inappropriate value (e.g., int("abc"))

TypeError #  wrong data type (e.g., adding a number and a string)

IndexError #  accessing an invalid list index

KeyError #  accessing a non-existent dictionary key

FileNotFoundError #  trying to open a file that doesn't exist

ZeroDivisionError #  division by zero

AttributeError #  trying to access an attribute that doesn’t exist

ImportError # import statement fails

RuntimeError #  generic error detected during runtime





















### try
# avec try, python gere les erreurs

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
# Enter a natural number: 5.0 # on indique 1 valeur autre que int pour générer une erreur
# I do not know what to do.


### try --> except
#des qu il y a un probleme, python cherche un except, 
# s il y en a un, tout le code situe entre l erreur et l except sera ignore

try:
    print("1")
    x = 1 / 0 # error, va aller a except et ignorer print("2")
    print("2") # ignoré
except:
    print("Oh dear, something went wrong...")
print("3")
# 1
# Oh dear, something went wrong...
# 3


### Multi except
# on peut preciser une action differente en fonction de l erreur
# The default except branch must be the last except branch
   
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...") # default except
print("THE END.")

# Enter a number: 0
# You cannot divide by zero, sorry.
# THE END.

# Enter a number: 
# Enter a number: 2.2
# You must enter an integer value.
# THE END.

# Enter a number: 3
# 0.3333333333333333
# THE END.


### on va gerer les erreurs par leur code en leur donnant une porte de sortie
# exemple:

# print(y = 1 / 0)
# ZeroDivisionError: division by zero

# -->
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")
print("THE END.")
# Oooppsss...
# THE END.


try:
    print(y = 1 / 0)
except BaseException:  # on peut remplacer le code d'erreur par n'importe  lequel de ses parents
    print("Oooppsss...")
print("THE END.")


### GOOD PRACTICES

# the order of the branches matters!

 
# don't put more general exceptions before more concrete ones
try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")
# Arithmetic problem!
# THE END.

# this will make the latter one unreachable and useless;
# moreover, it will make your code messy and inconsistent;
# Python won't generate any error messages regarding this issue.

try:
    y = 1 / 0
except ArithmeticError:  # more general exception should not be first
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")
# Arithmetic problem!
# THE END.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
print("THE END.")
# Zero Division!
# THE END.


### on peut mettre plusieurs exceptions dans un except
try:
    y = 1 / 0
except (ZeroDivisionError,ArithmeticError):
    print("Problem!")
print("THE END.")
# Problem!
# THE END.


### on peut inserer les exceptions dans une function

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
badFun(0)
print("THE END.")
# Arithmetic Problem!
# THE END.


### on peut insérer une  function dans un try

def badFun(n):
    return 1 / n
try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print("THE END.")
# What happened? An exception was raised!
# THE END.


### RAISE

# python keyword
# enables to:
#   simulate raising actual exceptions (e.g., to test your handling strategy)
#   partially handle an exception and make another part of the code responsible 
#       for completing the handling (separation of concerns)

def badFun(n):
    raise ZeroDivisionError
try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")
print("THE END.")
# What happened? An error?
# THE END.

def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise # traite le except dessous en plus

try:
    badFun(56)
except ArithmeticError:
    print("I see!")

print("THE END.")
# I did it again!
# I see!
# THE END.

# SANS raise dans la def
# I did it again!
# THE END.


### ASSERT

# you may want to put it into your code where you want to be absolutely safe 
# from evidently wrong data, and where you aren't absolutely sure that the data 
# has been carefully examined before (e.g., inside a function used by someone else)

# raising an AssertionError exception secures your code from producing invalid results, 
# and clearly shows the nature of the failure

# assertions don't supersede exceptions or validate the data 
# they are their supplements.

import math
x = float(input("Enter a number: "))
assert x >= 2.0
x = math.sqrt(x)
print(x)
Enter a number: 2 # match le assert
1.4142135623730951

Enter a number: 1,99 # ne match pas
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    assert x >= 2.0
AssertionError

# pour bien comprendre
def foo(x):
    assert x
    return 1/x
 
try:
    print(foo(0)) # l'assert est levé d'office avant le return 1/x
except ZeroDivisionError: # l'error n''est pas repertoriée telle quelle donc ne matche pas
    print("zero")
except: # matche le par defaut
    print("some")
    
# some