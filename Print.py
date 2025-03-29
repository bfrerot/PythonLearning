############################# VARIABLES + print #############################

animal = "tigre"
print (animal) # pas de "/' c'est une variable
# tigre

## print() avec plusieurs arguments string, un espace est INCLUS entre chaque, et TOUS sur la MEME ligne
print("The itsy bitsy spider","climbed up","the waterspout.")
#The itsy bitsy spider climbed up the waterspout.
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
#The itsy bitsy spider climbed up the waterspout.

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
# 1 1000.0 John Doe


var = "3.7.1"
print("Python version: " + var)
# Python version: 3.7.1


john = 3
mary = 5
adam = 6
print (john,mary,adam)
# 3,5,6

john = 3
mary = 5
adam = 6
totalApples = john + mary + adam
print ("Total number of apples = ",totalApples)
# Total number of apples =  14


sheep = 2
sheep += 1 # pour raccourcir sheep = sheep + 1
print (sheep)

# changer kilometres en miles
kilometers = 12.25
miles = 7.38
miles_to_kilometers = 	miles * 1.60934
kilometers_to_miles = kilometers * 0.621371
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")  # round(VARIABLE, x) = ARRONDIR la variable a x chiffres après la virgule
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# calculer y en fonction de x
x =  0
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
-1.0

# \n = aller a la ligne --> \ means the character following has not the usual meaning  +   n = new line
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")
#   *
#   * *
#  *   *
# *     *
#***   ***
#  *   *
#  *   *
#  *****

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")
"I'm"
""learning""
"""Python"""

------- STRING FORMATING for PRINTING -------

print() function

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


>>> print 'this is a string'
this is a string
>>> s='string'
>>> print s # ne marche pas en python 3
string

print("The itsy bitsy spider climbed up the waterspout.")
print() # --> pour sauter une ligne
print("Down came the rain and washed the spider out.")
The itsy bitsy spider climbed up the waterspout.

Down came the rain and washed the spider out.


print("The itsy bitsy spider\nlimbed up the waterspout.")  # --> \n renvoie à la ligne, qu'il soit suivi de data ou pas
print()
print("Down came the rain\nand washed the spider out.")
The itsy bitsy spider
limbed up the waterspout.
 
Down came the rain
and washed the spider out.

OU

print("The itsy bitsy spider\n")
print()
print("Down came the rain\n")
The itsy bitsy spider
 
 
Down came the rain
 
print (r"i love \\\")
#le r avant le "string" indique un raw string donc ignore tous les escape characterisés
i love \\\


# " and '

print("Homer don't care")
Homer don't care

print('Homer don't care')
...
SyntaxError: invalid syntax


# end="" --> is undercover like end="\n", donc la on force python a changer son comportement par defaut
print("My name is", "Python.", end=" ") 
print("Monty Python.")
My name is Python. Monty Python.

for digit in "0165031806510":
    if digit == "0":
        print("X",end="")
    else:
        print(digit,end="")
# X165X318X651X


# sep="" --> meme chose mais on change le separateur par defaut (espace) par ce qu'on veut, ici "-"
print("My", "name", "is", "Monty", "Python.", sep="-") 
My-name-is-Monty-Python.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
My_name_is*Monty*Python.*


# jeu de fleches avec print
# Sample Solution

###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

# end --> permet de modifier le end par defaut 
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
OpenEDG # l'espace est affiche meme si on le voit pas

# without end="", les lettres seront ecrites a la suite avec un a-la-ligne par defaut
 
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter)
O
p
e
n
E
D
G



# -> print("\\") double \ if you want to print it once
print("\\")
\



# la "," implique un espace
print("The itsy bitsy spider","climbed up","the waterspout.")
The itsy bitsy spider climbed up the waterspout.



# mettre un \ avant un caractere special pour le rendre inactif comme un string
print("\"I'm\"\n""\"\"learning\"\"\n""\"\"\"Python\"\"\"")
"I'm"
""learning""
"""Python"""


# print avec .format
print ('hello {} {}'.format('prenom','nom')) # --> on aura un brace par mot à inserer
hello prenom nom
print ('hello {1} {0}'.format('prenom','nom')) # --> on peut preciser par indexation (on commence à 0)
hello nom prenom
print ('hello {p} {n}'.format(p='prenom',n='nom')) # --> on peut definir une variable et l'indiquer
hello prenom nom
# attention si oubli d'une variable, pas de default behavior, ca plante
print ('hello {} {}'.format('prenom'))
IndexError: Replacement index 1 out of range for positional args tuple

name = "pacho"
print('Hello, his name is {}'.format(name))
print(f'Hello, his name is {name}') # Pythonv3

name = 'Sam'
age = 3
print(f'{name} is {age} years old.')
Sam is 3 years old.

# Agrandir et doubler des formes (strings made)
###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)




# Arrondir
result = 100.0/777 
result
0.1287001287001287
print('the result is {r:1.4f}'.format(r=result)) # precision à 4 chiffres après la virgule
the result is 0.1287
print('the result is {r:10.4f}'.format(r=result)) # 10 = nbre de chiffres du premier entier a la derniere decimale,
the result is     0.1287



# floating or integer ?
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
8
8.0
8.0
8.0


print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
2.0 # --> can be a problem when you need the result to be an integer
2.0
2.0
2.0
si on veut un resultat en integer seulement on doit doubler le backslash, 
mais ne prendra jamais en compte le chiffre derriere la virgule
print(6 // 3)
2
print(18 // 4)
4 # 4.5 normalement

# Arrondissement
print(-10 // 3)
print(6. // -4)
-4 # au lieu de 3.333333
-2.0 # au lieu de 1.5
# on arrondit au up integer value


# %(var)

x = 'String'
print ('Place my variable here: %s' %(x)) # %s' = s'attend à une variable %(x) = va y mettre la variable x
Place my variable here: String

y = 2
print ('Place my variable here: %s' %(y))
Place my variable here: 2

propGC = (4500.0 + 2575.0)/14800
print ("La proportion de GC est, %.2f" % propGC) # un peu etrange



x=2.25
print ('place my variable here: %s' %(x))
s="string"
print ('place my variable here: %s' %(s))
x=1.123456789
print ('floating point number: %1.1f' %(x))
1.1


print ('floating point number: %1.1f' %(x))  # va prendre que le nbre desire de chiffres apres la virgule, et inserer des 0 si necessaire (ex 1.45 --> 1.450000)
floating point number: 1.1
print ('floating point number: %1.9f' %(x))
floating point number: 1.123456789
print ('floating point number: %25.9f' %(x)) # va en meme temps inserer des espaces
floating point number:               1.123456789
print ('floating point number: %.9f' %(x))  # .1 ou 0.1 c'est pareil
floating point number: 1.123456789
print ('floating point number: %0.9f' %(x))
floating point number: 1.123456789


first:2, second:3
print ('First: {x} Second {y} Third: {x}'.format(x='inserted',y='two!'))
First: inserted Second two! Third: inserted


On peut refaire les meme exemples avec int au lieu de float (voir types de valeurs --> float/int/long int/complex)





#  ------- INPUT -------

# sert à inclure une donnée dans le programme
# le resultat d'un input NE PEUT ETRE QU UN STRING
# on ne peut pas faire d'operations avec le resultat d'un input


print("Tell me anything...")
anything = input() # on a alors un prompt qui attend que l'on tape quelquechose, mais ça pourrait etre aussi du son de l'image ou video etc
print("Hmm...", anything, "... Really?")
Tell me anything...
#prompt#
nada
Hmm... nada ... Really?

anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
Tell me anything#prompt#)nada
Hmm... nada ...Really?#prompt# input

#calcul hypotenuse

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
Input first leg length: 2.4
Input second leg length: 5.6
Hypotenuse length is 6.092618484691126

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = round(((leg_a**2 + leg_b**2) ** .5),2)
print ("Hypotenuse length is", hypo) # on arrondit à 2 chiffres apres la virgule
Input first leg length: 6
Input second leg length: 7
Hypotenuse length is 9.22

# pour contourner le probleme --> int() et float() permettent de changer la string en integer ou float

anything = int(input("Enter a number: "))
something = anything ** 2
print(anything, "to the power of 2 is", something)
Enter a number: 2
2 to the power of 2 is 4

anything = int(float("Enter a number: "))
something = anything ** 2
print(anything, "to the power of 2 is", something)
Enter a number: 2
2 to the power of 2 is 4.0


# concatenation, ajouter des inputs et d'autres strings

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
May I have your first name, please? benoit
May I have your last name, please? frerot
Thank you.

Your name is benoit frerot.


# RAPPEL REPLICATION
# "James" * 3 gives "JamesJamesJames"
# 3 * "an" gives "ananan"
# 5 * "2" (or "2" * 5) gives "22222" (not 10!)
exemple:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
+----------+
|          |
|          |
|          |
|          |
|          |
+----------+


# transformer un number en string avec str() dans une concatenation de strings et numbers

print ("j'aime" + "" + 2 +"" + "femmes")
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print ("j'aime" + "" + 2 +"" + "femmes")
TypeError: must be str, not int 


print ("j'aime" , "" , 2 ,"" , "femmes") # contourne l impossibilite de concatener directement (+) des strings avec des int
j'aime  2  femmes