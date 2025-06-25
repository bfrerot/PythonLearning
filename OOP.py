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


### EXEMPLE SUPERCLASS//CLASS

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



########## PROPERTIES

##### INSTANCE VARIABLES

### code example method publique

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


### exemple code method privée avec __

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

    
### ==> pourquoi créer des functions de class (methods) alors que l'on peut créer des attributs en direct ?

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



##### CLASS VARIABLES
# class variable remains the same for all instances using the class
# if the class variable changes, it changes for ALL instances variables
class ExampleClass:
    counter = 0 # class variable
    def __init__(self, val = 1):
        self.__first = val # instance variable
        ExampleClass.counter += 1
 
 
example_object_1 = ExampleClass()
print(example_object_1.__dict__, example_object_1.counter)
# 1
example_object_2 = ExampleClass(2)
print(example_object_2.__dict__, example_object_2.counter)
# 2
example_object_3 = ExampleClass(4)
print(example_object_3.__dict__, example_object_3.counter)
# 3

# __dict__ de class

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


##### CLASS vs INSTANCE variables again

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



########## Checking attribute existence

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


# fix with try/except

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
 

# hasattr
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