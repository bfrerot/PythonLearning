########## STRINGS ##########

## Immutability: we cannot change iteration into a string, ex: Paris --> Karis 
name = "Paris"
name[0] = 'K'
# Traceback (most recent call last):
#   File "main.py", line 1, in <module>
#     name = Paris
# NameError: name 'Paris' is not defined



## Quotes
'string'
"string" # the same thing

# Triple quotes """ ... """ allow to write a string on multiple lines, but the output will be displayed with the same line breaks and spaces as in the code
print("""red roses 
      
      
      
      and violet roses""")
# red roses
# 
# 
# 
#       and violet roses

# but if write a single line string with triple quotes, it will be displayed as a single line
print("""red roses and violet roses""")
# red roses and violet roses 


# " ' " ==> ok
# " I'm going on a run " # ok

# ' ' ' ==> nok
# ' I'm going on a run ' # nok
# SyntaxError: invalid syntax

print('I like "Monty Python"')
# I like "Monty Python"
print("I like 'Monty Python'")
# I like 'Monty Python'



## Multiple lines - ''' 

texte_multiligne = """this is an example
of a multi-line string."""
print(texte_multiligne)
# this is an example
# of a multi-line string.



## Concatenation

# we can concatenate strings with the "+" operator
s="hello"
print(s + ' concatenate me!')
# hello concatenate me!

print("Pales" "tine")
# Palestine ==> no need for "+" between strings

# We cannot concatenate str with int/float/bool/complex/None

s="hello"
print(s + None)
# TypeError: can only concatenate str (not "NoneType") to str

s="hello"
print(s + True)
# TypeError: can only concatenate str (not "bool") to str

s="hello"
print(s + 1J)
# TypeError: can only concatenate str (not "complex") to str

s="hello"
print(s + 10)
# TypeError: can only concatenate str (not "int") to str

s="hello"
print(s + 10.5)
# TypeError: can only concatenate str (not "float") to str



## Multiplication
letter = 'z'
L=letter*10 
print (L)
# zzzzzzzzzz



## Print
print ('string')
# string

print ('string' 'string2') # no need for "+" between strings, but no space will be added between them
# stringstring2

print ('string'' ''string2') # overcomes the previous problem by adding a space between the two strings
# string string2

print ('string \n string2') # \n is a special character that allows to go to the next line, but add a space at the beginning of the next line
# string 
#  string2

print ('string \nstring2') # sticks the two strings together without adding a space at the beginning of the next line
# string 
# string2

print ('first part \t second part') # tabulation = 2*spaces
# first part 	 second part

print("I like \"Monty Python\"") # \ followed by a special character allows to escape the special meaning of that character
# I like "Monty Python"



## Indexing & Slicing

s='hello'

s[0] # iteration starts at 0
# h
s[1]
# e

s[1:] # all from 2nd character to the end
# ello

s[1:3] # all from 1st to 2nd character, the last one being excluded
# el
s[1:4] # all from 1st to 3rd character, the last one being excluded
# ell

s[:3] # from the beginning to the 2nd character, the last one being excluded
# hel

s[:20] # displays the string without error if the number is greater than the actual number of characters
# hello
s[14:20]
# = nothing but no error

s[-1] # last character
# o
s[-5:-1] 
# a bit weird: -5 = o-->l-->l-->e-->h   -4 = e   etc 
# hello

s[-5:0] # n'affiche rien car dans ce cas la boundary doit exister
# rien à afficher mais pas d'erreur; le premier est EGAL au second


s = "Bonjour"
print(s[-5:0])

s[:-1] # all from the beginning to the last character, the last one being excluded
# hell
s[:] # all
# hello

s[::1] # all
# hello
s[::2] # skips 1 character each time
# hlo
s[::-1] # all characters but in reverse order
# olleh
s[::-2] # skips 1 character each time but in reverse order
# olh


mystring = "abcdefgijk"
mystring[2:7:2] # start at index 2 (c), up to index 7 (but not including g) and skip 1 letter every 2
# ceg
mystring[0:9:3] # start at index 0 (a), up to index 9 (but not including k) and skip 1 letter every 3
# adg



##  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
# True
print("F" not in alphabet)
# True

# funny thing
# ==> "", empty string is a part of any string
print ("" in "nimportequ'elle string")
# True
print ("" in "")
# True



## f-strings - formatted strings litterals - 

# python 3.6 and above
n = 3
m = 4
print (f"{n} times {m} is {n*m}")
# 3 times 4 is 12

# Before PYTHON 3.6 
# we use .format()
monster = "titus"
a = 8
h = 4
print ("{} has {} heads and {} arms".format(monster, h, a))
# titus has 4 heads and 8 arms

# or %
print('%(language)s has %(number)01d quote types.' %{'language': "Python", "number": 2})
# Python has 2 quote types.
print('%(language)s has %(number)03d quote types.' %{'language': "Python", "number": 2})
# Python has 002 quote types.

# ==> cf Functions-PRINT.py



## Strings from lists

# we can unpack a list into variables, but the number of variables must match the number of elements in the list
fruits = ("Apples", "Oranges", "Bananas")
a, b, c = fruits
print(b)
# Oranges

fruits = ("Apples", "Oranges", "Bananas")
a, b, c, d = fruits # d cannot be unpacked because there are only 3 elements in the list, but we are trying to unpack into 4 variables
print(b)
# Traceback (most recent call last):
#   File "c:\PythonLearning\bac-à-sable.py", line 2, in <module>
#     a, b, c, d = fruits
#     ^^^^^^^^^^
# ValueError: not enough values to unpack (expected 4, got 3)



## Lists from strings

# create a list
x = list(('apple', 'banana', 'cherry'))
print(x)
# ['apple', banana', 'cherry']

# create a list from a string + sort it
first_greek_3 = sorted('omega')
print(first_greek_3)
# ['a', 'e', 'g', 'm', 'o']