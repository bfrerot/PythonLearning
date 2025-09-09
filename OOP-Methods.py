########## OOP - METHODS ##########   

# we know now that methods are functions embedded into classes
# the method must have at least a parameter and if only one, it should be "self"


### SELF

# The keyword "self" is used to indicate that this variable is created coherently and individually for the instance to make it independent 
# from other instances of the same class

class Demo:
    def __init__(self, value):
        self.instance_var = value
d1 = Demo(100)
d2 = Demo(200)
print("d1's instance variable is equal to:", d1.instance_var)
# 100
print("d2's instance variable is equal to:", d2.instance_var)
# 200
# ==> we instantiate the class twice, each time passing a different value to be stored inside the object
#     the print instructions prove the fact that instance variable values are kept independently because the printed values differ

class Example:
    def __init__(self, value):
        self.__internal = value

    def get_internal(self):
        return self.__internal

example1 = Example(10)
example2 = Example(99)
print(example1.get_internal())
# 10
print(example2.get_internal())
# 99


# self parameter is used to obtain access to the object's instance and class variables
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
obj = Classy()
obj.var = 3
obj.method()
# 2 3


# 2 ways for print

# ==> with return, clean and the best for clarity

class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

    def prin(self):
        return(self.get())    # via self.attribute 

stuff = Storage()
print(stuff.prin())  
# 1

class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

    def prin(self):
        return(Storage.get(self))  # via Class.attribute(self)

stuff = Storage()
print(stuff.prin())  
# 1

# ==> with print, a bit weirdy, à éviter mais comprendre le fonctionnement est bon pourla compréhension en général

class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

    def prin(self):
        print(self.get())     # via self.attribute

stuff = Storage()
print(stuff.prin())  
# 1
# None ==> print None en plus car pas d'action return définie

class Storage:
    def __init__(self):
        self.rack = 1

    def get(self):
        return self.rack

    def prin(self):
        print(Storage.get(self))    # via Class.attribute(self) 

stuff = Storage()
print(stuff.prin())  
# 1
# None ==> print None en plus car pas d'action return définie


# une method qui appelle une autre method dans la meme Class

class Classy:
    def other(self):
        print("other")
 
    def method(self):
        print("method")
        self.other()
 
obj = Classy() # rattache l'objet obj à la class Classy()
obj.method()
# method
# other



## 1*parameter, self

class Classy:
    def method(self):
        print("method")

obj = Classy()
obj.method()
# method



## 2*parameters, self & par
class Classy:
    def method(self, par):
        print("method:", par)
 
obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)
# method: 1
# method: 2
# method: 3



### __INIT__ 

# = constructor

# If a class has a constructor, it is invoked automatically and implicitly when the object of the class is instantiated

# constructor:
#   MUST have the self parameter (it's set automatically, as usual)
#   MAY have more parameters than just self; if this happens, the way in which the class name
#       is used to create the object must reflect the __init__ definition;
#   CAN be used to set up the object, i.e., properly initialize its internal state, create 
#       instance variables, instantiate any other objects if their existence is needed, etc.
#   CAN raise an Exception
#   CANNOT return a result


## __init__ avec 1*parameter en + de self
class Classy:
    def __init__(self, value):
        self.var = value

obj_1 = Classy("object") # 1*parameter obligatoire et l'__init__ attribue le parameter à l'objet
print(obj_1.var)
# object


## __init__ avec 1*parameter (avec valeur par défaut) en + de self
class Classy:
    def __init__(self, value = None):
        self.var = value

obj_1 = Classy("object")
obj_2 = Classy()
print(obj_1.var)
# object
print(obj_2.var)
# None



### STATIC & CLASS methods

# These alternative types of method should be understood as tool methods, extending our ability to use classes,
# and not necessarily requiring the creation of class instances to use them



### CLASS methods

# use cases:
#    control access to class variables
#    control access to a class variable containing information about the number of created instances or the serial number given to the last produced object
#    modify the state of the class variables
#    create a class instance in an alternative way, so the class method can be implemented by an alternative constructor.
#    etc

# to distinguish a class method from an instance method, we signal it with the @classmethod decorator preceding the class method definition

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal()) # __init__ is not invoked 
# of objects created: 0

example1 = Example(10) # instance creation => class variable impacted by __init__
print(Example.get_internal()) 
# of objects created: 1

example2 = Example(99) # instance creation => class variable impacted by __init__
print(Example.get_internal())
# of objects created: 2


## Class methods & Class __init__ interaction

class Car:
    def __init__(self, vin):    # __init__, self + 1*argument
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = "Renault"
        self.logo = "*"

    @classmethod
    def including_brand(cls, vin2, brand2, logo2):  # as "self" for instance, "cls" is a convention, is for the Class and is tagged: (parameter) cls: type[Self@Car]
        print('Class method was called')
        car = cls(vin2) # invokes __init__ => self.vin = vin2
        car.brand = brand2 # invokes __init__ => self.brand = brand
#        car.logo = logo2
        return car

# classic class instance:

#car1 = Car('ABCD1234')   # car1 instance created, __init__ invoked, car1.vin & car1.brand created ==> "ABCD1234" & ""
# Ordinary __init__ was called for ABCD1234
#print(car1.__dict__)
# {'vin': 'ABCD1234', 'brand': 'Renault', 'logo': '*'} => all attributes come from __init__ 
#print(car1.vin, car1.brand)
# ABCD1234 Renault



# class method

#   number of args in instance call = nuber of class method args 
#car2 = Car.including_brand('DEF567', 'NewBrand', "<>")  # car2 instance created using class method
# Class method was called
# Ordinary __init__ was called for DEF567
#print(car2.__dict__)
# {'vin': 'DEF567', 'brand': 'NewBrand', 'logo': '<>'}
#print(car2.vin, car2.brand)
# DEF567 NewBrand

#   number of args in instance call > number of class method args WITH # self.logo = "*"
#car3 = Car.including_brand('GHI8910', 'Tesla', "_-|-_")  # car3 instance created using class method
# Class method was called
# Ordinary __init__ was called for GHI8910
#print(car3.__dict__)
# {'vin': 'GHI8910', 'brand': 'Tesla', 'logo': '_-|-_'} # logo arg is created thru the class method
#print(car3.vin, car3.brand, car3.logo)
# GHI8910 Tesla _-|-_

#   number of args in instance call < number of class method args WITH # car.logo = logo2
car4 = Car.including_brand('JKL111213', 'Porsche', "£")  # car4 instance created using class method
# Class method was called
# Ordinary __init__ was called for JKL111213
print(car4.__dict__)
# {'vin': 'JKL111213', 'brand': 'Porsche', 'logo': '*'} # logo arg is taken from __init__, like a default 
print(car4.vin, car4.brand, car4.logo)
# JKL111213 Porsche *



### STATIC methods

# Static methods are methods that do not require (and do not expect!) a parameter indicating the class object 
# or the class itself in order to execute their code

# EX: a class that provides methods to operate on bank accounts including a method that validates 
# the correctness of the account number recorded in accordance with the IBAN standard


class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban
            
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222'] # "8"*20 is an element, etc

for element in account_numbers:
    if Bank_Account.validate(element): # implicit == True
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
# We can use 88888888888888888888  to create a bank account
# The account number 7777 is invalid
# The account number 2222 is invalid



### STATIC vs CLASS methods

# a class method requires 'cls' as the first parameter and a static method does not
# a class method has the ability to access the state or methods of the class, and a static method does not
# a class method is decorated by '@classmethod' and a static method by '@staticmethod'
# a class method can be used as an alternative way to create objects, and a static method is only a utility method
