########## LISTS ##########



### BASICS 

# The elements inside a list may have different types: integers, floats, lists, bool, complex dictionnaries
my_list=[1,2.3,True,1J,["a","b","c"], (1,), {1:"a", 2:"b"}]
print(my_list)
# [1, 2.3, True, 1j, ['a', 'b', 'c'], (1,), {1: 'a', 2: 'b'}]


# The elements in a list are always numbered starting from 0
# Lists can be nested, e.g.: myList = [1, 'a', ["list", 64, [0, 1], False]]
# Put into [] and separate by ,
my_list=[1,2,3] 
print (my_list)
# [1, 2, 3]



### INDEXATION


## indexation start from 0
my_list=[1,2,3]
print (my_list[0])
# 1


## indexation can be negative
numbers = [111, 7, 2, 1]
print(numbers[-1]) # = the last list element
# 1
numbers = [111, 7, 2, 1]
print(numbers[-2]) # = the penultimate list element
# 2


## Attribute values to variables from a list, uses indexation
# ! number of variables MUST BE EQUAL to the number of list elements
cat = ['fat', 'black', 'loud'] 
size, color, disposition = cat
print (size)
# fat

fruits = ("Apples", "Oranges", "Bananas")
a, b, c, d = fruits # d est en trop
print(b)
# ValueError: not enough values to unpack (expected 4, got 3)


## Replacement with indexation
# We CAN change an element in a list, it is NOT POSSIBLE with STRINGS
new_list = [1, 2, 3, 4, 5, 6]
new_list[0]=777
print(new_list)
# [777, 2, 3, 4, 5, 6]


## List with negative range
vowels = ["a", "e", "i", "o", "u"]
all = list (range(-2)) # de 0 à -2.. pas possible MAIS pas d'erreur
print(all) 
# []

myList = [10, 8, 6, 4, 2]
newList = myList[-1:1] # doesn't work
print(newList)
# []



### CONCATENATION

# , - / are not supported

## addition

my_list=[1,2,3]
my_other_list=[4, 5, 6]
print (my_list + my_other_list)
# [1, 2, 3, 4, 5, 6]

my_list=[1,2,3]
my_other_list=[4, 5, 6]
print (my_other_list + my_list) # result is linkeed to addition order
# [4, 5, 6, 1, 2, 3]


## multiplication

list1 = [1,2,3,4,5]
print (list1 * 3)
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]


## len()
# counts the list size, meaning number of elements
numbers = [10, 5, 7, 2, 1]
print ("List length:", len(numbers)) # printing the list's length
# List length: 5


## del
# Delete elements/list
del numbers[1] 
del numbers # remove all the list
del numbers[1:3] # delete a slice from element 1 to 2 as end (3) not included
del numbers [:] # remove all the elements NOT the list itself
 

## Checker si un element est dans la list ou pas, et attribuer un True/False en fonction
myList = [0, 3, 12, 8, 2]
print(5 in myList)
# False
print(5 not in myList)
# True
print(12 in myList)
# True



### LIST COPY

## id()

# built-in id() function returns the 'identity' of an object
# = integer, which is guaranteed to be unique and constant for this object DURING ITS LIFETIME
# Two objects with non-overlapping lifetimes may have the same id() value

a_list = [ 1, 'New York', 100]
print(id(a_list))
# 2616098317760

## Copy a list to point to the same memory id
list_2 = [1,2,3,4,5,6,7,8,9]
list_1 = list_2


## Copy a list with a separate memory id
list_1 = list_2[:] # whole list => cf SHALLOW vs DEEP copy


## Copy options with indexation => separate memory id as well
list_2 = [1,2,3,4,5,6,7,8,9]
list_1 = list_2[0:-1] # end NOT included
list_1 = list_2[1:] # end is last element = len(myList) - 1
list_1 = list_2[:-1] # start is first element = 0, end NOT included


## ==> SHALLOW copy = default

# immutable elements
list_2 = [1,2,3,4,5,6,7,8,9]
list_1 = list_2[:] # copy the list content, list_1 = list_2 BUT list_1 is not list_2
print(list_1)
# [1,2,3,4,5,6,7,8,9] => same elements than in list_1
list_1[0] = 100
print(list_1)
# [100,2,3,4,5,6,7,8,9]
print(list_2)
# [1,2,3,4,5,6,7,8,9] => list_2 unchanged

# nested mutable objects
a_list = [10, "banana", [997, 123]]
b_list = a_list[:]
print("a_list contents:", a_list)
# a_list contents: [10, 'banana', [997, 123]]
print("b_list contents:", b_list)
# b_list contents: [10, 'banana', [997, 123]]
print("Is it the same object?", a_list is b_list)
b_list[2][0] = 112  # => refers to a "nested mutable object" [997, 123]
print("a_list contents:", a_list)
# a_list contents: [10, 'banana', [112, 123]]
print("b_list contents:", b_list)
# # a_list contents: [10, 'banana', [112, 123]]  => a_list modified as well ?!!
print("Is it the same object?", a_list is b_list)
# Is it the same object? False                   => a_list != b_list

print(id(a_list = [ 1, 'New York', 100]))

#==> During a list copy, nested mutable objects keep the same memory id, BY DEFAULT, = SHALLOW COPY


## ==> DEEP copy

# If we want to make an independent copy of a compound object (list, dictionary, custom class instance) we should make use of deep copy:
#   - constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original
#   - takes more time to complete, as there are many more operations to be performed
#   - is implemented by the deepcopy() function, delivered by the python 'copy' module


import copy

a_list = [10, "banana", [997, 123]]
b_list = copy.deepcopy(a_list)  # Copie profonde

b_list[2][0] = 112
print("a_list:", a_list)  
# [10, 'banana', [997, 123]]    => unchanged
print("b_list:", b_list)  
# [10, 'banana', [112, 123]]    => modified


## to understand impact of copy type

import copy
import time

a_list = [(1,2,3) for x in range(1_000_000)]

# Single reference copy
time_start = time.time()
b_list = a_list
print('Execution time:', round(time.time() - time_start, 3))
# the process is starting, time = 1758101542.422257
print('Memory chunks:', id(a_list), id(b_list))
# Memory chunks: 3117412034816 3117412034816
print('Same memory chunk?', a_list is b_list)
# Same memory chunk? True


# Shallow copy
time_start = time.time()
b_list = a_list[:]
print('Execution time:', round(time.time() - time_start, 3))
# Execution time: 0.008
print('Memory chunks:', id(a_list), id(b_list))
# Memory chunks: 3117412034816 3117411886528
print('Same memory chunk?', a_list is b_list)
# Same memory chunk? False


# Deep copy
time_start = time.time()
b_list = copy.deepcopy(a_list)
print('Execution time:', round(time.time() - time_start, 3))
# Execution time: 3.471
print('Memory chunks:', id(a_list), id(b_list))
# Memory chunks: 3117412034816 3117414573952
print('Same memory chunk?', a_list is b_list)
# Same memory chunk? False



### LIST & LOOP

## Populate a list with a for loop
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


## Additionate elements with a for loop
myList = [10, 1, 8, 3, 5]
total = 0
for i in range(len(myList)):
    total += myList[i]
print(total)
# 27

# builtin sum() is here for that
hat_list = [1, 2, 3, 4, 5]
print (sum(hat_list))
# 15



### USE CASES
## find a list elem in a list and give its position (index)
toFind = int(input("Which number are you looking for?: "))
myList = [1, 2, 3, 4, 5, 4, 6, 7, 8, 9, 10]
for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break
if found:
    print("Element found at index", i) # i value is kept
else:
    print("Element absent")
# Element found at index 4


# find the bigger number in a list
myList = [1, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in range(1, len(myList)): 
    if myList[i] > largest:
        largest = myList[i]
print(largest)
# 15


# inverse elements position
my_list = []
for e in range (1,100):
    my_list.append(e)
print (my_list)
length = len(my_list)
print (length)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# 99
# [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


## Bubble sort List : ordonate list elements with an algorithm
# version simple
my_list = [8, 10, 6, 2, 4]  # list to sort
for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.
print(my_list)
# [8, 6, 2, 4, 10]


# with user interaction
my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
# How many elements do you want to sort: 10
# Enter a list element: 3
# Enter a list element: 2
# Enter a list element: 98
# Enter a list element: 45
# Enter a list element: 34
# Enter a list element: 23
# Enter a list element: 67
# Enter a list element: 65
# Enter a list element: 44
# Enter a list element: 34
# [2.0, 3.0, 23.0, 34.0, 34.0, 44.0, 45.0, 65.0, 67.0, 98.0]


# list elem and classify them from biggest to smallest
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


# Remove duplicates from a list
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
for number in myList:  # Browse all numbers from the source list.
	if number not in newList:  # If the number doesn't appear within the new list...
		newList.append(number)  # ...append it here.
print("The list with unique elements only:")
print(newList)
[1, 2, 4, 6, 9]


# Create a chess game
EMPTY = "-"
BROOK = "BROOK"
BPAWN = "BPAWN"
BKNIGHT = "BKNIGHT"
BBISHOP = "BBISHOP"
BQUEEN = "BQUEEN"
BKING = "BKING"
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    print(row)
    board.append(row)
print()
print("Now let's place the the pieces")
# THE BLACKS
board[0][0] = board[0][7] = BROOK
board[0][1] = board[0][6] = BKNIGHT
board[0][2] = board[0][5] = BBISHOP
board[0][3] = BQUEEN
board[0][4] = BKING
board[1] = [BPAWN] * 8
# THE WHITES
board[7][0] = board[7][7] = BROOK
board[7][1] = board[7][6] = BKNIGHT
board[7][2] = board[7][5] = BBISHOP
board[7][3] = BQUEEN
board[7][4] = BKING
board[6] = [BPAWN] * 8

for row in board:
    print(row)

# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
#
# Now let's place the the pieces
# ['BROOK', 'BKNIGHT', 'BBISHOP', 'BQUEEN', 'BKING', 'BBISHOP', 'BKNIGHT', 'BROOK']
# ['BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['-', '-', '-', '-', '-', '-', '-', '-']
# ['BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN', 'BPAWN']
# ['BROOK', 'BKNIGHT', 'BBISHOP', 'BQUEEN', 'BKING', 'BBISHOP', 'BKNIGHT', 'BROOK']

 
# nested lists
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


# Hotel rooms management
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
print (rooms)
# [[[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]], [[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]]

rooms[1][9][13] = True  # if we want to select room 14 floor 10 aisle 2
print (rooms[1][9][13])
# True  => was False

 
 ## list as a function parameter

def sumOfList(lst):
    sum = 0
    for elem in lst:
        sum += elem
    return sum
print(sumOfList([5, 4, 3]))
# 12


## list as a function result

def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.insert(0, i)
    return strangeList
print(strangeListFunction(5))
# [4, 3, 2, 1, 0]

# OR

def strangeListFunction(n):
    strangeList = []
    for i in range(0, n):
        strangeList.append(i)
    return strangeList
print(strangeListFunction(5))
# [0, 1, 2, 3, 4]


## Convert into a list
list(('cat', 'dog', 5)) # from tuple to a list
['cat', 'dog', 5] 

list('hello') # from string to a list
['h', 'e', 'l', 'l', 'o']


## min() - max()

# numeric values
a=1
b=2
c=3
t = [a,b,c]
print(t)
# [1, 2, 3]
print(min(t))
# 1

# ASCII values
t = ["a","b","c"]  
print(t)
# ['a', 'b', 'c']
print(min(t))
# a

t = ["1","2","3"] 
print(t)
# ['1', '2', '3']
print(min(t))
# 1