## RULES

# The PEP 8 -- Style Guide for Python Code recommends the following naming convention for variables and functions in Python:
    # variable names should be lowercase, with words separated by underscores to improve readability (e.g., var, my_variable)
    # function names follow the same convention as variable names (e.g., fun, my_function)
    # it's also possible to use mixed case (e.g., myVariable), but only in contexts where that's already the prevailing style, to retain backward compatibility with the adopted convention.
    # a variable is name + value, the value is a string or a number or a Boolean 

# name = uper/lower-case,digits,_, and punctuation
# cannot start by a number / starts by a letter (_ is a letter)
# no space
# only latin characters
# forbidden special characters :"',<>/?|\()!@#$%^&*~-+
# case sensitive
# can't be a reserved Python variable
['False', 'None', 'True', 'and', 'as', 'assert', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
 'return', 'try', 'while', 'with', 'yield']
# best pratcice: lower case, avoid including special python terms

# simple var
my_dogs=2
print (my_dogs)
# 2


# printing var and strings
var = "3.8.5"
print("Python version: " + var)
Python version: 3.8.5


#printing var and numbers
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
# c = 5.0

var1 = "ab"
print(2*var1)
# abab


# variable can change its data type during code execution
my_dogs=2 # = number
print (my_dogs)
# 2
# ... later on
my_dogs=["kad","imane"] # = list
print (my_dogs)
# ['kad', 'imane']


#how many apples ?
j=3
m=5
a=6
total_apples=j+m+a
print("John has",j,"apples,","Mary ",m,"and Adam",a)
print("Total number of apples:",total_apples)
John has 3 apples, Mary  5 and Adam 6
Total number of apples: 14


#shortcup operator
x=x*2 = x*=2
b=b+10 = b+=10

var = 1
print(var)
# 1
var = var + 1
print(var)
# 2
var+=1
print(var)
# 3
print(var+=1) ## NOR Syntax error - you to redefine variable before printing it
# SyntaxError: invalid syntax