########## PLATFORM MODULE ##########

## The platform module gives access to the underlying platform's data:
#   - hardware
#   - operating system
#   - interpreter version information


## platform.platform(aliased = False, terse = False) 
# returns a string describing the underlying hardware architecture and OS
# aliased → if True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones
# terse → if True (or any non-zero value) it may convince the function to present a briefer form of the result if possible

# Toutes les combinaisons possibles
from platform import platform
print("Défaut (0,0):", platform())          # Complet, pas d'alias
print("Aliased (1,0):", platform(1))        # Complet, avec alias
print("Terse (0,1):", platform(0, 1))       # Court, pas d'alias  
print("Les deux (1,1):", platform(1, 1))    # Court, avec alias

# depuis Windows
from platform import platform
print(platform())
# Windows-11-10.0.26100-SP0
print(platform(1))
# Windows-11-10.0.26100-SP0 # meme resultat car Windows n'a pas d'alias spécial
print(platform(0, 1))
# Windows-11 # Version simplifiée, sans les détails de build (10.0.26100-SP0)

# depuis Linux
from platform import platform
print(platform())     
# Linux-5.15.0-72-generic-x86_64-with-glibc2.35
print(platform(0, 1))
# Linux-5.15.0-72-generic


## platform.machine() 
# returns a string with the generic name of the host processor

from platform import machine
print(machine())
# x86_64


## platform.processor() 
# returns a string with the real name of the host processor

from platform import processor
print(processor())
# Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz


## platform.system() 
# returns a string with the generic name of the host OS

from platform import system
print(system())
# Windows


## platform.version() 
# returns a string with the version of the host OS

from platform import version
print(version())
# 10.0.26100


## platform.python_implementation()
# returns a string denoting the Python implementation
# return values are CPython , IronPython , Jython , PyPy

from platform import python_implementation
print(python_implementation())
# CPython


## platform.python_version_tuple() 
# returns a three-element tuple filled with:
#   - the major part of Python's version
#   - the minor part
#   - the patch level number

from platform import python_version_tuple
print(python_version_tuple())
# ('3', '13', '3')