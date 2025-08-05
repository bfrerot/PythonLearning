########## METHOD TUPLES ##########


## .count()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
# 2


## .index()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
# 3 # ne prend en compte que le premier

foo = (1, 2, 3)
foo.index(0)
# ValueError: tuple.index(x): x not in tuple