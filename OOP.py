########## OBJECT ORIENTED PROGRAMMATION ##########




##### BASICS



### BASIS TERMS
# CLASS — an idea, blueprint, or recipe for an instance
# INSTANCE — an instantiation of the class; very often used interchangeably with the term 'object'
# OBJECT — Python's representation of data and methods; objects could be aggregates of instances
# ATTRIBUTE — any object or class trait; could be a variable or method
# METHOD — a function built into a class that is executed on behalf of the class or object; some say that it’s a 'callable attribute'
# TYPE — refers to the class that was used to instantiate the object



### CLASS
# A class (among other definitions) is a set of objects. An object is a being belonging to a class.
# A class is an idea (more or less abstract) which can be used to create a number of incarnations – such an incarnation is called an object.
# When a class is derived from another class, their relation is named inheritance. The class which derives from the other class is named a subclass. The second side of this relation is named superclass

# define a class
class TheSimplestClass:
    pass



### OBJECT/INSTANCE OF A CLASS

# An object is one particular physical instantiation of a class that occupies memory and has data elements
# This is what 'self' refers to when we deal with class instances.

# !! An object is everything in Python that you can operate on, like a class, instance, list, or dictionary.
# The term instance is very often used interchangeably with the term object, because object refers to a particular instance of a class. 
# It’s a bit of a simplification, because the term object is more general than instance.

# An instance is an incarnation of the requirements, traits, and qualities assigned to a specific class
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


## define an object
my_first_object = TheSimplestClass()
# The act of creating an object of the selected class is also called an instantiation (as the object becomes an instance of the class).



### ATTRIBUTE

# An attribute is a capacious term that can refer to two major kinds of class traits:
#   - variables, containing information about the class itself or a class instance; classes and class instances can own many variables
#   - methods, formulated as Python functions; they represent a behavior that could be applied to the object

# It is said that methods are the 'callable attributes' of Python objects



### TYPE

# type is one of the most fundamental and abstract terms of Python

# it is the foremost type that any class can be inherited from; as a result, if you’re looking for the type of class, 
# then type is returned

# in all other cases, it refers to the class that was used to instantiate the object; it’s a general term describing 
# the type/kind of any object

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



### CLASS & OBJECT & ATTRIBUTE Example

class Duck: # example of a Class
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight # example of an Atribute
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')
        
canard = Duck(21,3.5,"male") # example of an Object
duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(weight=3.7, height=25, sex="male")
hen = Duck(sex="female", weight=3.4, height=20 )
print(canard.sex)
# male
print(duckling.height)
# 10
print(hen.weight)
# 3.4
print((drake.sex))
# male
canard.quack()
# Quack



### INHERITANCE
# Any object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements and qualities) defined inside any of the superclasses.



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


## __ = private !
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


## EXEMPLE SUPERCLASS//CLASS

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





##### PROPERTIES



### INSTANCE VARIABLES


## code example method publique

class ExampleClass:
    def __init__(self, val1 = 1): # le constructor, si on ne precise pas de val, val=1 par défaut
        self.first = val1
 
    def set_caca(self, val2): # une fonction dans la class, attend une val
        self.caca = val2

example_object_1 = ExampleClass() # ici val(val1) = 1 par défaut, que le constructor __init__ est invoqué
print(example_object_1.__dict__) # .__dict__ est un attribut spécial de chaque objet en Python
# {'first': 1}
print(example_object_1.first)
# 1
example_object_2 = ExampleClass(2) # ici val(val1) est spécifié et = 2
print(example_object_2.__dict__)
# {'first': 2}
print(example_object_2.first)
# 2
example_object_2.set_caca(10) # on invoque la fonction set_caca qui attend une valeur(val2): OBLIGATOIRE d'avoir créé example_object_2 = ExampleClass(2) avant sinon erreur
print(example_object_2.caca)
# 10
print(example_object_2.__dict__)
# {'first': 2, 'caca': 10} # l'objet example_object_2 se voit rajouter un attribut caca et = 10
 
example_object_3 = ExampleClass(4) # ici val(val2) est spécifié et = 4
print(example_object_3.__dict__)
# {'first': 4}
example_object_3.third = 5 # on crée un attribut directement SANS invoquer une fonction de la class
print(example_object_3.__dict__)
# {'first': 4, 'third': 5}
print(example_object_3.third)
# 5


## exemple code method privée avec __

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
# {'_ExampleClass__first': 1} # le print reprend le nom de la class: _CLASSNAME__METHODNAME
print(example_object_2.__dict__)
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
print(example_object_3.__dict__)
# {'_ExampleClass__first': 4, '__third': 5} # ici third est créé hors classe donc __METHODNAME
print(example_object_3.__third)
# 5

    
## ==> pourquoi créer des functions de class (methods) alors que l'on peut créer des attributs en direct ?

# 1. **Contrôler et Protéger les Données**

# avec les methods on peut :
# - Vérifier que la valeur est correcte (par exemple, s’assurer qu’un âge est positif)
# - Limiter ou transformer la valeur avant de l’enregistrer
# - Empêcher de mettre n’importe quoi dans l’attribut

# Ex
def set_age(self, age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    self.age = age


# 2. **Maintenir la Cohérence de l’Objet**

# - mettre à jour plusieurs attributs en même temps ou garder une logique, la méthod permet de le faire proprement.
# - déclencher d’autres actions** quand on modifie une valeur ex : recalculer un score, sauvegarder dans un fichier, etc.).


# 3. **Faciliter la lecture et l’utilisation du code**

# - Une méthode bien nommée explique clairement ce qu’elle fait (ex : `set_nom_utilisateur()`)
# - Le code est plus lisible et plus facile à maintenir, surtout dans de gros projets


# 4. **Préparer l’évolution future du code**

# - Si on ajoute une règle, un contrôle ou une action plus tard, il n'y a qu’à modifier la méthode, 
# pas tous les endroits où l’attribut est modifié directement


# 5. **Utiliser les propriétés (`@property`)**

# Python permet de masquer l’accès direct à un attribut avec des propriétés, 
# pour gérer la lecture et l’écriture tout en gardant une syntaxe simple.
# ex

    @property
    def caca(self):
        return self._caca

    @caca.setter
    def caca(self, val):
        if val < 0:
            raise ValueError("Impossible")
        self._caca = val

# on pourra ainsi faire : obj.caca = 10 mais avec des contrôles cachés derrière.


## __slots__ ou comment bloquer la création d'attributs à la volée

# Quand on utilise __slots__ dans la class :
# - on bloque la création d'attributs hos class
# - les objets n’ont plus d’attribut par défaut comme .__dict__ ni individuel ce qui peut etre vu comme un inconvénient
#   AttributeError: 'NomDeTaClasse' object has no attribute '__dict__'
# - EN PLUS, en Python, chaque objet de classe possède un dictionnaire d’attributs (`__dict__`) qui lui permet d’avoir 
#   dynamiquement de nouveaux attributs. CEPENDANT, cela consomme de la mémoire, donc il peut etre bon de s'en passer

# Comment afficher quand même les valeurs ?

# créer une méthode spéciale pour récupérer les valeurs des attributs déclarés dans `__slots__`.**  

class ExampleClass:
    __slots__ = ['first', 'second']
    
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        self.second = val

    def as_dict(self):
        return {slot: getattr(self, slot, None) for slot in self.__slots__}

obj = ExampleClass()
print(obj.as_dict())
# {'first': 1}

obj.set_second(20)
print(obj.as_dict())
# {'first': 1, 'second': 20}

obj.set_rogue(666)
# AttributeError: 'ExampleClass' object has no attribute 'set_rogue'


# Exemple SANS __slots__

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = Personne("Alice", 30)
p.adresse = "123 Rue Exemple"  # Possible, même si "adresse" n'est pas prévu
print(p.adresse)  # Affiche : 123 Rue Exemple
# Ici, on peut ajouter n’importe quel attribut à l’objet p


# Exemple AVEC __slots__

class Personne:
    __slots__ = ['nom', 'age']
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

p = Personne("Alice", 30)
p.adresse = "123 Rue Exemple"  
# AttributeError: 'p' object has no attribute 'adresse'


## return depuis le constructor

class ExampleClass:
    def __init__(self, val1 = 1): 
        self.first = val1
        return self.first
        
example_object_1 = ExampleClass() 
print(example_object_1)
# TypeError: __init__() should return None, not 'int'

# Python attend que __init__() retourne None
# Donc lorsqu'on écrit return self.first, Python lève le TypeError
# La méthode __init__() est un constructeur qui sert à initialiser l’objet après sa création
# Elle doit toujours retourner None — elle ne doit pas avoir de return explicite avec une valeur.


## return depuis une method (function de class)

class ExampleClass:
    def __init__(self, val1 = 1): 
        self.first = val1
        
    def set_caca(self, val2):
        self.caca = val2
        return self.caca
    
example_object_2 = ExampleClass(10) 
print(example_object_2)
# <__main__.ExampleClass object at 0x000001BA8EFE8CD0>

# Ce résultat est le comportement par défaut de Python quand on essaie d’afficher un objet d’une classe 
# qui ne définit pas de méthode spéciale __str__() ou __repr__()
# Python affiche alors le nom de la classe (__main__.ExampleClass)  
# suivi de l’adresse mémoire de l’objet (at 0x000001BA8EFE8CD0)


## print object depuis __init_ et method
# si pas de __str__ ni __repr__, le print envoie l'emplacement mémoire
class ExampleClass:
    def __init__(self, val1 = 1): 
        self.first = val1
        
    def set_caca(self, val2):
        self.caca = val2
        
example_object_1 = ExampleClass() 
print(example_object_1)
# <__main__.ExampleClass object at 0x000001BA8EC37230>
example_object_2 = ExampleClass(10) 
print(example_object_2)
# <__main__.ExampleClass object at 0x000001BA8EFE8CD0>


## __repr__

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


## __str__

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


## __dict__ de class

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__) # __dict__ d’une classe montre ses attributs, y compris les variables de class et méthods
# {'__module__': '__main__', '__firstlineno__': 1, 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x000001EFEB9B3E20>, '__static_attributes__': (),
# '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

example_object = ExampleClass(2) # la variable de class "varia" passe à 2
# {'__module__': '__main__', '__firstlineno__': 1, 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x000001EFEB9B3E20>, '__static_attributes__': (),
# '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
print(ExampleClass.__dict__)

print(example_object.__dict__)
# {} # vide, logique car aucune action pour l'instance elle-meme



### CLASS vs INSTANCE variables

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

# Modifier la variable de classe
Animal.espèce = "Vertébré"

print(a1.espèce)  
# Vertébré
print(a2.espèce)  
# Vertébré



### Checking attribute existence

# error code example

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1) # val % 2 != 0 donc a=1
print(example_object.a)
# 1
print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'


## fix with try/except

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
try:
    print(example_object.a) # 1
except AttributeError:
    pass
try:
    print(example_object.b) # pass
except AttributeError:
    pass
    
example_object = ExampleClass(2)
try:
    print(example_object.a) # pass
except AttributeError:
    pass
try:
    print(example_object.b) # 1
except AttributeError:
    pass
 

## hasattr
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
    
    
## s'applique aussi aux class

class ExampleClass:
    attr = 1
print(hasattr(ExampleClass, 'attr'))
# True
print(hasattr(ExampleClass, 'prop'))
# False


## attribut de class vs instance

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



### self parameter

# self parameter is used to obtain access to the object's instance and class variables
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)
 
obj = Classy()
obj.var = 3
obj.method()
# 2 3


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



### __init__ 

# __init__ method = constructor

# If a class has a constructor, it is invoked automatically and implicitly when 
# the object of the class is instantiated.

# constructor:
# MUST have the self parameter (it's set automatically, as usual)
# MAY have more parameters than just self; if this happens, the way in which the class name
#   is used to create the object must reflect the __init__ definition;
# CAN be used to set up the object, i.e., properly initialize its internal state, create 
#   instance variables, instantiate any other objects if their existence is needed, etc.


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



### visible vs hidden methods

class Classy:
    def visible(self):
        print("visible")
 
    def __hidden(self): # the __ before hidden sets the method as private
        print("hidden")
 
obj = Classy() # object obj is linked to Classy() class
obj.visible() # invokes visible method from Classy() class
# visible

try:
    obj.__hidden() # won't work as __hidden is privet, we need to add the class name
except:
    print("failed")
# failed

obj._Classy__hidden() # the good way adding _CLASSNAME to private method name
# hidden





##### INNER LIFE of classes and objects

# Each Python class object is pre-equipped with a set of useful attributes which 
# can be used to examine its capabilities.



### __dict__

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



### __name__
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



### __module__
# stores the name of the module which contains the definition of the class
class Classy:
    pass

print(Classy.__module__)
# __main__ ==> any module named __main__ is actually not a module, but the file currently being run
obj = Classy()
print(obj.__module__)
# __main__



### __bases__
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
   
    
    


##### INHERITANCE

# The most important factor of the process is the relation between the superclass and all of its subclasses 
# a single inheritance class is always simpler, safer, and easier to understand and maintain
# multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying 
#   these parts of the superclasses which will effectively influence the new class
# multiple inheritance may make overriding extremely tricky; moreover, using the super() function becomes ambiguous
# multiple inheritance violates the single responsibility principle (https://en.wikipedia.org/wiki/Single_responsibility_principle) 
#   as it makes a new class of two (or more) classes that know nothing about each other
# multiple inheritance should be the last of all possible solutions – if you really need the many different functionalities offered 
#   by different classes, composition may be a better alternative



### transitivity

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



### issubclass(class,subclass)

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



### isinstance(object,class)

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



### object_one is object_two
# The is operator checks whether two variables (object_one and object_two here) refer to the same object

class SampleClass:
    def __init__(self, val):
        self.val = val

object_1 = SampleClass(0) # = 0
object_2 = SampleClass(2) # = 2
object_3 = object_1 # = 0 mais aussi object_1 et object_3 partagenet désormais le meme emplacement mémoire, la meme valeur
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
print(object_1.val, object_2.val, object_3.val)
# 1 2 1



### super()

# ==> appel direct à la classe parente
# manière directe, mais pas recommandée en Python moderne, car cela ne gère pas 
# certains aspects liés à l'héritage multiple ou à la chaîne d'héritage multiple.

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name) # ici Super() est la superclass =! super() la fonction python builtin

obj = Sub("Andy")
print(obj) # Python looks for __str__() or __repr__() 
# My name is Andy.


## utilisation de super() Python builtin fonction

#  super() retourne une "super classe" c'est-à-dire la classe parente dans le contexte actuel et appelle sa méthode __init__
# Avantages :
#  - Plus flexible, surtout dans le contexte de l'héritage multiple.  
#  - Respecte la chaîne d'héritage et peut faire appel à la méthode __init__ de la classe suivante dans l'ordre MRO (Method Resolution Order) ==> A CREUSER

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name) # ici super() est la fonction builtin Python attention

obj = Sub("Andy")
print(obj)
# My name is Andy.    



### Method Resolution Order
# MRO, in general, is a way, a strategy, in which a particular programming language scans through the upper part of a class’s hierarchy
# in order to find the method it currently needs

# class variables
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
# 2 ==> class Sub
print(obj.supVar)
# 1 ==> class Super (upper class)

# instance variables
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()
# 12 ==> Sub.subVar
# 11 ==> Super.supVar

# When you try to access any object's entity, Python will try to (in this order):
#   - find it inside the object itself;
#   - find it in all classes involved in the object's inheritance line from bottom to top;
#   - If both of the above fail, AttributeError

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
object.m_middle()
# middle
object.m_top()
# top
    
# Logical inheritance path is Bottom==> Middle ==> Top
# But if we try to force an other way it won't work:
class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Top, Middle): # Logicall inheritance path is Bottom==> Middle ==> Top, so should be class Bottom(Middle, Top)
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle  

# If we had foced it in the good way, would be ok:
class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle, Top): # Logicall inheritance path is Bottom==> Middle ==> Top, so should be class Bottom(Middle, Top)
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
# bottom
object.m_middle()
# middle
object.m_top()
# top


        
### Level-Line inheritance

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


class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())
# 200 201 ==> cherche dans la class level3 = nok, cherche dans la class Level2 OK
print(obj.var, obj.fun())
# 200 201 ==> meme requete pas de changement dans le resultat
# Python looks for an entity from bottom to top
    
    
    
### Multiple inheritance

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
# ici pas d'homonyme entre les class


class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A, B):
    pass

o = C()
print(o)
# a


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right): # Python ira chercher dans la class Left, puis Right
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())
# L LL RR Left


class Sub2(Right, Left): # Python ira chercher dans la class Right, puis LEft
    pass

obj = Sub()
print(obj.var, obj.var_left, obj.var_right, obj.fun())
# R LL RR Right



### Building a Hierarchy of classes


## POLYMORPHISM

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
    def do_it(self): # 3 - back tu Upper class
        print("do_it from One") # 4

    def doanything(self): # 1
        self.do_it()

class Two(One): # 2 - is any "self.do_it()" ? No
    pass

one = One()
two = Two()

one.doanything()
# do_it from One
two.doanything() # 1 - 2 - 3 - 4
# do_it from One

# no class is given once and for all
# Each class's behavior may be modified at any time by any of its subclasses
# We can use polymorphism to extend class flexibility

class Personne:
    def dire_bonjour(self):
        print("Bonjour, je suis une personne.")

class Animal:
    def dire_bonjour(self):
        print("Miaou !")

def saluer(objet):
    objet.dire_bonjour()

# On peut passer une Personne ou un Animal à la fonction
p = Personne()
a = Animal()

saluer(p)  
# Bonjour, je suis une personne.
saluer(a)  
# Miaou !





##### Exceptions in OOP context


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



### .args

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