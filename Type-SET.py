########## SET ##########

# Sets are used to store multiple items in a single variable
# Set is one of 4 built-in data types in Python used to store collections of data
#   the other 3 are List, Tuple, and Dictionary, all with different qualities and usage

# ==> A set is a collection which is unordered, unchangeable, unindexed, do not accept duplicates
# ==> Once a set is created we cannot change its items but we can remove items and add new items

# create an empty set
myset = set()
print(myset)
# set()

# add an elem
myset.add(1)
print(myset)
# {1}

myset.add(2)
print(myset)
# {1, 2}

# trying to add a duplicate
myset.add(2)
print(myset)
# {1, 2} ==> 2 déjà présent, PAS DE DOUBLON, pas d'erreur non plus

mylist = [1,1,1,2,2,2,3,3,3]
set1 = set(mylist)
print(set1)
# {1, 2, 3} # PAS DE DOUBLON

# remove un elem
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
# {'apple', 'cherry'}



## data dans les set

# string
set1 = {"apple", "banana", "cherry"}
print(set1)
# {'apple', 'banana', 'cherry'}

# int
set2 = {1, 5, 7, 9, 3}
print(set2)
# {1, 3, 5, 7, 9}

# float
set5 = {1.1, 5.5, 7.7, 9.9, 3.3}
print(set5)
# {1.1, 3.3, 5.5, 7.7, 9.9}

# boolean
set3 = {True, False, False}
print(set3)
# {False, True}

# mix
set4 = {"abc", 34, True, 40, "male"}
print(set4)
# {True, 34, 'male', 'abc', 40}



## len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# 3



## type()
myset = {"apple", "banana", "cherry"}
print(type(myset))
# <class 'set'>



## set() constructor

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# {'apple', 'banana', 'cherry'}



## Reminder ==> Python Collections (Arrays)
# There are 4 collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members
# Dictionary is a collection which is ordered** and changeable. No duplicate members