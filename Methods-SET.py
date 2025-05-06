########## METHODS SETs ##########


add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set


### difference()	-	Returns a set containing the difference between two or more sets
# a.difference(b)	Éléments dans a mais pas dans b
# b.difference(a)	Éléments dans b mais pas dans a

a = {1, 2, 3, 4, 5, 6}
b = {3, 4, 5}
print(a.difference(b))
# {1, 2, 6}


difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item


### intersection()	&	Returns a set, that is the intersection of two other sets


intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others