########## BUILT-IN FUNCTIONS ##########

## Functions need "arguments"
# ex: sin(x)= ? --> x is an argument

## there cannot be more than one instruction in a line !!!

## The instructions in the code are executed in the same order in which they have been placed in the source file 
# no subsequent instruction is executed until the previous one is completed

## What happens when Python encounters an invocation
# 1- Python checks if the name specified is legal: it browses its internal data in order to find an existing function of the name
#   if this search fails, Python aborts the code
# 2- Python checks if the function's requirements for the number of arguments allows you to invoke the function in this way
# 3- Python leaves your code for a moment and jumps into the function you want to invoke; of course, it takes your argument(s) too and passes it/them to the function
# 4- the function executes its code, causes the desired effect (if any), evaluates the desired result(s) (if any) and finishes its task
# finally, Python returns to your code (to the place just after the invocation) and resumes its execution



### abs()	
# Returns the absolute value of a number

x = abs(-7.25)
print(x)
7.25



### all()	
# Returns True if all items in an iterable object are true

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

x = bool(None)
print(x)
False

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
# This built-in method in Python checks and returns True if the object passed appears to be callable, otherwise False

def x():
  a = 5
print(callable(x))
True

print(callable(5))  
# False 
print(callable("Hello"))  
# False 
print(callable(len))  
# True 



### chr()
# Returns a character from the specified Unicode code.
# Invoking it with an invalid argument (e.g., a negative or invalid code point) causes ValueError or TypeError exceptions

x = chr(97)
print (x)
"a"

x = chr(32)
print (x)
"a"

x = chr(32) # SPACE
print (x)
# 



### classmethod()
# Converts a method into a class method

class Person:
    age = 25
    def printAge(cls):
        print('The age is:', cls.age)
Person.printAge = classmethod(Person.printAge) # create printAge class method
Person.printAge()
"The age is: 25"



### compile()	
# Returns the specified source as an object, ready to be executed
# compile() takes 3*arguments :
# 1st = source code ex:()'print(55)\nprint(88)')
# 2nd = file name
# 3rd = execution mode ex:('exec')
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
55
88



### complex()
# Returns a complex number, complex(real,imaginary)

x = complex(3, 5)
print(x)
# (3+5j)
# In Python, suffix "j" is used to represent the virtual part

x = complex(3)
print(x)
# (3+0j)

x = complex('3+5j') 
print(x)
# (3+5j)



### delattr()	
# Deletes the specified attribute (property or method) from the specified object

class Person:
  name = "John"
  age = 36
  country = "Norway"
delattr(Person, 'age') # The Person object will no longer contain an "age" property



### dict()	
# Returns a dictionary (Array)

x = dict(name = "John", age = 36, country = "Norway")
print(x)
{'name': 'John', 'age': 36, 'country': 'Norway'}

# .__dict__
# __dict__ is a special attribut spécial of any object in Python
#It is a dictionnary which contains all the object attributes from constructor, methods, direct, along with thei values

# Example 
class MaClass:
    class_var = 1
    def __init__(self):
        self.x = 10
        self.y = 20
    
    def print(self):
        return self.x + self.y
    
    def print2(self):
        self.z = self.x + self.y
        return self.z
    
obj = MaClass()
print(obj.__dict__)
# {'x': 10, 'y': 20} ==> from __init__
print(obj.print())
# 30
print(obj.__dict__)
# {'x': 10, 'y': 20}
print(obj.print2())
30
print(obj.__dict__)
{'x': 10, 'y': 20, 'z': 30}

print(MaClass.__dict__) # ==> class variables de class + functions + static attributes (here x, y, z)
# {'__module__': '__main__', '__firstlineno__': 1, 'class_var': 1, 
#  '__init__': <function MaClass.__init__ at 0x00000170C5F03E20>, 'print': <function MaClass.print at 0x00000170C5F11940>, 
#  'print2': <function MaClass.print2 at 0x00000170C5F10C20>,
#  '__static_attributes__': ('x', 'y', 'z'), '__dict__': <attribute '__dict__' of 'MaClass' objects>,
#  '__weakref__': <attribute '__weakref__' of 'MaClass' objects>, '__doc__': None}



### dir()	
# != de .__dict__ !!
# returns a list of the specified object's properties and methods
# PARAMETER can be a variable, a module, (), None
# RETURN can be a list of:
#   the module's attribute
#   names of class attributes
#   names of object attributes
#   names of the base class attributes


# object/class
class MaClass:
    class_var = 1
    def __init__(self):
        self.x = 10
        self.y = 20
    
    def print(self):
        return self.x + self.y
    
    def print2(self):
        self.z = self.x + self.y
        return self.z
    
obj = MaClass()
print(obj.__dict__)
# {'x': 10, 'y': 20} ==> from __init__

print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 
#  'class_var', 'print', 'print2', 'x', 'y'] 

print(MaClass.__dict__) # ==> class variables + functions + static attributes (ici x, y, z)
# {'__module__': '__main__', '__firstlineno__': 1, 'class_var': 1, 
#  '__init__': <function MaClass.__init__ at 0x00000170C5F03E20>, 'print': <function MaClass.print at 0x00000170C5F11940>, 
#  'print2': <function MaClass.print2 at 0x00000170C5F10C20>,
#  '__static_attributes__': ('x', 'y', 'z'), '__dict__': <attribute '__dict__' of 'MaClass' objects>,
#  '__weakref__': <attribute '__weakref__' of 'MaClass' objects>, '__doc__': None}

print(dir(MaClass))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__',
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 
#  'class_var', 'print', 'print2']


# module
import math
for name in dir(math):
  print(name, end=" ")
# __doc__ __loader__ __name__ __package__ __spec__ acos acosh asin asinh atan atan2 atanh cbrt ceil comb 
# copysign cos cosh degrees dist e erf erfc exp exp2 expm1 fabs factorial floor fma fmod frexp fsum gamma 
# gcd hypot inf isclose isfinite isinf isnan isqrt lcm ldexp lgamma log log10 log1p log2 modf nan nextafter 
# perm pi pow prod radians remainder sin sinh sqrt sumprod tan tanh tau trunc ulp


# current local
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# None
print(dir(None))
# ['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



### divmod()	
# Returns the quotient and the remainder when argument1 is divided by argument2

x = divmod(5, 2)
print(x)
(2, 1)



### enumerate()	
# Takes a collection (e.g. a tuple) and returns it as an enumerate object

x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
# enumerate object at 0x14dd63cdc300 # ?? To see what is into this obect, we must convert it into a list or iterate it thru a loop
print(list(y))
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]

animaux = ['girafe', 'tigre', 'singe', 'souris']
for i, animal in enumerate(animaux):
    print(i, animal)
#0 girafe
#1 tigre
#2 singe
#3 souris



### eval()	
# Evaluates and executes an expression

x = 'print(55)'
eval(x)
# 55

result = eval("2 + 3")
print(result)  
# 5

# Evaluating variables
x = 10
print(eval("x + 5"))  
# 15

x, y = eval(input('Enter two numbers: ')) # 3, 4
print(x)
print(y)
# 3
# 4



### exec()	
# Executes the specified code (or object)

x = 'name = "John"\nprint(name)'
exec(x)
# 'John'



### filter()	
# Use a filter function to exclude items in an iterable object

numbers = (1, 2, 5, 9, 15)
 
def filter_numbers(num):
    nums = (1, 5, 17)
    if num in nums:
        return True
    else:
        return False
 
filtered_numbers = filter(filter_numbers, numbers)
for n in filtered_numbers:
    print(n)
# 1
# 5


ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages) # not printable, it is just a filter 
print (adults)
# <filter object at 0x0000023D9F925C00>
for x in adults:
  print(x)
# 18
# 24
# 32  



### float()	
# Returns a floating point number

x = float(3)
print(x)
# 3.0

print (float("1, 3"))
# ValueError: could not convert string to float: '1,3'
# float() waits a point . de séparation not a comma ,
print (float("1.3"))
# or
z = float("1,3".replace(",", "."))
print(z)
# we can replace it with an input.replace



### format()	
# Formats a specified value

x = format(0.5, '%')
print(x)
# 50.000000%



### frozenset()	
# Returns a frozenset object

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
# frozenset({'apple', 'cherry', 'banana'})



### getattr()	
# Returns the value of the specified attribute (property or method)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)
# 36



### globals()	
# Returns the current global symbol table as a dictionary A QUOI CA SERT ???

x = globals()
print(x)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x02A8C2D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}



### hasattr()	
# Returns True if the specified object has the specified attribute (property/method)

class Person:
  name = "John"
  age = 36
  country = "Norway"
x = hasattr(Person, 'age')
print(x)
# True



### hash()	
# Returns the hash value of a specified object
# hash for integer unchanged= integer itself ==> ?
x = "test"
y = 35689
z = 35689.23
print (hash(x), hash(y), hash(z))
# -9195877821982143216 35689 530343892126567273



### help()	
# Executes the built-in help system

print (help(list))
'''
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
 |      Return first   of value.
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
'''



### hex()	
# Converts a number into a hexadecimal value

x = hex(255)
print(x)
# 0xff



### id()	
# Returns the id of an object = the memory address of the object
# will be different every time you run the program

x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
# 47642599593984


x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
# 22520260536256


class A:
    def __init__(self, x=0):
        self.x = x
 
obj1 = A(2)
obj2 = A(2)
print(id(obj1) == id(obj2)) 
# False # objects are different
print(id(obj1))
# 2384063197744
print(id(obj2))
# 1253138468048

obj1 = A(2)
obj2 = obj1 # here obj2 is a strict copy of obj1
print(id(obj1) == id(obj2))
# True
print(id(obj1))
# 1773527200304
print(id(obj2))
# 1773527200304


dict1 = {1:"a",2:"b"}
dict2 = dict1
print(id(dict1) == id(dict2))
# True

str1 = 'Hello'
str2 = 'Hello'
print(id(str1) == id(str2))
# True ==> varaibles sharing the same string value have the same id()
print(id(str1))
# 1905559360672
print(id(str2))
# 1905559360672



### input()	
# Allowing user input, the result of the input() function is a string

fnam = input("May I have your first name, please? ")
# James
lnam = input("May I have your last name, please? ")
#Bond
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# Thank you.
#
# Your name is James Bond.



### int()	
# Returns an integer number

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

data = ['Peter', 'Paul', 'Mary']
print(data[int(-1 / 2)]) # = data[0]
# Peter



### isinstance()	
# Returns True if a specified object is an instance of a specified object

x = isinstance(5, int)
y = isinstance("test", float)
print(x)
print(y)
# True
# False



### issubclass()	
# Returns True if a specified class is a subclass of a specified object

# Check if the class myObj is a subclass of myAge
class myAge:
  age = 36
class myObj(myAge):
  name = "John"
  age = myAge
x = issubclass(myObj, myAge)
print(x)
# True



### iter()	
# Returns an iterator object

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
# apple
# banana
# cherry

# if more (next(x)) than existing iterations ==> error, we should use prefer "for" loop
x = iter(["apple", "banana", "cherry"])
for item in iter(["apple", "banana", "cherry"]):
	print(next(x))
# apple
# banana
# cherry



### len()	
# Returns the length of an object

mylist = ["apple", "orange", "cherry"]
x = len(mylist)
print(x)
# 3

i_am = 'I\'m' # = I'm
print(len(i_am))
# 3

multiline = '''Line #1
Line #2'''
print(len(multiline))
# 15 as \n = 1 character

data = ()
print(data.__len__())
# 0
print(data.__len__() == len(data))
# True



### list()	
# Returns a list

x = list(('apple', 'banana', 'cherry'))
print(x)
# ['apple', banana', 'cherry']



### locals()	
# Returns an updated dictionary of the current local symbol table

x = locals()
print(x)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0327C2D0>, 
#  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'demo_ref_globals.py', '__cached__': None, 'x'_ {...}}



### map()	
# Returns the specified iterator with the specified function applied to each item

def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x)) #convert the map into a list, for readability:
# <map object at 0x056D44F0>
# [5, 6, 6]

letters = ["beach", "car"]
funified = list(map(lambda word: f"{word} is fun!", letters)) # Cette partie est une fonction anonyme (ou fonction lambda)
                                                              # Elle prend un argument word et retourne une nouvelle chaîne de caractères
print(funified)
# ['beach is fun!', 'car is fun!']



### max()	
# Returns the largest item in an iterable

x = max(5, 10)
y = max([5, 10, 552, 10489 , 10000003])
z = max({"horse" : 14, "dog" : 20, "cat" : 18})
print(x)
print(y)
print(z)
# 10
# 10000003
# "horse" # takes item alphabetic order, not its value



### memoryview()	
# Returns a memory view objectcherry

x = memoryview(b"Hello")
print(x)
# <memory at 0x03348FA0>



### min()	
# Returns the smallest item in an iterable

x = min(5, 10)
y = min([5, 10, 552, 10489 , 10000003])
z = min({"horse" : 14, "dog" : 20, "cat" : 18})
print(x)
print(y)
print(z)
# 5
# 5
# "cat" # takes item alphabetic order, not its value



### next()	
# Returns the next item in an iterable

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



### object()	
# Returns a new object

x = object()
print(dir(x))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', 
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



### oct()	
# Converts a number into an octal

x = oct(12)
print(x)
# Oo14



### open()	
# Opens a file and returns a file object

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



### ord()	
# Convert an integer representing the Unicode of the specified character

x = ord("h")
print(x)
# 104



### pow(x, y)	
# Returns the value of x to the power of y

print(pow(2, 4))
# 16



### print()	
# Prints to the standard output device

print('hello world')
# hello world



### property()	
# Gets, sets, deletes a property



### range() 
# Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# range(x) ==> de 0 à x-1
# range(i,x) ==> de i à x-1

# print i en fonction d'un range
for n in range(3):# de 0 à 2
    print("Python")
# Python # n = 0
# Python # n = 1
# Python # n = 2   



### repr()	
# Returns a readable version of an object

numbers = [1, 2, 3, 4, 5]
printable_numbers = repr(numbers) # create a printable representation of the list
print(printable_numbers)
# [1, 2, 3, 4, 5]



### reversed()	
# Returns a reversed iterator

alph = ["a", "b", "c", "d"]
print(list(reversed(alph)))
# ['d', 'c', 'b', 'a']
ralph = reversed(alph)

print(ralph)
# <list_reverseiterator object at 0x1499438eb370>

for x in ralph:
  print(x)
# d
# c
# b
# a



### round()	
# Rounds a numbers

print (round(1.1))
# 2
print (round(1.9))
# 2
print (round(1.5))
# 2
print (round(2.5))
# 2
print (round(3.5))
# 4 # rounds to the upper ==> ROUNDING TIES RULES
print (round(10.5))
# 10

x = round(5.76543)
print(x)
# 6
x = round(5.76543, 2)
print(x)
# 5.77



### set()	
# Returns a new set object. Note: the set list is unordered, so the result will display the items in a random order.

x = set(("apple", "banana", "cherry"))
print(x)
# {'cherry', 'apple', 'banana'}



### setattr()	
# Sets an attribute (property/method) of an object

class Person:
  name = "John"
  age = 36
  country = "Norway"
setattr(Person, 'age', 40) # The age property will now have the value: 40
x = getattr(Person, 'age')
print(x)
# 40



### slice()	
# Returns a slice object, slice(start, end, step), end excluded

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



### sorted()	
# Returns a sorted LIST

a = ("b", "g", "a", "d", "f", "c", "h", "e") # a is a tupple
print (type(a))
# <class 'tuple'>
x = sorted(a) # x is a list
print (type(x))
# <class 'list'>
print(x)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']



### staticmethod()	
# returns a static method for a given function.

class Calculator:
  def add_numbers(num1, num2):
    return num1 + num2
# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)
sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)
# Sum: 12



### str()	
# Returns a string object

a= 2.2
print (str(a))
# "2.2"

# from float or int to str

a= 2.2
print (str(a))
# 2.2  ==> "2.2"

d= 4
print (str(d))
4 # ==> "4"

b = "20.2"
print (str(int(float(b))))
# 20



### sum()	
# Sums the items of an iterator

##tupple
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)
# 15

## list
hat_list = [1, 2, 3, 4, 5]
print (sum(hat_list))
# 15

## start with basis number
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)
# 22



### super()	
# Returns an object that represents the parent class 

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

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name) # here super() is the builtin Python function

obj = Sub("Andy")
print(obj)
# My name is Andy.    



### tuple()	
# Returns a tuple, You cannot change or remove items in a tuple

x = tuple(("apple", "banana", "cherry"))
print(x)
# ('banana', 'cherry', 'apple')



### type()	
# Returns the type of an object

a = ('apple', 'banana', 'cherry')
print(type(a))
# <class 'tuple'>

b = "Hello World"
print(type(b))
# <class 'str'>

c = 33
print(type(c))
# <class 'int'>

d = 33.3
print(type(d))
# <class 'float'>

e = {a,1,True}
print(type(e))
# <class 'set'>

f = {1:a,2:b}
print(type(f))
# <class 'dict'>

g = [1,2,3,"a", "b"]
print(type(g))
# <class 'list'>

h = 1J
print(type(h))
# <class 'complex'>

data = [1, {}, (2,), (), {3}, [4, 5]] # = int,dict,tup,tup,set,list
points = 0
for i in range(len(data)):
    if type(data[i]) == list:
        points += 1
    elif type(data[i]) == tuple:
        points += 10
    elif type(data[i]) == set:
        points += 100
    elif type(data[i]) == dict:
        points += 1000
    else:
        points += 10000
print(points)
# 11 121



### vars()	
# Returns the __dict__ property of an object

class Person:
  name = "John"
  age = 36
  country = "norway"
x = vars(Person)
# {'__module__': '__main__', 'name': 'John', 'age': 36, 'country': 'norway', '__dict__': <attribute '__dict__' of 'Person' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}




### zip()	
# Returns an iterator, from two or more iterators

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
print(tuple(x)) # use the tuple() function to display a readable version of the result
# (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))