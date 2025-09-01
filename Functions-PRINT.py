########## PRINT() ##########


print()

#1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window

#2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported
#   Python 3.7.1 comes with 69 built-in functions
#   You can find their full list provided in alphabetical order in the Python Standard Library

#3. To call a function (function invocation), you need to use the function name followed by parentheses
#   You can pass arguments into a function by placing them inside the parentheses. You must separate arguments
#   with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen

#4. Python strings are delimited with quotes, e.g., "I am a string", or 'I am a string, too'

#5. Computer programs are collections of instructions. An instruction is a command to perform
#   a specific task when executed, e.g., to print a certain message to the screen

#6. In Python strings the backslash (\) is a special character which announces that the next
#   character has a different meaning, e.g., \n (the newline character) starts a new output line

#7. Positional arguments are the ones whose meaning is dictated by their position
#   the second argument is outputted after the first, the third is outputted after the second, etc

#8. Keyword arguments are the ones whose meaning is not dictated by their location
#   but by a special word (keyword) used to identify them

#9. The end and sep parameters can be used for formatting the output of the print() function
#   The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-")
#   whereas the end parameter specifies what to print at the end of the print statement



## print("string")
print("tigre")
# tigre



## print(variable)
animal = "tigre"
print (animal) # not any "" as animal is a variable
# tigre



## print(many "string")

# ==> if a comma is inserted between occurence (,) then a space will be included between them, and all on the same line

print("The itsy bitsy spider","climbed up","the waterspout.")
# The itsy bitsy spider climbed up the waterspout.

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
# 1 1000.0 John Doe


# ==> If no comma , NO space (like a concatenation with (+)) and all on the same line
print("Who" "are" "you")
# Whoareyou



## print("string" + var)

var = "3.7.1"
print("Python version: " + var)
# Python version: 3.7.1

john = 3
mary = 5
adam = 6
totalApples = john + mary + adam
print ("Total number of apples = ",totalApples)
# Total number of apples =  14



## \n

# \n = (n = new line) [RETURN KEY], goes to the next line, end = \n by default

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
#    *
#   * *
#  *   *
# *     *
#***   ***
#  *   *
#  *   *
#  *****



## \
# place before a character we want to ignore the default value/effect: '   "   \   n
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")
# "I'm"
# ""learning""
# """Python"""

print(len("\\\\")) # ==> \\ = \, * 2
# 2



## Next line

# with print()

print("The itsy bitsy spider climbed up the waterspout.") # goes to next line by default (end = \n)
print() # --> pour sauter une ligne
print("Down came the rain and washed the spider out.")
# The itsy bitsy spider climbed up the waterspout.
#
# Down came the rain and washed the spider out.


# with \n


print("The itsy bitsy spider\n\n\n") # default \n + 3*(\n), so lets 3 lines free
print("Down came the rain")
# The itsy bitsy spider
#
#
#
# Down came the rain

print("The itsy bitsy spider\n\n") # default \n + 2*(\n), so lets 2 lines free
print("Down came the rain")
# The itsy bitsy spider
#
#
# Down came the rain


print("The itsy bitsy spider\n") # default \n + 1*(\n), so lets 1 line free
print("Down came the rain")
# The itsy bitsy spider
#
# Down came the rain

print("The itsy bitsy spider") # default \n 
print("Down came the rain")
# The itsy bitsy spider
# Down came the rain



## " and '

print("Homer don't care")
# Homer don't care

print('Homer don't care')
# SyntaxError: invalid syntax


## end =
# default is end="\n"

print("My name is", "Python.", end=" ") # insert a space in place of default line return
print("Monty Python.")
# My name is Python. Monty Python.

for digit in "0165031806510":
    if digit == "0":
        print("X",end="")
    else:
        print(digit,end="")
# X165X318X651X


## sep =
# linked to the comma (,) separation role
# defaut sep = espace

print("My", "name", "is", "Monty", "Python.", sep="-") 
# My-name-is-Monty-Python.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
# My_name_is*Monty*Python.*

# sep=None = DEFAULT " "
print("Hello","World",sep=None)
# Hello World



## print with .format
print ('hello {} {}'.format('prenom','nom')) # --> a brace pair by value to insert
# hello prenom nom
print ('hello {1} {0}'.format('prenom','nom')) # --> we can use indexation (starting at 0)
# hello nom prenom
print ('hello {p} {n}'.format(p='prenom',n='nom')) # --> we can use variable(s) name(s)
# hello prenom nom
# !! if any mismatch ==> IndexError
print ('hello {} {}'.format('prenom'))
# IndexError: Replacement index 1 out of range for positional args tuple


## Rounding
result = 100.0/777 
print(result)
# 0.1287001287001287
print('the result is {r:1.4f}'.format(r=result)) # 4 numbers after comma
# the result is 0.1287
print('the result is {r:10.4f}'.format(r=result)) # 10 = number of character(s) ==> if needed filled with spaces on the left
# the result is     0.1287



## %(var)

x = 'String'
print ('Place my variable here: %s' %(x)) # %s = waits a variable ==> %(x) = put the x variable
# Place my variable here: String

y = 2
print ('Place my variable here: %s' %(y))
# Place my variable here: 2

propGC = (4500.0 + 2575.0)/14800
print ("GC proportion is %.2f" % propGC) # 2*float after the comma
# GC proportion is 0.48


print ('floating point number: %1.1f' %(x))  # limits the float number after the comma, and insert 0 ti fill in if necessary (ex 1.45 --> 1.450000)
# floating point number: 1.1

print ('floating point number: %1.9f' %(x))
# floating point number: 1.123456789
print ('floating point number: %.9f' %(x))  # .x or 0.1x or 1.1x outputs the same
# floating point number: 1.123456789
print ('floating point number: %0.9f' %(x))
# floating point number: 1.123456789

print ('floating point number: %25.9f' %(x)) # insert spaces to fill in the 25 characters space
# floating point number:               1.123456789

print ('First: {x} Second {y} Third: {x}'.format(x='inserted',y='two!')) # a variable may be used many times
# First: inserted Second two! Third: inserted



## input()

# to retrieve data from the user
# input() gives a STRING

print("Tell me anything...")
anything = input() # a prompt appears, waiting for input, could be sound or image
print("Hmm...", anything, "... Really?")
# Tell me anything...
# nada
# Hmm... nada ... Really?


# int() et float() allow to cpe with the default string return of input() function

anything = int(input("Enter a number: "))
something = anything ** 2
print(anything, "to the power of 2 is", something)
# Enter a number: 2
# 2 to the power of 2 is 4

anything = int(float("Enter a number: "))
something = anything ** 2
print(anything, "to the power of 2 is", something)
# Enter a number: 2
# 2 to the power of 2 is 4.0


# concatenation

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# May I have your first name, please? benoit
# May I have your last name, please? frerot
# Thank you.

# Your name is benoit frerot.