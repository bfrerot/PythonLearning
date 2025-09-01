########## OOP - INHERITANCE ##########

# Any object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements and qualities) defined inside any of the superclasses

# The most important factor of the process is the relation between the superclass and all of its subclasses:

#       - single inheritance class is always simpler, safer, and easier to understand and maintain

#       - multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying 
#           these parts of the superclasses which will effectively influence the new class
#         multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous
#         multiple inheritance violates the single responsibility principle (https://en.wikipedia.org/wiki/Single_responsibility_principle) 
#           as it makes a new class of two (or more) classes that know nothing about each other
#         multiple inheritance should be the last of all possible solutions – if you really need the many different functionalities offered 
#           by different classes, composition may be a better alternative



### Method Resolution Order - MRO

# MRO, in general, is a way, a strategy, in which a particular programming language scans through the upper part of a class’s hierarchy
# in order to find the method it currently needs

# Main rule in multiple inheritance:
#	- Python needs to be able to figure out in which order to look for methods, attributes if many parent classes own homonyms
#	- MRO must be consistent

class Top:
    pass

class Left(Top): # class Left inherits from class Top
    pass

class Right(Top): # class Right inherit from class Top
    pass

class Bottom(Left, Right): # class Bottom inherit from Left and Right, which is consistent because Left and Right sharea common parent, class Top
    pass

class Bottom1(Left, Top): # ok as Left inherits already from Top
    pass



class Bottom2(Top, Left): # MRO error : (Top, Left)
    pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Left

# ==> Python cannot create a consistent MRO
#     Left already inherits from Top, Left is already a Top subclass, so this hierarchy creates a MRO conflict



class A:
    pass
 
class B(A):
    pass
 
class C(A):
    pass
 
class D(B):
    pass
  
  

## VALID inheritance schemes 

# ==> from BOTTOM to TOP
class Class_2(D, B): 
    pass
  
class Class_3(C, A): 
    pass

class Class_4(D, A): 
    pass

# ==> SEPARATE paths
class Class_1(C, D): 
    pass
  
class Class_1(D, C): 
    pass


## UNVALID inheritance schemes    
class Class_2(B, D): 
    pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases B, D
  
class Class_3(A, C): 
    pass 
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C


## use case
class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

class E(C, B):
    pass

D().info()
# Class B
E().info()
# Class C




# the object is able to access superclasses instance variables
class Sup:
    supVar = 1

class Sub(Sup):
    subVar = 2

obj = Sub()

print(obj.subVar)
# 2 ==> class Sub
print(obj.supVar)
# 1 ==> class Super (upper class)


# the object IS NOT ABLE to access the superclass __init__ variables + __static_attributes__ by default:
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        self.subVar = 12

obj = Sub()
print(obj.supVar)
# AttributeError: 'Sub' object has no attribute 'supVar'

# to overcome this, we can use super().__init__():
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__() # ici !
        self.subVar = 12

obj = Sub()
print(obj.supVar)
# 11


# When you try to access any object's entity, Python will try to:
#   1 ==> find it inside the object itself, NOK ?
#   2 ==> find it in all classes involved in the object's inheritance line from bottom to top, NOK ?
#   3 ==> AttributeError

class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
# bottom
object.m_middle() # in Bottom() ?, no ==> in Middle() ?, yes
# middle
object.m_top()
# top

object2 = Top()
object2.m_bottom() # in Top() ?, no ==> Error
# AttributeError: 'Top' object has no attribute 'm_bottom'
    


### TRANSITIVITY

# if B is a subclass of A and C is a subclass of B, this also means that C is a subclass of A, the relationship is fully transitive

class Vehicle:
    pass
 
class LandVehicle(Vehicle):
    pass
 
class TrackedVehicle(LandVehicle):
    pass
# The Vehicle class is the superclass for both the LandVehicle and TrackedVehicle classes
# The LandVehicle class is a subclass of Vehicle and a superclass of TrackedVehicle at the same time
# The TrackedVehicle class is a subclass of both the Vehicle and LandVehicle classes



### LEVEL-LINE INHERITANCE
# Python looks for an entity from bottom to top

class Level1:
    variable_1 = 100
    
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102

class Level2(Level1):
    variable_2 = 200
    
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202

class Level3(Level2):
    variable_3 = 300
    
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302

obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
# 100 101 102
print(obj.variable_2, obj.var_2, obj.fun_2())
# 200 201 202
print(obj.variable_3, obj.var_3, obj.fun_3())
# 300 301 302


    
### MULTIPLE INHERITANCE

# Python can go into either way between classes and its upper classes to find variable, methods etc, from bottom to upper
class Alpha:
    value = "Alpha"  # 2- looks for a variable "value", in upper class Alpha() ?, ok !

    def say(self):
        return self.value.lower()

class Beta(Alpha):
    pass

class Gamma(Alpha):
    def say(self):
        return self.value.upper() # 1- looks for a variable "value", in Gamma() ?, nok

class Delta(Gamma, Beta):
    pass

d = Delta()
print(d.say())
# ALPHA
# ==>
# 1- looks for method say()
#   1a- in Delta() ?, nok
#   1b- in Gamma() ?, yes !
#       2- looks for variable "value"
#           2a- in Delta() ?, nok
#           2b- in Gamma() ?, nok
#           2c- in Alpha() ?, yes !
#               3- returns "Alpha" in uppercase = ALPHA


# WITHOUT HOMONYM
# without priorisation between upper classes
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
class Sub(SuperA, SuperB): # multiple inheritance
    pass
 
obj = Sub()
print(obj.var_a, obj.fun_a())
# 10 11
print(obj.var_b, obj.fun_b())
# 20 21


# WITH HOMONYM

class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B): # A() is looked in before B()
    pass

class D(B, A): # B() is looked in before A()
    pass

o = C()
print(o)
# a
o2 = D()
print(o2)
# b



### SUPER()

# ==> direct call to the parent class
# not recommended

# super() returns a "super class" meaning the parent class in the current context and invokes its __init__ method
# Advantages :
#  - More flexible, even more in multiple inheritance context
#  - Respect the inheritance chain and can invoke __init__ method of next classes, following MRO hierarchy

class Sup:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # Python always checks if any method __str__() or __repr__()
        return "My name is " + self.name + "."

class Sub(Sup):
    def __init__(self, name):
        Sup.__init__(self, name)

obj = Sub("Andy")
print(obj)  
# My name is Andy.


## invoke super().__init__()

# choice A, python3+, recommended
class SpamException (Exception):
    def __init__ (self, message):
        super().__init__(message)
        self.message = message
#raise SpamException( "Spam" ) ==> remove # to test

# Traceback (most recent call last):
#   File "c:\PythonLearning\error_test.py", line 5, in <module>
#     raise SpamException( "Spam" )
# SpamException: Spam


# choice B, python2/3
class Spam2Exception (Exception):
    def __init__ (self, message):
        super(Spam2Exception, self).__init__(message)
        self.message = message
# raise Spam2Exception( "Spam" ) ==> remove # to test


## question, what if many superclasses ?
# ==> super() in Python 3 manages automatically multiple inheritance thanks to MRO
class A:
    def __init__(self, value):
        print(f"A init: {value}")
        self.a_value = value

class B:
    def __init__(self, value):
        print(f"B init: {value}")
        self.b_value = value

class C(A, B):
    def __init__(self, value):
        print(f"C init: {value}")
        super().__init__(value)  # automatically invokes following MRO
        self.c_value = value

c = C("test")

c = C()
# C init: test
# A init: test

# to check MRO order:
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


## to target a particular superclass
class A:
    def __init__(self, value):
        print(f"A init: {value}")
        self.a_value = value

class B:
    def __init__(self, value):
        print(f"B init: {value}")
        self.b_value = value

class C(A, B):
    def __init__(self, value):
        # Invoke specifically B, bypassing MRO
        B.__init__(self, value)

c = C("test")
# B init: test


## to target all superclasses, avecwith **kwargs or "kwargs" (canbemodified by any "string")
class A:
    def __init__(self, **kwargs):
        print("A init")
        super().__init__(**kwargs)

class B:
    def __init__(self, **kwargs):
        print("B init")
        super().__init__(**kwargs)

class C(A, B):
    def __init__(self, **kwargs):
        print("C init")
        super().__init__(**kwargs)

c = C()
# C init
# A init
# B init

class A:
    def __init__(self, **caca):
        print("A init")
        super().__init__(**caca)

class B:
    def __init__(self, **caca):
        print("B init")
        super().__init__(**caca)

class C(A, B):
    def __init__(self, **caca):
        print("C init")
        super().__init__(**caca)

c = C()
# C init
# A init
# B init



### POLYMORPHISM

# Polymorphism is a mechanism which enables the programmer to modify the behavior of any of the object's superclasses 
#   without modifying these classes themselves
# One way to carry out polymorphism is inheritance, when subclasses make use of base class methods, or override them
# By combining both approaches, the programmer is given a very convenient way of creating applications, as:
#   - most of the code could be reused and only specific methods are implemented, which saves a lot of development time and improves code quality
#   - the code is clearly structured
#   - there is a uniform way of calling methods responsible for the same operations, implemented accordingly for the types

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self): # 1
        self.do_it()
        

class Two(One):
    def do_it(self): # 2
        print("do_it from Two") # 3

one = One()
two = Two()

one.doanything()
# do_it from One
two.doanything() # 1 - 2 - 3
# do_it from Two


# the situation in which the subclass is able to modify its superclass behavior is polymorphism 
# below we remove the choice to find the variable instance Two() class
class One:
    def do_it(self): # 4a- One.do_it()
        print("do_it from One") # 4b- = print "do_it from One"

    def doanything(self): # 2- doanything() ?,yes !
        self.do_it() # 3a- is do_it() already in Two() ?,nok ==> 3b- ok so we use One.do_it()

class Two(One): # 1- doanything() ?,nok   # 3a- nok
    pass

one = One()
two = Two()

one.doanything()
# do_it from One
two.doanything() # 1 - 2 - 3 - 4
# do_it from One

# other example
class Device:
    def turn_on(self):
        print('The device was turned on')

class Radio(Device):
    pass

class PortableRadio(Device):
    def turn_on(self):
        print('PortableRadio type object was turned on')

class TvSet(Device):
    def turn_on(self):
        print('TvSet type object was turned on')

device = Device()
radio = Radio()
portableRadio = PortableRadio()
tvset = TvSet()

for element in (device, radio, portableRadio, tvset):
    element.turn_on()
# The device was turned on
# The device was turned on
# PortableRadio type object was turned on
# TvSet type object was turned on


# example with Exception handling
class Wax:
    def melt(self):
        print("Wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started!")

for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print('No melt() method')
# Wax can be used to form a tool
# Cheese can be eaten
# No melt() method