class A:
    def __init__(self):
        self.calc(10)
    def calc(self, i):
        self.i = 3 * i
 
 
class B(A):
    def __init__(self):
        super().__init__()
        print('i from B is', self.i)
 
    def calc(self, i):
        self.i = 2 * i
 
 
b = B()


##############

def o(p):
    def q():
        return '*' * p
    return q
 
 
r = o(1)
s = o(2)
print(r() + s())


#################

def foo(x, y):
    return y(x) + (x + 1)
 
print(foo(1, lambda x: x * x))

##############"

str = 'abcdef'
def fun(s):
    del s[2]
    return s
 
print(fun(str))

#############

def func(data):
    data = [7, 23, 42]
    print('Function scope: ', data)
data = ['Peter', 'Paul', 'Mary']
func(data) # prefer its own "data" variable
print('Outer scope: ', data) # as "data" from func(data) is not global, data = ['Peter', 'Paul', 'Mary'] is used
# Function scope:  [7, 23, 42]
# Outer scope:  ['Peter', 'Paul', 'Mary']

#############

def func():
    text = 'Paul'
    names = lambda x: text + ' ' + x
    return names
people = func() 
print(people('Peter'))
# Paul Peter

#############

import random
print(random.seed(3))
# None

##############

def func(n):
    try:
        print(1 / n)
    except ValueError as ve:
        print(ve)
 
try:
    func(0)
except ArithmeticError as ae:
    print(ae)
# division by zero
'''La division par zéro (1/0) génère une ZeroDivisionError.
Cette erreur n'est pas capturée dans la fonction func, donc elle remonte.
Elle est capturée dans le except ArithmeticError du bloc extérieur.'''

################

data = (1, 2, 4, 8)
data = data[-2:-1]
data = data[-1]
print(data)
# 4  et pas (4,) ??

################

def func(x):
    if x % 2 == 0:
        return 1
    else:
        return # None ==> None + int = TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' 
print(func(func(2)) + 1)

###############

text1 = "caca"
text2 = "caca"
print(id(text1) == id(text2))
# True
# n variables disctinctes ayant la meme valeur de string partagent le meme emplacement mémoire
# VALABLE UNIQUEMENT POUR LES STRINGS

###############

x = 42
y = 7
data = "I'm gonna make him an offer he can't refuse."
 
print(data.find('an') if data else None)   # donne l'index ou commence "an"
# 19

print(19 if None else x / y) # valeur_si_vrai if condition else valeur_si_faux
# None est considéré comme falsy et la condition None est évaluée comme False
# donc else s'applique               
# 6.0

print(data.rfind('an') if data else None) # ici data.rfind() donne l'index du "an" le plus droite, la dernière occurence dans tout le strinig 
# 32

print(7 if len(data) > 19 else 6) # len(data)>19 donc le else s'applique         
# 7

################

# First execute the following to create the needed file:
data = '''Peter
Paul
Mary
'''
with open('data.txt', 'w') as f:
    f.write(data)
 
file = open('data.txt', 'at')
file.write('Jane')
file.close()
 
with open('data.txt', 'r') as f:
    print(f.read())
"""
Peter
Paul
Mary
Jane
"""
 
print('----------')
 
# This would open for writing and reading
file = open('data.txt', 'at+')
file.seek(0)
print(file.read())
file.close()
 
"""
Peter
Paul
Mary
Jane
"""
 
file = open('data.txt', 'ab')
# file.write('Jane')  # TypeError: ...
file.close()
 
file = open('data.txt', 'ab+')
# file.write('Jane')  # TypeError: ...
file.close()


#############

# name = input('What is your name?')
name = 'Peter'  # Just for convenience
sum = 0
score = 0
count = 0
"""
while score != -1:
    score = int(input('Enter your scores: (-1 to end)'))
    if score == -1:
        break
    sum += score
    count += 1
"""
sum = 120 + 180 + 165 + 224  # Just for convenience
count = 4  # Just for convenience
average = sum / count
print('%-20s, your average score is: %5.1f' % (name, average))
# Peter , your average score is: 172.2
 
# print('%-20i, ... %5.1f' % (name, average)) # TypeError: ...
# print('%-20d, ... %5.1f' % (name, average)) # TypeError: ...
# print('%-20f, ... %5.1f' % (name, average)) # TypeError: ...
print('%-20s, ... %1.5s' % (name, average))   # ... 172.
print('%-20s, ... %1.5f' % (name, average))   # ... 172.2500
print('%-20s, ... %5.1s' % (name, average))   # ... 1
 
# Other possibilities to format a string in Python:
name, age = 'Peter', 30
print(f'My name is {name} and I am {age} years old.')
# My name is Peter and I am 30 years old.
s = 'My name is {name} and I am {age} years old.'
print(s.format(name='Peter', age=30))
# My name is Peter and I am 30 years old.


#############

list = ['Peter', 'Paul', 'Mary']
 
def list(data): # ecrase la list par la fonction, qui elle-meme reprend un nom de fonction built-in..
    del data[1]
    data[1] = 'Jane'
    return data

print(list(list))


###############

list = ['Peter', 'Paul', 'Mary']
 
def list(data): # ecrase la list par la fonction, qui elle-meme reprend un nom de fonction built-in..
    del data[1]
    data[1] = 'Jane'
    return data

print(list(list))
# TypeError: 'function' object does not support item deletion
# un peu tricky comme cas tordu

##############

# un  piège dans le return

class A:
 
    def __init__(self, x=1):
        self.x = x
 
    def set(self, x):
        self.x = x + 3
        return self.x, x # si que x, on a tendance à confondre avec self.x
 
a = A()
print(a.set(a.x + 1))
# (5, 2)


#############

# tricky Exception case

class Failure(IndexError):
    def __init__(self, message):
        self.message = message
 
    def __str__(self):
        return "problem"
 
 
try:
    print("launch")
    raise Failure("ignition")
except RuntimeError as error:
    print(accident)
except IndexError as error:
    print("ignore")
else:
    print("landing")
# launch
# ignore

#############

# TypeError vs ValueError

import math
try:
    print(math.pow(2))
except TypeError:
    print('A')
else:
    print('B')
 
# math.pow(2)
# TypeError: pow expected 2 arguments, got 1
 
print(math.pow(2, 8))  # 256.0

# TypeError occurs when an operation or function is applied to an object of an inappropriate type
# ValueError occurs when a function receives an argument of the correct type but with an inappropriate value


###################

# comparer des strings

ata = ['abc', 'def', 'abcde', 'efg']
print(max(data))  # efg # ne  compare pas la  somme ou le nombre du string mais la premiève lettre
 
print(ord('a'))   # 97
print(ord('d'))   # 100
print(ord('e'))   # 101

# max() will look for the character with the highest Unicode character number