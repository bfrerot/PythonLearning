########## MODULES ##########


# Packages contain Modules which contain functions/variables

## python general index

https://docs.python.org/3/py-modindex.html



### __MAIN__ vs __NAME__

# when you run a file directly, its __name__ variable is set to __main__;
# when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)



### NAMESPACE

# Inside a certain namespace, each name must remain unique
# Si on compare aux prénoms:
#   dans un namespace, les prenoms sont uniques ex FREROT.benoit
#   les prénoms peuvent etre dupliqués entre différents namespace ex FREROT.benoit GEFFROY.benoit DUMAS.benoit
#   les prénoms pevent oujours exister comme variable dans le code général, sans etre confondu

## variable
import math
sin = 10
x=45
print(math.sin(x)) # on invoque une method du module math = MATH.sin
# 0.8509035245341184

## function
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



### IMPORT ###

## one module
import math


## many modules
import math, random


## all entities form a module
from math import * 


## valid imports from a module or chain of modules
from packageA.subpackageB.subpackageC.moduleD import * # all functions
from packageA.subpackageB.subpackageC.moduleD import function
from packageA.subpackageB.subpackageC.moduleD import function as f # renaming the function


## valid functions invocations

from p.m import f
f() # f() is well known

from p.m import f as func_f
func_f() # f() is well known but as func_f()

import p
p.m.f()

import p.m
p.m.f() # f() is not explicitely known and could have homonyms so we MUST add the full name

import p.m as module_m  # like an alias for a chain of modules
module_m.f() # same as before 


## relative import

# Relative imports use leading dots "."
# A single leading dot indicates a relative import, starting with the current package. 
# Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after the first

'''
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
'''
# imports relatifs valides depuis package/subpackage1/__init__.py ou package/subpackage1/moduleX.py:
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo



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
 

## aliasing : is giving any module and/or entity a name we prefer 
# or to avoid same names in the code even it coexists

import math as boringstuff

import math as m
print (m.sin(m.pi/2))
1.0

from math import pi as P

# plusieurs à la fois si on veut
# from module import n as a, m as b, o as c
  

## __pycache__/[modulename].cpython-[verMverm]
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



### PATH ###
### si les fichiers module et main sont dans des répertoires différents il faudra amender le PATH
# voir en fonction du besoin, OS, etc

#| Méthode                            | Fonctionne tout le temps ? | Explication                    |
#| ---------------------------------- | -------------------------- | ------------------------------ |
#| `path.append('../packages')`       | ❌ Non                      | Dépend du dossier d'exécution  |
#| `path.append('C:/chemin/complet')` | ✅ Oui                      | Mais pas portable              |
#| `path.append(...) via __file__`    | ✅ Oui                      | Recommandée et multiplateforme |

# import depuis le main.py SI le module/package n'est pas dans le meme dossier ni dans un dossier PATH par défaut
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'packages')))
# si zipfile
import sys
import os
zip_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'packages', 'extrapack.zip'))
sys.path.append(zip_path)


#Python considère un dossier comme un package seulement s’il contient un fichier __init__.py 
#(même vide).
#Si un dossier n’a pas ce fichier, Python ne peut pas l’interpréter comme un package Python, 
#donc il ne pourra pas importer les modules contenus dans ce dossier.

#Si on veut importer extra.good.best.sigma, alors les dossiers suivants 
#doivent contenir un __init__.py :

#packages/
#├── extra/
#│   ├── __init__.py     ← Obligatoire ici
#│   ├── iota.py
#│   ├── good/
#│       ├── __init__.py ← Obligatoire ici aussi
#│       ├── best/
#│           ├── __init__.py ← Obligatoire aussi
#│           ├── sigma.py
#│           ├── tau.py
#Sans l’un de ces fichiers, l’import import extra.good.best.sigma va planter, 
#car Python ne pourra pas "traverser" ces dossiers comme packages.

#Depuis Python 3.3, il existe les namespace packages qui peuvent fonctionner 
#sans __init__.py en théorie.
#Mais dans la pratique, surtout si on manipule des chemins personnalisés (comme avec sys.path.append),
#ça peut poser problème.
#Il vaut mieux mettre ces fichiers __init__.py pour garantir la compatibilité 
#et éviter les erreurs d’import.


## dir("module")
# when WHOLE MODULE IS IMPORTED we can dir() it to know all functions contained in the module
# use alias if module has been aliased
import math
print(dir(math))
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh',
 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e',
 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma',
 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10',
 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau',
  'trunc']