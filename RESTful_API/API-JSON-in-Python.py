##########  JSON in Python ##########


### Python vs JSON types

#   Python      |   JSON
#-------------------------------
#    dict       |   object
#  list/tuple   |   array
#    string     |   string
#   int/float   |   number
#  True/False   |  true/false
#    None       |    null



### json MODULE

import json


## dumps()
# Ability to automatically convert Python data (not all of it and not always) into a JSON string
# To carry out such an operation we use dumps()
# It takes data (even somewhat complicated data) and produces a string filled with a JSON message.

electron = 1.602176620898E10−19
print(json.dumps(electron))
# 16021766189.98

comics = '"The Meaning of Life" by Monty Python\'s Flying Circus'
print(json.dumps(comics))
# "\"The Meaning of Life\" by Monty Python's Flying Circus"

my_list = [1, 2.34, True, "False", None, ['a', 0]]
print(json.dumps(my_list))
# [1, 2.34, True, "False", null, ["a", 0]]
# /!\ JSON cannot distinguish between lists and tuples ==> both of these are converted into JSON arrays

my_dict = {'me': "Python", 'pi': 3.141592653589, 'data': (1, 2, 4, 8), 'set': None}
print(json.dumps(my_dict))
# {"me": "Python", "pi": 3.141592653589, "data": [1, 2, 4, 8], "set": null}


## .__dict__ VS dumps()

import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_who(w):
    if isinstance(w, Who):
        return w.__dict__
    else:
        raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

some_man = Who('John Doe', 42)

print(some_man.__dict__)
# {'name': 'John Doe', 'age': 42}  ==> Python output

print(json.dumps(some_man, default=encode_who))
# {"name": "John Doe", "age": 42}  ==> JSON format


## default()

import json

class Who:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class MyEncoder(json.JSONEncoder):  # it is not a MetaClass here, just a Class inheriting from an other
    def default(self, w):
        if isinstance(w, Who):         # matched by some_man
            return w.__dict__
        else:                          # matched by other_man
            return super().default(w)

some_man = Who('John Doe', 42)
print(some_man.__dict__)
# {'name': 'John Doe', 'age': 42}            ==> Python output from .__dict__
print(json.dumps(some_man, cls=MyEncoder))   
# {"name": "John Doe", "age": 42}            ==> Applique .dumps(), so ' becomes "

other_man = ('Winny', 10)      # ==> JSON knows only list, so it will return a list, not a tuple 
print(json.dumps(other_man, cls=MyEncoder))
# ["Winny", 10]


## loads()

# Function which gets a JSON string and to turns it into Python data 
# it takes a string and tries to create a Python entity corresponding to the received data

import json

# => with a string

jstr = '"\\"The Meaning of Life\\" by Monty Python\'s Flying Circus"'
# here the \ before other backslashes below, are related to JSON formating
#   \"The Meaning
#   \" by Monty   
#   Python\'s
# in a Python way it would be printable this way: print("\"The Meaning of Life\" by Monty Python's Flying Circus")
comics = json.loads(jstr) # => will format in a Python way, here remove "\" before others "\" and the "'"

print(type(comics))
# <class 'str'>

print(comics)
# "The Meaning of Life" by Monty Python's Flying Circus


# => with a list

import json

jstr = '[1, 2.34, true, "False", null, ["a", 0]]'
my_list = json.loads(jstr)

print(type(my_list))
# <class 'list'>

print(my_list)
# [1, 2.34, True, 'False', None, ['a', 0]] # does not change a lot, just " becomes ' in Python format, even if " would be fine


# with a JSON object => to a Python dict

import json

json_str = '{"me":"Python","pi":3.141592653589, "data":[1,2,4,8],"friend":"JSON","set": null}'
my_dict = json.loads(json_str)

print(type(my_dict))
# <class 'dict'>

print(my_dict)
# {'me': 'Python', 'pi': 3.141592653589, 'data': [1, 2, 4, 8], 'friend': 'JSON', 'set': None} # "  becomes ', null becomes None


# with Class

import json                          # import json module

class Who:                           # create class "Who"
    def __init__(self, name, age):   # 2*args mandatory
        self.name = name
        self.age = age

class MyEncoder(json.JSONEncoder):    # create a Class which inherits from json.JSONEncoder Class
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, w)

class MyDecoder(json.JSONDecoder):    # create a Class which inherits from json.JSONDecoder Class
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)    # create an instance of Class "Who"
print(some_man)
# <__main__.Who object at 0x000001D1FFB92E40>
print(some_man.name)
# Jane Doe
print(some_man.age)
# 23

json_str = json.dumps(some_man, cls=MyEncoder)   # build a JSON format dict/object
print(type(json_str))
# <class 'str'>     # it is now seen as a "string" by Python !
print(json_str)
# {"name": "Jane Doe", "age": 23}

new_man = json.loads(json_str, cls=MyDecoder)
print(type(new_man))
# <class '__main__.Who'>
print(new_man.__dict__)
# {'name': 'Jane Doe', 'age': 23}                # rebuild in Python format