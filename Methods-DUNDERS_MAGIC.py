########## METHODS DUNDERs MAGIC ##########



##### COMPARISON METHODS


### __eq__(self, other)	 ==     equality operator
###	__ne__(self, other)	 !=     inequality operator
###	__lt__(self, other)  < 	    less-than operator
###	__gt__(self, other)	 >      greater-than operator
###	__le__(self, other)	 <=     less-than-or-equal-to operator
###	__ge__(self, other)	 >=     greater-than-or-equal-to operator

class Point:
    def __init__(self, x, y):   # init(self, x, y): each instance of the class Point must have x et y parameters
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):   # if p2 isnot an instance of Point, will return "NotImplemented"
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)   #  (1, 2) == (2, 1) ? NO, so False

    def __ne__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) != (other.x, other.y)   #  (1, 2) != (2, 1) ? Yes, so False

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)    # like a tuple comparison, (1, 2) < (2, 1) because 1 < 2, so True

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) <= (other.x, other.y)   # like a tuple comparison, (1, 2) < (2, 1) because 1 < 2, so True

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) > (other.x, other.y)    # like a tuple comparison, False 

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) >= (other.x, other.y)   # like a tuple comparison, False 

    def __repr__(self):
        return f"Point({self.x}, {self.y})"  # to have a readable return if any debug (output, error message)

p1 = Point(1, 2)
p2 = Point(2, 1)

print(p1 == p2)  
# False
print(p1 != p2)  
# True
print(p1 < p2)   
# True
print(p1 <= p2)  
# True
print(p1 > p2)   
# False
print(p1 >= p2)  
# False




##### NUMERIC METHODS - UNARY OPERATORS & FUNCTIONS


### __eq__(self, other)	 ==     equality operator
###	__ne__(self, other)	 !=     inequality operator
###	__lt__(self, other)  < 	    less-than operator
###	__gt__(self, other)	 >      greater-than operator
###	__le__(self, other)	 <=     less-than-or-equal-to operator
###	__ge__(self, other)	 >=     greater-than-or-equal-to operator


class NumValue:
    def __init__(self, v):          # constructor, waits 1*parameter
        self.v = float(v)

    def __pos__(self):
        print("unary plus (+)")
        return NumValue(+self.v)    # returns +(v) ==> +(+1) = +1  //   +(-1) = -1

    def __neg__(self):
        print("unary minus (-)")
        return NumValue(-self.v)    # returns -(v) ==> -(+1) = -1  //   -(-1) = +1

    def __abs__(self):
        print("abs")
        return NumValue(abs(self.v))   # returns absolute valor of (v) ==> abs(+1) = +1  //   abs(-1) = +1

    def __round__(self, ndigits=None):
        print("round with ndigits =", ndigits)
        if ndigits is None:
            return NumValue(round(self.v))   # builtin function ==> round(x, OPTIONAL n digits)
        else:
            return NumValue(round(self.v, ndigits))

    def __repr__(self):
        return f"NumValue is {self.v}"      # automaticaly executed for each call
    
    
a = NumValue(3.14)
abyss = NumValue(6.51)
b = NumValue(-4)

print(+a)          
# unary plus (+)
# NumValue is 3.14

print(+b) 
# unary plus (+)
# NumValue is -4.0

print(-a)          
# unary minus
# NumValueis -3.14

print(-b)
# unary minus (-)
# NumValue is 4.0

print(abs(a))      
# abs
# NumValue is 3.14

print(abs(b))      
# abs
# NumValue is 4.0

print(round(a))
# round with ndigits = None
# NumValue is 3.0

print(round(abyss))
# round with ndigits = None
# NumValue is 7.0

print(round(b))
# round with ndigits = None
# NumValue is -4.0

print(round(a, 1)) # round() avec ndigits
# round with ndigits = 1
# NumValue is 3.1

print(round(b, 4)) # round() avec ndigits
# round with ndigits = 4
# NumValue is -4.0




##### NUMERIC METHODS - BINARY OPERATORS & FUNCTIONS


### __add__(self, other)            +	   addition operator
### __sub__(self, other)	        -      subtraction operator
### __mul__(self, other)	        *      multiplication operator
### __floordiv__(self, other)       //	   integer division operator
### __div__(self, other)	        /      division operator
### __mod__(self, other)	        %      modulo operator
### __pow__(self, other)	        **     exponential (power) operator


class NumValue:
    def __init__(self, v):            # constructor, waits 1*parameter
        self.v = float(v)             # converts in the meantime any V value to float type

    def __repr__(self):
        return f"Result is {self.v}"   # executes at the end of each call

    def __add__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v + other.v)   # returns 6 + 4 = 10.0
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v - other.v)   # returns 6 - 4 = 2.0
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v * other.v)    # returns 6 * 4 = 24.0
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v // other.v)   # returns 6 // 4 = 1.0
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v / other.v)    # returns 6 / 4 = 1.5
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v % other.v)    # returns 6 % 4 = 1.0
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, NumValue):
            return NumValue(self.v ** other.v)   # returns 6 * 4 = 1296.0
        return NotImplemented


a = NumValue(6)     # instance creation of the Class NumValue
b = NumValue(4)

print(a + b)    
# Result is 10.0
print(a - b)    
# Result is 2.0
print(a * b)    
# Result is 24.0
print(a // b)   
# Result is 1.0 (floor division)
print(a / b)   
# Result is 1.5
print(a % b)    
# Result is 2.0
print(a ** b)   
# Result is 1296.0




##### NUMERIC METHODS - BINARY OPERATORS & FUNCTIONS


###   +=    __iadd__(self, other)
###   -=    __isub__(self, other)
###   *=    __imul__(self, other)
###   //=   __ifloordiv__(self, other)
###   /=    __idiv__(self, other)
###   %=    __imod__(self, other)
###   **=   __ipow__(self, other)


class Number:
    def __init__(self, value):         # constructor, waits 1*parameter
        self.value = value

    def __repr__(self):
        return f"Result is {self.value}"   # executes at each instance call

    def __iadd__(self, other):
        print(f"__iadd__ called: {self.value} += {other}") # match if action is +=
        self.value += other
        return self           # returns result self + other

    def __isub__(self, other):
        print(f"__isub__ called: {self.value} -= {other}") # match if action is -=
        self.value -= other
        return self          # returns result self - other

    def __imul__(self, other):
        print(f"__imul__ called: {self.value} *= {other}") # match if action is *=
        self.value *= other
        return self          # returns result self * other

    def __ifloordiv__(self, other):
        print(f"__ifloordiv__ called: {self.value} //= {other}") # match if action is //=
        self.value //= other
        return self          # returns result self // other

    def __itruediv__(self, other):  # !!  ==> idiv not supported anymore in Python 3
        print(f"__itruediv__ called: {self.value} /= {other}")  # match if action is /=
        self.value /= other
        return self           # returns result self / other

    def __imod__(self, other):
        print(f"__imod__ called: {self.value} %= {other}")  # match if action is %=
        self.value %= other
        return self          # returns result self % other

    def __ipow__(self, other):
        print(f"__ipow__ called: {self.value} **= {other}") # match if action is **=
        self.value **= other
        return self          # returns result self ** other
    


a = Number(10) 
a += 5  # call a.__iadd__()        
print(a)        
# Result is 15

a -= 3
print(a)        
# Result is 12

a *= 2
print(a)
# Result is 24

a //= 5
print(a)        
# Result is 4

a /= 2
print(a)        
# Result is 2.0

a %= 3
print(a)        
# Number(2.0)

a **= 3
print(a)        
# Number(8.0)




##### TYPE CONVERSION MODELS


###   int()	    __int__(self)	  conversion to integer type
###   float()	__float__(self)	  conversion to float type
###   oct()	    __oct__(self)	  conversion to string, containing an octal representation
###   hex()	    __hex__(self)	  conversion to string, containing a hexadecimal representation

# In Python3, __oct__() and __hex__() are not used by oct() and hex() functions
# These functions do use index or int. 
# So to make oct(n) and hex(n) work, we need:
#       define index (or int) and let oct()/hex() convert the int
#       OR explicitely call the methods which call octales/hex chains

class Number:
    def __init__(self, value):  # constructor
        self.value = value

    def __repr__(self):
        return f"Number({self.value})"

    def __int__(self):
        print(f"__int__ called: int({self.value})")
        return int(self.value)

    def __float__(self):
        print(f"__float__ called: float({self.value})")
        return float(self.value)

    def __index__(self):  
        return int(self.value)

    def __oct__(self):
        print(f"__oct__ called: oct({self.value})")
        return oct(int(self.value))

    def __hex__(self):
        print(f"__hex__ called: hex({self.value})")
        return hex(int(self.value))


n = Number(255)

print(int(n))
# __int__ called: int(255)
# 255

print(float(n))
# __float__ called: float(255)
# 255.0

print(oct(int((n))))       # simplest way to make sure n is seen by Python as an integer
# __int__ called: int(255)
# 0o377

print(hex(int((n))))       # simplest way to make sure n is seen by Python as an integer
# __int__ called: int(255)
# 0xff





##### OBJECT INTROSPECTION

### str()	     __str__(self)	                responsible for handling str() function calls
### repr()	     __repr__(self)              	responsible for handling repr() function calls
### format()	 __format__(self, formatstr)	called when new-style string formatting is applied to an object
### hash()	     __hash__(self)	                responsible for handling hash() function calls
### dir()	     __dir__(self)    	            responsible for handling dir() function calls
### bool()	     __nonzero__(self)	            responsible for handling bool() function calls


### __str__(self)
# to launch a retrun, well known function

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
          return f"{self.name}, {self.age} years"

p = Person("Alice", 30)
print(str(p))  
# Alice, 30 years
print(p)
# Alice, 30 years ==> uses __str__ first if defined or else __repr__



### __repr__(self)
# create a return, well-known function

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 3)
print(repr(p))  
# Point(2, 3)
print(p)   
# Point(2, 3)  ==> uses __str__ if defined first, else __repr__


#! if not any __str__ nor __repr__, a print(object) outputs a memory reference
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p)
# <__main__.Person object at 0x000001F3CD6F7230>



### __format__(self, formatstr)
# data formatin: f-strings, format()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __format__(self, spec):
        if spec == "w x h":
            return f"{self.width} multiplicated by {self.height}"
        return f"{self.width} * {self.height}"
r = Rectangle(4, 5)
print(format(r, "w x h"))  #==> spec = "w * h" = format
# 4 multiplicated by 5
print(format(r)) #==> no spec, so empty value is passed thru as spec + default return applied
# 4 * 5



### __hash__(self)
# Make an object hashable to be usable in dicts, sets
# in CPython, hash() is "salted" by default, meaning its value will change at each program execution
# it's why we'll see a different value at each code execution

class User:
    def __init__(self, username):
        self.username = username
    def __hash__(self):
        return hash(self.username)
    def __eq__(self, other):
        return isinstance(other, User) and self.username == other.username

u1 = User("bob") # username = "bob"
s = {u1} # create a set andneeds the hash value of "bob" so invokes __hash__(self.username)
print(s)
# {<__main__.User object at 0x0000022A07167380>} ==> does change at each repetition of the code
print(hash(u1)) 
# -677639030044872848    ==> does change at each repetition of the code
print(hash("bob")) 
# -677639030044872848    ==> does change at each repetition of the code
print(User("bob") in s)  
# True



### __dir__(self)

class Custom:
    def __init__(self):
        self.a = 1
    def __dir__(self):
        return ["a", "b", "c", "custom_method"] 

c = Custom()
print(dir(c))
# ['a', 'b', 'c', 'custom_method']



### __bool__(self)  
# ! __nonzero__ is Python 2 ==> Python 3 is __bool__
# bool() returns len(self.items) > 0

class Box:
    def __init__(self, items):
        self.items = items
    def __bool__(self):
        return len(self.items) > 0

b1 = Box([1, 2])  # ==> items = [1, 2]
b2 = Box([])      # ==> items = None
b3 = Box((1,2,3))
b4 = Box({1:"a",2:"b"}) 
print(bool(b1))  
# True
print(bool(b2))  
# False
print(type(bool(b2)))  
print(bool(b3))  
# True
print(bool(b4))
# True





##### OBJECT RETROSPECTION

### isinstance(object, class)	   __instancecheck__(self, object)  	responsible for handling isinstance() function calls
### issubclass(subclass, class)	   __subclasscheck__(self, subclass)	responsible for handling issubclass() function calls


### __instancecheck__(self, obj)
# manipulates how an object is made an instance of a class

class Meta(type):
    def __instancecheck__(cls, instance):
        return hasattr(instance, "id")
        # any object having an attribute "id" is considered being an instance

class MyClass(metaclass=Meta): # refers to metaclass
    pass

class WithID:
    id = 123

print(isinstance(WithID(), MyClass))  # True (parce que l'objet a l'attribut 'id')
print(isinstance(object(), MyClass))  # False  ==> object(): When called, it accepts no arguments and returns a new featureless
#                                                              instance that has no instance attributes and cannot be given any


### __subclasscheck__(self, subclass)
# manipulates issubclass(subclass, Class) behavior

class Meta(type):
    def __subclasscheck__(cls, subclass):
        # considérer toutes les classes dont le nom commence par 'IF' comme sous-classes
        return isinstance(subclass, type) and subclass.__name__.startswith("IF")

class IFBase(metaclass=Meta):
    pass

class IFDerived(IFBase):
    pass

class Derived(IFBase):
    pass

class Other:
    pass

print(issubclass(IFDerived, IFBase))  
# True   ==> as class IFDerived does not start by "IF"
print(issubclass(Derived, IFBase))  
# False  ==> as class Derived does not start by "IF"
print(issubclass(Other, IFBase))       
# False  ==> normal

#! isinstance(subclass, type) ==> checks if we have really a class
# Other() seems to have no upperclass but any class in Python3 is an implicit object() subclass 




##### OBJECT ATTRIBUTE ACCESS

### object.attribute	        __getattr__(self, attribute)	      responsible for handling access to a non-existing attribute
#                   	        __getattribute__(self, attribute)	  responsible for handling access to an existing attribute
### object.attribute = value	__setattr__(self, attribute, value)   responsible for setting an attribute value
### del object.attribute	    __delattr__(self, attribute)	      responsible for deleting an attribute



### __getattr__(self, name)
# defines an action when attribute is not found

class Fallback:
    def __getattr__(self, name):
        if name == "dynamic":
            return 42
        raise AttributeError(name)

f = Fallback()
print(f.dynamic)  
# 42
print(f.other)  # ==> AttributeError
'''Traceback (most recent call last):
  File "c:\PythonLearning\SandBox.py", line 10, in <module>
    print(f.other)  # ==> AttributeError
          ^^^^^^^
  File "c:\PythonLearning\SandBox.py", line 5, in __getattr__
    raise AttributeError(name)
AttributeError: other'''



### __getattribute__(self, name)

class LogGet:
    def __init__(self):
        self.x = 10
    def __getattribute__(self, name):
        print(f"Getting {name}")
        return object.__getattribute__(self, name)

lg = LogGet()
print(lg.x)  # __getattribute__("x") is called
# Getting x
# 10


#! ==> __getattr__ VS __getattribute__
# __getattribute__ is invoked for all accesses est appelé pour tous les accès (synchronisé avec la réalité des attributs présents).
# __getattr__ is invoked if access fails, if the attribute does not exist (c’est-à-dire si l’attribut n’existe pas). Ça permet de fournir des valeurs “à la demande” seulement lorsque l’attribut manque.



### __setattr__(self, name, value)
# set an attribute and controls how it's done

class ReadOnlyAfterSet:
    def __setattr__(self, name, value):
        if name == "fixed" and hasattr(self, "fixed"): # hasattr(self, "fixed") here self refers to instance itself
            raise AttributeError("fixed is READ ONLY after initial affectation")
        object.__setattr__(self, name, value)

r = ReadOnlyAfterSet()   # instance creation

r.fixed = 5   # __setattr__("fixed", 5) is invoked

print(dir(r))   # the attribute "fixed" is viewable in dict(r)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
 '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
 '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'fixed']

print(r.fixed) # the attribute "fixed" has the assigned value of 5
# 5

r.fixed = 10  # we try to change r.fixed attribute
# ...
# AttributeError: fixed is READ ONLY after initial affectation



### __delattr__(self, name)
# to del attributes and manages the way it's done
class NoDelete:
    def __init__(self):
        self.important = "keep me"
        self.other = "delete me if you want"
    def __delattr__(self, name):
        if name == "important":
            raise AttributeError("Impossible to delete 'important' attribute")
        print(f"{name} attribute is going to be deleted")
        object.__delattr__(self, name)

n = NoDelete()
del n.other
# other attribute is going to be deleted
del n.important  
# ...
# AttributeError: Impossible to delete 'important' attribute





##### METHODS ALLOWING ACCESS TO CONTAINERS

### len(container)	            __len__(self)	                 returns the length (number of elements) of the container
### container[key]	            __getitem__(self, key)	         responsible for accessing (fetching) an element identified by the key argument
### container[key] = value	    __setitem__(self, key, value)	 responsible for setting a value to an element identified by the key argument
### del container[key]	        __delitem__(self, key)	         responsible for deleting an element identified by the key argument
### for element in container	__iter__(self)	                 returns an iterator for the container
### item in container	        __contains__(self, item)	     responds to the question: does the container contain the selected item?



### __len__(self)
# Returns the number of elements stored in the container

class SimpleBag:
    def __init__(self, items=None):
        self.items = list(items) if items is not None else []

    def __len__(self):
        return len(self.items)

bag = SimpleBag([1, 2, 3])
emptybag = SimpleBag()
print(len(bag))  
# 3
print(len(emptybag)) 
# 0



### __getitem__(self, key)
# Fetches the element identified by key

class SimpleDictLike:
    def __init__(self, initial=None):
        self.data = dict(initial or {})

    def __getitem__(self, key):
        return self.data[key]

d = SimpleDictLike({'a': 1, 'b': 2})
print(d['a'])  
# 1
print(d[2])  
# ...
# KeyError: 2
print(d['c']) 
# ...
# KeyError: 'c'



### __setitem__(self, key, value)
# Sets the element identified by key to value

class SimpleDictLike:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

d = SimpleDictLike()
d['x'] = 42         # calls __setitem__('x', 42)
print(d['x'])       
# 42



### __delitem__(self, key)
# Deletes the element identified by key

class SimpleDictLike:
    def __init__(self):
        self.data = {'a': 1, 'b': 2}

    def __delitem__(self, key):
        del self.data[key]

    def __getitem__(self, key):
        return self.data[key]

d = SimpleDictLike()
# {'a': 1, 'b': 2}
print(d.data) 
del d['a']          # calls __delitem__('a')
print(d.data)         
# {'b': 2}



### __iter__(self)  
# Returns an iterator that yields elements of the container

class SimpleBag:
    def __init__(self, items=None):
        self.items = list(items or [])

    def __iter__(self):
        return iter(self.items)

bag = SimpleBag([10, 20, 30])
for x in bag:
    print(x)
# 10
# 20
# 30



### __contains__(self, item)
# Checks if the container contains the given item

class SimpleSetLike:
    def __init__(self, items=None):
        self.data = set(items or [])

    def __contains__(self, item):
        return item in self.data

s = SimpleSetLike([1, 2, 3])
print(2 in s)   
# True
print(5 in s)   
# False
