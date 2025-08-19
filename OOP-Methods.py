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