########## SHELVE MODULE ##########

# Serialization of Python objects using the shelve module

# "pickle" module is used for serializing objects as a single byte stream
# Both serializing and deserializing parties must abide by the order of all the elements placed into a file or database, or sent via a network

# "shelve" built on top of pickle, implements a serialization dictionary where objects are pickled and associated with a key
# The keys must be ordinary strings, because the underlying database (dbm) requires strings
# we can open the shelved data file and access pickled objects via the keys the same way with dictionaries


import shelve

shelve_name = 'first_shelve.shlv'  # will be the shelve name
print(shelve_name)
# first_shelve.shlv

my_shelve = shelve.open(shelve_name, flag='c') # flag='c' == create if does not exist => first_shelve.shlv creation 
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()
print(my_shelve)
# <shelve.DbfilenameShelf object at 0x000001687A42B0E0>

with shelve.open(shelve_name) as db:
    keys = list(db.keys())
    for key in keys:
        print(key, ":", db[key])
# EUR : {'code': 'Euro', 'symbol': '€'}
# GBP : {'code': 'Pounds sterling', 'symbol': '£'}
# JPY : {'code': 'Japanese yen', 'symbol': '¥'}
# USD : {'code': 'US dollar', 'symbol': '$'}

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
# {'code': 'US dollar', 'symbol': '$'}
new_shelve.close()

print(new_shelve)
# <shelve.DbfilenameShelf object at 0x0000029A1EB0ED50>



## shelve.open(file, flag="x")

# ==> file
# best practice is to create a variable and to name it the sheve name string value

# ==> flag
# flag='c' => : create file if does not exist, or open it
# flag='r' : read only
# flag='w' : file must exist, read/write
# flag='n' : new file, replace existing one