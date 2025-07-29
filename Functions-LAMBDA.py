########## LAMBDA ##########  


# The lambda function is a concept borrowed from mathematics, more specifically, from a part called the Lambda calculus

# Mathematicians use the Lambda calculus in many formal systems connected with logic, recursion, or theorem provability
# Programmers use the lambda function to simplify the code, to make it clearer and easier to understand

# lambda function is a function without a name 
# It's not a problem, as we can name such a function if we really need, but in many cases the lambda function can exist and work while remaining fully incognito

# lambda function accept any number of argument(s)
# BUT lambda function can evaluate ONLY 1 expression

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))
# 4 4
# 1 1
# 0 0
# 1 1
# 4 4


## Pourquoi des parenthèses après two ?

# two = fonction elle-même = une référence à la fonction.
# two() = l’appel de la fonction qui exécute le code à l’intérieur (ici, return 2) et retourne la valeur

two = lambda: 2     # La fonction
print(two)          
# <function <lambda> at 0x000001AE9EAA8C20>  ==> référence à la fonction
print(two())    
# 2 ==> exécution de la fonction


## lambda n'accepte PAS de RETURN
# Lambda functions are single expressions, and return is not allowed inside them

lambda x, y: return x + y

# Correct way:
lambda x, y: x + y


## cas d'usage

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)
# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2    


## mélande de lambda et de fonction

def f(a, b):
    return a(b)
# La fonction f prend deux arguments : a (une fonction) et b (une valeur)

print(f(lambda x: x and True, 1 > 0))   
# ==> évalue x and True pour x = 1>0, = True, True and True = True
# True


# ==> avec LAMBDA
# pas besoin de créer la fonction poly() ==> remplacée par lambda x: 2 * x**2 - 4 * x + 2

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2

# ==> code has become shorter, clearer, and more legible


## LAMBDA + map()

# map()	# Returns the specified iterator with the specified function applied to each item

map(function, list)
# takes minimum two arguments but map() can accept more than two arguments:
#   - a function
#   - a list

# the second map() argument may be any entity that can be iterated: a tuple, or just a generator

# map() applies the function passed by its first argument to all its second argument's elements
# and returns an iterator delivering all subsequent function results
# We can use the resulting iterator in a loop, or convert it into a list using the list() functionl


def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
# <map object at 0x056D44F0>
print(list(x)) #convert the map into a list, for readability:
# [5, 6, 6]


letters = ["beach", "car"]
funified = list(map(lambda word: f"{word} is fun!", letters)) 
# Cette partie est une fonction anonyme (ou fonction lambda)
# Elle prend un argument word et retourne une nouvelle chaîne de caractères
print(funified)
# ['beach is fun!', 'car is fun!']


list_1 = [x for x in range(5)]
print(list_1)
# [0, 1, 2, 3, 4]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)
# [1, 2, 4, 8, 16]
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
# 1 4 16 64 256 


## LAMBDA + filter()

from random import seed, randint

seed() # vide ne sert pas à grand chose..Python produit une sequence différente sans seed()
# seed() sans argument permet d'obtenir une séquence différente de nombres aléatoires à chaque exécution du script
# seed(x), ex seed(42), la séquence sera toujours la même à chaque exécution, ce qui est utile pour la reproductibilité

data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))
print(data)
# [-6, 8, 0, -1, 9]
print(filtered)
# [8]

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x > 1, my_tuple))
print(foo)
# (2, 3, 4, 5, 6)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x: x-0 and x-1, my_tuple))
print(foo)
# (2, 3, 4, 5, 6)


numbers = [i*i for i in range(5)]              # 1. Génère une liste des carrés
foo = list(filter(lambda x: x % 2, numbers))   # 2. Filtre les nombres impairs
print(foo)                                     # 3. Affiche le résultat
# [1,9]

# Pour chaque x dans numbers :
# x = 0  → lambda 0: 0 % 2  → 0  → falsy → ❌ rejeté
# x = 1  → lambda 1: 1 % 2  → 1  → truthy → ✅ gardé  
# x = 4  → lambda 4: 4 % 2  → 0  → falsy → ❌ rejeté
# x = 9  → lambda 9: 9 % 2  → 1  → truthy → ✅ gardé
# x = 16 → lambda 16: 16 % 2 → 0  → falsy → ❌ rejeté


