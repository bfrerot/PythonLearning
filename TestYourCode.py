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


############################

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



##################

pairs = [[2, 1], [-1, -1]]
new_pairs = map(lambda p: sorted(p), pairs)
print(list(new_pairs)[0][0])
print(list(new_pairs)[:])
1
[]

##################

class A:
 
    def __init__(self):
        pass
 
    def func1(self):
        return 1
 
    def func2():
        return self.func1()
 
 
x = A()
print(x.func2())
Traceback (most recent call last):
  File "c:\PythonLearning\error_test.py", line 14, in <module>
    print(x.func2())
          ~~~~~~~^^
TypeError: A.func2() takes 0 positional arguments but 1 was given

###################

num = 1
 
 
def func():
    num = num + 3
    print(num)
 
 
func()
 
print(num)

Traceback (most recent call last):
  File "c:\PythonLearning\error_test.py", line 9, in <module>
    func()
    ~~~~^^
  File "c:\PythonLearning\error_test.py", line 5, in func
    num = num + 3
          ^^^
UnboundLocalError: cannot access local variable 'num' where it is not associated with a value

'''
Explication générale
Topics: def shadowing

Try it yourself:

num = 1
 
 
def func():
    # num = num + 3  # UnboundLocalError: ...
    print(num)
 
 
func()
print(num)
 
print('----------')
 
num2 = 1
 
 
def func2():
    x = num2 + 3
    print(x)  # 4
 
 
func2()
 
print('----------')
 
num3 = 1
 
 
def func3():
    num3 = 3     # Shadows num3 from outer scope
    print(num3)  # 3
 
 
func3()
Explanation:

A variable name shadows into a function.

You can use it in an expression like in func2()

or you can assign a new value to it like in func3()

BUT you can not do both at the same time like in func()

There is going to be the new variable num

and you can not use it in an expression before its first assignment.
'''

######################

class Test:
    def __init__(self, id):
        self.id = id
        id = 100
 
 
x = Test(23)
 
print(x.id)

########################

def f(x, y):
    nom, denom = x, y
    def g():
        return nom / denom
    return g  # c quoi ce g ?
 
a = f(1, 2)
print(a())
# 0.5
b = f(3, 4)
print(b())

#######################

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)
# 1 1 2

'''
Explication générale
Topic: multiple assignments

Try it yourself:

x = 1
y = 2
# x, y, z = x, x, y
x, y, z = 1, 1, 2  # -> x=1; y=1; z=2
# z, y, z = x, y, z
z, y, z = 1, 1, 2  # -> y=1; z=2
# z will be 1 first and then become 2
# x is still 1
print(x, y, z)     # 1 1 2
Explanation:

We have multiple assignment in Python.

You can assign multiple values to multiple variables.

a, b = 3, 7

It is just shorter than

a = 3
b = 7
It does not have practical use, but what also works is

c, c = 23, 42

First c becomes 23 and then c becomes 42

You better write

c = 42

The same happens in this question in

z, y, z = 1, 1, 2

First z becomes 1 and then z becomes 2

You can also assign the same value to multiple variables:

a = b = c = d = 1
print(a, b, c, d) # 1 1 1 1
'''

#####################

for x in open('file', 'rt'):
    print(x)
#reads line by line

####################

'''
Explication générale
Topic: map()

Try it yourself:

list1 = [1, 2, 3]
list2 = [10, 100, 1000]
a = map(lambda x, y: x*y, list1, list2)
a = list(a)
print(a)  # [10, 200, 3000]


Explanation:

Yes, the map() function can accept more than two arguments.

The elements of the second parameter of the map() function (here list1)

will be assigned to the first parameter of the lambda function (here x).

The elements of the third parameter of the map() function (here list2)

will be assigned to the second parameter of the lambda function (here y).

There could even be more parameters.

And yes, the second map() function argument (here list1) can be a list.

But the first map() function argument must be a function.



Q169 (Please refer to this number, if you want to write me about this question.)
'''

#######################

'''
Explication générale
Topics: class __init__() self inheritance

             method overriding object variable

Try it yourself:

class A:
    def __init__(self, x=0):
        self.x = x
 
    def func(self):
        self.x += 1
 
 
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
 
    def func(self):
        self.y += 1
 
 
b = B()
b.func()
print(b.x, b.y)  # 3 1
Explanation:

The object b will inherit the object variable x from class A

and get the attribute y from its own class B

The start value of x will be 3

and the start value from y will be 0

The method func() will be from the class B

because the function from A with the same name will be overriden.

When b.func() is called, y will be incremented

and then the output is: 3 1
'''

###########################

'''
Explication générale
Topics: read() readline()



Try it yourself:

# First execute the following to create the needed file:
with open('index.txt', 'w') as f:
    f.write('Peter\n')
    f.write('Paul\n')
    f.write('Mary\n')
 
file = open('index.txt', 'r')
print(file.read(10))
# Peter
# Paul
Explanation:

file.read([size])

The read() method has one optional parameter.

If it is given, that number of characters are read.

If it is not given, the whole file is read.

file.readline([size])

The readline() method has also one optional parameter

to specify the number of characters to be read.

But it would only read that number of characters from

the first line.

If you want to read more characters,

only the read() method will work.
'''

####################

class.__dict__["method"] != None