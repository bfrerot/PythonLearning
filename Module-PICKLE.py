##########  PICKLE MODULE  ##########


### Serialization
# ==> process of converting an object structure into a stream of bytes to store the object in a file or database, or to transmit it via a network
# Python objects can be serialized using a module called 'pickle', and using this module, you can 'pickle' your Python objects for later use
# "pickle" module is a very popular and convinient module for data serialization
# The following types can be pickled:
#   None, booleans
#   integers, floating-point numbers, complex numbers
#   strings, bytes, bytearrays
#   tuples, lists, sets, and dictionaries containing pickleable objects
#   objects, including objects with references to other objects (remember to avoid cycles!)
#   references to functions and classes, but not their definitions


### Deserialization
# ==> reverse process, contains all the information necessary to reconstruct the object in another Python script

# Python objects can also be serialized using a module called 'pickle', and using this module, you can 'pickle' your Python objects for later use



### pickle.dump()
#   Purpose: Serializes an object and writes it directly to a file-like object
#   Parameters: Takes the object to serialize AND a file object
#   Output: Writes binary data to the file
#   Returns: Nothing (None)

import pickle

a_dict = dict()
a_dict['EUR'] = {'code':'Euro', 'symbol': '€'}
a_dict['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
a_dict['USD'] = {'code':'US dollar', 'symbol': '$'}
a_dict['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

a_list = ['a', 123, [10, 100, 1000]]

with open('multidata.pckl', 'wb') as file_out:   # create a binary file multidata.pckl
    pickle.dump(a_dict, file_out)    # to persist a_dict
    pickle.dump(a_list, file_out)    # to persist a_list
    
# =====> persist = save data to be able to reuse later on

with open('multidata.pckl', 'rb') as file_in:
    data1 = pickle.load(file_in)  # => "unpickeling" 
    data2 = pickle.load(file_in)  # => "unpickeling" 

print(type(data1))
# <class 'dict'>
print(data1)
# {'EUR': {'code': 'Euro', 'symbol': '€'}, 'GBP': {'code': 'Pounds sterling', 'symbol': '£'}, 'USD': {'code': 'US dollar', 'symbol': '$'}, 'JPY': {'code': 'Japanese yen', 'symbol': '¥'}}

print(type(data2))
# <class 'list'>
print(data2)
# ['a', 123, [10, 100, 1000]]



## pickle.dumps()
#   Purpose: Serializes an object and returns it as a bytes object in memory
#   Parameters: Takes ONLY the object to serialize
#   Output: Returns serialized data as bytes
#   Returns: Bytes object containing the pickled data

# with a list
import pickle

a_list = ['a', 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print('Intermediate object type, used to preserve data:', type(bytes))
# Intermediate object type, used to preserve data: <class 'bytes'>

# ======> now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)

print('A type of deserialized object:', type(b_list))
# A type of deserialized object: <class 'list'>

print('Contents:', b_list)
# Contents: ['a', 123, [10, 100, 1000]]


# with a function
import pickle

def f1():
    print('Hello from the jar!')

with open('function.pckl', 'wb') as file_out:
    pickle.dump(f1, file_out)

with open('function.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
# <class 'function'>
print(data)
# <function f1 at 0x000001FD5CBD1440>
data()
# Hello from the jar!


# with a class
import pickle

class Cucumber:
    def __init__(self):
        self.size = 'small'

    def get_size(self):
        return self.size

cucu = Cucumber()

with open('cucumber.pckl', 'wb') as file_out:
    pickle.dump(cucu, file_out)

with open('cucumber.pckl', 'rb') as file_in:
    data = pickle.load(file_in)

print(type(data))
# <class '__main__.Cucumber'>
print(data)
# <__main__.Cucumber object at 0x000002AC2DB29F90>
print(data.size)
# small
print(data.get_size())
# small