## ------- COMPARATIFs ------- ##

# == égal à ?
# != différent de
# > supérieur à
# >= supérieur ou égal à
# < inférieur à
# <= inférieur ou égal à
# On obtient True OU False
# S'applique aux strings ET numbers

# True and True = True
# True and False = False
# False and True = False
# False and False = False

# True or True = True
# True or False = True
# False or True = True
# False or False = False 

# not --> != 

# not True = False
# not not True = True
# not not not not True = True

# L'odre de priorite est:
# not
# and
# or
# and # true if all occurences are true =  CONJUNCTION
# or # true if at least one of all occurences is true = DISJUNCTION


# On peut mixer Boolean et Comparison

print ((4<5) and (4<6))
True
print ((8<5) and (4<6))
False
print ((8<5) or (4<6))
True

print(True > False)
print(True < False)
True
False


# ==, !=

animal = "tigre"
print (animal == "tig")
False
print (animal != "tig")
True
print (animal == 'tigre')
True


# ATTENTION on peut comparer des lettres, c'est l'ordre alphabétique ASCII qui est pris en compte

print ("a" < "b")
True
print ("ali" < "alo")
True
print ("abb" < "ada")
True


# pour comparer une variable à une valeur

var = 0
print (var == 0)
True
var = 1
print (var == 0)
False
print (var != 0)
True

n = int(input("Enter a number: "))
#
print(n >= 100)


# Priorite des operateurs

#  Priority	  Operator	
#   1	       +, -	unary
#   2	       **	
#   3	       *, /, //, %	
#   4	       +, -	binary
#   5	       <, <=, >, >=	
#   6	       ==, !=	
#########################


# avec input
n = int(input("Enter n value: "))
print (n >= 100)
"Enter n value:" 55
False

"Enter n value:" 100
True


# <, >

print (1>2)
False
print (2>1)
True

# None

b = None
print (b)
      # ca n affiche rien (none)


#  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" not in alphabet)
True
True


## ------- BITWISE ------- ##


# x << y
# Returns x with the bits shifted to the left by y places
# (and new bits on the right-hand-side are zeros).
# This is the same as multiplying x by 2**y.

print (2<<2)
8
print (2*2**2)
8


# x >> y
# Returns x with the bits shifted to the right by y places. 
# This is the same as //'ing x by 2**y.

print (2>>2)
print (2//2**2)
0
0


# x & y - AND
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit 
# of x AND of y is 1, otherwise it's 0.


# x | y - OR
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit 
# of x AND of y is 0, otherwise it's 1.


# ~ x
# Returns the complement of x - the number you get by switching each 1 for a
# 0 and each 0 for a 1. This is the same as -x - 1.

x=2
print (~x)
-3

x=-1
print (~x)
0


# x ^ y
# Does a "bitwise exclusive or". 
# Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,
# and it's the complement of the bit in x if that bit in y is 1.


var = 1
while var < 10:
    print ("*")
    var = var << 1
"*"
"*"
"*"
"*"


##  Logic and bit operations 

# & (ampersand) - bitwise conjunction;
# | (bar) - bitwise disjunction;
# ~ (tilde) - bitwise negation;
# ^ (caret) - bitwise exclusive or (xor).

# Bitwise operations (&, |, and ^)
# Arg A	Arg B	Arg A & Arg B	Arg A | Arg B	Arg A ^ Arg B
# 0	    0	          0	              0	              0
# 0	    1	          0	              1	              1
# 1	    0	          0	              1	              1
# 1	    1	          1	              1	              0

# Bitwise operations (~)
# Arg	~Arg
# 0	 1
# 1	 0

# Let's make it easier:

# & requires exactly two 1 to provide 1 as the result;
# | requires at least one 1 to provide 1 as the result;
# ^ requires exactly one 1 to provide 1 as the result.

# abbreviated forms:
# x = x & y	x &= y
# x = x | y	x |= y
# x = x ^ y	x ^= y


# Augmented assignment statement Equivalent assignment statement 
# spam += 1                      spam = spam + 1 
# spam -= 1                      spam = spam - 1 
# spam *= 1                      spam = spam * 1 
# spam /= 1                      spam = spam / 1 
# spam %= 1                      spam = spam % 1



## bool() 

# Returns False as x is False 
x = False
print(bool(x)) 
False

# Returns True as x is True 
x = True
print(bool(x)) 
True


# True vs False
print(True > False)
print(True < False)
True
False


# Returns False as x is not equal to y 
x = 5
y = 10
print(bool(x==y)) 
False

# Returns False as x is None 
x = None
print(bool(x)) 
False

# Returns False as x is an empty sequence 
x = () 
print(bool(x)) 

# Returns False as x is an emty mapping 
x = {} 
print(bool(x)) 
False

# Returns False as x is 0 
x = 0.0
print(bool(x)) 
False

# Returns True as x is a non empty string 
x = 'GeeksforGeeks'
print(bool(x))
True

#verifier qu'un string est un digit: .isdigit()
ten = '10'
ten.isdigit()
True

bogus = '10a'
bogus.isdigit()
False

# .startswith()
ipadr = "10.1.1.13"
ipadr.startswith(10)
True

# .endswith()

ipadr = "10.1.1.13"
ipadr.endswith(13)
True

