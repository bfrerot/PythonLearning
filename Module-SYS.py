########## MODULE SYS ##########



## sys.argv 
# liste des arguments de la ligne de commande 
import sys
print(sys.argv)
# ['c:/PythonLearning/bac-à-sable.py']


## sys.path
# liste des chemins d’accès où Python recherche les modules à importer  
print(sys.path)
# ['c:\\PythonLearning', 'C:\\Python313\\python313.zip', 'C:\\Python313\\DLLs', 'C:\\Python313\\Lib', 'C:\\Python313',
#  'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages', 'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\win32',
#  'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\win32\\lib',
#  'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\Pythonwin', 'C:\\Python313\\Lib\\site-packages']


## sys.modules
# Dictionnaire contenant tous les modules déjà importés 
print(sys.modules)
# {'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, '_frozen_importlib': <module '_frozen_importlib' (frozen)>, '_imp': <module '_imp' (built-in)>,
#  '_thread': <module '_thread' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_weakref': <module '_weakref' (built-in)>, 'winreg': <module 'winreg' (built-in)>, 
#  '_io': <module '_io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, '_frozen_importlib_external': <module '_frozen_importlib_external' (frozen)>,
#  'time': <module 'time' (built-in)>, 'zipimport': <module 'zipimport' (frozen)>, '_codecs': <module '_codecs' (built-in)>, 'codecs': <module 'codecs' (frozen)>, 
#  'encodings.aliases': <module 'encodings.aliases' from 'C:\\Python313\\Lib\\encodings\\aliases.py'>, 'encodings': <module 'encodings' from 'C:\\Python313\\Lib\\encodings\\__init__.py'>, 
#  'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Python313\\Lib\\encodings\\utf_8.py'>, 'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Python313\\Lib\\encodings\\cp1252.py'>, 
#  '_signal': <module '_signal' (built-in)>, '_abc': <module '_abc' (built-in)>, 'abc': <module 'abc' (frozen)>, 'io': <module 'io' (frozen)>, '__main__': <module '__main__' from 'c:\\PythonLearning\\bac-à-sable.py'>,
#  '_stat': <module '_stat' (built-in)>, 'stat': <module 'stat' (frozen)>, '_collections_abc': <module '_collections_abc' (frozen)>, 'genericpath': <module 'genericpath' (frozen)>, '_winapi': <module '_winapi' (built-in)>,
#  'ntpath': <module 'ntpath' (frozen)>, 'os.path': <module 'ntpath' (frozen)>, 'os': <module 'os' (frozen)>, '_sitebuiltins': <module '_sitebuiltins' (frozen)>, 
#  'encodings.utf_8_sig': <module 'encodings.utf_8_sig' from 'C:\\Python313\\Lib\\encodings\\utf_8_sig.py'>, '_distutils_hack': <module '_distutils_hack' from 'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\_distutils_hack\\__init__.py'>,
#  'pywin32_system32': <module 'pywin32_system32' (namespace) from ['C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\pywin32_system32']>, 
#  'pywin32_bootstrap': <module 'pywin32_bootstrap' from 'C:\\Users\\bfrerot\\AppData\\Roaming\\Python\\Python313\\site-packages\\win32\\lib\\pywin32_bootstrap.py'>, 'site': <module 'site' (frozen)>}


## sys.version
# Version de Python sous forme de chaîne de caractères 
print(sys.version)
# 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)]


## sys.platform
# Plateforme (système d'exploitation) sur laquelle Python tourne
print(sys.platform)
# win32


# sys.maxsize
# valeur numérique max que peut prendre une int
print(sys.maxsize)
# 9223372036854775807 

## sys.exit([arg])
# Exit le programme
# Peut prendre un code de sortie (par défaut 0)
print(sys.exit(0))


## sys.getsizeof(object[, default]) 
# Retourne la taille en octets d’un objet
print(sys.getsizeof(42))
# 28


## sys.stdin, sys.stdout, sys.stderr  
# Flux standard d'entrée, sortie et erreur 
# peuvent être redirigés

print("Tapez quelque chose :")
ligne = sys.stdin.readline()
print("Vous avez tapé :", ligne)
# Tapez quelque chose :
# hello (input clavier)
# Vous avez tapé : hello

sys.stdout.write("Bonjour, ceci est un message sur la sortie standard.\n")
# Bonjour, ceci est un message sur la sortie standard

try:
    x = int(input("Entrez un nombre : "))
except ValueError:
    print("Ce n'est pas un nombre valide.", file=sys.stderr)
# Entrez un nombre : un
# Ce n'est pas un nombre valide.


## sys.setrecursionlimit(limit)
# Modifie la limite de récursion (par défaut, 1000).  
sys.setrecursionlimit(2000)


## sys.getrecursionlimit()`**  
# Retourne la limite actuelle de récursion.  
print(sys.getrecursionlimit())
# 1000

import sys
print(sys.getrecursionlimit())
# 1000
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
# 2000


## sys.path.append(path)
# Ajoute un nouveau chemin pour la recherche de modules.  
sys.path.append('/mon/nouveau/chemin')

import sys
import os
zip_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'packages', 'extrapack.zip'))
sys.path.append(zip_path)


## sys.path.insert(index, path) 
# Insère un chemin à une position spécifique dans sys.path



