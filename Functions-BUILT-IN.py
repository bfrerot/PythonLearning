###### BUILT-IN FUNCTIONS ######

## Functions need "arguments"
# ex: sin(x)= ? --> x is an argument

## there cannot be more than one instruction in a line !!!

## The instructions in the code are executed in the same order in which they have been placed in the source file; 
# no subsequent instruction is executed until the previous one is completed

## What happens when Python encounters an invocation like this one below?
# First, Python checks if the name specified is legal (it browses its internal data in order to find an existing function of the name; if this search fails, Python aborts the code)
# second, Python checks if the function's requirements for the number of arguments allows you to invoke the function in this way (e.g., if a specific function demands exactly two arguments, any invocation delivering only one argument will be considered erroneous, and will abort the code's execution)
# third, Python leaves your code for a moment and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function;
# fourth, the function executes its code, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task;
# finally, Python returns to your code (to the place just after the invocation) and resumes its execution.


### abs()	# Returns the absolute value of a number

x = abs(-7.25)
print(x)
7.25


### all()	# Returns True if all items in an iterable object are true

mylist = [True, True, True]
x = all(mylist)
print(x)
True

mylist = [1, "string", [1,2,3], (1,2,3), {1:"one",2:"two"}]
x = all(mylist)
print(x)
True


### any()	
# Returns True if any item in an iterable object is true

mylist = [False, True, False]
x = any(mylist)
True


### ascii()	
# Returns a readable version of an object
# Replaces none-ascii characters with escape character + ascii characters

x = ascii("My name is Ståle")
print(x)
# My name is St\e5le


### bin()	
# Returns the binary version of a number; the result will always have the prefix 0b

x = bin(36)
print(x)
0b100100


### bool()	
# Returns the boolean value of the specified object and will always return True, unless the object is empty, like [], (), {}, False, 0, or None
# When bool() is provided an empty list, an empty string or the value 0 it returns False
# The expression will evaluate to True when bool () is given any other value, including negative numbers

x = bool(10)
print(x)
True

x = bool("jeanjaques)")
print(x)
True

x = []
y = ""
z = -1
print(bool(x),bool(y),bool(z))
# False False True


### bytearray()	
# Returns an array of bytes

x = bytearray(4)
print(x)
bytearray(b'\x00\x00\x00\x00') # à quoi ça sert ??


### bytes()	
# Returns a bytes object

x = bytes(6)
print(x)
b'\x00\x00\x00\x00\x00\x00'


### callable()
# In general, a callable is something that can be called
# This built-in method in Python checks and returns True if the object passed appears to be callable
# but may not be, otherwise False

def x():
  a = 5
print(callable(x))
True

print(callable(5))  # False (un entier n'est pas appelable)
print(callable("Hello"))  # False (une chaîne n'est pas appelable)
print(callable(len))  # True (len est une fonction intégrée, donc appelable)


### chr()
# Returns a character from the specified Unicode code.

x = chr(97)
print (x)
"a"


### classmethod()
# Converts a method into a class method

class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)
Person.printAge = classmethod(Person.printAge) # create printAge class method
Person.printAge()
"The age is: 25"


### compile()	# Returns the specified source as an object, ready to be executed
# La fonction compile() prend trois arguments :
# premier argument = code source sous forme de chaîne ('print(55)\nprint(88)')
# deuxième argument = nom du fichier (ou simplement un identifiant pour le code compilé, ici 'test')
# troisième argument = mode d'exécution ('exec' pour exécuter plusieurs instructions)
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
55
88


### complex()
# Returns a complex number, complex(real,imaginary)

x = complex(3, 5)
print(x)
# (3+5j)
# En Python, le suffixe j est utilisé pour représenter 
# la partie imaginaire (au lieu de i utilisé en mathématiques)

x = complex(3)
print(x)
(3+0j)

x = complex('3+5j') # interprete le string comme nombre complexe
print(x)
(3+5j)


### delattr()	# Deletes the specified attribute (property or method) from the specified object

class Person:
  name = "John"
  age = 36
  country = "Norway"
delattr(Person, 'age') # The Person object will no longer contain an "age" property


### dict()	# Returns a dictionary (Array)

x = dict(name = "John", age = 36, country = "Norway")
print(x)
{'name': 'John', 'age': 36, 'country': 'Norway'}


### dir()	# Returns a list of the specified object's properties and methods

class Person:
  name = "John"
  age = 36
  country = "Norway"
print(dir(Person))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']


### divmod()	# Returns the quotient and the remainder when argument1 is divided by argument2

x = divmod(5, 2)
print(x)
(2, 1)


### enumerate()	# Takes a collection (e.g. a tuple) and returns it as an enumerate object

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
# enumerate object at 0x14dd63cdc300 # ?? Pour afficher ce que contient cet objet, tu dois le convertir en une liste ou le parcourir dans une boucle
print(list(y))
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

animaux = ['girafe', 'tigre', 'singe', 'souris']
for i, animal in enumerate(animaux):
    print(i, animal)
#0 girafe
#1 tigre
#2 singe
#3 souris


### eval()	# Evaluates and executes an expression

x = 'print(55)'
eval(x)
# 55


### exec()	# Executes the specified code (or object)

x = 'name = "John"\nprint(name)'
exec(x)
# 'John'


### filter()	# Use a filter function to exclude items in an iterable object

ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages) # pas reussi à le printer, c juste un filtre 
print (adults)
for x in adults:
  print(x)
# 18
# 24
# 32  


### float()	# Returns a floating point number

x = float(3)
print(x)
# 3.0

print (float("1, 3"))
# ValueError: could not convert string to float: '1,3'
# float() attend un point . de séparation PAS une virgule ,
print (float("1.3"))
# ou
z = float("1,3".replace(",", "."))
print(z)
# on pourra ajouter un input.replace à la place


### format()	# Formats a specified value

x = format(0.5, '%')
print(x)
# 50.000000%


### frozenset()	# Returns a frozenset object

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
frozenset({'apple', 'cherry', 'banana'})
???


### getattr()	# Returns the value of the specified attribute (property or method)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)
# 36


### globals()	# Returns the current global symbol table as a dictionary A QUOI CA SERT ???

x = globals()
print(x)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02A8C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}


### hasattr()	# Returns True if the specified object has the specified attribute (property/method)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = hasattr(Person, 'age')
print(x)
# True


### hash()	# Returns the hash value of a specified object
# hash for integer unchanged
x = "test"
y = 35689
z = 35689.23
print (hash(x), hash(y), hash(z))
# -9195877821982143216 35689 530343892126567273


### help()	# Executes the built-in help system

print (help(list))
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
 |      
 |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |      
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |      
 |      The reverse flag can be set to sort in descending order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __class_getitem__(...) from builtins.type
 |      See PEP 585
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
None


### hex()	# Converts a number into a hexadecimal value

x = hex(255)
print(x)
# 0xff


### id()	# Returns the id of an object = the memory address of the object / 
          # will be different every time you run the program

x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
# 47642599593984


x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
# 22520260536256


### input()	# Allowing user input
# the result of the input() function is a string.

anything = input("Enter a number: ")
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
# error beacause we cannot apply an exponet to a string
# -->
# ->  
anything = float(input("Enter a number: ")) # on transforme l'input en un float (ou int)
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
# Enter a number: 8
# 8.0 to the power of 2 is 64.0

# si on met un string on aura une erreur logique
# Enter a number: rt
# Traceback (most recent call last):
#   File "main.py", line 1, in 
#     anything = float(input("Enter a number: "))
# ValueError: could not convert string to float: 'rt'  <-- WE CAN'T DO IT

# Find hypothenuse length
leg_a = float(input("Input first leg length: "))
# 7
leg_b = float(input("Input second leg length: "))
# 10
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
# Hypotenuse length is 12.806248474865697

# Ask identity
fnam = input("May I have your first name, please? ")
# James
lnam = input("May I have your last name, please? ")
#Bond
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# Thank you.
#
# Your name is James Bond.

# Print a rectangle
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="") # at the 5th line we DO NOT GO to the next line (end="")
print("+" + 10 * "-" + "+") # we change iterence so we go to the line
# +----------+
# |          |
# |          |
# |          |
# |          |
# |          | # at the 5th line we DO NOT GO to the next line (end="")
# +----------+ # we change iterence so we go to the line

# ask values, doing calculation and returns operation results

a = float(input("give me a float value for a:")) # input a float value for variable a here
# give me a float value for a:74
b = float(input("give me a float value for b:")) # input a float value for variable b here
# give me a float value for b:85
print("the value of a + b is: ", a + b ) # output the result of addition here
print("the value of a - b is: ", a - b ) # output the result of subtraction here
print("the value of a * b is: ", a * b ) # output the result of multiplication here
print("the value of a / b is: ", a / b ) # output the result of division here
print("\nThat's all, folks!")
# the value of a + b is:  159.0
# the value of a - b is:  -11.0
# the value of a * b is:  6290.0
# the value of a / b is:  0.8705882352941177

# That's all, folks!


print("Enter your name:")
x = input()
print("Hello, " + x)
"Enter your name:" # toto
# "Hello, toto"

print("Tell me anything...")
anything = input() # leave me alone
print("Hmm...", anything, "... Really?")
# Hm... leave me alone .. Really ?
# simplified version
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
# Hm... leave me alone .. Really ?


### int()	# Returns an integer number

x = int(3.5)
y = int(3.7)
print(x)
print(y)
# 3
# 3

b = "20.2"
print (int(b))
# ..
#    print (int(b))
# ValueError: invalid literal for int() with base 10: '20.2'


### isinstance()	# Returns True if a specified object is an instance of a specified object

x = isinstance(5, int)
y = isinstance("test", float)
print(x)
print(y)
# True
# False


### issubclass()	# Returns True if a specified class is a subclass of a specified object

# Check if the class myObj is a subclass of myAge
class myAge:
  age = 36
class myObj(myAge):
  name = "John"
  age = myAge
x = issubclass(myObj, myAge)
print(x)
# True


### iter()	# Returns an iterator object

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
# apple
# banana
# cherry

# attention si plus de print(next(x)) que d'itérations ==> error, contourner avec boucle for
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# Traceback (most recent call last):
#   File "./prog.py", line 5, in <module>
# StopIteration

x = iter(["apple", "banana", "cherry"])
for item in iter(["apple", "banana", "cherry"]):
	print(next(x))
# apple
# banana
# cherry


### len()	# Returns the length of an object

mylist = ["apple", "orange", "cherry"]
x = len(mylist)
print(x)
# 3


### list()	# Returns a list

x = list(('apple', 'banana', 'cherry'))
print(x)
# ['apple', banana', 'cherry']


### locals()	# Returns an updated dictionary of the current local symbol table

x = locals()
print(x)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0327C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}


### map()	# Returns the specified iterator with the specified function applied to each item

def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x)) #convert the map into a list, for readability:
# <map object at 0x056D44F0>
# [5, 6, 6]

letters = ["beach", "car"]
funified = list(map(lambda word: f"{word} is fun!", letters)) # Cette partie est une fonction anonyme (ou fonction lambda). Elle prend un argument word et retourne une nouvelle chaîne de caractères
print(funified)
# ['beach is fun!', 'car is fun!']


### max()	# Returns the largest item in an iterable

x = max(5, 10)
y = max([5, 10, 552, 10489 , 10000003])
z = max({"horse" : 14, "dog" : 20, "cat" : 18})
print(x)
print(y)
print(z)
# 10
# 10000003
# "horse" # prend l'ordre alphabétique de l'item ET PAS SA valeur..


### memoryview()	# Returns a memory view objectcherry

x = memoryview(b"Hello")
print(x)
# <memory at 0x03348FA0>


### min()	# Returns the smallest item in an iterable

x = min(5, 10)
y = min([5, 10, 552, 10489 , 10000003])
z = min({"horse" : 14, "dog" : 20, "cat" : 18})
print(x)
print(y)
print(z)
# 5
# 5
# "cat" # prend l'ordre alphabétique de l'item ET PAS SA valeur..


### next()	# Returns the next item in an iterable

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
# "apple"
x = next(mylist)
print(x)
# "banana"
x = next(mylist)
print(x)
# "cherry"


### object()	# Returns a new object

x = object()
print(dir(x))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


### oct()	# Converts a number into an octal

x = oct(12)
print(x)
# Oo14


### open()	# Opens a file and returns a file object

f = open("demofile.txt", "r")
print(f.read())
# 30/08/2022	ACHAT CB ASF-LANCON 30.08.22
# CARTE NUMERO 816	- 3,00 â‚¬	
# 
# 30/08/2022	ACHAT CB ASF-SENAS 30.08.22
# CARTE NUMERO 816	- 3,00 â‚¬	
# 
# 29/08/2022	ACHAT CB ESCOTA CAPITOU 29.08.22
# CARTE NUMERO 816	- 15,80 â‚¬	
# 
# 29/08/2022	ACHAT CB ESCOTA LA BARQ 29.08.22
# CARTE NUMERO 816	- 15,80 â‚¬	
# 
# 26/08/2022	ACHAT CB ASF, 4 PAIEMEN 25.08.22
# CARTE NUMERO 816	- 14,80 â‚¬	
# 
# 22/08/2022	ACHAT CB ASF-LANCON 19.08.22
# CARTE NUMERO 816	- 3,00 â‚¬	
# 
# 22/08/2022	ACHAT CB ASF-SENAS 19.08.22
# CARTE NUMERO 816	- 3,00 â‚¬	
# 
# 16/08/2022	ACHAT CB ESCOTA, 2 PAIE 16.08.22
# CARTE NUMERO 816	- 27,20 â‚¬	
# 
# 16/08/2022	ACHAT CB ASF-AVIGNON-N 16.08.22
# CARTE NUMERO 816	- 7,20 â‚¬	
# 
# 08/08/2022	ACHAT CB ESCOTA CAPITOU 08.08.22
# CARTE NUMERO 816	- 15,80 â‚¬	
# 
# 08/08/2022	ACHAT CB ESCOTA LA BARQ 08.08.22
# CARTE NUMERO 816	- 15,80 â‚¬	
# 
# 05/08/2022	ACHAT CB ESCOTA MEYRARG 02.08.22
# CARTE NUMERO 816	- 13,60 â‚¬	


### ord()	# Convert an integer representing the Unicode of the specified character

x = ord("h")
print(x)
# 104


### pow(x, y)	# Returns the value of x to the power of y

x = ord("h")
print(x)
# 64


### print()	# Prints to the standard output device

print('hello world')
# hello world


### property()	# Gets, sets, deletes a property


### range() # Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# range(x) ==> de 0 à x-1
# range(i,x) ==> de i à x-1

# print i en fonction d'un range
for n in range(3):# de 0 à 2
    print("Python")
# Python # n = 0
# Python # n = 1
# Python # n = 2   

# utiliser i en fonction d'un range + faire opération
for n in range(10, 20):
    print(n * n)
100 # n = 10
121 # n = 11
144 # n = 12
169 # n = 13
196 # n = 14
225 # n = 15
256 # n = 16
289 # n = 17
324 # n = 18
361 # n = 19

# print i in list par indexation + usage de range() pour déterminer l'indexation
animaux = ['girafe', 'tigre', 'singe', 'souris']
for i in range(4): # On peut melanger avec du range pour n'afficher qu'une partie ou tout
	print (animaux[i]) # 0,1,2,3
#girafe
#tigre
#singe
#souris
for i in range(2): # 0,1
	print (animaux[i])
#girafe
#tigre

# including non-default increment, default value of the increment is 1
for i in range(2, 8, 3): # increment 3 --> 2...3/4...5...6/7 END because 8 is excluded
    print("The value of i is currently", i)
#The value of i is currently 2
#The value of i is currently 5

# for/else, subtilité de range() 
for i in range(5):
    print(i)
else:
    print("else:", i)
#0
#1
#2
#3
#4
#else: 4 # i reste sur la dernière valeur utilisée dans la loop


### repr()	# Returns a readable version of an object

numbers = [1, 2, 3, 4, 5]
printable_numbers = repr(numbers) # create a printable representation of the list
print(printable_numbers)
# [1, 2, 3, 4, 5]


### reversed()	# Returns a reversed iterator

alph = ["a", "b", "c", "d"]
print(list(reversed(alph)))
# ['d', 'c', 'b', 'a']
ralph = reversed(alph)
# <list_reverseiterator object at 0x1499438eb370>

print(ralph)
for x in ralph:
  print(x)
# d
# c
# b
# a


round()	# Rounds a numbers

print (round(1.1))
print (round(1.9))
print (round(1.5))
print (round(2.5))
print (round(3.5))
print (round(10.5))
# 1
# 2
# 2
# 2
# 4 # arrondit au supérieur, pourquoi ? ROUNDING TIES RULES
# 10

x = round(5.76543)
print(x)
# 6
x = round(5.76543, 2)
print(x)
# 5.77


### set()	# Returns a new set object. Note: the set list is unordered, so the result will display the items in a random order.

x = set(("apple", "banana", "cherry"))
print(x)
# {'cherry', 'apple', 'banana'}


### setattr()	# Sets an attribute (property/method) of an object

class Person:
  name = "John"
  age = 36
  country = "Norway"
setattr(Person, 'age', 40) # The age property will now have the value: 40
x = getattr(Person, 'age')
print(x)
# 40


### slice()	# Returns a slice object, slice(start, end, step), le end n'est pas inclus

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
# ('a', 'b')

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(-1)
print(a[x])
# ('a', 'b', 'c', 'd', 'e', 'f', 'g')

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(1, len(a)-1, 2)
print(len(a))
# 8
print(a[x])
# ('b', 'd', 'f')


### sorted()	# Returns a sorted LIST

a = ("b", "g", "a", "d", "f", "c", "h", "e") # a est un tupple
print (type(a))
# <class 'tuple'>
x = sorted(a) # x est une liste
print (type(x))
# <class 'list'>
print(x)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


### staticmethod()	# staticmethod(function) The staticmethod() built-in function returns a static method for a given function.

class Calculator:
  def add_numbers(num1, num2):
    return num1 + num2
# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)
sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)
# Sum: 12


### str()	# Returns a string object

a= 2.2
print (str(a))
# "2.2"

# de float ou int vers str

a= 2.2
print (str(a))
# 2.2  en fait "2.2"

d= 4
print (str(d))
4 # en fait "4"

b = "20.2"
print (str(int(float(b))))
# 20

total_pancakes = 10
pancakes_eaten = 5
print ("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
# Only 5 pancakes left.# on a changé le resultat d'une operation en str


### sum()	# Sums the items of an iterator

##tupple
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)
# 15

## list
hat_list = [1, 2, 3, 4, 5]
print (sum(hat_list))
# 15

## commencer avec un nombre de départ
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)
# 22


### super()	# Returns an object that represents the parent class RIEN COMPRIS A L EXEMPLE

class Parent:
  def __init__(self, txt):
    self.message = txt
  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")
x.printmessage()
# Hello, and welcome!


### tuple()	# Returns a tuple, You cannot change or remove items in a tuple.

x = tuple(("apple", "banana", "cherry"))
print(x)
# ('banana', 'cherry', 'apple')


### type()	# Returns the type of an object

a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33
x = type(a)
y = type(b)
z = type(c)
print(x)
print(y)
print(z)
# <class 'tuple'>
# <class 'str'>
# <class 'int'>

a=5
print(type(a))
# <class 'int'>
a=5.2
print(type(a))
# <class 'float'>
a="papa"
print(type(a))
# <class 'str'>

### vars()	# Returns the __dict__ property of an object

class Person:
  name = "John"
  age = 36
  country = "norway"
x = vars(Person)
# {'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


### zip()	# Returns an iterator, from two or more iterators

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(tuple(x)) # use the tuple() function to display a readable version of the result
# (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))