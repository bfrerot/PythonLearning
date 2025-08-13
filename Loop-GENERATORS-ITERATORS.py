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
    def __init__(self, nn): # s'execute 1 fois
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self): # s'execute 1 fois
        print("__iter__")
        return self

    def __next__(self): # s'execute n+1*fois pour Fib(n) et fais return n*fois, le n+1 pour casser l'itération
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


# par principe un iterator devrait faire çà
def fun(n):
    for i in range(n):
        return i # ici le retrun casse la boucle dès le premier tour
print(fun(4))
0
1
2
3    


# introduction de yield
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

# Lors du premier appel (par exemple, dans une boucle), la fonction démarre, power = 1
# Elle atteint "yield power" : elle renvoie 1 et se met en pause
# La prochaine fois que l'on demande une valeur (avec next() ou dans une boucle) la fonction reprend juste après le yield

def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c
for x in I():
    print(x, end='')
# ace


def fun(n):
    s = '+'  # pris en compte 
    for i in range(n):
        s += s
        yield s
for x in fun(2):
    print(x, end='');
# ++++++  ==> +  ++(0)  ++++(1)


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


## rappel
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
print() # va à la ligne car on a mis " " comme end au-dessus
print(type(the_generator))
# <class 'generator'>
print(len(the_generator))
# TypeError: object of type 'generator' has no len()


## LIST vs GENERATOR

# LIST
#   - La syntaxe ici est une list comprehension []
#   - évalue toutes les valeurs immédiatement et stocke tous les éléments en mémoire
#   - Résultat : une liste contenant x éléments, ici 10 - [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#   - Consomme plus de mémoire (stocke tous les éléments)
#   - Accès direct via index

# GENERATOR
#   - La syntaxe est une expression génératrice ()
#   - ne calcule pas immédiatement tous les éléments
#   - Résultat : un objet générateur qui produit les valeurs à la demande
#   - Moins de mémoire, car il génère un élément à la fois
#   - Ne supporte pas l'indexation, uniquement l'itération


## Cas d'usage : traitement d’un fichier très volumineux

# Supposons un très gros fichier texte (par exemple plusieurs gigaoctets) que l'on souhaite analyser ligne par ligne
# sans charger tout le fichier en mémoire.
# ==> Problème : si le fichier est énorme cela peut consommer beaucoup de mémoire ou même faire planter votre programme