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