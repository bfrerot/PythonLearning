########## OBJECT ORIENTED PROGRAMMATION ##########




##### BASIS TERMS

### CLASS — an idea, blueprint, or recipe for an instance

class TheClass:
    class_variable = True  # This is a class variable (property)

    def __init__(self):
        self.instance_variable = False  # This is an instance variable

    def do_this(self):  # This is a class function (method)
        return TheClass.class_variable
    
    
    
### OBJECT/INSTANCE — an instantiation of the class; very often used interchangeably with the term 'object'

class TheClass:
    pass

the_object = TheClass()  # the_object is an object of TheClass class



### ATTRIBUTE — any object or class trait; could be a variable or method

### METHOD — a function built into a class that is executed on behalf of the class or object; some say that it’s a 'callable attribute'

######################################################################################################################################################################################



##### CLASS

# A class (among other definitions) is a set of objects. An object is a being belonging to a class
# A class is an idea (more or less abstract) which can be used to create a number of incarnations – such an incarnation is called an object
# When a class is derived from another class, their relation is named inheritance ==> subclass(superclass)
# Each subclass is more specialized (or more concrete) than its superclass
# Conversely, each superclass is more general (more abstract) than any of its subclasses


# define a class
class TheSimplestClass:
    pass

# inheritance
class Alpha: # superclass of Beta
    value = "Alpha"

    def say(self):
        return self.value.lower()

class Beta(Alpha): # subclass of Alpha()
    pass


class Stack:
    def __init__(self):
        self._stack_list = [] # crée une list vide
        
    def get_list(self):
        return self._stack_list
        
    def push(self, val):
        self._stack_list.append(val) # crée une fonction qui ajout une val à la fin de la list
        return self._stack_list      # return la value

    def pop(self):
        value = self._stack_list[-1] # crée une fonction qui delete le dernier elem de la list 
        del self._stack_list[-1]     # et renvoie la valeur de l'elm poppé
        return value


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self) # invoque l'upper class Stack
        self.__sum = 0       # crée une variable privée sum, integer

    def get_sum(self):       # la fonction créée return la valeur de sum
        return self.__sum

    def push(self, val):      # la fonction ajoute une valeur à sum
        self.__sum += val
        Stack.push(self, val)

    def pop(self):               # la fonction enleve une valeur à sum 
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())
10
print(stack_object.get_list())
[0, 1, 2, 3, 4]

for i in range(5):
    print(stack_object.pop())
    4
    3
    2
    1
    0
print(stack_object.get_sum())
0
print(stack_object.get_list())
[0]





##### OBJECT/INSTANCE OF A CLASS

# An object is one particular physical instantiation of a class that occupies memory and has data elements
# This is what 'self' refers to when we deal with class instances

# !! An object is everything in Python that you can operate on, like a class, instance, list, or dictionary
# The term instance is very often used interchangeably with the term object, because object refers to a particular instance of a class
# It’s a bit of a simplification, because the term object is more general than instance !!

# An instance is an incarnation of the requirements, traits, and qualities assigned to a specific class
# every existing object may be equipped with three groups of attributes:
#    a name that uniquely identifies it within its home namespace 
#    a set of individual properties which make it original, unique, or outstanding
#    a set of abilities to perform specific activities

# Whenever we describe an object we use:
#   a noun = object's name
#   an adjective = object's property
#   a verb = object's activity

# example:
# A pink Cadillac went quickly.
# ==>
# Object name = Cadillac
# Home class = Wheeled vehicles
# Property = Color (pink)
# Activity = Go (quickly)

# Rudolph is a large cat who sleeps all day.
# ==>
# Object name = Rudolph
# Home class = Cat
# Property = Size (large)
# Activity = Sleep (all day)


# define an object
my_first_object = TheSimplestClass()
# The act of creating an object of the selected class is also called an instantiation (as the object becomes an instance of the class).





##### CLASS vs INSTANCE variables

class Animal:
    espèce = "Mammifère"  # Variable de classe

    def __init__(self, nom):
        self.nom = nom  # Variable d'instance

# Toutes les instances partagent la variable espèce
a1 = Animal("Lion")
a2 = Animal("Tigre")

print(a1.espèce)  
# Mammifère
print(a2.espèce)  
# Mammifère


# Modifier la variable de classe depuis la Class !! ==> impacte tous les Objets = Good practice
Animal.espèce = "Vertébré"

print(a1.espèce)  
# Vertébré
print(a2.espèce)  
# Vertébré


## Il faut EVITER de creer des variables d'instance du meme nom que des variables de class
# ci-dessous un exemple du fonctionnement

class Demo:
    class_var = 'shared variable'

d1 = Demo()
d3 = d1
d2 = Demo()

# both instances allow access to the class variable
print(d1.class_var)
# shared variable
print(d2.class_var)
# shared variable

# d1 object has no instance variable
print('contents of d1:', d1.__dict__)
# contents of d1: {}

# d1 object receives an instance variable named 'class_var'
d1.class_var = "I'm messing with the class variable"

# d1 object owns the variable named 'class_var' which holds a different value than the class variable named in the same way
print('contents of d1:', d1.__dict__)
# contents of d1: {'class_var': "I'm messing with the class variable"}
print(d1.class_var)
# I'm messing with the class variable

# d3 object is linked to d1 so has the same value
print(d3.class_var)
# I'm messing with the class variable

# d2 object variables were not influenced
print('contents of d2:', d2.__dict__)
# contents of d2: {}

# d2 object variables were not influenced
print('contents of class variable accessed via d2:', d2.class_var)
# contents of class variable accessed via d2: shared variable


# Bien comprendre l'interaction sur les variables de Class, selon qu'elle soient modifiées via l'Objet ou la Class
class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __action(self):
        pass

product = BluePrint()
print(product.__dict__)
# {'component': 1} # pas de __element, la variable de Class n'est PAS une variable d'Objet

# How change the private BluePrint class variable "stamps" value ?

# ==> Via l'Object

product._BluePrint__element +=1 # va chercher la variable de Class et en crée une spécifique à l'Objet, indépendante de celle de de Class, et l'augmente de 1
print(BluePrint._BluePrint__element) # n'agira pas sur la variable de Class
# 1
print(product._BluePrint__element) # agira bien sur la variable d'objet
# 2
print(product.__dict__)
# {'component': 1, '_BluePrint__element': 2} # la variable est bien dans le object.__dict__ maintenant

# ==> Via la Class

BluePrint._BluePrint__element +=1
print(BluePrint._BluePrint__element) # +1 sur la variable de Class
# 2
print(product._BluePrint__element) # aucun changement sur la variable d'Objet
# 2



### ATTRIBUTE

# An attribute is a capacious term that can refer to two major kinds of class traits:
#   - variables, containing information about the class itself or a class instance; classes and class instances can own many variables
#   - methods, formulated as Python functions; they represent a behavior that could be applied to the object
# It is said that methods are the 'callable attributes' of Python objects

class Person:
    species = "Homo sapiens" # Variable de classe

    def __init__(self, name, age):  # Method dite constructor
        self.name = name    # Attribut d'instance
        self.age = age      # Attribut d'instance
        self.__secret = "secret_value"    # Attribut privé d'instance - ENCAPSULATION

    def greet(self):        # Méthode d'instance
        return f"Bonjour, je m'appelle {self.name}"



### CLASS VARIABLES

# class variable remains the same for all instances using the class
# if the class variable changes, it changes for ALL instances variables

class A:
    X = 0
    def __init__(self,v = 0):
        self.Y = v
        A.X += v

a = A() # A.X += v ==> X = 0
b = A(1) # A.X += v ==> X = 0 + 1 = 1
c = A(2) # A.X += v ==> X = 1 + 2 = 3
print(c.X)
# 3


class ExampleClass:
    counter = 0 # class variable
    def __init__(self, val = 1):
        self.__first = val # instance variable
        ExampleClass.counter += 1
 
example_object_1 = ExampleClass()
print(example_object_1.__dict__, example_object_1.counter)
# {'_ExampleClass__first': 1} 1
example_object_2 = ExampleClass(2)
print(example_object_2.__dict__, example_object_2.counter)
# {'_ExampleClass__first': 2} 2
example_object_3 = ExampleClass(4)
print(example_object_3.__dict__, example_object_3.counter)
# {'_ExampleClass__first': 4} 3


class Package:
    spam = ''

    def __init__(self, content):
        Package.spam += content + ":"

envelope_1 = Package("Capacitors")
print(Package.spam)
# Capacitors
envelope_2 = Package("Transistors")
print(Package.spam)
# Capacitors:Transistors: # spam value has changed
print(envelope_2.spam)
# Capacitors:Transistors:



### attributes for classes VS for instances:

class Person:
    species = "Homo sapiens" # Attribut de classe

    def __init__(self, name, age):  # ==> = __static_attributes__
        self.name = name    # Attribut d'instance
        self.age = age      # Attribut d'instance
        self.__secret = "secret_value"    # Attribut privé d'instance - ENCAPSULATION

    def greet(self):        # Méthode d'instance
        return f"Bonjour, je m'appelle {self.name}"

p = Person("Alice", 30)      # Création d’une instance (objet) de la class Person

# ==> Attributs de la classe
print(Person.__dict__)  # Dictionnaire des attributs de la classe Person()
# {'__module__': '__main__', '__firstlineno__': 48, 'species': 'Homo sapiens', '__init__': <function Person.__init__ at 0x000002047D312020>, 
#  'greet': <function Person.greet at 0x000002047D3120C0>, '__static_attributes__': ('__secret', 'age', 'name'), 
#  '__dict__': <attribute '__dict__' of 'Person' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
# on voit bien: species, __init__ + __static_attributes__ associés, greet

# ==> Attributs de l’objet
print(p.__dict__)  # Dictionnaire des attributs de l’objet p(Person)
# {'name': 'Alice', 'age': 30, '_Person__secret': 'secret_value'}
# on voit bien: name et age qui sont attendus comme argument pour créer l'instance + _Person__secret qui est "encapsulée" (cachée)


# Accès aux attributs
print("Classe :", Person.species)
print("Objet :", p.species)  # hérité de la class

print("Nom de l'objet :", p.name)
print("Age de l'objet :", p.age)

# Accès à l'attribut privé (name mangling)
print(p._Person__secret)  # Attention !!! accès direct déconseillé en pratique
# secret_value






##### ENCAPSULATION - private attribute
# __ = private !

# L'encapsulation en Python (et en programmation orientée objet en général) désigne le fait de cacher certains détails internes d'une class
# pour éviter qu'ils soient modifiés ou utilisés de manière inappropriée directement depuis l'extérieur
# Cela permet de protéger l'intégrité des données et de contrôler l'accès à celles-ci via des méthodes (getter, setter)

# C'est une pratique qui consiste à limiter l'accès direct à certains attributs ou méthodes d'une classe
# La façon la plus courante d'implémenter cela est de rendre certains attributs "privés" ou "protégés"
# En Python, cette notion est basée sur la convention plutôt que sur une restriction stricte, contrairement à d'autres langages (comme Java)


# Différents types d'encapsulation en Python

# | Syntaxe         | Signification                        | Description                                              
# |-----------------|--------------------------------------|----------------------------------------------------------------------------
# | _attribut       | **Protégé** (convention)             | Indique que l'attribut est destiné à un usage interne
# | __attribut      | **Privé** (manglé, name mangling)    | Renomme l'attribut pour le rendre difficile d'accès direct depuis l'extérieur

class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))
# AttributeError: 'Stack' object has no attribute '__stack_list'  
# on voit bien que l'on ne peut pas accéder "simplement" à l'attribut privé





##### TYPE

# type is one of the most fundamental and abstract terms of Python

# it is the foremost type that any class can be inherited from
# if we look for the type of class, type is returned

# in all other cases, it refers to the class that was used to instantiate the object
# it’s a general term describing the type/kind of any object

# it’s the name of a very handy Python function that returns the class information about the objects passed as arguments to that function

# it returns a new type object when type() is called with three arguments

# Python comes with a number of built-in types, like numbers, strings, lists, etc., that are used to build more complex types
# Creating a new class creates a new type of object, allowing new instances of that type to be made

# Information about an object’s class is contained in __class__

class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

print(type(Duck))
# <class 'type'>
print(Duck.__class__)
# <class 'type'> 
print(duckling.__class__)
# <class '__main__.Duck'>
print(duckling.sex.__class__)
# <class 'str'>
print(duckling.quack.__class__)
# <class 'method'>





##### INHERITANCE

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

# La règle principale en héritage multiple:
#	- Python doit pouvoir déterminer dans quel ordre il va rechercher les méthodes ou attributs si plusieurs classes parents ont des méthodes du même nom
#	- la MRO doit être cohérente et respecter la hiérarchie pour éviter des ambiguïtés ou des cycles

class Top:
    pass

class Left(Top): # La class Left hérite de Top
    pass

class Right(Top): # La class Right hérite de Top
    pass

class Bottom(Left, Right): # La class Bottom hérite de Left et Right, ce qui est cohérent car Left et Right ont un ancêtre commun Top
    pass

class Bottom1(Left, Top): # ok mais inutile car Left hérite déjà de Top plus haut
    pass

class Bottom2(Top, Left): # ici on inverse l’ordre : (Top, Left)
    pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Left
# ==> Python ne peut pas créer une MRO cohérente parce que :
#     Left hérite dejà de Top, Left est déjà une sous-classe de Top donc cette hiérarchie crée un conflit de MRO
# La MRO doit respecter la hiérarchie des class !!


# L'objet peut accéder aux variables d'instance de la superclass
class Sup:
    supVar = 1

class Sub(Sup):
    subVar = 2

obj = Sub()

print(obj.subVar)
# 2 ==> class Sub
print(obj.supVar)
# 1 ==> class Super (upper class)


# L'objet NE PEUT PAS accéder aux variables de __init__ + __static_attributes__ associés de la superclass, par défaut:
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        self.subVar = 12

obj = Sub()
print(obj.supVar)
# AttributeError: 'Sub' object has no attribute 'supVar'

# sauf si on utilise super().__init__() qui va aller chercher les statics_attributes de la superclass:
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
    value = "Alpha"

    def say(self):
        return self.value.lower()

class Beta(Alpha):
    pass

class Gamma(Alpha):
    def say(self):
        return self.value.upper() # 1- va chercher une variable "value", Gamma() ?, nok

class Delta(Gamma, Beta):
    pass

d = Delta()
print(d.say())
# ALPHA
# ==>
# 1- va chercher une method say()
#   1a- dans Delta() ?, nok
#   1b- dans Gamma() ?, yes !
#       2- va chercher une variable "value"
#           2a- dans Delta() ?, nok
#           2b- dans Gamma() ?, nok
#           2c- dans Alpha() ?, yes !
#               3- return "Alpha" en uppercase = ALPHA


# SANS HOMONYME
# sans priorisation entre upper classes
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


# AVEC HOMONYME
# ici __str__(), dont l'existence est automatiquement recherchée, et print le return configuré
class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B): # A() est consulté avant B()
    pass

class D(B, A): # B() est consulté avant A()
    pass

o = C()
print(o)
# a
o2 = D()
print(o2)
# b



### ISSUBCLASS(CLASS,SUBCLASS)

# python builtin function to check if a class is subclass of another class

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
# True    False   False
# True    True    False
# True    True    True    

# each class is a subclass of itself !



### ISINSTANCE(OBJECT,CLASS)

# python builtin function to check if an object is related to a class
# Let's assume that you've got a cake (OBJECT) and we want to know what recipe (CLASS) has been used to make it
# Why? Because we want to know what to expect from it, whether it contains nuts or not, which is crucial information to some people.

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
# True    False   False
# True    True    False
# True    True    True

# if an obect is an instance of a class, it will be an instance of all upperclass of this class




### OBJECT1 = OBJECT2
# The is operator checks whether two variables (object_one and object_two here) refer to the same object

class SampleClass:
    def __init__(self, val):
        self.val = val

object_1 = SampleClass(0) # = 0
object_2 = SampleClass(2) # = 2
object_3 = object_1 # = 0 mais aussi object_1 et object_3 partagent désormais le meme emplacement mémoire, la meme valeur
print(object_1.val)
# 0
print(object_3.val)
# 0
object_3.val += 1 # = 1  ==> object_1.val += 1 en //
print(object_1.val)
# 1
print(object_3.val)
# 1

print(object_1 is object_2)
# False
print(object_2 is object_3)
# False
print(object_3 is object_1)
# True ==> like list, the 2*objects are linked



### SUPER()

# ==> appel direct à la classe parente
# manière directe PAS RECOMMANDEE car ne gère pas certains aspects liés à l'héritage multiple ou à la chaîne d'héritage multiple

# super() retourne une "super class" c'est-à-dire la classe parente dans le contexte actuel et appelle sa méthode __init__
# Avantages :
#  - Plus flexible, surtout dans le contexte de l'héritage multiple
#  - Respecte la chaîne d'héritage et peut faire appel à la méthode __init__ de la classe suivante dans l'ordre MRO (Method Resolution Order)

class Sup:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # Python check toujours si method __str__() or __repr__()
        return "My name is " + self.name + "."

class Sub(Sup):
    def __init__(self, name):
        Sup.__init__(self, name)

obj = Sub("Andy")
print(obj)  
# My name is Andy.


## invoquer super().__init__()

# choix A, python3+, recommandé
class SpamException (Exception):
    def __init__ (self, message):
        super().__init__(message)
        self.message = message
#raise SpamException( "Spam" ) # enlever le # pour voir tester

# Traceback (most recent call last):
#   File "c:\PythonLearning\error_test.py", line 5, in <module>
#     raise SpamException( "Spam" )
# SpamException: Spam


# choix B, python2/3
class Spam2Exception (Exception):
    def __init__ (self, message):
        super(Spam2Exception, self).__init__(message)
        self.message = message
# raise Spam2Exception( "Spam" ) # enlever le # pour voir tester


## question, si plusieurs superclass ?
# ==> super() en Python 3 gère automatiquement l'héritage multiple grâce au MRO (Method Resolution Order)
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
        super().__init__(value)  # Appelle automatiquement selon le MRO
        self.c_value = value

c = C("test")

c = C()
# C init: test
# A init: test

# pour voir l'orde de résolution:
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


## pour viser une superclass en particulier
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
        # Appeler spécifiquement B, peu importe le MRO
        B.__init__(self, value)

c = C("test")
# B init: test


## pour viser toutes les superclass, avec **kwargs ou "kwargs" peut etre modifié par n'importe quel string
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

# Polymorphism is a mechanism which enables the programmer to modify the behavior of any of the object's superclasses without modifying these classes themselves

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





##### STACK
# A stack is a structure developed to store data in a very specific way.
# The alternative name for a stack (but only in IT terminology) is LIFO = Last In First Out
# A stack is an object with two elementary operations, conventionally named push (when a new element is put on the top) and pop (when an existing element is taken away from the top)


## PROCEDURAL approach

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


## OBJECT approach

# how the object stack begins,  class [name]:

# we have to install a list inside each object of the class
# we want the list to be hidden from the class users' sight
# we have to add a specific statement or instruction
# The properties have to be added to the class manually
# we will equip the class with a specific function – its specificity is dual:
#   it has to be named in a strict way
#   it is invoked implicitly, when the new object is created
# Such a function is called a constructor, as its general purpose is to construct a new object
# The constructor should know everything about the object's structure, 
#   and must perform all the needed initializations.

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


## STACK approach

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





##### PROPERTIES


### __REPR__()

class ExampleClass:
    def __init__(self, val1=1): 
        self.first = val1

    def set_caca(self, val2):
        self.caca = val2
        
    def __repr__(self):
        return f"ExampleClass(first={self.first}, caca={getattr(self, 'caca', None)})"

example_object_2 = ExampleClass(10)
print(example_object_2)
# ExampleClass(first=10, caca=None)
example_object_2.set_caca(666)
print(example_object_2.caca)
# 666

# ==> Pourquoi __repr__() s'exécute-t-elle même si tu ne l'as pas appelée explicitement ?
# print(objet) :
# Python tente d’afficher une représentation lisible de l’objet
# Pour cela, il cherche d’abord si la classe de l’objet a défini la méthode __str__()
#   Si oui, il l'appelle pour obtenir la chaîne à afficher
#   Si __str__() n’est pas défini, Python appelle alors la méthode __repr__() pour obtenir cette représentation
#   Si aucune de ces méthodes n’est définie
#       Python affiche le nom de la classe et l’adresse mémoire par défaut



### __STR__()

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Personne: {self.nom}, âge: {self.age}"

# Création d'une instance
p = Personne("Alice", 30)

# Affichage avec print()
print(p)
# Personne: Alice, âge: 30
print(p.nom)
# Alice

# __str__() définit la chaîne de caractères qui sera affichée lorsque l'on print() l’objet.
# Sans __str__(), ou __repr__, Python afficherait quelque chose comme <__main__.Personne object at 0x...>

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy

sun = Star("Sun", "Milky Way")
print(sun)
# Sun in Milky Way    



### HASATTR(OBJECT,ATTRIBUTE)

# check si un objet possède un attribut

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
 
 
example_object = ExampleClass(1)

if hasattr(example_object, 'a'):
    print(example_object.a) # 1
if hasattr(example_object, 'b'):
    print(example_object.b)
    
example_object = ExampleClass(2)

if hasattr(example_object, 'a'):
    print(example_object.a) 
if hasattr(example_object, 'b'):
    print(example_object.b) # 1
    
    
# s'applique aussi aux class

class ExampleClass:
    attr = 1
print(hasattr(ExampleClass, 'attr'))
# True
print(hasattr(ExampleClass, 'prop'))
# False


# attribut de class vs instance

class ExampleClass:
    a = 1 # pour la class et les objets
    def __init__(self):
        self.b = 2 # pour les objets seulement
 
 
example_object = ExampleClass()
 
print(hasattr(example_object, 'b')) # true
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a')) # true





##### METHODS   

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





##### INNER LIFE of classes and objects

# Each Python class object is pre-equipped with a set of useful attributes which 
# can be used to examine its capabilities.


### __DICT__() in depth

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()

print(obj.__dict__)
# {'var': 2} 

print(Classy.__dict__)
# {'__module__': '__main__', '__firstlineno__': 1, 'varia': 1, '__init__': <function Classy.__init__ at 0x000001B773103E20>, 'method': <function Classy.method at 0x000001B773111940>, '_Classy__hidden': <function Classy.__hidden at 0x000001B773110C20>, '__static_attrib<function Classy.method at 0x000001B773111940>, '_Classy__hidden': <function Classy.__hidden at 0x000001B773110C20>, '__static_attributes__': ('var',), '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objectutes__': ('var',), '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}


# {'__module__': '__main__',           
# Module où la classe est définie

# '__firstlineno__': 1,             
# ligne à laqualle la class commence       

# 'varia': 1,           
# attribut de class partagé par tous les objects

# '__init__': <function Classy.__init__ at 0x000001B773103E20>,             
# constructor, et emplacement mémoire

# 'method': <function Classy.method at 0x000001B773111940>,             
# method d'instance et emplacement mémoire

# '_Classy__hidden': <function Classy.__hidden at 0x000001B773110C20>,              
# methode privée d'instance 

# '__static_attributes__': ('var',),              
# Tuple listant les attributs statiques

# '__dict__': <attribute '__dict__' of 'Classy' objects>,
#

# '__weakref__': <attribute '__weakref__' of 'Classy' objects>,             
# Cet attribut permet la gestion des références faibles, référence à un objet qui ne 
# l’empêche pas d’être collecté par le ramasse-miettes ==> ???
# Cela est utile pour éviter les cycles de références ou pour suivre des objets sans empêcher
# leur suppression.

# '__doc__': None}    
# C’est la chaîne de documentation (docstring) de la classe ou de l’objet. Ici, elle est `None`,
# ce qui indique qu’il n’y a pas de documentation associée à cette classe ou cet objet.



### __NAME__
# contains the name of the class. It's nothing exciting, just a string
# it exists ONLY inside CLASSES
# so to find the class name of a particular OBJECT, you can use a function named type(), 
# which is able (among other things) to find a class which has been used to instantiate any object

class Classy:
    pass

print(Classy.__name__)
# Classy

obj = Classy()
print(type(obj))
# <class '__main__.Classy'>
print(type(obj).__name__)
# Classy


class Snake:
    pass
 
class Python(Snake):
    pass
 
print(Python.__name__, 'is a', Snake.__name__)
# Python is a Snake



### __MODULE__
# stores the name of the module which contains the definition of the class
class Classy:
    pass

print(Classy.__module__)
# __main__ ==> any module named __main__ is actually not a module, but the file currently being run
obj = Classy()
print(obj.__module__)
# __main__



### __BASES__
# __bases__ is a tuple. The tuple contains classes (not class names) which are direct 
# superclasses for the class
# The order is the same as that used inside the class definition

class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls): # un peu artificiel le résultat mais on comprend le principe
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne)
# ( object )
printBases(SuperTwo)
# ( object )
printBases(Sub)
# ( SuperOne SuperTwo )


class Snake:
    pass
class Python(Snake):
    pass

print(Python.__bases__[0].__name__, 'can be', Python.__name__)
# Snake can be Python





##### REFLECTION & INTROSPECTION

# introspection is the ability of a program to examine the type or properties of an object at runtime
# reflection is the ability of a program to manipulate the values, properties and/or functions of an object at runtime





##### INVESTIGATING CLASSES

# Both reflection and introspection enable a programmer to do anything with any object, no matter where it comes from

class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys(): # in ['a', 'b', 'i', 'ireal', 'integer', 'z']
        if name.startswith('i'): # ['i', 'ireal', 'integer']
            val = getattr(obj, name) # [3, 3.5, 4]
            if isinstance(val, int): # sous-entendu is True donc ok pour ['i', 'integer']
                setattr(obj, name, val + 1) # i passe de 3 à 4 et integer de 4 à 5, etc à chaque tour

print(obj.__dict__.keys())
# dict_keys(['a', 'b', 'i', 'ireal', 'integer', 'z'])
print(obj.__dict__)
# {'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
incIntsI(obj)
print(obj.__dict__)
# {'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}
incIntsI(obj)
print(obj.__dict__)
# {'a': 1, 'b': 2, 'i': 5, 'ireal': 3.5, 'integer': 6, 'z': 5}
   
    
    


##### EXCEPTIONS in OOP context


### Exceptions are Classes

# when an exception is raised, an object of the class is instantiated and goes through all levels of program execution,
# looking for the except branch that is prepared to deal with it

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)

# BaseException
#    +---BaseExceptionGroup
#    |   +---ExceptionGroup
#    +---Exception
#    |   +---ArithmeticError
#    |   |   +---FloatingPointError
#    |   |   +---OverflowError
#    |   |   +---ZeroDivisionError
#    |   +---AssertionError
#    |   +---AttributeError
#    |   +---BufferError
#    |   +---EOFError
#    |   +---ImportError
#    |   |   +---ModuleNotFoundError
#    |   |   +---ZipImportError
#    |   +---LookupError
#    |   |   +---IndexError
#    |   |   +---KeyError
#    |   |   +---CodecRegistryError
#    |   +---MemoryError
#    |   +---NameError
#    |   |   +---UnboundLocalError
#    |   +---OSError
#    |   |   +---BlockingIOError
#    |   |   +---ChildProcessError
#    |   |   +---ConnectionError
#    |   |   |   +---BrokenPipeError
#    |   |   |   +---ConnectionAbortedError
#    |   |   |   +---ConnectionRefusedError
#    |   |   |   +---ConnectionResetError
#    |   |   +---FileExistsError
#    |   |   +---FileNotFoundError
#    |   |   +---InterruptedError
#    |   |   +---IsADirectoryError
#    |   |   +---NotADirectoryError
#    |   |   +---PermissionError
#    |   |   +---ProcessLookupError
#    |   |   +---TimeoutError
#    |   |   +---UnsupportedOperation
#    |   +---ReferenceError
#    |   +---RuntimeError
#    |   |   +---NotImplementedError
#    |   |   +---PythonFinalizationError
#    |   |   +---RecursionError
#    |   |   +---_DeadlockError
#    |   +---StopAsyncIteration
#    |   +---StopIteration
#    |   +---SyntaxError
#    |   |   +---IndentationError
#    |   |   |   +---TabError
#    |   |   +---_IncompleteInputError
#    |   +---SystemError
#    |   |   +---CodecRegistryError
#    |   +---TypeError
#    |   +---ValueError
#    |   |   +---UnicodeError
#    |   |   |   +---UnicodeDecodeError
#    |   |   |   +---UnicodeEncodeError
#    |   |   |   +---UnicodeTranslateError
#    |   |   +---NotShareableError
#    |   |   +---UnsupportedOperation
#    |   +---Warning
#    |   |   +---BytesWarning
#    |   |   +---DeprecationWarning
#    |   |   +---EncodingWarning
#    |   |   +---FutureWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ImportWarning
#    |   |   +---ImportWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---ResourceWarning
#    |   |   +---RuntimeWarning
#    |   |   +---SyntaxWarning
#    |   |   +---UnicodeWarning
#    |   |   +---UserWarning
#    |   +---InterpreterError
#    |   |   +---InterpreterNotFoundError
#    |   +---ExceptionGroup
#    +---GeneratorExit
#    +---KeyboardInterrupt
#    +---SystemExit



### .ARGS

# la méthode .args est un attribut des objets d'exception (instances de classes dérivées de BaseException, comme Exception). 
# Si l'exception est levée sans argument (raise Exception()), alors e.args est une liste vide ([]).
# Si l'exception est levée avec un seul argument (raise Exception("message")), alors e.args est une tuple avec un seul élément (("message",)).
# Si plusieurs arguments sont donnés (raise Exception("msg1", "msg2")), alors e.args est une tuple contenant tous ces arguments (("msg1", "msg2")).

def print_arguments(arguments):
    lng = len(arguments)
    if lng == 0:
        print("")
    elif lng == 1:
        print(arguments[0])
    else:
        print(str(arguments))


try:
    raise Exception # La ligne raise Exception génère une exception de type Exception sans message.

except Exception as e: # L'exception est attrapée dans le bloc except sous la variable e
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_arguments(e.args) # = []
#  :  : 

try:
    raise Exception("my exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = (my exception) tupple
# my exception : my exception : my exception

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = ("my", "exception") tupple
# ('my', 'exception') : ('my', 'exception') : ('my', 'exception')

try:
    raise Exception(12345)
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_arguments(e.args) # = ("12345") tupple, l'int 12345 a bien été chagée en str
# 12345 : 12345 : 12345



### Exemple intéressant
# class + Error + boucle for

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I(): # va executer chaque method de la fonction
    print(x,end='') # print le return final snas aller à la ligne, sans espace  
# abc


#  Étape | Action                                   | Résultat / Variable                                   | Affichage            |
# |---------|------------------------------------------|--------------------------------------------------------|----------------------|
# | 1       | Crée instance `I()`                      | `self.i=0`, `self.s='abc'`                              |                      |
# | 2       | Appel `__iter__()`                       | Retourne l'objet lui-même                              |                      |
# | 3       | Appel `__next__()`                       | `i=0`, retourne `'a'`, `i=1`                          | Affiche `'a'`        |
# | 4       | Appel `__next__()`                       | `i=1`, retourne `'b'`, `i=2`                          | Affiche `'b'`        |
# | 5       | Appel `__next__()`                       | `i=2`, retourne `'c'`, `i=3`                          | Affiche `'c'`        |
# | 6       | Appel `__next__()`                       | `i=3`, levée `StopIteration`                          | Fin de la boucle     |

# raise StopIteration est la façon officielle en Python de dire :  
# ==> Fini, il n'y a plus d'éléments à fournir
#     La boucle for ou tout autre code qui utilise l'itérateur va alors arrêter automatiquement la boucle