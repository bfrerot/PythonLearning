########## OOP - CLASS and OBJECT ##########



#### CLASS

# A CLASS is an idea which can be used to create a number of incarnations 
# such an incarnation is called an OBJECT

# When a class is derived from another class, their relation is named inheritance 

## define a class
class TheSimplestClass:
    pass

## inheritance
class Alpha: # superclass of Beta
    value = "Alpha"

    def say(self):
        return self.value.lower()

class Beta(Alpha): # subclass of Alpha()
    pass




#### OBJECT/INSTANCE OF A CLASS

# An object is one particular physical instantiation of a class that occupies memory and has data elements
# This is what 'self' refers to when we deal with class instances

# !! An object is everything in Python that you can operate on, like a class, instance, list, or dictionary
# The term instance is very often used interchangeably with the term object, because object refers to a particular instance of a class
# It’s a bit of a simplification, because the term object is more general than instance !!

# An instance is an incarnation of the requirements, traits, and qualities assigned to a specific class
# Every existing object may be equipped with three groups of attributes:
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



## define an object
my_first_object = TheSimplestClass()
# The act of creating an object of the selected class is also called an instantiation 
# The object becomes an instance of the class




#### CLASS & OBJECT VARIABLES  

# ==> Exemple

class Animal:
    espèce = "Mammifère"  # Variable de classe

    def __init__(self, nom):
        self.nom = nom  # Variable d'instance


# Toutes les instances partagent la variable de class "espèce"
a1 = Animal("Lion")
a2 = Animal("Tigre")
print(a1.espèce)  
# Mammifère
print(a2.espèce)  
# Mammifère


## Modifier un variable

# une variable de class peut etre modifiée via la Class ==> GOOD PRACTICE
Animal.espèce = "Cétacé"
print(a1.espèce)  
# Cétacé
print(a2.espèce)  
# Cétacé

# une variable de class peut etre modifiée via l'Objet ==> BAD PRACTICE
# ==> cela crée un doublon de nom de variable, cela fonctionne mais ça n'est pas cohérent
a1.espèce = "Poisson"
print(a1.espèce)  
# Poisson  # la variable d'instance prend le pas sur la variable du meme nom de la Class
print(a2.espèce)  
# Cétacé

# une variable peut etre ajoutée à une instance de façon indépendante
a2.color = 'red'
print(a2.color) 
# red


## Cas des variables privées
class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __action(self):
        pass

product = BluePrint()
print(product.__dict__)
# {'component': 1} # 'component' via __init__

# Modifier via l'instance ==> BAD PRACTICE
product._BluePrint__element +=1 # va chercher la variable de Class et en crée une spécifique à l'Objet, indépendante de celle de de Class, et l'augmente de 1
print(BluePrint._BluePrint__element) # n'agira pas sur la variable de Class
# 1
print(product._BluePrint__element) # agira bien sur la variable d'objet
# 2
print(product.__dict__)
# {'component': 1, '_BluePrint__element': 2} # la variable est bien dans le object.__dict__ maintenant, 
#                                              MAIS le nom est trompeur, il est inspiré de celle de Class et personnalisé en valeur...

# Modifier via la Class
BluePrint._BluePrint__element +=1
print(BluePrint._BluePrint__element) # +1 sur la variable de Class
# 2
print(product._BluePrint__element) # aucun changement sur la variable d'Objet
# 2


## class variable remains the same for all instances using the class
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



## INSTANCE.__DICT__

print(a1.__dict__)
# {'nom': 'Lion', 'espèce': 'Poisson'}  # 'nom' via __init_ + 'espèce' via l'objet en direct
print(a1.Animal.espèce)
# AttributeError: 'Animal' object has no attribute 'Animal'

print(a2.__dict__)
{'nom': 'Tigre', 'color': 'red'}        # 'nom' via __init_ car + 'color' via l'objet en direct ET 'espèce' n'apparait pas car c'est une variable de Class
print(a2.espèce)                        #  mais si on invoque la variable on l'a bien
# Cétacé



## DIR(INSTANCE)

print(dir(a1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__',
# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'espèce', 'nom']  ==> 'nom' via Class.__init__ 
#                                                                                                                            + 'espèce' en direct

print(dir(a2))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
#  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'color', 'espèce', 'nom'] ==> 'nom' via Class.__init__  
#                                                                                                                                     + 'espèce' via la class
#                                                                                                                                     + 'color' en direct



## INSTANCE.__DIR__

print(a2.__dir__)
# ['nom', 'color', '__module__', '__firstlineno__', 'espèce', '__init__', '__static_attributes__', '__dict__', 
#  '__weakref__',  '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', 
#  '__delattr__', '__lt__',  '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', 
#  '__getstate__', '__subclasshook__',  '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']



## CLASS.__DICT__

class Animal:
    espèce = "Mammifère"  # Variable de classe

    def __init__(self, nom):
        self.nom = nom  # Variable d'instance

# Toutes les instances partagent la variable espèce
a1 = Animal("Lion")
a2 = Animal("Tigre")

print(Animal.__dict__)
# {'__module__': '__main__', '__firstlineno__': 1, 'espèce': 'Mammifère',      ==> variable de Class 'espèce' + function __init__ (et toute autre fonction)
# '__init__': <function Animal.__init__ at 0x0000012AFE6A3E20>,
#  '__static_attributes__': ('nom',), '__dict__': <attribute '__dict__' of 'Animal' objects>,
# '__weakref__': <attribute '__weakref__' of 'Animal' objects>, '__doc__': None}



## DIR(CLASS)

print(dir(Animal))
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', 
 '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
 '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'espèce']   # ==> 'espèce' variable de Class



## CLASS.__DIR__

print(Animal.__dir__)
# <method '__dir__' of 'object' objects>



## .__DICT__ VS DIR()

class Cat:
    Species = 1
 
    def get_species(self):
        return 'kitty'
 
class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
 
    def set_species(self):
        pass

# ==> object 
creature = Tiger()
print(creature.__dict__)                       
# {}
print(dir(creature))
# ['Species', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', 
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'get_species', 'set_species']

# ==> Class
print(Tiger.__dict__)
# {'__module__': '__main__', '__firstlineno__': 8, 'get_species': <function Tiger.get_species at 0x000001F4A1481940>, 
# 'set_species': <function Tiger.set_species at 0x000001F4A1480C20>, # '__static_attributes__': (), '__doc__': None}
print(dir(Tiger))
# ['Species', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', 
#  '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#  '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'get_species', 'set_species']

# ==> Superclass
print(Cat.__dict__)
# {'__module__': '__main__', '__firstlineno__': 1, 'Species': 1, 'get_species': <function Cat.get_species at 0x000001F4A1473E20>,
#  '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Cat' objects>, '__weakref__': <attribute '__weakref__' of 'Cat' objects>, '__doc__': None}
print(dir(Cat))
# ['Species', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', 
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'get_species']



## __DICT__() in depth

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
# {'__module__': '__main__', '__firstlineno__': 1, 'varia': 1, '__init__': <function Classy.__init__ at 0x000001B773103E20>, 
#  'method': <function Classy.method at 0x000001B773111940>, '_Classy__hidden': <function Classy.__hidden at 0x000001B773110C20>, 
#  '__static_attrib<function Classy.method at 0x000001B773111940>, '_Classy__hidden': <function Classy.__hidden at 0x000001B773110C20>,
#  '__static_attributes__': ('var',), '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objectutes__': ('var',), 
#  '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}


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



## __NAME__
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



## __MODULE__
# stores the name of the module which contains the definition of the class
class Classy:
    pass

print(Classy.__module__)
# __main__ ==> any module named __main__ is actually not a module, but the file currently being run
obj = Classy()
print(obj.__module__)
# __main__



## __BASES__
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



## BAD PRACTICE ==> creer des variables d'instance du meme nom que des variables de class
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




#### ATTRIBUTE

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


# attributes for classes VS for instances:

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
# on voit bien: varible de Class:species, functions:__init__, greet + __static_attributes__: '__secret', 'age', 'name'

# ==> Attributs de l’objet
print(p.__dict__)  # Dictionnaire des attributs de l’instance p(Person)
# {'name': 'Alice', 'age': 30, '_Person__secret': 'secret_value'}
# on voit bien: name et age qui sont attendus comme argument pour créer l'instance + _Person__secret qui est "encapsulée" (cachée)


# Accès aux attributs de Class
print("Classe :", Person.species)
# Classe : Homo sapiens
print("Objet :", p.species)  # hérité de la class
# Objet : Homo sapiens

# Accès à l'attribut privé (name mangling) de la class
print(Person._Person__odor)
# stinky

# Accès aux attributs d'instance
print("Nom de l'objet :", p.name)
# Nom de l'objet : Alice
print("Age de l'objet :", p.age)
# Age de l'objet : 30

# Accès à l'attribut privé (name mangling) de l'instance
print(p._Person__secret)
# secret_value




#### ENCAPSULATION
# __ = private !

# L'encapsulation en Python (et en programmation orientée objet en général) désigne le fait de cacher certains détails internes d'une class
# pour éviter qu'ils soient modifiés ou utilisés de manière inappropriée directement depuis l'extérieur
# Cela permet de protéger l'intégrité des données et de contrôler l'accès à celles-ci via des méthods (getter, setter)
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
# AttributeError: 'Stack' object has no attribute '__stack_list'  ==>  on voit bien que l'on ne peut pas accéder "simplement" à l'attribut privé

print(len(stack_object._Stack__stack_list))
# 0
