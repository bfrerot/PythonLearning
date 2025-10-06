######## METHODS LISTS ########


## .append()
# add an element at the END of the list

list=[777, 2, 3, 4, 5, 6]
list.append(7)
print(list)
# [777, 2, 3, 4, 5, 6, 7]

spam = ['cat', 'dog', 'bat'] 
spam.append('moose')
print (spam)
# ['cat', 'dog', 'bat', 'moose']

groceries_list1 = ["Milk", "Cheese"]
groceries_list2 = ["Bread", "Butter"]
groceries_list1.append(groceries_list2)
print(groceries_list1)
['Milk', 'Cheese', ['Bread', 'Butter']] # append a list not the list elements
# ==> if we want to add a list's element we must use EXTEND



## .clear()
# clear all list's elements but does not delete the list itselfe
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
# []



## .copy()
# copy a list's element in an other DISTINCT list
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)
# ["apple", "banana", "cherry"]
print( fruits is x)
# False



## .count(value)
# count the value occurences into the list
fruits = ["apple", "banana", "cherry"]
x = fruits.count("apple")
print(x)
# 1

# giving a value is mandatory
fruits = ["apple", "banana", "cherry"]
x = fruits.count()
print(x)
# Traceback (most recent call last):
#  File "./prog.py", line 3, in <module>
# TypeError: list.count() takes exactly one argument (0 given)

list = [1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9]
duplicates = list.count(2)
print (duplicates)
# 4



## .extend()
# add elements at the end of a list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
# ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# MAIS NE RENVOIE PAS DE VALEUR
ones = [1, 11, 111]
ones_again = ones.extend([11, 111])
print(ones_again)  
# None
print(ones)
# [1, 11, 111, 11, 111]

ones = [1, 11, 111]
ones.extend([11, 111])
print(ones)         
# [1, 11, 111, 11, 111]



## .index()
# gives index matching an element in a list
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.index("cherry")
print(x)
# 2

# if many occurences of an element, considers only th first
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.index("cherry")
print(x)
# 2

spam = ['hello', 'hi', 'howdy', 'heyas'] 
print (spam.index('hello'))
0



## .insert(index, value)
# insert an element at the given index
spam = ['cat', 'dog', 'bat'] 
spam.insert(1, 'chicken') 
print (spam)
# ['cat', 'chicken', 'dog', 'bat']

spam = ['cat', 'dog', 'bat'] 
spam.insert(1, 4) 
print (spam)
# ['cat', 4, 'dog', 'bat']

 
 
## .pop()
# delete the given index
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# ['apple', 'cherry']

# if not any given index pop the last in Py3, or randomly in Py2
fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits)
# ['apple', 'cherry']



## .remove()
# delete the iven element
spam = ['cat', 'bat', 'rat', 'elephant'] 
spam.remove('bat') 
print (spam)
['cat', 'rat', 'elephant']

# if same value many times in a list, ONLY the first is taken in account
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
spam.remove('cat')
print (spam)
# ['bat', 'rat', 'cat', 'hat', 'cat']
# to bypass we'll use a loop
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] 
for cat in spam:
    spam.remove('cat')
print (spam)
# ['bat', 'rat', 'hat']



## .reverse()
# reverse the list order
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# ['cherry', 'banana', 'apple']



## .sort()
# sort the list alphabetically

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# ['BMW', 'Ford', 'Volvo']

# sort(reverse=True)
spam = ['cat', 'rat', 'cat', 'cat'] 
spam.sort(reverse=True)
print (spam)
# ['rat', 'cat', 'cat', 'cat']

# PYTHON3 ==> we cannot use this method with a mix of int and str
cars = ['Ford', 23, 'BMW', 4, 'Volvo']
cars.sort()
print(cars)
# Traceback (most recent call last):
#  File "c:\PythonLearning\bac-à-sable.py", line 2, in <module>
#    cars.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
# PS C:\PythonLearning> 

# PYTHON2 ==> int will stand before str
spam = ['cat', 1, 'rat', 2,'cat',3,  'cat'] 
spam.sort()
print (spam)
# [1, 2, 3, 'cat', 'cat', 'cat', 'rat']

# STR stand before str
spam = ['a', 'z', 'A', 'Z'] 
spam.sort() 
print(spam) 
['A', 'Z', 'a', 'z'] # matches ASCII values