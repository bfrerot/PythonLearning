########## OBJECT ORIENTED PROGRAMMATION ##########


### CLASS
# A class (among other definitions) is a set of objects. An object is a being belonging to a class.
# A class is an idea (more or less abstract) which can be used to create a number of incarnations – such an incarnation is called an object.
# When a class is derived from another class, their relation is named inheritance. The class which derives from the other class is named a subclass. The second side of this relation is named superclass

# define a class
class TheSimplestClass:
    pass



### OBJECT
# An object is an incarnation of the requirements, traits, and qualities assigned to a specific class
# every existing object may be equipped with three groups of attributes:
# an object has a name that uniquely identifies it within its home namespace (although there may be some anonymous objects, too)
# an object has a set of individual properties which make it original, unique, or outstanding (although it's possible that some objects may have no properties at all)
# an object has a set of abilities to perform specific activities, able to change the object itself, or some of the other objects
# Each subclass is more specialized (or more concrete) than its superclass. Conversely, each superclass is more general (more abstract) than any of its subclasses.

# hint  which can help you identify any of the three spheres above. 
# Whenever you describe an object and you use:
# a noun – you probably define the object's name;
# an adjective – you probably define the object's property;
# a verb – you probably define the object's activity.

# example:

# A pink Cadillac went quickly.

# Object name = Cadillac
# Home class = Wheeled vehicles
# Property = Color (pink)
# Activity = Go (quickly)

# Rudolph is a large cat who sleeps all day.

# Object name = Rudolph
# Home class = Cat
# Property = Size (large)
# Activity = Sleep (all day)

# define an object
my_first_object = TheSimplestClass()
# The act of creating an object of the selected class is also called an instantiation (as the object becomes an instance of the class).


### INHERITANCE
#  inheritance. Any object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements and qualities) defined inside any of the superclasses.



### STACK
# A stack is a structure developed to store data in a very specific way.
# The alternative name for a stack (but only in IT terminology) is LIFO = Last In First Out
# A stack is an object with two elementary operations, conventionally named push (when a new element is put on the top) and pop (when an existing element is taken away from the top)

## the procedural approach
# 1- decide how to store the values which will arrive onto the stack
#       a list [] is the best option
stack = []
# 2- define a function that puts a value onto the stack
def push(val):
    stack.append(val)
# 3- define a unction to take a value off the stack
def pop():
    val = stack[-1]
    del stack[-1]
    return val
# to summarize:
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3) # stack = [3]
push(2) # stack = [3,2]
push(1) # stack = [3,2,1]

print(pop())
1
print(pop())
2
print(pop())   
3

## the object approach
# how the object stack begins,  class [name]:

# we have to install a list inside each object of the class
# we want the list to be hidden from the class users' sight
# we have to add a specific statement or instruction. 
# The properties have to be added to the class manually
# we will equip the class with a specific function – its specificity is dual:
#   it has to be named in a strict way
#   it is invoked implicitly, when the new object is created.
# Such a function is called a constructor, as its general purpose is to construct a new object. 
# The constructor should know everything about the object's structure, 
# and must perform all the needed initializations.

class Stack:
    def __init__ (self):
        print("Hi!")
 
stack_object = Stack()
# Hi!

class Stack:
    def __init__(self):
        self.name = [1,2]

stack_object = Stack()
print(len(stack_object.name))
2
# we've used dot notation, just like when invoking methods; this is the general convention
# for accessing an object's properties
# we need to name the object, put a dot (.) after it, and specify the desired property's name
# we don't use parentheses! we do not invoke a method but a property;

## __
class Stack:
    def __init__(self):
        self.__stack_list = []


stack_object = Stack()
print(len(stack_object.__stack_list))
# AttributeError: 'Stack' object has no attribute '__stack_list'  
  
# When any class component has a name starting with two underscores (__), it becomes private 
# this means that it can be accessed ONLY FROM WITHIN the class.

## the stack approach

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.push(3) # stack_object = [3]
stack_object.push(2) # stack_object = [3,2]
stack_object.push(1) # stack_object = [3,2,1]

print(stack_object.pop())
1
print(stack_object.pop())
2
print(stack_object.pop())
3

# IF we start functions names by 2*_ or more, we have a problem, as explained above
class Stack:
    def __init__(self):
        self.__stack_list = []

    def __push(self, val):
        self.__stack_list.append(val)

    def __pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object.__push(3) # stack_object = [3]
stack_object.__push(2) # stack_object = [3,2]
stack_object.__push(1) # stack_object = [3,2,1]

print(stack_object.__pop())
print(stack_object.__pop())
print(stack_object.__pop())
# AttributeError: 'Stack' object has no attribute 'push'

# 1*_ is ok
class Stack:
    def __init__(self):
        self.__stack_list = []

    def _push(self, val):
        self.__stack_list.append(val)

    def _pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object = Stack()

stack_object._push(3) # stack_object = [3]
stack_object._push(2) # stack_object = [3,2]
stack_object._push(1) # stack_object = [3,2,1]

print(stack_object._pop())
print(stack_object._pop())
print(stack_object._pop())
1
2
3

# Here, both functions have a parameter named "self" at the first position of the parameters list
# it is NEEDED
# All methods have to have this parameter. It plays the same role as the first constructor parameter
# It allows the method to access entities (properties and activities/methods) carried out by the actual object
# Every time Python invokes a method, it implicitly sends the current object as the first argument
# This means that a method must have at least one parameter, which is used by Python itself 

# two stacks created from the same base class
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object_1 = Stack() 
stack_object_2 = Stack()

stack_object_1.push(3) # = [3]
stack_object_2.push(stack_object_1.pop()) # = [3]

print(stack_object_2.pop()) # = [3]
3

# three ...
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack() # = []
another_stack = Stack() # = []
funny_stack = Stack() # = []

little_stack.push(1) # = [1]
another_stack.push(little_stack.pop() + 1)  # = [2]
funny_stack.push(another_stack.pop() - 2)  # = [0]

print(funny_stack.pop())
# 0