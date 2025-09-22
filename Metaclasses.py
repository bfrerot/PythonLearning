########## METACLASSES ##########

# a metaclass:
#   - is a class whose instances are classes
#   - allows for the customization of class instantiation
#   - redirect class instantiations to dedicated logic, contained in metaclasses
#   - is applied when class definitions are read to create classes, well before classes are instantiated

# use cases:
#   - logging
#   - registering classes at creation time
#   - interface checking
#   - automatically adding new methods
#   - automatically adding new variables



### Class reminder

## important attributes
# .__name__   ==>  inherent for classes, contains the name of the class
# .__class__  ==>  inherent for both classes and instances, contains information about the class to which a class instance belongs
# .__bases__  ==>  inherent for classes, tuple containing information about the base classes of a class
# .__dict__   ==>  inherent for both classes and instances, contains a dictionary of the object's attributes

class Dog:
    pass

dog = Dog()

print('"dog" is an object of class named:', Dog.__name__)
# "dog" is an object of class named: Dog

print('class "Dog" is an instance of:', Dog.__class__)
# class "Dog" is an instance of: <class 'type'>

print('instance "dog" is an instance of:', dog.__class__)
# instance "dog" is an instance of: <class '__main__.Dog'>

print('class "Dog" is  ', Dog.__bases__)
# class "Dog" is   (<class 'object'>,)

print('class "Dog" attributes:', Dog.__dict__)
# class "Dog" attributes: {'__module__': '__main__', '__firstlineno__': 1, 
# '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Dog' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}

print('object "dog" attributes:', dog.__dict__)
# object "dog" attributes: {}


## .__class__  ==  type()
# The same information stored in __class__could be retrieved by calling a type() function with one argument:

for element in (1, 'a', True):
    print(element, 'is', element.__class__, type(element))
# 1 is <class 'int'> <class 'int'>
# a is <class 'str'> <class 'str'>
# True is <class 'bool'> <class 'bool'>



### Creating Class with type(,,)

Dog = type('Dog', (), {})

print('The class name is:', Dog.__name__)
# The class name is: Dog

print('The class is an instance of:', Dog.__class__)
# The class is an instance of: <class 'type'>

print('The class is based on:', Dog.__bases__)
# The class is based on: (<class 'object'>,)

print('The class attributes are:', Dog.__dict__)
# The class attributes are: {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>,
# '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}


### Metaclasses

# Anything in Python is a n "object" including classes
# Metaclasses are classes of classe: they define how to create and structurate classes
# The default metaclass is "type" as seen above


def bark(self):            # => a function \
    print('Woof, woof')    #                \____ bark() and "Animal" class will be parents of new class
                           #                /
class Animal:              # => a class    /
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})  # instance creation, indeed a class
# class constructor ==> type(class name, parents tuple, attributes dictionary)
#                               'Dog'      (Animal, )   {'age':0, 'bark':bark}
# type() is the MetaClass of Dog

print('The class name is:', Dog.__name__)
# Dog

print('The class is an instance of:', Dog.__class__)
# <class 'type'>

print('The class is based on:', Dog.__bases__)
# (<class '__main__.Animal'>,)

print('The class attributes are:', Dog.__dict__)
# # The class attributes are: {'age': 0, 'bark': <function bark at 0x000001F026EB1440>,
# '__module__': '__main__', '__doc__': None}

doggy = Dog()
doggy.feed()
# It is feeding time!
doggy.bark()
# Woof, woof

## This is the equivalent of this below:
class Dog(Animal):
    age = 0
    
    def bark(self):
        print('Woof, woof')

# This show that:
#   Classes are objects, created by MetaClasses, by default type
#   We can create Classes dynamiquely
#   type has 2 roles : 
#   - builtin function to know an object type : type(obj)
#   - Class constructor : type(name, parents, attributes)



### Create your own MetaClass

class My_Meta(type):                                         # we create a Class inheriting from type, so My_Meta is aMetaClass as well
    def __new__(mcs, name, bases, dictionary):               # mcs = My_Meta, name = "will be" My_Object, bases = () as not any inheritance here, dictionary ) dict of Class attributes
        obj = super().__new__(mcs, name, bases, dictionary)  # is the same than type(name, bases, dictionary)
        obj.custom_attribute = 'Added by My_Meta'            # we add a static attribute
        return obj                                           # we return the so created Class

class My_Object(metaclass=My_Meta):      # will use MetaClass My_MEta to build instance, the My_Object Class
    pass                                 # empty Class but will be populated by My_Meta MetaClass


print(My_Object.__dict__)
# {'__module__': '__main__', '__firstlineno__': 7, '__static_attributes__': (),
# '__dict__': <attribute '__dict__' of 'My_Object' objects>,
# '__weakref__': <attribute '__weakref__' of 'My_Object' objects>, '__doc__': None,
# 'custom_attribute': 'Added by My_Meta'} ==> # 'custom_attribute' is here !

print(My_Object.custom_attribute)  
# 'Added by My_Meta'

obj = My_Object()
print(obj.custom_attribute)  
# 'Added by My_Meta'


## __new__

class Example:
    def __init__(self, value):
        print("3. __init__ invoked - OBJECT INITIALISATION")
        self.value = value
        print(f"4. Objet initialised with value = {self.value}")
    
    def __new__(cls, *args, **kwargs):      # cls = Example, *args/**kwargs = any arguments passed
        print("1. __new__ invoked - OBJECT CREATION")
        instance = super().__new__(cls)     # must return an new instance
        print(f"2. Object created: {instance}")
        return instance  # if returns None, __init__ won't be executed

    
obj = Example("Hello")
# 1. __new__ invoked - OBJECT CREATION
# 2. Object created: <__main__.Example object at 0x...>
# 3. __init__ invoked - OBJECT INITIALISATION
# 4. Objet initialised with value = Hello


## build a metaclass responsible for completing classes with a method (if missing) to ensure that all your classes are equipped with a method

def greetings(self):  # basic function
    print('Just a greeting function, but it could be something more serious like a check sum')  # prints the Output

class My_Meta(type):  # Creates a MetaClass
    def __new__(mcs, name, bases, dictionary):
        if 'greetings' not in dictionary:       # checks if "greetings" attribute (function) is NOT in the Object's (a Class here) dictionary
            dictionary['greetings'] = greetings # if so, we add an item => {"greetins";greetings} , key,value, value being the function greetings()
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

class My_Class1(metaclass=My_Meta):
    pass

class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print('We are ready to greet you!')

myobj1 = My_Class1()

print (My_Class1.__dict__)
# {'__module__': '__main__', '__firstlineno__': 11, '__static_attributes__': (), 
# 'greetings': <function greetings at 0x000001BCBACC1440>,                        ==> 'greetings' has been added ! AFTER __static_attributes__
# '__dict__': <attribute '__dict__' of 'My_Class1' objects>,
# '__weakref__': <attribute '__weakref__' of 'My_Class1' objects>, '__doc__': None}
print (myobj1.__dict__)
# {}
myobj1.greetings()
# Just a greeting function, but it could be something more serious like a check sum


myobj2 = My_Class2()
print (My_Class2.__dict__)
# {'__module__': '__main__', '__firstlineno__': 14, 
# 'greetings': <function My_Class2.greetings at 0x00000188C3190C20>,                ==> already present, BEFORE __static_attributes__
# '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'My_Class2' objects>,
# '__weakref__': <attribute '__weakref__' of 'My_Class2' objects>, '__doc__': None}
print (myobj2.__dict__)
# {}
myobj2.greetings()
# We are ready to greet you!