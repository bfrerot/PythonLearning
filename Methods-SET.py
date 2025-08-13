########## METHODS SETs ##########


### .add()	 	
# Adds an element to the set

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# {'cherry', 'banana', 'orange', 'apple'}



### .clear()	 	
# Removes all the elements from the set

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
# set()  ==> set vide



### .copy()	 	
# Returns a copy of the set

fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
# {'banana', 'apple', 'cherry'}



### .difference()	
# Returns a set containing the difference between two or more sets
# a.difference(b)	Éléments dans a mais pas dans b

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) # = ce qui est dans x et pas dans y
print(z)
# {'cherry', 'banana'}

a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5}
print(a.difference(b))
# {1, 2, 6}



### .difference_update()	
# Removes the items in this set that are also included in another, specified set

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) # enleve de x ce qui est dans y
print(x)
# {'banana', 'cherry'}



### .discard()	 	
# Remove the specified item
# Si x n’est pas dans le set, ne fait rien et ne lève pas d’erreur CONTRAIREMENT à remove()

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
# {'apple', 'cherry'}
fruits.discard("caca") # n'existe pas mais pas d'erreur
print(fruits)
# {'apple', 'cherry'}



### .intersection()	
# Returns a set, that is the intersection of two other sets

a = {1, 2, 3, 4, 5, 6}
b = {2, 6}
print(a.intersection(b))
# {2, 6}



### .intersection_update()	
# Removes the items in this set that are not present in other, specified set(s)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) # laisse dans x que ce qui est dans y
print(x)
# {'apple'}



### .isdisjoint()	 	
# Returns whether two sets have a intersection or not

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
# True

x = {"apple", "banana", "facebook"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
# False



### .issubset()	
# Returns whether another set contains this set or not

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# True

x = {"z", "t", "y"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# False



### .issuperset()	
# Returns whether this set contains another set or not

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# True

x = {"f", "e", "d", "c", "b", "a"}
y = {"z", "t", "y"}
z = x.issuperset(y)
print(z)
# False



### .pop()	 	
# Removes an element from the set

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
# {'cherry', 'apple'}



### .remove()	 	
# Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
# {'cherry', 'apple'}
fruits.remove("caca") # n'existe pas ==> KeyError
print(fruits)
# KeyError: 'caca'



### symmetric_difference()	
# returns a set that contains all items from both set but not the items that are present in both sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
# {'cherry', 'google', 'microsoft', 'banana'}



### symmetric_difference_update()	
# Remove the items that are present in both sets, AND insert the items that is not present in both sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
{'banana', 'google', 'microsoft', 'cherry'}



### union()	
# Return a set containing the union of sets

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
# {'apple', 'microsoft', 'banana', 'google', 'cherry'}



### update()	
# Rajoute dans x ce qui est dans y et pas dans x

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
# {'google', 'apple', 'microsoft', 'cherry', 'banana'}