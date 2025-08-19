########## OOP - PROPERTIES ##########


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
