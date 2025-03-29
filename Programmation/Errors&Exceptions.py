# Error will occur wherever it is possible
# Syntax error = code's form not allowed in Python
# Runtime error = error not detectable before start of program

import math

x = float(input("Enter x: ")) # if user write a string, error will occur
y = math.sqrt(x) # if user write a negative number, error again

print("The square root of", x, "equals to", y)


# when code does somethng wrong
# Python stop the program
# and creates an exception
# = raising an exception    
# if exception is addressed --> program continues
# if nothing is done --> program stops and generate an error


BaseException # anyerror
# source tree


ZeroDivisionError # you cannot divide by 0
BaseException ← Exception ← ArithmeticError ← ZeroDivisionErro

value = 1
value /= 0
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    value /= 0
ZeroDivisionError: division by zero

overflowError # when an operation produces a number too big to be successfully stored
BaseException ← Exception ← ArithmeticError ← OverflowError


IndexError # index introuvable,inexistant
BaseException ← Exception ← LookupError ← IndexError

list = []
x = list[0]
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    x = list[0]
IndexError: list index out of range


ArithmeticError # any arithmetic error
BaseException ← Exception ← ArithmeticError 


AssertionError # concrete exception raised by the assert instruction when its argument evaluates to False,
# None, 0, or an empty string
BaseException ← Exception ← AssertionError


KeyboardInterrupt # raised when the user uses a keyboard shortcut designed 
# to terminate a program's execution (Ctrl-C in most OSs)
BaseException ← KeyboardInterrupt

MemoryError # cannot be completed due to a lack of free memory
BaseException ← Exception ← MemoryError

LookupError # errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
BaseException ← Exception ← LookupError

ImportError # an import operation fails
BaseException ← Exception ← StandardError ← ImportError

KeyError # when you try to access a collection's non-existent element
BaseException ← Exception ← LookupError ← KeyError





# try
# avec try, python gere les erreurs

# option 1 sans try

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

if secondNumber != 0:
    print(firstNumber / secondNumber)
else:
    print("This operation cannot be done.")

print("THE END.")

# option 2 avec try

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

try:
    print(firstNumber / secondNumber)
except:
    print("This operation cannot be done.")

print("THE END.")

# try --> except
#des qu il y a un probleme, python cherche un except, 
# s il y en a un, tout le code situe entre l erreur et l except sera ignore

try:
    print("1")
    x = 1 / 0 # error, va aller a except et ignorer print("2")
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")
1
Oh dear, something went wrong...
3

# on peut preciser une action differente en fonction de l erreur

try:
    :
except exc1:
    :
except exc2:
    :
except:
    :


    
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
Enter a number: 0
You cannot divide by zero, sorry.
THE END.
Enter a number: 
Enter a number: 2.2
You must enter an integer value.
THE END.
Enter a number: 3
0.3333333333333333
THE END.












# on va gerer les erreurs par leur code en leur donnant une porte de sortie
# exemple:

print(y = 1 / 0)
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(y = 1 / 0)
ZeroDivisionError: division by zero

# now
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")
Oooppsss...
THE END.

# so

try:
    print(y = 1 / 0)  # avec print
except ZeroDivisionError: 
    print("Oooppsss...")

print("THE END.")
Oooppsss...
THE END.

# on peut remplacer par n importe quel code situe au dessus 
# dans le tree d exception le plus haut etant BaseException

try:
    print(y = 1 / 0)
except BaseException:  
    print("Oooppsss...")

print("THE END.")


# Remember:

# the order of the branches matters!
# don't put more general exceptions before more concrete ones;
# this will make the latter one unreachable and useless;
# moreover, it will make your code messy and inconsistent;
# Python won't generate any error messages regarding this issue.

try:
    y = 1 / 0
except ArithmeticError:  # more general exception should not be first
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
print("THE END.")
Arithmetic problem!
THE END.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
print("THE END.")
Zero Division!
THE END.

# on peut mettre plusieurs exceptions dans un except
try:
    y = 1 / 0
except (ZeroDivisionError,ArithmeticError):
    print("Problem!")
print("THE END.")
Problem!
THE END.

# on peut inserer les exceptions DANS une function

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None
badFun(0)
print("THE END.")
Arithmetic Problem!
THE END.

# ou en dehors

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")
print("THE END.")
What happened? An exception was raised!
THE END.

# with "raise"

def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")
What happened? An error?
THE END.

def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        # raise # si on ne met raise

try:
    badFun(56)
except ArithmeticError:
    print("I see!")

print("THE END.")
I did it again!
I see!
THE END.
# sanns raise dans la def
I did it again!
########
THE END.


# assert

# you may want to put it into your code where you want to be absolutely safe 
# from evidently wrong data, and where you aren't absolutely sure that the data 
# has been carefully examined before (e.g., inside a function used by someone else)

# raising an AssertionError exception secures your code from producing invalid results, 
# and clearly shows the nature of the failure

# assertions don't supersede exceptions or validate the data 
# they are their supplements.

import math
x = float(input("Enter a number: "))
assert x >= 2.0
x = math.sqrt(x)
print(x)
Enter a number: 2 # match le assert
1.4142135623730951

Enter a number: 1,99 # ne match pas
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    assert x >= 2.0
AssertionError



#### lab ####

def readint(prompt, min, max):
    ok = True
    while not ok:
        try:
            value = int(input(prompt))
            ok = False
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value;

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)


## Compare strings --  think ASCII code

# 0 --> 9 = 48 --> 57
# a --> z = 97 --> 122
# A --> Z = 65 --> 90
# Numbers < CAPITAL < minuscule

print ('a' < 'b')
print ('a' < 'A')
print ('b' < 'A')
print ('aa' < 'ab')
print ('aa' < 'a1')
print ('a9' < 'a1')
print ('0' > 'a')
True
False
False
True
False
False
False

    
print ('10' == '010') # 4948 =! 484948
print ('10' > '010') # 4948 > 484948
print ('10' > '8') # 4948 < 56
print ('20' < '8') # 5048 < 56
print ('20' < '80') # 5048 < 5648
False
True
False
True
True


## ().sort // sorted()


secondGreek = ['omega', 'alpha', 'pi', 'gamma']
secondGreek.sort()
print(secondGreek)
print(secondGreek)
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']


firstGreek = ['omega', 'alpha', 'pi', 'gamma']
firstGreek2 = sorted(firstGreek)
print(firstGreek)
print(firstGreek2)
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

 
## str() - make numbers become string

itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)
print(si + ' ' + sf)
13 1.3