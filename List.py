#  ------- LISTS -------

The elements inside a list may have different types. Some of them may be integers, others floats,
and yet others may be lists.

The elements in a list are always numbered starting from zero

Lists can be nested, e.g.: myList = [1, 'a', ["list", 64, [0, 1], False]]

The assignment: list2 = list1 copies the name of the array, not its contents.
In effect, the two names (list1 and list2) identify
the same location in the computer memory. Modifying one of them affects the other,
and vice versa.


# Mettre entre crochets []
my_list=[1,2,3] 
print (my_list)
[1, 2, 3]

# Indexation des elements commence à 0
my_list=[1,2,3]
print (my_list[0])
1

0 = premier
-1 = dernier
-2 = avant-dernier

# Concatenation, - and / are not supported
my_list=[1,2,3]
my_other_list=[4, 5, 6]
print (my_list + my_other_list)
[1, 2, 3, 4, 5, 6]
new_list = my_list + my_other_list
print (new_list)
[1, 2, 3, 4, 5, 6]

list1 = [1,2,3,4,5]
print (list1 * 3)
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


# Donner une valeur a des variables a partir d'une list
cat = ['fat', 'black', 'loud'] 
size, color, disposition = cat
print (size)
fat


# Remplacement avec indexation
On peut changer un element dans la liste (contrairement à un string)
new_list[0]=777
new_list
[777, 2, 3, 4, 5, 6]


# Append -- ajoute un element a la fin de list
new_list.append(7)
new_list
[777, 2, 3, 4, 5, 6, 7]


# Insert
numbers.insert(0, 222) # ajoute un element a la place du premier element par 222

listeA.insert(0; 'element') # insert ajoute à un emplacement donné


# Popper des elements, efface le dernier de le list par defaut ou par indexation
new_list = [777, 2, 3, 4, 5, 6, 7]
new_list.pop()
print (new_list)
[777, 2, 3, 4, 5, 6]

# On peut creer avec/attribuer a une variable l'element poppé
popped_item = new_list.pop()
print (popped_item)
5


# Classer par ordre alphabetique ou de grandeur
new_list = ['a','e','x','b','c']
new_list.sort()
print (new_list)
['a', 'b', 'c', 'e', 'x']

myList = [8, 10, 6, 2, 4]
myList.sort()
print (myList)
[2, 4, 6, 8, 10]


# Inverser les positions
Inverser la position
lst = [5, 3, 1, 2, 4]
lst.reverse()
print(lst)
[4, 2, 1, 3, 5]


# Mesurer la taille de la liste = nbre d 'elements
numbers = [10, 5, 7, 2, 1]
print ("List length:", len(numbers)) # printing the list's length
List length: 5


# Deleter des elements
del numbers[1] 
del numbers # remove all the list
del numbers[1;3] # delete a slice from element 1 to 2 as end (3) not included
del numbers [:] # remove all the elements NOT the list itself
 
# on ne peut pas réassigner le resultat d'un .sort() comme ci-dessous
my_sorted_list=[]
new_list=[e,d,c,b,a]
my_sorted_list = new_list.sort() 
print (new_list)
print (my_sorted_list)

# RAPPEL - si des list sont liees par une egalite, alors elles sont storees au meme endroit meme si elles on nom different
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2
del l1[0]
del l2 # ne delete pas l1 et l3
print(l3)
["B", "C"]
print(l2)
error

# Populer une list avec une boucle for
myList = [] # creating an empty list
for i in range(5): # loop to insert elements
    myList.append(i + 1)
print(myList)
[1,2,3,4,5]


# Compter les elem similaires dans une liste
list = [1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9]
duplicates = list.count(2)
print (duplicates)
4 # il y a 4 "2" dans la list


# Additionner les elements d une liste avec une boucle for
myList = [10, 1, 8, 3, 5]
total = 0
for i in range(len(myList)):
    total += myList[i]
print(total)
27


# Inverser la position des elements d une liste

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)
[5,3,8,1,10]


# Copier une list
Si on ajoute pas [:] les deux listes partageront le meme emplacement memoire meme si elles
ont un nom different et ont l air de deux list differentes
myList[start:end] # end NOT included
myList[start:] # end is last element = len(myList) - 1
myList[:end] # start is first element = 0
myList[:] # whole list


list1 = [1]
list2 = list1[:] # Copying the whole list
list1[0] = 2
print(list2)
1

myList = [10, 8, 6, 4, 2]
newList = myList[0:1] # Copying part of the list
print(newList)
[10]


# attention end ne peut pas etre situe avant start
myList = [10, 8, 6, 4, 2]
newList = myList[-1:1] # doesn't work
print(newList)
[0]


# Checker si un element est dans la list ou pas et attribuer un True/False
myList = [0, 3, 12, 8, 2]
print(5 in myList)
print(5 not in myList)
print(12 in myList)
False
True
True


# trouver une elem dans un liste et donner sa position
myList = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10]
toFind = 5
found = False
for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break
if found:
    print("Element found at index", i)
else:
    print("absent")
Element found at index 4

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
for number in bets:
    if number in drawn:
        hits += 1
		print(hits)
4


# Trouver le plus large number d une liste
myList = [1, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in range(1, len(myList)): 
    if myList[i] > largest:
        largest = myList[i]
print(largest)
15



# Evolution du groupe des Beatles
beatles = []
beatles.append ("John Lennon")
beatles.append ("Paul McCartney")
beatles.append ("George Harrison")
print("Step 1:", beatles)
length = len(beatles)
for length in range (3,5):
    beatles.append (input("Quel autre membre a rejoint le groupe ?"))
    print("Step 2/3:", beatles) # add Stu Sutcliffe and Pete Best
del beatles[-1]
del beatles[-1]
beatles.append ("Ringo Star")
print("Step 4:", beatles)
print("The Fab", len(beatles))

Step 1: ['John Lennon', 'Paul McCartney', 'George Harrison']
Quel autre membre a rejoint le groupe ?Stu Sutcliffe
Step 2/3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe']
Quel autre membre a rejoint le groupe ?Pete Best
Step 2/3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']
Step 4: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']
The Fab 4


# Buble sort List : ordonner les elements d une liste avec un algorithme
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop
while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            print(myList)
[8, 6, 10, 2, 4]
[8, 6, 2, 10, 4]
[8, 6, 2, 4, 10]
[6, 8, 2, 4, 10]
[6, 2, 8, 4, 10]
[6, 2, 4, 8, 10]
[2, 6, 4, 8, 10]
[2, 4, 6, 8, 10] # apres swapped passe en #false et la boucle s'arrete


# lister des elem donnes et les classer du plus petit au plus grand
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))
for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)
while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
print("\nSorted:")
print(myList)
How many elements do you want to sort: 5
Enter a list element: 5
Enter a list element: 4
Enter a list element: 3
Enter a list element: 2
Enter a list element: 1

Sorted:
[1.0, 2.0, 3.0, 4.0, 5.0]


# Enlever les doublons d une liste
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in myList:  # Browse all numbers from the source list.
	if number not in newList:  # If the number doesn't appear within the new list...
		newList.append(number)  # ...append it here.
print("The list with unique elements only:")
print(newList)
[1, 2, 4, 6, 9]


# Creer table jeu d'echecs
EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)
[['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'],
 ['-', '-', '-', '-', '-', '-', '-', '-'], 
 ['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK']]

 
# list composee d'autres list - Exemple du cube
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
print(cube)
print(cube[0][0][0]) # outputs: ':('
print(cube[2][2][0]) # outputs: ':)'
:(
:)


# Repertorier toutes les chambres d un hotel a 3 batiments de 15 etages de 20 chambres
# avec boucle for comme elem de la list
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
# rooms[1][9][13] = True  --> si on veut occuper la chambre 14 etage 10 bat 2
print (rooms)
[[[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], 
 [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], 
 [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] 
 [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]]
 
 
 
# list comme parameter d'une function - faire la somme des elem d une list

def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
print(sumOfList([5, 4, 3]))
12


# list comme result d'une function

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))
[4, 3, 2, 1, 0] # insert a chaue fois a la place du premier

OU

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.append(i)
    
    return strangeList

print(strangeListFunction(5))
[0, 1, 2, 3, 4] # on append a la suite


# SETs - serie d'items uniques

>>> myset = set()
>>> myset.add(1)
>>> myset
set([1])
>>> myset.add(2)
>>> myset
set([1, 2])
>>> myset.add(2)

>>> mylist = [1,1,1,2,2,2,3,3,3]
>>> set(mylist)
set([1, 2, 3])

Pas de répétition


### METHODS LISTS ###


## list.index

spam = ['hello', 'hi', 'howdy', 'heyas'] 
print (spam.index('hello'))
0

# if same value many times in a list, ONLY the first is taken in account

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka'] 
spam.index('Pooka')
1


## list.append

spam = ['cat', 'dog', 'bat'] 
spam.append('moose')
print (spam)
['cat', 'dog', 'bat', 'moose']


## list.insert(index,"string")

spam = ['cat', 'dog', 'bat'] 
spam.insert(1, 'chicken') 
print (spam)
['cat', 'chicken', 'dog', 'bat']

 
#Note the spam = spam.insert() or spam>append() value is None


## list.remove

spam = ['cat', 'bat', 'rat', 'elephant'] 
spam.remove('bat') 
print (spam)
['cat', 'rat', 'elephant']

# if same value many times in a list, ONLY the first is taken in account

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
for cat in spam:
    spam.remove('cat')
print (spam)
['bat', 'rat', 'hat']


## list.sort

# PYTHON2
si list contient str et int, les int seront avant les str
spam = ['cat', 1, 'rat', 2,'cat',3,  'cat'] 
spam.sort()
print (spam)
[1, 2, 3, 'cat', 'cat', 'cat', 'rat']
NE MARCHE PAS EN PYTHON3 !!!

ou en decroissant avec sort(reverse=True)
spam = ['cat', 'rat', 'cat', 'cat'] 
spam.sort(reverse=True)
print (spam)
['rat', 'cat', 'cat', 'cat']

les str en MAJ sont avant les str en min
spam = ['a', 'z', 'A', 'Z'] 
spam.sort() 
print(spam) 
['A', 'Z', 'a', 'z']

# UTILISER key=str.lower pour classer par ordre alphabetique, min/MAJ
spam = ['a', 'z', 'A', 'Z'] 
spam.sort(key=str.lower) 
print(spam)
['a', 'A', 'z', 'Z']


# Convertir en list

list(('cat', 'dog', 5)) # tuple en list
['cat', 'dog', 5] 

list('hello') # string en list
['h', 'e', 'l', 'l', 'o']


# .join() - joindre des données et possibilité d'insérer des caracteres entre

print ('ABC'.join(['My', 'name', 'is', 'Simon']))
MyABCnameABCisABCSimon

print (' '.join(['My', 'name', 'is', 'Simon']))
My name is Simon 

commands = ['conf t', 'int gi0/0', 'shut', 'no shut']
print('\n'.join(commands))

conf t
int gi0/0
shut
no shut


## min() - max()

a=1
b=2
c=3
t = [a,b,c]
print(t)
print(min(t))
[1, 2, 3]
1

t = [a,b,c] # si a b et c sont des lettres, error
print(t)
print(min(t))
[1, 2, 3]
1
Traceback (most recent call last):

  File "main.py", line 1, in <module>

    t = [a,b,c]

NameError: name 'a' is not defined

 