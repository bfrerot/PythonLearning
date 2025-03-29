#rules

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

my_dogs=2
print (my_dogs)
2

var = "3.8.5"
print("Python version: " + var)
Python version: 3.8.5

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
c = 5.0

# variable can change its data type during code execution
my_dogs=2
print (my_dogs)
2
# ... later on
my_dogs=["kad","imane"]
print (my_dogs)
['kad', 'imane']

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
x=x*2
x*=2
b=b+10
b+=10