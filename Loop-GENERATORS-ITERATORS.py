########## GENERATORS - ITERATORS ##########



### RANGE()

for i in range(5):
    print(i,end='')
# 01234



### ITERATOR PROTOCOL

# The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements
# An object conforming to the iterator protocol is called an iterator

# An iterator must provide two methods:
#       __iter__() ==> should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)
#       __next__() ==> intended to return the next value (first, second, and so on) of the desired series 
#                      it will be invoked by the for/in statements in order to pass through the next iteration
#                      if there are no more values to provide the method should raise the StopIteration exception


## ==> ex: Fibonacci numbers
'''
Fibonacci numbers (Fibi) are defined as follows:
Fib1 = 1
Fib2 = 1
Fibi = Fibi-1 + Fibi-2  
==> cf processus.xls/Fibonacci 
'''


class Fib:
    def __init__(self, nn): # executes once
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self): # executes once
        print("__iter__")
        return self

    def __next__(self): # executes n+1*times for Fib(n) and returns n*times, n+1 is to break the iteration
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
# __init__
# __iter__
# __next__
# 1
# __next__
# 1
# __next__
# 2
# __next__
# 3
# __next__
# 5
# __next__
# 8
# __next__
# 13
# __next__
# 21
# __next__
# 34
# __next__
# 55
# __next__



### YIELD

# 1. provides the value of the expression specified after the yield keyword, just like return, 
#    but doesn't lose the state of the function
# 2. all the variables' values are frozen and wait for the next invocation, when the execution 
#    is resumed, not taken from scratch, like after return
# 3. The invocation will return the object's identifier, not the series we expect from the generator


# by principle an iterator should do that:
def fun(n):
    for i in range(n):
        return i # here the return breaks the loops at the first round
print(fun(4))
0
1
2
3    


# introduction to yield
def fun(n):
    for i in range(n):
        yield i # turns the function into a generator
print(fun(4))
# <generator object fun at 0x000001DD5B9EB850>


#==> build a generator
def powers_of_2(n):  
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
for v in powers_of_2(8):
    print(v)
# 1
# 2
# 4
# 8
# 16
# 32
# 64
# 128

# at the firts round, function starts, power = 1
# it reaches "yield power" and return 1, and stand by
# at the next iteration (with next() or in a loop) the fonction restarts just after the yield

def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c
for x in I():
    print(x, end='')
# ace


def fun(n):
    s = '+'  # applies
    for i in range(n):
        s += s
        yield s
for x in fun(2):
    print(x, end='');
# ++++++  ==> +(s)  ++(0)  ++++(1)


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
t = [x for x in powers_of_2(5)]
print(t)
# [1, 2, 4, 8, 16]


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
t = list(powers_of_2(5))
print(t)
# [1, 2, 4, 8, 16]


def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(8):
        print(i)
# 1
# 2
# 4
# 8
# 16


# Fibonacci again
def fibonacci(n):
    p2 = p1 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p2 + p1
            p1, p2 = p2, n
            yield n
 
fibs = list(fibonacci(10))
print(fibs)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
processus

n 	10										
p1	1										
p2  1										
i	             0	      1	      2      3	      4	      5	     6	     7	     8	     9	     10
i in[1,2]   	True	True	False	False	False	False	False	False	False	False	THE END
yield        	 1	      1									
n= p1 + p2			          2	     3	      5       8	     13 	 21	     34	     55	
p1  		                      1	     2	      3	      5	     8	     13      21	     34	
p2  			                  2	     3	      5	      8	     13	     21      34	     55	
yield n			              2	     3	      5	      8	     13	     21      34	     55	
'''



### List comprehension


## reminder
list_1 = []
for ex in range(6):
    list_1.append(10 ** ex)
print(list_1)
# [1, 10, 100, 1000, 10000, 100000]

list_2 = [10 ** ex for ex in range(6)] # shorter code
print(list_2)
# [1, 10, 100, 1000, 10000, 100000]



## turn any list comprehension into a generator

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
for v in the_list:
    print(v, end=" ")
# 1 0 1 0 1 0 1 0 1 0 
print(type(the_list))
# <class 'list'>
print(len(the_list))
# 10

the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
for v in the_generator:
    print(v, end=" ")
# 1 0 1 0 1 0 1 0 1 0 
print() 
print(type(the_generator))
# <class 'generator'>
print(len(the_generator))
# TypeError: object of type 'generator' has no len()


## LIST vs GENERATOR

# LIST
#   - syntax list comprehension []
#   - evaluate all evaluate allvalues and stores them
#   - Result : a list with x elements, here 10 ==> [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#   - consume more memory (store all elements)
#   - direct access thru indexing

# GENERATOR
#   - syntaxe is generative expression ()
#   - does not evaluate all values at once
#   - Result : a generator producing values at demand
#   - Less memory consumming
#   - Does not support indexation, only iteration


## Use case : big file processing

# Lets consider a very big file, many gigaoctets which want to analyse line by line without loading the whole file
# ==> Problem : risk to overuse the computing resource