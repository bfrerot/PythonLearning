########## EXCEPTIONS ##########



# Error will occur wherever it is possible = Murphy law
# when code does something wrong Python does stop the program and creates an exception = raising an exception    
#   if exception is addressed --> program continues
#   if nothing is done --> program stops and generate an error



##### TRY/EXCEPT

# Avec try/except, python gere les erreurs et des qu il y a un probleme, python cherche un except qui matche
# Tout le code situe entre l erreur et l except sera ignore

try:
    value = int(input('Enter a natural number: ')) # 5.0
    print('The reciprocal of', value, 'is', 1/value) # ignored 
except: # match par défaut
    print('I do not know what to do.') # exécuté
# I do not know what to do.


try:
    print("1") # exécuté sans problème
    x = 1 / 0 # ArithmeticError, division par 0 interdite
    print("2") # ignoré
except:
    print("Oh dear, something went wrong...") # exécuté
print("3") # exécuté
# 1
# Oh dear, something went wrong...
# 3



### TRY/multiple EXCEPT

# Permet de preciser une action differente en fonction de l erreur
# On peut préciser plusieurs type d'error par Except, via un tuple
# The default except branch MUST be the last except branch, or SyntaxError
# on peut remplacer le code d'erreur par n'importe  lequel de ses parents
   
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


try :
    print("all clear!")
except (TypeError, ValueError): # tuple including errors types
    print("oh no!")
# all clear!


try:
    print(y = 1 / 0)
except BaseException:  # parent de Exception\ArithmeticError\ZeroDivisionError
    print("Oooppsss...")
print("THE END.")


# on peut mettre plusieurs exceptions dans un except si l'action visée est la meme, le code sera plus propre
try:
    y = 1 / 0
except (ZeroDivisionError,ArithmeticError):
    print("Problem!")
print("THE END.")
# Problem!
# THE END.



### EXCEPT order counts

# Order of the branches matters! First match = execution !
 
# Avoid put more general exceptions before more concrete ones, it is suboptimal
try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")
# Arithmetic problem!
# THE END.



### Exceptions dans Functions

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

badFun(0)
# Arithmetic Problem!



### Exceptions dans try

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
# What happened? An exception was raised!





##### RAISE

# python keyword
# enables to:
#   simulate raising actual exceptions
#   partially handle an exception and make another part of the code responsible for completing the handling


### raise depuis une function

def badFun(n): # lève explicitement une exception ZeroDivisionError à chaque appel, peu importe l’argument n
    raise ZeroDivisionError

try:
    badFun(0) # lève immédiatement une exception ZeroDivisionError
except ArithmeticError: # ZeroDivisionError est une sous-classe de ArithmeticError, et donc matchée par cet except
    print("What happened? An error?") # exécutée
# What happened? An error?


def badFun(n):
    try:
        return n / 0   # retourne une ZeroDivisionError quel que soit n 
    except:
        print("I did it again!") # s'execute si Exception, ici toute exception par défaut
        raise # traite le except dessous en plus, propage le ZeroDivisionError

try:
    badFun(56)
except ArithmeticError:
    print("I see!")
# I did it again!
# I see!



### raise + FROM


## from None
try:
    raise IOError # déclenche volontairement une exception de type IOError
except IOError: # remove # before raise as it was putting things down..
#   raise RuntimeError from None # exception IOError capturée ==> from None supprime la chaîne de causes
    pass
# Traceback (most recent call last):
#   File "c:\PythonLearning\error_test.py", line 4, in <module>
#     raise RuntimeError from None
# RuntimeError


## from "Exception"
try :
    raise IOError
except IOError as e: # remove # before raise as it was putting things down..
#   raise RuntimeError from e
    pass

# Traceback (most recent call last):
#   File "c:\PythonLearning\error_test.py", line 2, in <module>
#     raise IOError
# The above exception was the direct cause of the following exception:
# Traceback (most recent call last):
#   File "c:\PythonLearning\error_test.py", line 4, in <module>
#     raise RuntimeError from e
# RuntimeError

# OSError   ==> Depuis Python 3.3, IOError a été fusioné dans OSError
#               Même si on raise IOError, Python 3 le traduit en levée de OSError
#               C’est pourquoi dans le Traceback l’exception de départ est une OSError, pas une IOError



### raise + tuple en arg
try :
    raise Exception( 'spam' , 'eggs' )
except Exception as exception:
    print(exception) # représentation de l'objet exception lui-même
    print(exception.args)
#  ('spam', 'eggs') ==> représentation de la tuple que vous avez passées en argument
#  ('spam', 'eggs') ==> exception.args est le tuple ('spam', 'eggs')


try :
    raise Exception( 'spam' , 'eggs' )
except Exception as inst:
    x, y = inst.args # le nombre de variable (x, y , etc) doit matcher avec le nbre d'arg
print(x, y)
# spam eggs



### raise et super()
class AgeException (Exception): # hérite de la classe Exception, ce qui en fait une exception personnalisée
    def __init__ (self, age): # Le constructeur __init__ prend un paramètre age, mais dans ce code, il ne l'utilise pas directement
        super(AgeException, self).__init__( "AgeException" ) # appelle le constructeur de la classe parente (Exception) en lui passant le message "AgeException"
#                                                              Donc, quand cette exception sera levée, son message sera "AgeException"
try :
    raise AgeException(16)
except AgeException as e:
    print(e)
# AgeException   





##### ASSERT

# you may want to put it into your code where you want to be absolutely safe from wrong data
# raising an AssertionError exception secures your code from producing invalid results and clearly shows the nature of the failure
# assertions don't supersede exceptions or validate the data, they are their supplements

import math
x = float(input("Enter a number: "))
assert x >= 2.0
x = math.sqrt(x)
print(x)
# Enter a number: 2 # match le assert
# 1.4142135623730951

# Enter a number: 1,99 # ne match pas
# AssertionError


### assert VS Except match

def foo(x):
    assert x
    return 1/x
 
try:
    print(foo(0)) # l'assert est levé avant le return 1/x
except ZeroDivisionError: # l'error n''est pas repertoriée telle quelle donc ne matche pas
    print("zero")
except: # capturé par le defaut except
    print("some")
# some
    
### assert (condition, message)
assert (False, 'Trigger Assertion')
# ici la condition est un Tuple qui est considérée comme True TANT qu'elle n'est pas vide

assert (False, 'Trigger Assertion')
# SyntaxWarning: assertion is always true, perhaps remove parentheses?

assert () 
# seul ne fonctionne pas
   
    



##### FINALLY

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


# ! finally est TOUJOURS exécuté avant le return
# Il s'exécuter juste avant que la fonction ne termine et ne return une valeur, même si cette valeur a été spécifiée dans le return avant
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine") # --1
        return n     # --3
    finally:
        print("It's time to say goodbye") # --2
       
print(reciprocal(2))
# Everything went fine --1
# It's time to say goodbye  --2
# 0.5 --3
    
def func():
    try:
        print(23)
        return 100
    finally:
        print(42)
 
print(func())   
# 23
# 42
# 100 ==> retourne chercher le return du try



##### Exceptions are Classes

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
#    |   |   +---FileExistsError  ==> includes mkdir issues about already existing Directories !
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



### Create our own Exceptions/Classes

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





##### ELSE

# La partie ELSE s’exécute si pas d'exception levée dans le try + aucun catch n'est effectué par un Except
try :
    pass
except ZeroDivisionError:
    print( 'ZeroDivisionError' ) # NOK
except TypeError: # NOK
    print( 'TypeError' )
else :  # un except est levé donc le ELSE s'applique
    print( 'ELSE' )
# ELSE


# La partie ELSE ne s’exécute pas si à une exception levée dans le try, aucun catch n'est affectué par un Except
try :
    raise Exception
except ZeroDivisionError: # NOK
    print( 'ZeroDivisionError' )
except TypeError: # NOK
    print( 'TypeError' )
else :
    print( 'ELSE' ) # La partie ELSE ne s’exécute que si aucune exception n’est levée dans le try
# Exception


# La partie ELSE ne s’exécute pas si exception levée dans le try + catch effectué par un Except
try :
    raise ZeroDivisionError
except ZeroDivisionError:
    print( 'ZeroDivisionError' )
except TypeError:
    print( 'TypeError' )
else :
    print( 'ELSE' )
# ZeroDivisionError

# si raise vide ==> RuntimeError
try :
    raise 
except ZeroDivisionError:
    print( 'ZeroDivisionError' )
except TypeError:
    print( 'TypeError' )
else :
    print( 'ELSE' )
# RuntimeError: No active exception to reraise





##### DIVERS

# raise + else + finally
try :
    print( "1" , end= '' )
    raise Exception
    print( "2" , end= '' ) # après un raise, rien n'est pris en compte
except BaseException:
    print( "3" , end= '' ) # BaseException matche tout
else :
    print( "4" , end= '' ) # pas utilisé
finally :
    print( "5" ) # toujours en dernier
# 135


#  savoir si une exception a été levée sans intention de la gérer
class E (Exception):
    def __init__ (self, message):
      self.message = message
    def __str__ (self):
        return "Surprise"
    
try :
    raise Exception( "Stop" )
except E as e:
    print(e)
else :
    print( "Goodbye" )
# Traceback (most recent call last):
# File "c:\PythonLearning\bac-à-sable.py", line 8, in <module>
#    raise Exception( "Stop" )
# Exception: Stop    ==>  = unhandled Exception





##### ERRORS REFs

# --> voir Python_error_tree.mmd pour voir le tree complet

### BaseException 
# BaseException
# = any error source tree 
# ==> 4 branches
#   Exception ==> concerne beaucoup d'eereurs que l'on va gérer au quotidien
#   System Exit
#   KeyboardInterrupt
#   GeneratorExit



### Exception

ArithmeticError 
# any arithmetic error
# BaseException ← Exception ← ArithmeticError 
# including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain


ZeroDivisionError 
# you cannot divide by 0
# BaseException ← Exception ← ArithmeticError ← ZeroDivisionErro
# si on essaie  de mettre 0 en diviseur avec /, //, ou %
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     value /= 0
#  ZeroDivisionError: division by zero


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


AssertionError 
# BaseException ← Exception ← AssertionError
# concrete exception raised by the assert instruction when its argument evaluates to False,
# None, 0, or an empty string


AttributeError
# BaseException ← Exception ← AttributeError
# when you try to activate a method which doesn't exist in an item you're dealing with
short_list = [1]
short_list.append(2)
print(short_list)
# [1, 2]
short_list.depend(3)
# AttributeError: 'list' object has no attribute 'depend'. Did you mean: 'append'?


ImportError
# BaseException ← Exception ← ImportError
# raised when an import operation fails
# One of these imports will fail – which one?
try:
    import math
    import time
    import abracadabra: # will cause an issue
except:
    print('One of your imports has failed.')
# One of your imports has failed.


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


IndexError 
# BaseException ← Exception ← LookupError ← IndexError
# Lookup error, parent, peut suffir
# index introuvable, inexistant
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
    

SyntaxError
# BaseException ← Exception ← SyntaxError
# raised when the control reaches a line of code which violates Python's grammar
print("Bonjour tout le monde")
# SyntaxError: unexpected EOF while parsing
  

TypeError
# BaseException ← Exception ← TypeError
# when you try to apply a data whose type cannot be accepted in the current context
short_list = [1]
one_value = short_list[0.5] # [0.5] cannot be a float


ValueError
# BaseException ← Exception ← ValueError
# with values which may be inappropriately used in some context
short_list = [1]
one_value = short_list[0.5]  

int("abc") # right type but incorrect value


OSError 
# et errno
# BaseException ← Exception ← OSError
# ==>
# ├── PermissionError
# │   ├── errno.EPERM
# │   ├── errno.EACCES
# │   ├── errno.EBADF # si l’erreur concerne un descripteur invalide ou fermé
# │   ├── errno.ESRCH # si l’objet existe mais inaccessible
# ├── FileNotFoundError
# │   ├── errno.ENOENT
# │   ├── errno.EBADF
# │   ├── errno.ESRCH
# ├── FileExistsError
# │   ├── errno.EEXIST
# ├── IsADirectoryError
# │   ├── errno.EISDIR
# ├── ConnectionError
# │   ├── errno.ECONNREFUSED,
# │   ├── errno.ETIMEDOUT,
# │   ├── errno.EHOSTUNREACH,
# │   ├── errno.ENETDOWN,
# │   ├── errno.ENETUNREACH
# │   ├── errno.EINTR

# Fichiers et système de fichiers
# │   ├── errno.EFBIG
# │   ├── errno.EMFILE

# Entrée/Sortie
# │   ├── errno.EIO


  
### KeyboardInterrupt 
# BaseException ← KeyboardInterrupt
# raised when the user uses a keyboard shortcut designed to terminate a program's execution (Ctrl-C in most OSs)



### SystemExit
# levée lorsqu’on appelle sys.exit().
# But = Indiquer que le programme doit se terminer proprement.
import sys
sys.exit()  # Lève SystemExit, termine le programme sauf si attrapéecatchée par un try/except



### GeneratorExit
# levée lorsqu’un générateur est fermé, par exemple avec generator.close()
# But : Permet au générateur de faire du nettoyage avant de se terminer
def gen():
    try:
        yield 1
    finally:
        print("Nettoyage lors de la fermeture du générateur")
        
g = gen()
g.close()  # Lève GeneratorExit dans le générateur