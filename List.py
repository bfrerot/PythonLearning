########## LISTS

# The elements inside a list may have different types: integers, floats, lists.
# The elements in a list are always numbered starting from 0
# Lists can be nested, e.g.: myList = [1, 'a', ["list", 64, [0, 1], False]]
# Mettre entre crochets [], séparés par une ,
my_list=[1,2,3] 
print (my_list)
[1, 2, 3]


### INDEXATION

# L'indexation des elements commence à 0
my_list=[1,2,3]
print (my_list[0])
# 1

# L'indexation peut etre négative
numbers = [111, 7, 2, 1]
print(numbers[-1]) # = le dernier élément de la liste
# 1
numbers = [111, 7, 2, 1]
print(numbers[-2]) # = l'avant-dernier élément de la liste
# 2


# Donner une valeur a des variables a partir d'une list, en // de l'indexation
cat = ['fat', 'black', 'loud'] 
size, color, disposition = cat
print (size)
# fat

# Remplacement avec indexation
# On peut changer un element dans la liste (contrairement à un string)
new_list = [1, 2, 3, 4, 5, 6]
new_list[0]=777
print(new_list)
# [777, 2, 3, 4, 5, 6]


### Concatenation, - and / are not supported

# ADDITION
my_list=[1,2,3]
my_other_list=[4, 5, 6]
print (my_list + my_other_list)
# [1, 2, 3, 4, 5, 6]
new_list = my_list + my_other_list
print (new_list)
# [1, 2, 3, 4, 5, 6]
new_list = my_other_list + my_list 
print (new_list)
# [4, 5, 6, 1, 2, 3]


#MULTIPLICATION
list1 = [1,2,3,4,5]
print (list1 * 3)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]




# Mesurer la taille de la liste = compter le nbre d 'elements
numbers = [10, 5, 7, 2, 1]
print ("List length:", len(numbers)) # printing the list's length
# List length: 5


# Deleter des elements
del numbers[1] 
del numbers # remove all the list
del numbers[1:3] # delete a slice from element 1 to 2 as end (3) not included
del numbers [:] # remove all the elements NOT the list itself
 

# RAPPEL - si des list sont liees par une egalite, alors elles sont storees au meme endroit meme si elles on nom different
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2
print(l1)
print(l2)
print(l3)
# ["A", "B", "C"]
# ["A", "B", "C"]
# ["A", "B", "C"]
del l1[0] # modifie l1 + l2 + l3
del l2 # ne delete pas l1 et l3
print (l1)
print(l3)
print(l2)
# ['B', 'C']
# ['B', 'C']
# Traceback (most recent call last):
#   File "c:\PythonLearning\bac-à-sable.py", line 11, in <module>
#     print(l2)
#           ^^
# NameError: name 'l2' is not defined. Did you mean: 'l1'?


# Populer une list avec une boucle for
myList = [] # creating an empty list
for i in range(5): # loop to insert elements
    myList.append(i + 1)
print(myList)
# [1,2,3,4,5]

lst = [i for i in range (-1,2)] # the first argument determines the initial (first) value of the control variable
print (lst)
#[-1, 0, 1]


lst = [[0,1,2,3] for i in range (2)]
print (lst)
#[[0, 1, 2, 3], [0, 1, 2, 3]]


# Additionner les elements d'une liste avec une boucle for
myList = [10, 1, 8, 3, 5]
total = 0
for i in range(len(myList)):
    total += myList[i]
print(total)
# 27


# Copier une list avec un emplacement mémoire séparé
# Si on ajoute pas [:] les deux listes partageront le meme emplacement memoire meme si elles
# ont un nom different et ont l air de deux list differentes
myList[start:end] # end NOT included
myList[start:] # end is last element = len(myList) - 1
myList[:end] # start is first element = 0, end NOT included
myList[:] # whole list

list1 = [1]
list2 = list1[:] # Copying the whole list, but in separate memory
list1[0] = 2
print(list2)
# [1]

myList = [10, 8, 6, 4, 2]
newList = myList[0:1] # Copying part of the list
print(newList)
# [10]


# attention end ne peut pas etre situe avant start
myList = [10, 8, 6, 4, 2]
newList = myList[-1:1] # doesn't work
print(newList)
[0]


# Checker si un element est dans la list ou pas, et attribuer un True/False en fonction
myList = [0, 3, 12, 8, 2]
print(5 in myList)
print(5 not in myList)
print(12 in myList)
# False
# True
# True


# trouver une elem dans un liste et donner sa position
toFind = int(input("Which number are you looking for?: "))
myList = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10]
for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break
if found:
    print("Element found at index", i)
else:
    print("Element absent")


# Trouver le plus large number d'une liste
myList = [1, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in range(1, len(myList)): 
    if myList[i] > largest:
        largest = myList[i]
print(largest)
# 15


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
# Step 1: ['John Lennon', 'Paul McCartney', 'George Harrison']
# Quel autre membre a rejoint le groupe ?Stu Sutcliffe
# Step 2/3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe']
# Quel autre membre a rejoint le groupe ?Pete Best
# Step 2/3: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Stu Sutcliffe', 'Pete Best']
# Step 4: ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Star']
# The Fab 4


# Buble sort List : ordonner les elements d une liste avec un algorithme
myList = [8, 10, 6, 2, 4]  # Liste à trier
swapped = True
pass_num = 0  # Pour compter les passages
print("Liste initiale:", myList)
print("Début du tri...\n")
while swapped:
    swapped = False
    pass_num += 1
    print(f"--- Passage numéro {pass_num} ---")
    for i in range(len(myList) - 1):
        print(f"Comparaison entre {myList[i]} et {myList[i + 1]}")
        if myList[i] > myList[i + 1]:
            print(f"  ➤ Échange: {myList[i]} ↔ {myList[i + 1]}")
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
            swapped = True
            print("  Liste actuelle:", myList)
        else:
            print("  ➤ Pas d'échange")
    print("État de la liste après ce passage:", myList, "\n")

print("✅ Tri terminé ! Liste finale:", myList)
# Liste initiale: [8, 10, 6, 2, 4]
# Début du tri...
# 
# --- Passage numéro 1 ---
# Comparaison entre 8 et 10
#   ➤ Pas d'échange
# Comparaison entre 10 et 6
#   ➤ Échange: 10 ↔ 6
#   Liste actuelle: [8, 6, 10, 2, 4]
# Comparaison entre 10 et 2
#   ➤ Échange: 10 ↔ 2
#   Liste actuelle: [8, 6, 2, 10, 4]
# Comparaison entre 10 et 4
#   ➤ Échange: 10 ↔ 4
#   Liste actuelle: [8, 6, 2, 4, 10]
# État de la liste après ce passage: [8, 6, 2, 4, 10]
# 
# --- Passage numéro 2 ---
# Comparaison entre 8 et 6
#   ➤ Échange: 8 ↔ 6
#   Liste actuelle: [6, 8, 2, 4, 10]
# Comparaison entre 8 et 2
#   ➤ Échange: 8 ↔ 2
#   Liste actuelle: [6, 2, 8, 4, 10]
# Comparaison entre 8 et 4
#   ➤ Échange: 8 ↔ 4
#   Liste actuelle: [6, 2, 4, 8, 10]
# Comparaison entre 8 et 10
#   ➤ Pas d'échange
# État de la liste après ce passage: [6, 2, 4, 8, 10]
# 
# --- Passage numéro 3 ---
# Comparaison entre 6 et 2
#   ➤ Échange: 6 ↔ 2
#   Liste actuelle: [2, 6, 4, 8, 10]
# Comparaison entre 6 et 4
#   ➤ Échange: 6 ↔ 4
#   Liste actuelle: [2, 4, 6, 8, 10]
# Comparaison entre 6 et 8
#   ➤ Pas d'échange
# Comparaison entre 8 et 10
#   ➤ Pas d'échange
# État de la liste après ce passage: [2, 4, 6, 8, 10]
# 
# --- Passage numéro 4 ---
# Comparaison entre 2 et 4
#   ➤ Pas d'échange
#   ➤ Pas d'échange
#   ➤ Pas d'échange
# Comparaison entre 4 et 6
#   ➤ Pas d'échange
# Comparaison entre 4 et 6
# Comparaison entre 4 et 6
#   ➤ Pas d'échange
#   ➤ Pas d'échange
# Comparaison entre 6 et 8
#   ➤ Pas d'échange
# Comparaison entre 8 et 10
# Comparaison entre 8 et 10
#   ➤ Pas d'échange
# État de la liste après ce passage: [2, 4, 6, 8, 10]
# État de la liste après ce passage: [2, 4, 6, 8, 10]
# 
# ✅ Tri terminé ! Liste finale: [2, 4, 6, 8, 10]



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
# How many elements do you want to sort: 5
# Enter a list element: 5
# Enter a list element: 4
# Enter a list element: 3
# Enter a list element: 2
# Enter a list element: 1
# 
# Sorted:
# [1.0, 2.0, 3.0, 4.0, 5.0]


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
# [['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'],
#  ['-', '-', '-', '-', '-', '-', '-', '-'], 
#  ['ROOK', '-', '-', '-', '-', '-', '-', 'ROOK']]

 
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
print(cube[0][0][0])
print(cube[2][2][0])
# [[[':(', 'x', 'x'], [':)', 'x', 'x'], [':(', 'x', 'x']], [[':)', 'x', 'x'], [':(', 'x', 'x'], [':)', 'x', 'x']], [[':(', 'x', 'x'], [':)', 'x', 'x'], [':)', 'x', 'x']]]
# :(
# :)


# Repertorier toutes les chambres d un hotel a 3 batiments de 15 etages de 20 chambres
# avec boucle for comme elem de la list
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print (rooms)
rooms[1][9][13] = True  # si on veut occuper la chambre 14 etage 10 bat 2
print (rooms)
print (rooms[1][9][13])
# [[[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]]
# [[[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]]
# True
 
 
# list comme parameter d'une function - faire la somme des elem d une list

def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum
print(sumOfList([5, 4, 3]))
# 12


# list comme result d'une function

def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList
print(strangeListFunction(5))
# [4, 3, 2, 1, 0] # insert a chaque fois a la place du premier

OU

def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.append(i)
    return strangeList
print(strangeListFunction(5))
# [0, 1, 2, 3, 4] # on append a la suite


## Convertir en list
list(('cat', 'dog', 5)) # tuple en list
['cat', 'dog', 5] 

list('hello') # string en list
['h', 'e', 'l', 'l', 'o']


## min() - max()

a=1
b=2
c=3
t = [a,b,c]
print(t)
print(min(t))
# [1, 2, 3]
# 1

t = ["a","b","c"] # si a b et c sont des lettres
print(t)
print(min(t))
# ['a', 'b', 'c']
# a
t = ["1","2","3"] # si a b et c sont des lettres, error
print(t)
print(min(t))
# ['1', '2', '3']
# 1