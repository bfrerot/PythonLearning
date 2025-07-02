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
print("Bonjour tout le monde")
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
# Enter a number: 2 # match le assert
1.4142135623730951

# Enter a number: 1,99 # ne match pas
# ..
#     assert x >= 2.0
# AssertionError

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
    
    
    
### FINALLY

# additionnal branch behing the try/Except block

# ex SANS:
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n

print(reciprocal(2))
# Everything went fine
# 0.5
print(reciprocal(0))
# Division failed
# None

# ex AVEC:
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
# Everything went fine
# It's time to say goodbye
# 0.5

# ! à savoir: le finally est toujours exécuté avant que la valeur soit renvoyée à l'appelant. 
# En d'autres termes, le finally est conçu pour s'exécuter juste avant que la fonction ne termine 
# et ne retourne une valeur, même si cette valeur a été spécifiée dans le return avant:

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
        return n
    finally:
        print("It's time to say goodbye")
        return n
        
print(reciprocal(2))
# Everything went fine
# It's time to say goodbye
# 0.5
    
    

### errors are Classes

# ex simple:
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__()) # dans ce cas précis, l'output sera le meme
# invalid literal for int() with base 10: 'Hello!'
# invalid literal for int() with base 10: 'Hello!'


# ex plus compliqué: afficher la hierarchie d'une class d'Error

def print_exception_tree(thisclass, nest = 0): 
# Paramètre thisclass : la classe dont on veut afficher les sous-classes.
# Paramètre nest : indique le niveau d'imbrication pour le rendu graphique (initialement 0)
    if nest > 1:
        print("   |" * (nest - 1), end="") # si plus de 1 sous-class, on met tab "   |" (n-1) fois
    if nest > 0:
        print("   +---", end="") # dès lors qu'on est dans une sous class de la class visée, on ajoute "   +---"

    print(thisclass.__name__) # imprime le nom de la class, sans le .__name__ on aurait "<class 'ImportError'>"

    for s in thisclass.__subclasses__(): # RECURSION, pour chaque subclass de la class visée
        print_exception_tree(s, nest + 1) # la fonction s'appelle elle-même en augmentant nest de 1, cela permet de parcourir toute la hiérarchie

print_exception_tree(ImportError)
# ImportError
#    +---ModuleNotFoundError
#    +---ZipImportError

print_exception_tree(BaseException)
# BaseException
#    +---BaseExceptionGroup
#    |   +---ExceptionGroup
#    +---Exception
#    |   +---ArithmeticError
#    |   |   +---FloatingPointError
#    |   |   +---OverflowError
#    |   |   +---ZeroDivisionError
#    |   +---AssertionError
#    |   +---AttributeError
#    |   +---BufferError
#    |   +---EOFError
#    |   +---ImportError
#    |   |   +---ModuleNotFoundError
#    |   |   +---ZipImportError
#    |   +---LookupError
#    |   |   +---IndexError
#    |   |   +---KeyError
#    |   |   +---CodecRegistryError
#    |   +---MemoryError
#    |   +---NameError
#    |   |   +---UnboundLocalError
#    |   +---OSError
#    |   |   +---BlockingIOError
#    |   |   +---ChildProcessError
#    |   |   +---ConnectionError
#    |   |   |   +---BrokenPipeError
#    |   |   |   +---ConnectionAbortedError
#    |   |   |   +---ConnectionRefusedError
#    |   |   |   +---ConnectionResetError
#    |   |   +---FileExistsError
#    |   |   +---FileNotFoundError
#    |   |   +---InterruptedError
#    |   |   +---IsADirectoryError
#    |   |   +---NotADirectoryError
#    |   |   +---PermissionError
#    |   |   +---ProcessLookupError
#    |   |   +---TimeoutError
#    |   |   +---UnsupportedOperation
#    |   +---ReferenceError
#    |   +---RuntimeError
#    |   |   +---NotImplementedError
#    |   |   +---PythonFinalizationError
#    |   |   +---RecursionError
#    |   |   +---_DeadlockError
#    |   +---StopAsyncIteration
#    |   +---StopIteration
#    |   +---SyntaxError
#    |   |   +---IndentationError
#    |   |   |   +---TabError
#    |   |   +---_IncompleteInputError
#    |   +---SystemError
#    |   |   +---CodecRegistryError
#    |   +---TypeError
#    |   +---ValueError
#    |   |   +---UnicodeError
#    |   |   |   +---UnicodeDecodeError
#    |   |   |   +---UnicodeEncodeError
#    |   |   |   +---UnicodeTranslateError
#    |   |   +---NotShareableError
#    |   |   +---UnsupportedOperation
#    |   +---Warning
#    |   |   +---BytesWarning
#    |   |   +---DeprecationWarning
#    |   |   +---EncodingWarning
#    |   |   +---FutureWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---UnicodeWarning
#    |   |   +---UserWarning
#    |   +---InterpreterError
#    |   |   +---InterpreterNotFoundError
#    |   +---ExceptionGroup
#    +---GeneratorExit
#    +---KeyboardInterrupt
#    +---SystemExit



### Create our own exceptions

# The exceptions hierarchy is neither closed nor finished, and we can always extend it
# It may be useful when we create a complex module which detects errors and raises exceptions, 
#   and we want the exceptions to be easily distinguishable from any others brought by Python
# This is done by defining our own new exceptions as subclasses derived from predefined ones

# Choice 1: if we want to create an exception which will be utilized as a specialized case of any built-in exception
# ==> derive it from just this one

# Choice 2: If you want to build our own hierarchy, and don't want it to be closely connected to Python's exception tree
# ==> derive it from any of the top exception classes, like Exception.

class PizzaError(Exception): # cette classe hérite de Exception
    def __init__(self, pizza, message): # Prend deux arguments : pizza (nom de la pizza concernée) et message (description de l’erreur)
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError): # cette classe hérite de PizzaError
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
# Pizza ready!
# too much cheese : 110
# no such pizza on the menu : mafia