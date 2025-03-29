------- TUPLES -------

IMMUTABLES list: comme des Lists mais immuable cad on ne peut pas changer l'ordre contrairement aux list qui peuvent etre sequentially moved
Sera utilise pour s'assurer que la "list" ne bouge pas

Pour connaitre le type de data
type(('hello',)) 
<class 'tuple'>  
type(('hello')) 
<class 'str'>


L'indexation fonction comme pour les list
myTuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(myTuple[3])    # outputs: [3, 4]

list utilise des [], tupple utilise parenthèses () ou simple suite de donnees separees par des virgules
tuple1 = (1, 2, 4, 8)
tuple2 = 1., .5, .25, .125
MAIS le print sera affiché avec des parenthèses
print(tuple1)
print(tuple2)
(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)

ON NE PEUT PAS append ou modify ou delete un element d'un tuple, SEULEMENT ajouter des elements ou supprimer tout le tuple

SI tupple a une seule value, FINIR par un comma anyway
tupple3 = (1,)


# On peut printer des list a partir d'un tupple
myTuple = (1, 10, 100, 1000)

print(myTuple[0])
print(myTuple[-1])
print(myTuple[1:])
print(myTuple[:-2])

for elem in myTuple:
    print(elem)
1
1000
(10, 100, 1000)
(1, 10)
1
10
100
1000


# On peut ecraser un tup par une partie de lui-meme

tup = (1,2,4,8)
tup = tup [1:-1]
print (tup)
(2,4)


# on peut tupliser une list

tuple(['cat', 'dog', 5])
 ('cat', 'dog', 5) 


the len() function accepts tuples, and returns the number of elements contained inside;
the + operator can join tuples together
the * operator can multiply tuples, just like lists;
the in and not in operators work in the same way as in lists.

myTuple = (1, 10, 100)
t1 = myTuple + (1000, 10000)
t2 = myTuple * 3
print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)
9
(1, 10, 100, 1000, 10000)
(1, 10, 100, 1, 10, 100, 1, 10, 100)
True
True


# On peut ecraser la valeur d'un tupple par un autre comme avec les variables et les listst1 = (1, )
t2 = (2, )
t1 = t2
print (t1)
(2,)


# On peut donner des valeurs a des variables via des tuples

tup = 1, 2, 3
a, b, c = tup

print(a * b * c)
6

# pour checker si on a une list un un tuple
list1 = [1,2,3]
tupple1 = 1, 2,3
print (type(list1))
print (type(tupple1))
<class 'list'>
<class 'tuple'>


# Faire une list a partir d un tuple

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)
('car', 'Ford', 'flower', 'Tulip')


# Faire un dictionnary a partir d'un tuple

colors = (("green", "#008000"), ("blue", "#0000FF"))

colDict = dict(colors)
print(colDict)
{'green': '#008000', 'blue': '#0000FF'}


# Faire une tuple a partir d'une list

a = "car", "Ford", "flower", "Tulip"

b = list(a)
print(b)
['car', 'Ford', 'flower', 'Tulip']


# Compter les elem similaires dans un tuple

tuple = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tuple.count(2)
print (duplicates)
4 # il y a 4 "2" dans le tuple

# You can also create a tuple using a Python built-in function called tuple()
myTup = tuple((1, 2, "string"))
print(myTup)

lst = [2, 4, 6]
print(lst)    # outputs: [2, 4, 6]
print(type(lst))    # outputs: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

tup = 1, 2, 3, 
lst = list(tup)
print(type(lst))    