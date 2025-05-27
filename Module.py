########## MODULES ##########


# Packages contain Modules which contain functions/variables

### python general index

https://docs.python.org/3/py-modindex.html


### main/name
# when you run a file directly, its __name__ variable is set to __main__;
# when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)


### import module to be able to use it, one or many at a time

import <module1>, <module2>, <modulex>
import math
import math, random

from math import * # importe toutes les entities / difference avec import math ??


### namespace

## Inside a certain namespace, each name must remain unique
# Si on compare aux prénoms:
#   dans un namespace, les prenoms sont uniques ex FREROT.benoit
#   les prénoms peuvent etre dupliqués entre différents namespace ex FREROT.benoit GEFFROY.benoit DUMAS.benoit
#   les prénoms pevent oujours exister comme variable dans le code général, sans etre confondu

# variable
import math
sin = 10
x=45
print(math.sin(x)) # on invoque une method du module math = MATH.sin
# 0.8509035245341184

# function
import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
pi = 3.14
print(sin(pi/2))
print(math.sin(math.pi/2))
# 0.99999999
# 1.0

# On peut importer juste une entity + PAS BESOIN de qualifier (nommer) le module pour s'en servir
from math import pi
from math import sin, pi
print(sin(pi/2)) # et non pas print(math.sin(math.pi/2))
# 1.0

# MAIS, si on réutilise les keywords pour définir une variable/function/etc, alors ces derniers écrasent les keywords importés
from math import sin, pi
print(sin(pi / 2))
# 1.0
pi = 3.14 # défini après écrase le math.pi importé individuellement
def sin(x): # écrase le math.sin importé individuellement
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))
# 0.99999999

# ET INVERSEMENT
pi = 3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi / 2))
0.99999999
from math import sin, pi
print(sin(pi / 2))
# 1.0

# ET ENCORE, on peut importer tout par defaut
from math import * # * veut dire TOUT par défaut
# pas recommandé
 

### aliasing : is giving any module and/or entity a name we prefer 
# or to avoid same names in the code even it coexists

import math as boringstuff

import math as m
print (m.sin(m.pi/2))
1.0

from math import pi as P

# plusieurs à la fois si on veut
# from module import n as a, m as b, o as c
  

### __pycache__/[modulename].cpython-[verMverm]
# dans un dossier on place un module.py et un main.py
# lorsque module.py est importé dans main.py, cela engendre:
#   la création d'un répertoire __pycache__
#   la création d'un fichier en .pyc
#       ce type de fichier est du code semi-compilé python, pret à etre exécuté
#       son nom reprend le nom du module et la version de Python
#       ex: module.cpython-313.pyc

# Lorsqu'un module est importé, il est implicitement exécuté
# Cela explique que les fonctions soient créées, des variables etc

# un module ne sera importé qu'une seule fois, meme si plusieurs instructions d'import du meme module

# when you run a file directly, its __name__ variable is set to __main__
# when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)
# __name__ == '__main__' permet d’écrire du code qui ne s’exécute que si le fichier est lancé directement, et pas quand il est importé

# exemple
# module= outil.py
def addition(a, b):
    return a + b
if __name__ == "__main__":
    print("Outil chargé.")
    print("Test : 2 + 3 =", addition(2, 3))
# si on veut le tester/executer:
# Outil chargé.
# Test : 2 + 3 = 5

# mais si on l'importe, o , ne veut pas à chaque fois avoir l'information "outil chargé"
import module
print(module.addition(4, 4))
# on execute et on aura pas le message inutile
# 8


### si les fichiers module et main sont dans des répertoires différents il faudra amender le PATH
# voir en fonction du besoin, OS, etc


# dir("module")

## when WHOLE MODULE IS IMPORTED we can dir() it to know all functions contained in the module
## use alias if module has been aliased
import math
print(dir(math))
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh',
 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e',
 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10',
 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',
  'trunc']
 
 
# Useful function group in math
 
trigonometry : sin cos tan + all related like asin asinh etc, pi radians, degrees
exponentiation : exp log log2 etc
 
 
# random

par defaut donne un chiffre decimal entre 0.0 et 1.0
random () -->     0.0 <= x < 1.0

from random import random
for i in range(5):
    print(random())
0.3487027093205528
0.04681702702249857
0.3734602288166339
0.9930295466333776
0.023790533052207796
# apply code again
0.7749265363690918
0.4410949970809025
0.6166792403249517
0.4278524071314551
0.10833578213742012
# we see there is full randomness

## seed() set the generator's seed to apply the calculation from BUT will remove randomness
seed() # uses current time
seed(int) # uses int value

from random import random, seed
seed(0)
for i in range(5):
    print(random())
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085
# apply code again
0.8444218515250481
0.7579544029403025
0.420571580830845
0.25891675029296335
0.5112747213686085
# we sme values each time


# randrange - randint
from random import randrange, randint
print(randrange(2), end=' ') # rightsided exclusion
print(randrange(0, 2), end=' ') # rightsided exclusion
print(randrange(0, 2, 1), end=' ') # rightsided exclusion
print(randint(0, 2)) # equal to (left,right + 1)
## many applies later
0 1 1 1
1 1 1 0
0 0 1 0
0 1 1 1
1 0 0 1
0 1 1 0
0 1 0 1
1 1 1 2 


## sorting a list with random
from random import randint
for i in range(10):
    print(randint(1, 10), end=',')
5,9,1,9,8,6,4,6,10,4,


## the same WHITOUT REPETITION

from random import choice, sample
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(lst))  # 1 element de la liste
10
print(sample(lst, 5))    #   5 elements de la liste dans un sens au hasard
[10, 9, 8, 1, 4]
print(sample(lst, 10))     #   10 elements de la liste dans un sens au hasard
[4, 10, 5, 2, 7, 3, 9, 6, 1, 8]



# platform

##utile pour recuperer des informations sur les couches inferieures (OS, hardware)

platform(aliased = False, terse = False)

## This is how you can invoke it: platform(aliased = False, terse = False) = (0,0) by default

And now:

## aliased → when set to True (or any non-zero value) it may cause the function
#  to present the alternative underlying layer names instead of the common ones;
##terse → when set to True (or any non-zero value) it may convince the function 
# to present a briefer form of the result (if possible)

## from Netacad Sandbox
from platform import platform
print(platform())
print(platform(1))
print(platform(0, 1))
Linux-4.4.0-164-generic-x86_64-with
Linux-4.4.0-164-generic-x86_64-with
Linux-4.4.0-164-generic-x86_64-with

## from Windows laptop
from platform import platform
print(platform())
Windows-10-10.0.18362-SP0
print(platform(1))
Windows-10-10.0.18362-SP0
print(platform(0, 1))
Windows-10
print(platform)
<function platform at 0x00C3F4A8>



from platform import machine
print(machine())
x86_64


from platform import processor
print(processor())
Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz


from platform import system
print(system())
Linux


from platform import version
print(version())
#192-Ubuntu SMP Fri Sep 13 12:02:50 UTC 2019


from platform import python_implementation, python_version_tuple
print(python_implementation())
print (python_version_tuple())
for atr in python_version_tuple():
    print(atr)
CPython
('3', '6', '8') # major.minor.patch
3 # major
6 # minor
8 # patch


# pyperclip

import pyperclip 
pyperclip.copy('Hello world!') 
print (pyperclip.paste())
Hello world!
