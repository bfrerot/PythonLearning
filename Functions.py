########## FUNCTIONS ##########


## A function is able to:
#   cause some effect
#   evaluate a value


## Every function has two parts:
# 1. The function signature defines the name of the function and any inputs it expects.
# 2. The function body contains the code that runs every time the function is used.
def multiply(x, y): # Function signature
# Function body below
    product = x * y
    return product


## The function signature has four parts:
# 1. The def keyword
# 2. The function name, multiply
# 3. The parameter list, (x, y)
# 4. A colon (:) at the end of the line


## Function name STARTS by a letter and contains ONLY letters, numbers and _
# You MUST NOT have a function and a variable of the same name
# It's legal, and possible, to have a variable named the same as a function's parameter
# the meaning of the argument is dictated by its name, not by its position = keyword argument passing


## Functions come from at least three places:

# 1- from Python itself - numerous functions (like print()) are an integral part of Python, 
# and are always available without any additional effort on behalf of the programmer; 
# we call these functions built-in functions;

# 2- from Python's preinstalled modules - a lot of functions, very useful ones, 
# but used significantly less often than built-in ones, are available in a number 
# of modules installed together with Python; the use of these functions requires 
# some additional steps from the programmer in order to make them fully accessible 

# 3- directly from your code - you can write your own functions, place them inside 
# your code, and use them freely


## The process for executing a function can be summarized in three steps:
# 1. The function is called, and any arguments are passed to the function as input.
# 2. The function executes, and some action is performed with the arguments.
# 3. The function returns, and the original function call is replaced with the return value.




### RETURN
# 1- you are always allowed to ignore the function's result, and be satisfied with 
# the function's effect (if the function has any)
# 2- if a function is intented to return a useful result, it must contain the second 
# variant of the return instruction.
# 3- all part AFTER return is IGNORED


## un return clot la fonction
def hi():
    return
    print("Hi!") # pas pris en compte
# (None)


## return without an expression
def happyNewYear(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes: # donc si wishes = False
        return # return None
    
    print("Happy New Year!")
happyNewYear ()
# Three...
# Two...
# One...
# Happy New Year!


## return with an expression
def boringFunction():
    return 123
x = boringFunction()
print("The boringFunction has returned its result. It's:", x)
# The boringFunction has returned its result. It's: 123


## ignore the return value
def boringFunction():
    print("'Boredom Mode' ON.")
    return 123
print("This lesson is interesting!")
boringFunction()
print("This lesson is boring...")
# This lesson is interesting!
# 'Boredom Mode' ON.
# This lesson is boring... # return value 123 is not used and it is fine


## return / none default if no result from the function
def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1))
True
# (None) # 1%2 = 1 donc return = None car rien de prevu par la function


## récupérer le return d'une fonction
def ma_fonction():
    return 42

ma_variable = ma_fonction()
print(ma_variable)  # Affiche : 42




### SCOPE

# The function func() has a different scope than the code that exists outside of the function 
# We can name an object inside func() the same name as something outside func() and Python keep the two separated.
# 1- a var defined out of the function is usable into a function
# 2- a var defined in a function is not recognised out of it
# 3- if a var has the same name into a function and out of it, the function uses the var as defined into it
# 4- with lists, if a list is processed by a function, it will reflect the changes outside the function


## Python resolves scope in the order in which each scope appears in the list LEGB
# 1- Local (L): The local, or current, scope. The scope that the Python interpreter is currently working in
# 2- Enclosing (E): The enclosing scope. This is the scope one level up from the local scope
#       If the local scope is an inner function, the enclosing scope is the scope of the outer function
#       If the scope is a top-level function, the enclosing scope is the same as the global scope
# 3- Global (G): The global scope, which is the top-most scope in the script and all of the names defined in the script that are not contained in a function body
# 4- Built-in (B): The built-in scope contains all of the names, such as keywords, that are built-in to Python

def func(data):
    data = [7, 23, 42]
    print('Function scope: ', data)
data = ['Peter', 'Paul', 'Mary']
func(data) # prefer its own "data" variable
print('Outer scope: ', data) # as "data" from func(data) is not global, data = ['Peter', 'Paul', 'Mary'] is used
# Function scope:  [7, 23, 42]
# Outer scope:  ['Peter', 'Paul', 'Mary']


## variable scope LOCAL vs GLOBAL

total = 0
def add_to_total(n):
    total = total + n
add_to_total(5)
print(total)
# Traceback (most recent call last):
#   File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 4, in <module>
#     add_to_total(5)
#   File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 3, in add_to_total
#     total = total + n
# UnboundLocalError: local variable 'total' referenced before assignment 

# The problem here is that the script attempts to make an assignment to
# the variable total, which creates a new name in the local scope. Then,when Python executes 
# the right-hand side of the assignment it finds the name total in the local scope with 
# nothing assigned to it yet.

# We need to use the GLOBAL keyword to fix it:
total = 0
def add_to_total(n):
    global total
    total = total + n
add_to_total(5)
print(total)
# 5


## interaction avec les variables
x = 1 
def a(x):
    return 2 * x
print(x)
# 1
x = 2 + a(x) 
print(x)
# 4 # x a bien changé de valeur
print(a(x))
# 8
print(x)
# 4 # mais x n'a pas changé de valeur ici

num = 1
def func(x):
    x = x + 3
    print(x)
func(num)
# 4
print(num)
# 1


num = 1
def func(y):
    global num # num devient global, donc la fonction agit sur  la variable exterieure "num"
    num = y + 3
    print(num)
func(num)
# 4
print(num)
# 4 # num a bien changé de valeur via la fonction


def increment(c, num):
    c.count += 1     # incrémente l'attribut .count de l'objet counter
    num += 1         # num += 1 : incrémente la variable LOCALE num
                     # Modifier num dans la fonction ne modifie pas la variable number en dehors de la fonction
class Counter:
    def __init__(self):
        self.count = 0
counter = Counter() # counter.count = 0
number = 0
for i in range(0, 100):
    increment(counter, number)
print(
    "counter is "
    + str(counter.count)    
    + ", number of times is "
    + str(number)
)
# counter is 100, number of times is 0


## interaction avec les list
def myFunction(myList1):
    print(myList1)
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)
# [3]

def test(lst):
    del lst[3]
    lst[3] = 'ram'
    return lst
testlist=[0,1,2,3,4]
print (test(testlist))
# [0, 1, 2, 'ram']




### Function VS Methods

#A method is a specific kind of function - it behaves like a function and looks like a function,
#but differs in the way in which it acts, and in its invocation style.
#result = data.method(arg)
#methods are used to play with lists




### ARGUMENTS, PARAMETERS

# Default arguments
# if not specified at the invokation, the default value is used

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")
introduction("Henry")
# Hello, my name is James Doe
# Hello, my name is Henry Smith


class Class:
    def __init__(self, val=0):
        self.val = val
# valid invokations
object_1 = Class()  # default is used
print(object_1.val)
# 0
object_2 = Class(1)  # value is forced
print(object_2.val)
# 1
object_3 = Class(None)  # None is a value
print(object_3.val)
# None
object_4 = Class(True)  # True is a value
print(object_4.val)
# True


## *args ==> Many parameters FLEXIBLE
# to define functions that accept variable number of arguments

def add(*args):
    return sum(args)
print(add(1, 1, 1))
# 3
print(add(1))
# 1




### POSITIONNAL VS KEYWORDS arguments

# MUST NOT follow keyword arguments
def subtra(a, b):
    print(a - b)
    
subtra(5, b=2) 
# 3

subtra(a=5, 2) 
# Syntax Error


def add_numbers(a, b=2, c):
    print(a + b + c)
add_numbers(a=1, c=3)
# Syntax Error


def add_numbers(a, c, b=2):
    print(a + b + c)
add_numbers(a=1, c=3)
# 6


def test(x, y=23, z=10):
    print('x is', x, 'and y is', y, 'and z is', z)
test(3, 7)
# x is 3 and y is 7 and z is 10
test(42, z=24)
# x is 42 and y is 23 and z is 24
test(z=60, x=100)
# x is 100 and y is 23 and z is 60



## parameters dans l'odre
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Luke", "Skywalker") # if parameter is not specified with an = + parameter value, default order is respected
# Hello, my name is Luke Skywalker
introduction("Jesse", "Quick")
# Hello, my name is Jesse Quick
introduction("Clark", "Kent")
# Hello, my name is Clark Kent


## parameters dans le desordre
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke") # if parameters are set in a different order with an = + parameter, the function doesn't care and sort it in the right way 
# Hello, my name is James Bond
# Hello, my name is Luke Skywalker


## parameters par defaut
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
introduction("James")
# Hello, my name is James Smith # parameter unique = premier (ici first name) + deuxieme par defaut

def fun(inp=2,out=3):
    return inp * out
print (fun(out=2))
# 4


## multiple parameters (*par)
def fun(*val): # fun() accepte de multiple parameters
    print(type(val))
lst=[1,2,3,4,5]
number = 400
fun(lst,number)
# <class 'tuple'> # car [1,2,3,4,5], 400 est un tuple


## parameter par defaut ecrasé par celui indiqué
def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)
introduction("James","Doe")
# Hello, my name is James Doe # Smith (default parameter) is replaced by Doe (specified parameter)


## usage des parameters
# on peut avoir une fonction qui appelle 2 parameters ou plus mais ne se sert que d'1

def fun(x,y=6):
    return x**3  # y ne sert à rien, n'est pas invoqué, mais pas de problème
print (fun(2))
# 8
def fun(data, *num ):
    print(data)
fun("Earth", 2, True, "Jupiter")
# Earth


## list comme parameter d'une function

def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum
print(sumOfList([5, 4, 3]))
# 12

# En Python, les listes sont mutables, donc si on modifie une liste in-place dans une fonction, on modifie aussi l’objet d’origine.
# del, .append(), .pop(), .sort(), etc. modifient la liste sur place
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
#  #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [3]
# Print #4: [3]
# Print #5: [3]




### OUTER/INNER Functions
# on peut avoir une fonction dans une fonction

x = 5
def outer_func():
    y = 3
    def inner_func():
        z = x + y
        return z
    return inner_func()
print (outer_func())
# 8

def quote(x):
    def embed(y):
        return x + y + x
    return embed

dq = quote('"')
print(dq('Jane Doe'))
# "Jane Doe"

# ==>
# quote(quo) : fonction qui crée une autre fonction
# embed(str), qui utilise la valeur quo capturée, ici ", est une fonction anonyme
# dblq = quote("") ==> quote() retourne la fonction embed(str) où quo est maintenant "
#                      dblq devient cette fonction embed(str)
# dblq('Jane Doe') ==> embed('Jane Doe'), return " + Jane Doe + "





### DOCSTRING
# to create Documentation about a function

def multiply(x, y):
    """Return the product of two numbers x and y.""" # comment in function =  docstring
    product = x * y
    return product

help(multiply)
# Help on function multiply in module __main__:
# 
# multiply(x, y)
#     Return the product of two numbers x and y. # comment returned when help function is used




### RETURN vs PRINT()

#invoquer
def wishes():
    print("My Wishes")
    return "Happy Birthday"
wishes()
# My Wishes

#printer
def wishes():
    print("My Wishes")
    return "Happy Birthday"
print(wishes())
# My Wishes
# Happy Birthday




### INFINITE LOOP 
# Exemple et correction avec insertion d'une termination condition

# SANS
def fun(a):
    return a + fun(a + 3)

print(fun(25))
...
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

# AVEC
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
56  # 25 + 28 + fun(31)=3 --> 56



### RECURSIVITE
# Exemple de function récursive

def fact(num):
    if num == 1:
        return 1
    return fact(num - 1) * num

print(fact(4))
# 24

# Calcul de fact(4) :
# fact(4) = fact(3) * 4
# fact(3) = fact(2) * 3
# fact(2) = fact(1) * 2
# fact(1) = 1 (cas de base)

# Donc :
# fact(2) = 1 * 2 = 2
# fact(3) = 2 * 3 = 6
# fact(4) = 6 * 4 = 24
# ✅ Résultat affiché : 24




### Exception handling

def spam(divideBy):
    return 42 / divideBy
print(spam(2)) 
print(spam(12)) 
print(spam(0)) # erreur due au fait qu on ne peut pas diviser par 0
print(spam(1))

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        return None  # ou une autre valeur par défaut
    except Exception as e:
        print(f'Unexpected error: {e}')
        return None
print(spam(2))
# 21.0
print(spam(12)) 
# 3.5
print(spam(0)) 
# Error: Invalid argument.
# None
print(spam(1))
# 42.0


def spam(divideBy):    
    return 42 / divideBy
try:
    print(spam(2))    
    print(spam(12))    
    print(spam(0))    
    print(spam(1)) 
except ZeroDivisionError:    
	print('Error: Invalid argument.')
# 21.0 
# 3.5 
# Error: Invalid argument. # ca ne continuera pas sur print(spam(1)), 
                           # car le code passe a except pour spam(0) et ne remontera pas 
                         


### CLOSURES

def outer(par):
    loc = par

    def inner():
        return loc # = 1
    
    return inner # = 1

var = 1
fun = outer(var)
print(fun())
# 1


def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64


def func():
    text = 'Paul'
    names = lambda x: text + ' ' + x
    return names
people = func() 
print(people('Peter'))
# Paul Peter


def o(p):
    def q():
        return '*' * p
    return q
 
r = o(1)
s = o(2)
print(r() + s())
# ***