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



















### __add__()


## int

number = 10
print(number.__add__(20))
# 30


## float

number = 10
print(number.__add__(20.))
# NotImplemented

number = 10
print(number.__add__(20.5))
# 30.5

number = 10.5
print(number.__add__(20))
# 31

number = 10.5
print(number.__add__(20.5))
# 31


## string

string1 = "Part1"
print(number.__add__("Part2"))
# NotImplemented


## Instance/Class

class Person:
    def __init__(self, weight, age, salary):   # constructor with self + 3*parameters
        self.weight = weight                   # instance variable
        self.age = age                         # instance variable
        self.salary = salary                   # instance variable

    def __add__(self, other):                  # magic method __add__()
        return self.weight + other.weight      # returns weight addition

p1 = Person(60, 40, 50)
p2 = Person(85, 45, 55)

print(p1 + p2)
# 145


## REMINDER

# dir() function gives you a quick glance at an object’s capabilities and returns a list of the attributes and methods of the object
# __add__() in it:

print(dir(100))
'''
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
 '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', 
 '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', 
 '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 
 '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
'''

print(dir("string"))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
 '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
 'title', 'translate', 'upper', 'zfill']
'''