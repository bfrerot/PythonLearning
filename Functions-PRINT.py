########## PRINT() ##########


print()

#1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.

#2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported.
#   Python 3.7.1 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.

#3. To call a function (function invocation), you need to use the function name followed by parentheses.
#   You can pass arguments into a function by placing them inside the parentheses. You must separate arguments
#   with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

#4. Python strings are delimited with quotes, e.g., "I am a string", or 'I am a string, too'.

#5. Computer programs are collections of instructions. An instruction is a command to perform
#   a specific task when executed, e.g., to print a certain message to the screen.

#6. In Python strings the backslash (\) is a special character which announces that the next
#   character has a different meaning, e.g., \n (the newline character) starts a new output line.

#7. Positional arguments are the ones whose meaning is dictated by their position, e.g.,
#   the second argument is outputted after the first, the third is outputted after the second, etc.

#8. Keyword arguments are the ones whose meaning is not dictated by their location,
#   but by a special word (keyword) used to identify them.

#9. The end and sep parameters can be used for formatting the output of the print() function.
#   The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"),
#   whereas the end parameter specifies what to print at the end of the print statement.



## print("string")
print("tigre")
# tigre



## print(variable)
animal = "tigre"
print (animal) # pas de "" c'est une variable
# tigre



## print(many "string") avec plusieurs arguments string

# ==> SI , ALORS un espace est INCLUS entre chaque, et TOUS sur la MEME ligne

print("The itsy bitsy spider","climbed up","the waterspout.")
# The itsy bitsy spider climbed up the waterspout.

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
# 1 1000.0 John Doe


# ==> SI PAS DE , ALORS PAS D'ESPACE entre chaque, et TOUS sur la MEME ligne
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

# \n = (n = new line) aller a la ligne, end = \n par défaut

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
# pour ignorer la valeur par défaut du caractère: '   "   \
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")
# "I'm"
# ""learning""
# """Python"""

print(len("\\\\")) # ==> \\ = \, * 2
# 2



## saut de ligne

# avec print()

print("The itsy bitsy spider climbed up the waterspout.") # va à la ligne par defaut
print() # --> pour sauter une ligne
print("Down came the rain and washed the spider out.")
# The itsy bitsy spider climbed up the waterspout.
#
# Down came the rain and washed the spider out.

# avec \n


print("The itsy bitsy spider\n\n\n") # # va a la ligne 4 fois
print("Down came the rain")
# The itsy bitsy spider
#
#
#
# Down came the rain

print("The itsy bitsy spider\n\n") # va a la ligne 3 fois
print("Down came the rain")
# The itsy bitsy spider
#
#
# Down came the rain


print("The itsy bitsy spider\n") # # va a la ligne 2 fois
print("Down came the rain")
# The itsy bitsy spider
#
# Down came the rain

print("The itsy bitsy spider") # va a la ligne
print("Down came the rain")
# The itsy bitsy spider
# Down came the rain



## " and '

print("Homer don't care")
# Homer don't care

print('Homer don't care')
# SyntaxError: invalid syntax


## end =
#default is end="\n"

print("My name is", "Python.", end=" ") # on ne va pas à la ligne mais un espace à la place
print("Monty Python.")
# My name is Python. Monty Python.

for digit in "0165031806510":
    if digit == "0":
        print("X",end="")
    else:
        print(digit,end="")
# X165X318X651X


## sep =
# lié à la virgule ET par defaut sep = espace

print("My", "name", "is", "Monty", "Python.", sep="-") 
# My-name-is-Monty-Python.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
# My_name_is*Monty*Python.*

# sep=None = DEFAULT soit " "
print("Hello","World",sep=None)
# Hello World



## print avec .format
print ('hello {} {}'.format('prenom','nom')) # --> on aura un brace par mot à inserer
# hello prenom nom
print ('hello {1} {0}'.format('prenom','nom')) # --> on peut preciser par indexation (on commence à 0)
# hello nom prenom
print ('hello {p} {n}'.format(p='prenom',n='nom')) # --> on peut definir une variable et l'indiquer
# hello prenom nom
# attention si oubli d'une variable, pas de default behavior, ca plante
print ('hello {} {}'.format('prenom'))
# IndexError: Replacement index 1 out of range for positional args tuple

# Arrondir
result = 100.0/777 
print(result)
# 0.1287001287001287
print('the result is {r:1.4f}'.format(r=result)) # precision à 4 chiffres après la virgule
# the result is 0.1287
print('the result is {r:10.4f}'.format(r=result)) # 10 = nbre de chiffres du premier entier a la derniere decimale, si pas de chiffre alors un espace
# the result is     0.1287



## %(var)

x = 'String'
print ('Place my variable here: %s' %(x)) # %s = s'attend à une variable %(x) = va y mettre la variable x
# Place my variable here: String

y = 2
print ('Place my variable here: %s' %(y))
# Place my variable here: 2

propGC = (4500.0 + 2575.0)/14800
print ("La proportion de GC est, %.2f" % propGC) # 2*float après la virgule
# La proportion de GC est, 0.48


print ('floating point number: %1.1f' %(x))  # va prendre que le nbre desire de chiffres apres la virgule, et inserer des 0 si necessaire (ex 1.45 --> 1.450000)
# floating point number: 1.1

print ('floating point number: %1.9f' %(x))
# floating point number: 1.123456789
print ('floating point number: %.9f' %(x))  # .x ou 0.1x ou 1.1x à l'air pareil
# floating point number: 1.123456789
print ('floating point number: %0.9f' %(x))
# floating point number: 1.123456789

print ('floating point number: %25.9f' %(x)) # va en meme temps inserer des espaces
# floating point number:               1.123456789

print ('First: {x} Second {y} Third: {x}'.format(x='inserted',y='two!')) # une variable peut etre utilisée plusieurs fois
# First: inserted Second two! Third: inserted



## input()

# sert à inclure une donnée dans le programme
# le resultat d'un input NE PEUT ETRE QU UN STRING

print("Tell me anything...")
anything = input() # on a alors un prompt qui attend que l'on tape quelquechose, mais ça pourrait etre aussi du son de l'image ou video etc
print("Hmm...", anything, "... Really?")
# Tell me anything...
# nada
# Hmm... nada ... Really?


# int() et float() permettent de changer la string en integer ou float

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


# concatenation, ajouter des inputs et d'autres strings

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
# May I have your first name, please? benoit
# May I have your last name, please? frerot
# Thank you.

# Your name is benoit frerot.