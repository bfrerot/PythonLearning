### basics

#print ("I like to be a module")
#import math
#print ("math imported")
#import random
#print ("random imported")
#print (__name__) # print module "package" name
                 ## if applied from module.py = "__main__"
                 ## if apply from a script = moduleORpackagefile name, here "module"
#counter=0
#if __name__ == "__main__":
#    print("I prefer to be a module") # from module.py
#else:
#    print("I like to be a module") # from main.py


print ("+---------------------------------------------------+")
print ("+---------------------------------------------------+")

### importer des def dans un module

# module.py

#!/usr/bin/env python3 

""" module.py - an example of Python module """

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)


print ("+---------------------------------------------------+")
print ("+---------------------------------------------------+")