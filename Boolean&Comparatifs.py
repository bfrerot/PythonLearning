########## BOOLEANs & COMPARATIFs ##########



### EQUALITES
'''
== EQUAL TO
!= NOT EQUAL TO
>  UPPER THAN
>= UPPER THAN or EQUAL TO
<  LESSER THAN
<= LESSER THAN OR EQUAL TO

Output is True OU False
True = 1 
False = 0
Applies on strings and numbers
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
# ==> bool(x) = True  SAUF si x = None or empty
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

# !!! We can compare strings, alphabetic order applies
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

# But a string IS NOT equal to the first matching codepoint
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

# We cannot compare STR with INT/FLOAT
print('10' > 10)
# TypeError: '>' not supported between instances of 'str' and 'int'

# We can compare Bool with INT
print(True == 1)
True
print(False == 0)
False

print(int(True == 1))
1
print(float(False == 0))
1.0




### REMINDR - Operators priority

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
print (b) # prints nothing (None)
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

# spécificité Python ==> empty string in string = TRUE !!
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
print (2>>2) # 10 ==> 00, we go out but no error
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
# if bits are equals ==> 0
# if bits are differents ==> 1
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
To understand:

Variable example on which we want to consider 1*bit:
flag_register = 0x1234

binary = 0000 0000 0000 0000 0001 0010 0011 0100 

bits order = 31, 30, etc, 0, from left to right

we are given the bit 3 = 4th bit from the first, from right to left
==> flag_register = 0000000000000000000000000000x000


## Check bit state

we can use conjunction property:
x & 1 = x
x & 0 = 0

we applay a bit mask to the bit we want to check
00000000000000000000000000001000
0000000000000000000000000000x000

if the result is True, equal to 1, the bit is activated
else, the bit is False, equal to 0, deactivated

ex:
the_mask = 8 # = 0000 0000 0000 0000 0000 0000 0000 1000
if flag_register & the_mask:
    print ("My bit is set")
else:
    print ("My bit is NOT set")


## Reset the bit state
flag_register = flag_register & ~the_mask
~the_mask = 1111 1111 1111 1111 1111 1111 1111 0111
flag_register &= ~the_mask


## Set the bit to 1
x | 1 = 1
x | 0 = x
flag_register = flag_register | the_mask
flag_register |= the_mask


## Inverse the bit
x ^ 1 = ~x
x ^ 0 = x
flag_register = flag_register ^ the_mask
flag_register ^= the_mask
'''