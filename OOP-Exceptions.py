########## EXCEPTIONS in OOP context ##########


### Exceptions are Classes

# when an exception is raised, an object of the class is instantiated and goes through all levels of program execution,
# looking for the except branch that is prepared to deal with it

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

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



### .ARGS

# la méthode .args est un attribut des objets d'exception (instances de classes dérivées de BaseException, comme Exception). 
# Si l'exception est levée sans argument (raise Exception()), alors e.args est une liste vide ([]).
# Si l'exception est levée avec un seul argument (raise Exception("message")), alors e.args est une tuple avec un seul élément (("message",)).
# Si plusieurs arguments sont donnés (raise Exception("msg1", "msg2")), alors e.args est une tuple contenant tous ces arguments (("msg1", "msg2")).

def print_arguments(arguments):
    lng = len(arguments)
    if lng == 0:
        print("")
    elif lng == 1:
        print(arguments[0])
    else:
        print(str(arguments))


try:
    raise Exception # La ligne raise Exception génère une exception de type Exception sans message.

except Exception as e: # L'exception est attrapée dans le bloc except sous la variable e
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_arguments(e.args) # = []
#  :  : 

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = (my exception) tupple
# my exception : my exception : my exception

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = ("my", "exception") tupple
# ('my', 'exception') : ('my', 'exception') : ('my', 'exception')

try:
    raise Exception(12345)
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = ("12345") tupple, l'int 12345 a bien été chagée en str
# 12345 : 12345 : 12345



### Exemple intéressant
# class + Error + boucle for

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I(): # va executer chaque method de la fonction
    print(x,end='') # print le return final snas aller à la ligne, sans espace  
# abc


#  Étape | Action                                   | Résultat / Variable                                   | Affichage            |
# |---------|------------------------------------------|--------------------------------------------------------|----------------------|
# | 1       | Crée instance `I()`                      | `self.i=0`, `self.s='abc'`                              |                      |
# | 2       | Appel `__iter__()`                       | Retourne l'objet lui-même                              |                      |
# | 3       | Appel `__next__()`                       | `i=0`, retourne `'a'`, `i=1`                          | Affiche `'a'`        |
# | 4       | Appel `__next__()`                       | `i=1`, retourne `'b'`, `i=2`                          | Affiche `'b'`        |
# | 5       | Appel `__next__()`                       | `i=2`, retourne `'c'`, `i=3`                          | Affiche `'c'`        |
# | 6       | Appel `__next__()`                       | `i=3`, levée `StopIteration`                          | Fin de la boucle     |

# raise StopIteration est la façon officielle en Python de dire :  
# ==> Fini, il n'y a plus d'éléments à fournir
#     La boucle for ou tout autre code qui utilise l'itérateur va alors arrêter automatiquement la boucle




### CHAINED EXCEPTIONS


## CHAIN OF EXCEPTION
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    print(0 / 0)
# Traceback (most recent call last):
#   File "c:\PythonLearning\SandBox.py", line 4, in <module>
#     print(a_list[3])
#           ~~~~~~^^^
# IndexError: list index out of range

# During handling of the above exception, another exception occurred:  ==> CHAIN of exceptions

# Traceback (most recent call last):
# #   File "c:\PythonLearning\SandBox.py", line 6, in <module>
#     print(0 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero


## IMPLICIT Chaining & .__context__
a_list = ['First error', 'Second error']

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10	but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print('Inner exception (f):', f)
        print('Outer exception (e):', e)
        print('Outer exception referenced:', f.__context__) # linked to e
        print('Is it the same object:', f.__context__ is e)
# Inner exception (f): division by zero
# Outer exception (e): list index out of range
# Outer exception referenced: list index out of range
# Is it the same object: True

# f.__context__ is e == True
#   1- IndexError is captured
#   2- e is associated to the current handled error = INdexError
#   3- ZeroDivisionError occurs, internal, because into the except block
#   4- Implicit chaining is created

# .__context__ refers to the exception being handled when a new one is raised during an except block


## EXPLICIT chaining

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])  # will cause an exception as crew[3] doesn't exist
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e  # explicit chaining


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100 / 2))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
check_list = [personnel_check, fuel_check]

print('Final check procedure')
# Final check procedure

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
#         The captain's name is John
#         The pilot's name is Mary
#         The mechanic's name is Mike
# RocketNotReady exception: "Crew is incomplete", caused by "list index out of range"
# Fuel tank is full in 50.0%

# .__raise__ refers to the direct cause of an exception when an explicit chaining is done with "raise"


## .__traceback__

# it is an attribute of each exception instance

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
# Final check procedure
#         The captain's name is John
#         The pilot's name is Mary
#         The mechanic's name is Mike
# <traceback object at 0x000001705F9F37C0>
# <class 'traceback'>


## traceback MODULE

# format_tb() method
# method delivered by the built-in traceback module to get a list of strings describing the traceback

# print_tb() method
# the same but to print strings directly to the standard output

import traceback

class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


crew = ['John', 'Mary', 'Mike']

print('Final check procedure')
# Final check procedure

try:
    personnel_check()
except RocketNotReadyError as f:
    print(f.__traceback__)
    print(type(f.__traceback__))
    print('\nTraceback details')
    details = traceback.format_tb(f.__traceback__)   # ==> format_tb()
    print("\n".join(details))
#         The captain's name is John
#         The pilot's name is Mary
#         The mechanic's name is Mike
# <traceback object at 0x00000217BD835680>
# <class 'traceback'>

# Traceback details
#   File "c:\PythonLearning\SandBox.py", line 22, in <module>
#     personnel_check()
#     ~~~~~~~~~~~~~~~^^

#   File "c:\PythonLearning\SandBox.py", line 14, in personnel_check
#     raise RocketNotReadyError('Crew is incomplete') from e

print('Final check is over')
# Final check is over