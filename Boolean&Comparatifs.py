########## BOOLEANs & COMPARATIFs ##########



### EGALITES
'''
== égal à
!= différent de
> supérieur à
>= supérieur ou égal à
< inférieur à
<= inférieur ou égal à

On obtient True OU False, rappel True = 1 et False = 0
S'applique aux strings ET numbers
'''



### BOOLEANs
'''
==> AND
True and True = True
True and False = False
False and True = False
False and False = False

==> OR
True or True = True
True or False = True
False or True = True
False or False = False 

==> NOT
not = INVERSE
not True = False
not not True = True
not not not not True = True

==> PRIORITE
1- NOT
2- AND = CONJUNCTION
3- OR = DISJONCTION

z = 2
y = 1
x = y < z or z > y and y > z or z < y ==>  x = y < z or (z > y and y > z) or z < y
print(x)
# True
'''



### bool()
# ==> bool(x) = True  SAUF si x = None ou vide
print(bool(23))
True
print(bool(True))
True

print(bool(None))
False
print(bool([]))
False
print(bool(()))
False
print(bool(''))
False




### Usages

# INT
print ((4<5) and (4<6))
True
print ((8<5) and (4<6))
False
print ((8<5) or (4<6))
True

# Bool
print(True > False)
True
print(True < False)
False


# STR
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
print ('alpha' < 'alphabet') # longer = bigger
True 
print ('beta' > 'Beta') # b = 98 vs B = 66
True 
print('10' > '010') # 1 = 49 vs 0 = 48
True 
print('10' > '8') # 1 = 49 vs 8 = 56
# False
print('20' < '8') # 2 = 50 vs 8 = 56
# True

# MAIS pas de précipitation, un string n'égale pas le premier codepoint correspondant
print('10' == 49) 
# False

print('10' == 10)
# False
print('10' != 10)
# True
print('10' == 1)
# False
print('10' != 1)
# True

# On ne PEUT PAS comparer entre STR et INT/FLOAT
print('10' > 10)
# TypeError: '>' not supported between instances of 'str' and 'int'

# On peut comparer entre Bool et INT
print(True == 1)
True
print(False == 0)
False

print(int(True == 1))
1
print(float(False == 0))
1.0




### RAPPEL - Priorite des operateurs

#  Priority	  Operator	
#   1	       +, -	unary
#   2	       **	
#   3	       *, /, //, %	
#   4	       +, -	binary
#   5	       <, <=, >, >=	
#   6	       ==, !=	
#########################



### None
# It is true that the None value CAN NOT BE USED AS AN ARGUMENT in ARITHMETIC OPERATIONS
# But the None value can be assigned and compared to variables and that can happen outside of a function

b = None
print (b) # ça n affiche rien (None)
#              

print(None + True)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'bool'
print(None + 2)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' 
print(None + "none")
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'



###  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
True
print("F" not in alphabet)
True

# spécificité Python ==> string vide DANS string = TRUE !!
print("" in "alphabet")
True



### BITWISE operations

## x << y

# Returns x with the bits shifted to the left by y places
# (and new bits on the right-hand-side are zeros).
# This is the same as multiplying x by 2**y.
print (2<<2)  # 0010 ==> 1000 = 8
# 8


## x >> y
# Returns x with the bits shifted to the right by y places. 
# This is the same as //'ing x by 2**y.
print (2>>2) # 10 ==> 00, on sort meme du shéma, pas d'erreur
# 0
a = 5            # 0101
print(a >> 1)    # 0010 = 2
# 2
print(a >> 2)    # 0001 = 1
# 1


## x & y - AND
# Does a "bitwise and". 
# Each bit of the output is 1 if x AND y is 1, otherwise it's 0.
a = 5           # (0101 in binary)
b = 3           # (0011 in binary)
print(a & b)    # (0001 in binary) = 1
# 1


## x | y - OR
# Does a "bitwise or". 
# Each bit of the output is 0 if x AND y is 0, otherwise it's 1.
### | (Bitwise OR)
# If at least one bit is 1, the result is 1.
a = 5           # (0101 in binary)
b = 3           # (0011 in binary)
print(a | b)    # (0111 in binary) = 7
# 7


## ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1
# ==> Calculer -(x + 1)
x=2
print (~x)
# -3

x=-1
print (~x)
# 0


## x ^ y
# Does a "bitwise exclusive or". 
# Si les bits sont identique ==> 0
# si les bits sont differents ==> 1
x = 5          # 101
y = 3          # 011
print(x ^ y)   # 110 = 6
# 6


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



### Deal with SINGLE bits

''' 
Pour comprendre:

exemple de variable sur laquelle on doit prendre 1 bit en considération pour notre tache/travail/etc
flag_register = 0x1234

en binaire = 0000 0000 0000 0000 0001 0010 0011 0100 

ordre des bits 31, 30, etc, 0, de gauche à droite

on nous attribue le bit 3 = 4ème bit en partant du premier
==> flag_register = 0000000000000000000000000000x000


## Checker l'état du bit

on peut utiliser cette conjunction property:
x & 1 = x
x & 0 = 0

on applique un bit mask au bit que l'on souhaite tester
00000000000000000000000000001000
0000000000000000000000000000x000

si le résultat est True égal à 1 c'est que le bit esc activé
sinon, le bit est False, égal à 0, désactivé

ex:
the_mask = 8 # = 0000 0000 0000 0000 0000 0000 0000 1000
if flag_register & the_mask:
    print ("My bit is set")
else:
    print ("My bit is NOT set")


## Reseter l'état du bit
flag_register = flag_register & ~the_mask
~the_mask = 1111 1111 1111 1111 1111 1111 1111 0111
flag_register &= ~the_mask


## Set le bit à 1
x | 1 = 1
x | 0 = x
flag_register = flag_register | the_mask
flag_register |= the_mask


## Inverser le bit
x ^ 1 = ~x
x ^ 0 = x
flag_register = flag_register ^ the_mask
flag_register ^= the_mask
'''