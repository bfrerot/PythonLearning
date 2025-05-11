########## TUPLES ##########


## IMMUTABLES list: comme des Lists mais immuable cad on ne peut pas changer l'ordre contrairement 
# aux list qui peuvent etre sequentially moved
# Sera utilise pour s'assurer que la "list" ne bouge pas

## ON NE PEUT PAS append ou modify ou delete un element d'un tuple, 
# SEULEMENT ajouter des elements ou supprimer tout le tuple

# the len() function accepts tuples, and returns the number of elements contained inside

# the + operator can join tuples together
# the * operator can multiply tuples, just like lists;
# the in and not in operators work in the same way as in lists.
myTuple = (1, 10, 100)
t1 = myTuple + (1000, 10000)
t2 = myTuple * 3
print(t1)
print(t2)
# (1, 10, 100, 1000, 10000)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)

myTuple = ("a", [10, 100], 2.0)
myTuple2 = ("a",)
print(myTuple-myTuple2)
# TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'


## L'indexation fonctionne comme pour les list
myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(myTuple[3])    # outputs: [3, 4]


## tuple utilise parenthèses () ou simple suite de donnees separees par des virgules

tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125
#MAIS le print sera affiché avec des parenthèses
print(tuple1)
print(tuple2)
# (1, 2, 4, 8)
# (1.0, 0.5, 0.25, 0.125)


## SI tupple a une seule value, FINIR par un comma anyway
tupple3 = (1,)


## On peut printer a partir d'un tupple des int/float/str/list/tuple
myTuple = (1, 10, 100, 1000)
print(myTuple[0])
# 0 --> des int
print(myTuple[-1])
# 1000
print(myTuple[1:])
# (10, 100, 1000) --> des tuple
print(myTuple[:-2])
# (1, 10)

myTuple = ("a", [10, 100], 2.0)
print(type(myTuple[0]))
print(type(myTuple[1]))
print(type(myTuple[2]))
# <class 'str'>
# <class 'list'>
# <class 'float'>


## On peut ecraser un tup par une partie de lui-meme

tup = (1,2,4,8)
tup = tup [1:-1] # slicing on commence à 1 et on s'arrete avant -1
print (tup)
# (2,4)


## Faire un tuple à partir d'une list

my_tuple=tuple(['cat', 'dog', 5])
x=type(my_tuple)
print(x)
# <class 'tuple'>

l = ["car", "Ford", "flower", "Tulip"]
t = tuple(l)
print(t)
# ('car', 'Ford', 'flower', 'Tulip')


## Faire un dictionnary a partir d'un tuple

colors = (("green", "#008000"), ("blue", "#0000FF"))
colDict = dict(colors)
print(colDict)
# {'green': '#008000', 'blue': '#0000FF'}


print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)
# 9
# (1, 10, 100, 1000, 10000)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)
# True
# True


## On peut donner des valeurs a des variables via des tuples

tup = 1, 2, 3
a, b, c = tup
print(a * b * c)
# 6


## pour checker si on a une list un un tuple
list1 = [1,2,3]
tupple1 = 1, 2,3
print (type(list1))
print (type(tupple1))
# <class 'list'>
# <class 'tuple'>


## Compter les elem similaires dans un tuple

tuple = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tuple.count(2)
print (duplicates)
4 # il y a 4 "2" dans le tuple