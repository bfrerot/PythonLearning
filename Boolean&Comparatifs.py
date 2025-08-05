### ------- COMPARATIFs ------- ##

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


### L'odre de priorite est:
# not
# and
# or
z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)
# True
x = y < z or (z > y and y > z) or z < y
print(x)
# True


# and # true if all occurences are true =  CONJUNCTION
# or # true if at least one of all occurences is true = DISJUNCTION


## On peut mixer Boolean et Comparison

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


### ==, !=

animal = "tigre"
print (animal == "tig")
False
print (animal != "tig")
True
print (animal == 'tigre')
True


### ATTENTION on peut comparer des lettres, c'est l'ordre alphabétique ASCII qui est pris en compte

print ("a" < "b")
True
print ("ali" < "alo")
True
print ("abb" < "ada")
True
print ('alpha' < 'alphabet')
True # longer = bigger
print ('beta' > 'Beta')
True # b = 98 vs B = 66
print('10' > '010')
True # 1 = 49 vs 0 = 48
print('10' > '8')
# False
print('20' < '8')
# True
print('10' == 10)
# False
print('10' != 10)
# True
print('10' == 1)
# False
print('10' != 1)
# True
print('10' > 10)
# TypeError: '>' not supported between instances of 'str' and 'int'



### pour comparer une variable à une valeur

var = 0
print (var == 0)
True
var = 1
print (var == 0)
False
print (var != 0)
True


x = 23.42
print(bool(x) + True)
# 2


### True or False ?
print(not 0)        
# True
print(not 23)       
# False
print(not '')       
# True
print(not 'Peter')  
# False
print(not None)     
# True



### Priorite des operateurs

#  Priority	  Operator	
#   1	       +, -	unary
#   2	       **	
#   3	       *, /, //, %	
#   4	       +, -	binary
#   5	       <, <=, >, >=	
#   6	       ==, !=	
#########################


### avec input
n = int(input("Enter n value: "))
print (n >= 100)
# "Enter n value:" 55
False

# "Enter n value:" 100
True


### <, >

print (1>2)
False
print (2>1)
True


### None
# It is true that the None value can not be used as an argument of arithmetic operators
# But the None value can be assigned and compared to variables and that can happen outside of a function

b = None
print (b)
      # ca n affiche rien (none)

print(None + 2)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' 
print(None + "none")
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(7))
# None


###  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" not in alphabet)
True
True


### BITWISE operations

## x << y

# Returns x with the bits shifted to the left by y places
# (and new bits on the right-hand-side are zeros).
# This is the same as multiplying x by 2**y.
print (2<<2)
8 # on passe de 10 à 1000 en binaire


## x >> y
# Returns x with the bits shifted to the right by y places. 
# This is the same as //'ing x by 2**y.
print (2>>2)
0 # on passe de 10 à 0 en binaire


## x & y - AND
# Does a "bitwise and". 
# Each bit of the output is 1 if x AND y is 1, otherwise it's 0.


## x | y - OR
# Does a "bitwise or". 
# Each bit of the output is 0 if x AND y is 0, otherwise it's 1.


## ~ x
# Returns the complement of x - the number you get by switching each 1 for a
# 0 and each 0 for a 1. 
# Calculer -(x + 1)
x=2
print (~x)
# -3

x=-1
print (~x)
# 0


## x ^ y
# Does a "bitwise exclusive or". 
# Si les bits sont identique ==> 0
# si les bits sont differnets ==> 1
x = 5 # 101
y = 3 # 011
print(x ^ y)
# 6 ==> 110


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


# abbreviated forms:
# x = x & y ==>	x &= y
# x = x | y	==> x |= y
# x = x ^ y	==> x ^= y


### Augmented assignment statement Equivalent assignment statement 
# spam += 1                      spam = spam + 1 
# spam -= 1                      spam = spam - 1 
# spam *= 1                      spam = spam * 1 
# spam /= 1                      spam = spam / 1 
# spam %= 1                      spam = spam % 1



### bool() 

##  and (Logical AND)
# Returns True if both operands are True.Otherwise, returns False.

print(True and True)   # True
print(True and False)  # False
print(False and False) # False


## or (Logical OR)
# Returns True if at least one operand is True. Returns False only if both operands are False.

print(True or False)   # True
print(False or False)  # False
print(True or True)    # True


## not (Logical NOT)
# Reverses the boolean value.

print(not True)  # False
print(not False) # True


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

