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


class A:
    pass
 
class B(A):
    pass
 
class C(A):
    pass
 
class D(B):
    pass
  
  

### VALID inheritance schemes 

# ==> du plus BAS vers le plus HAUT 
class Class_2(D, B): 
    pass
  
class Class_3(C, A): 
    pass

class Class_4(D, A): 
    pass

## ==> SEPARATE paths
class Class_1(C, D): 
    pass
  
class Class_1(D, C): 
    pass


### UNVALID inheritance schemes    
class Class_2(B, D): 
    pass
  
class Class_3(A, C): 
    pass

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