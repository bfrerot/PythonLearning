########## NUMBERS ##########



### INTEGERS

# on peut écrire 11111111, ou 11_111_111 ==> pas utilisé mais correct
# INTERDIT ==> 11,111,111, ou  11.111.111


# integers = nbre entier negatif ou positif
print(type(4))
# <class 'int'>
print(type(int("4")))
# <class 'int'>


# Octal value
# 0o123 is an octal number with a (decimal) value equal to 83
print(type(0o123))
# <class 'int'>
print(0o123)
# 83


# Puissances
# 8*n/...8*3,8*2,8*1,8*0
print(type(8**2))
# <class 'int'>
print(8**3)
# 512
# RAPPEL x**0 = 1   ET  x**1 = x


# Hexadecimal value
# 0x123 is a hexadecimal number with a (decimal) value equal to 291
print(type(0x123))
# <class 'int'>
print(0x123)
# 291



### FLOATS

# 4.0 or 4. is a float
print(type(4.0))
# <class 'float'>
print(type(float("4.0")))
# <class 'float'>

# division and float result
print (2/4)
# 0.5
print (2./4)
# 0.5
print (2//4) # ==> result est une int
# 0



### INT vs FLOATS

# donner des operations en fonction de variables
a = float(input("give a float a:"))# input a float value for variable a here
b = float(input("give a float b:"))# input a float value for variable b here
print("a+b=",a+b)# output the result of addition here
print("a-b=",a-b)# output the result of subtraction here
print("a*b=",a*b)# output the result of multiplication here
print("a/b=",a+b)# output the result of division here
# give a float ==> a:2.0
# give a float ==> b:4
# a+b= 6.0
# a-b= -2.0
# a*b= 8.0
# a/b= 6.0

print (2/4.)
# 0.5
print (2*4.)
# 8.0
print (2+4.)
# 6.0
print (2-4.)
# -2.0

# dès lors qu'un float est impliqué dans une opération le résultat sera float par défaut



### COMPLEX NUMBERS

# En Python, un nombre complexe s’écrit avec l’unité imaginaire j (ou J)
c = 3j + 1
print(type(3j+1))
# <class 'complex'>
print(type(c))
# <class 'complex'>

# options complex numbers
n=1+2j
print (n)
# (1+2j) ==> n = 1 + 2j crée un nombre complexe dont la partie réelle est 1 et la partie imaginaire est 2

print (n.real) 
# 1.0  ==> n.real donne la partie réelle (ici 1.0, un float)
print (n.imag)
# 2.0  ==> n.imag donne la partie imaginaire (ici 2.0, un float)
print (n.conjugate())
# (1-2j) ==> retourne le conjugué du nombre: (1-2j). Le conjugué a la même partie réelle et la partie imaginaire opposée.

a = 1 + 2j
b = 3 - 4j
print (a + b)
# (4-2j)
print (a - b)
# (-2+6j)
print (a * b)
# (11+2j)
print (a ** b)
# (932.1391946432212+95.9465336603415j)
print (a / b)
# (-0.2+0.4j)



### Determiner type data

# with a function
def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
print(isInt(5))
# True
print(isInt(5.0))
# False
print(isInt("5"))
True
False
None

# whith is
print(4 is float)
# False
print(4 is int)
# true

# with type() builtin function
print(type(4))
# <class 'int'>
print(type(4.0))
# <class 'float'>
print(type(3j+1))
# <class 'complex'>



### OPERATORS  ==>    +    -    *    /    //    %    **


## Priorities and order

# Multiplications/divisions precede Addition/Soustraction

# Modulo will precede if on the left
print(5 % 4 ** 2 // 2)
# 2
# first 4 ** 2 = 16
# second 5 % 16 = 5
# third 5 // 2 = 2

# Modulo only ==> from Left to Right 
# ==> first 9 % 6 gives 3, and then 3 % 2 gives 1
print(9 % 6 % 2) 
# 1

# Exponent only ==> from Right to Left ==> 2 ** 3 → 8; 2 ** 8 → 256
print(2 ** 2 ** 3)
# 256



## -
print(3-2)
# 1
print (3-4)
# -1



# /  
# ==> le resultat sera TOUJOURS une FLOAT
print (3/2)
# 1.5
print (3.0/2)
# 1.5
print (float(3)/2)
# 1.5
print(2 / 3)
# 0.6666666666666666
print(6 / 3) 
# 2.0
print(6 / 3.)
# 2.0
print(6. / 3)
# 2.0
print(6. / 3.)
# 2.0



# //
# integer divisional operator
# the results are always rounded
# the result can be float if one of element has a point ==> float rule !
print(1 // 2)
# 0
print(1 // 2.)
# 0.0
print(6 // 3)
# 2
print(6 // 3.)
# 2.0
print(6. // 3)
# 2.0
print(6. // 3.)
# 2.0

# !!! VERY IMPORTANT: rounding always goes to the lesser integer
print(2 // 4)
# 0 
print(-2 // 4) # = -0.5
# -1 ==> lesser integer
print(-9 // 4) # = -2.25
# -3   ==> lesser integer
print(6 // 4)
#1
print(6. // 4)
#1.0
print(6 / 4)
#1.5
print(6./ 4)
#1.5



## **
# RAPPEL:
# x**0=1
# 0**x=0
print (2**3)
# 8
print (4**5)
# 1024
print (2+10*10+3)
# 105
print (2**2**3) # de droite à gauche
# 256



## racine 

# on peut passer par une fonction du module math
import math
print(math.sqrt(16))
# 4.0

# ou passer par exponent 1/x
print(16**(1/2))
# 4



## modulo %

# x%0 ==> interdit
print(8 % 0)
# ZeroDivisionError: integer modulo by zero

# 0%x = 0
print(0 % 8)
# 0

# x%y pour y>x = x
print(2 % 100)
# 2
print(2 % 8)
# 2

# x%y pour y<x = remaining m from all possible y from x
print (7 % 3)
# 1
print(100 % 2)
# 0


# modulo with negative numbers

# -x % y et x < y ==> x
print ((-3 % 6))
# 3
# -x % y et x > y ==> 0
print ((-6 % 3))
# 0

# -x % -y et x < y ==> -x
print ((-3 % -6))
# -3
# -x % -y et x > y ==> 0
print ((-6 % -3))
# 0

# x % -y et x < y ==> -x
print ((3 % -6))
# -3
# x % -y et x > y ==> 0
print ((6 % -3))
# 0


# modulo with floats
# pas de changement aux règles ==> result sera float
print (12%4.5)
# 3.0
print (4.5 % 12)
# 4.5
print ((3. % 6))
# 3.0
print ((6. % 3))
# 0.0


# modulo with negative numbers AND floats
# idem a negative mais result sera float

# -x % y et x < y ==> x
print ((-3. % 6))
# 3.0
# -x % y et x > y ==> 0
print ((-6. % 3))
# 0.0

# -x % -y et x < y ==> -x
print ((-3. % -6))
# -3.0
# -x % -y et x > y ==> 0
print ((-6. % -3))
# 0.0

# x % -y et x < y ==> -x
print ((3. % -6))
# -3.0
# x % -y et x > y ==> 0
print ((6. % -3))
# 0.0


# modulo & multiplication
# de gauche à droite
print(2 * 3 % 5)   # ==> 2*3= 6  puis 6%5 = 1
# 1
print(3 % 5 * 2)   # ==> 3%5=3  puis 3*2=6
# 6



## multiplication *
print(2 * 3)
# 6
print(2 * 3.)
# 6.0
print(2. * 3)
# 6.0
print(2. * 3.)
# 6.0



## exposant
# Notation scientifique: 1e8 signifie 1 × 10^8; 3e8 signifie 3 × 10^8
# Le E ou le e fonctionne aussi bien en majuscule qu’en minuscule

# 3*(10E8) = 3E8 ou 3e8
print(3*(10e8))
# 3000000000.0
print(3*(10E8))
# 3000000000.0


# xEy -->  X = float ou integer    Y = integer   E(ou e) = positif ou negatif

print(1e-22)
# 0.0000000000000000000001 #0 + 21*0 apres la virgule
print(0.0000000000000000000001)
1e-22 # Python utilise la forme la plus simple pour aficher une valeur

print(-1e-22)
# -1e-22
print(-0.0000000000000000000001)
# 1e-22 

print(-1e22)
# -1e+22
print(-1e5)
# -100000.0
print(-100000.0)
# -100000.0 

# si la valeur est trop grande Python simplifie en l'infini = "inf"
v=2e400
print (v)
# inf        
print(type(v))
# <class 'float'> # une int avec un exposant est une float




### OPERATIONS sur variables

## shortcup operator
x=x*2 # = x*=2
x=x/2 # = x/=2
b=b+10 # = b+=10
i=i+2*x # = i+=2*x


## INT
a=5
print (a)
# 5

print(a+a)
10
a = 10

a=2*a
print (a)
20

# int()
# builtin function
print(int("1"))
# 1
print(int("1, 3"))  # ValueError ...
print(int("1. 3"))  # ValueError ...
print(int("1,3"))   # ValueError ...
print(int("1.3"))    # ValueError ... 



## FLOAT

b= 5.2
print(b)
# 5.2
# ATTENTION PAS de , SINON créee un TUPLE
c= 5,2
print(c)
# (5, 2)
print(type(c))
# <class 'tuple'>

# float()
# builtin function
print(float("1.3"))     # 1.3
print(float("1, 3"))  # ValueError ...
print(float("1. 3"))  # ValueError ...
print(float("1,3"))   # ValueError ...

# float approximation error
print (0,1 + 0,2)
0.30000000000000004 # correspond à la somme des approximations de 0,1 et de 0,2



### F-STRINGS et numbers

## on pourra utiliser des raccourcis propres au f-strings pour agir sur les numbers que l'on veut inclure dans un string

n = 7.124
print (f"The value of n is {n:.2}")
# The value of n is 7.1

n = 7.125
print (f"The value of n is {n:.2}")
# The value of n is 7.1

n = 7.126
print (f"The value of n is {n:.2}")
# The value of n is 7.1


n = 7.124
print (f"The value of n is {n:.2f}")
# The value of n is 7.12

n = 7.125
print (f"The value of n is {n:.2f}")
# The value of n is 7.12

n = 7.126
print (f"The value of n is {n:.2f}")
# The value of n is 7.13

n = 7.1
print (f"The value of n is {n:.2f}")
# The value of n is 7.10



## on peut aussi formater les nombres

n = 1234567890
print (f"The value of n is {n:,}")
# The value of n is 1,234,567,890
print (f"The value of n is {n:_}")
# The value of n is 1_234_567_890

n = 1234.56
print (f"The value of n is {n:,.2f}")
# The value of n is 1,234.56

n=150000
print (f"The value of n is {n:_.2f}")
# The value of n is 150_000.00



## on peut aussi deduire un pourcentage à partir d'un ratio

ratio = 0.9
print (f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'")
# Over 90.0% of Pythonistas say 'Real Python rocks!'
print (f"Over {ratio:.2%} of Pythonistas say 'Real Python rocks!'")
# Over 90.00% of Pythonistas say 'Real Python rocks!'

ratio = 0.999999999999
print (f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'")
# Over 100.0% of Pythonistas say 'Real Python rocks!'
print (f"Over {ratio:.2%} of Pythonistas say 'Real Python rocks!'")
# Over 100.00% of Pythonistas say 'Real Python rocks!'

n=(2/10)
print (f"The value of n is {n:.0%}")
# The value of n is 20%


# cas PCAP

name = 'Peter'  
sum = 120 + 180 + 165 + 224  # Just for convenience
count = 4  # Just for convenience
average = sum / count

print('%-20s, your average score is:%10.1f' % (name, average)) # %-20 = centré à gauche      is:%10.1f  10 mouvements de curseurs entre : et dernier caractère
# Peter               , your average score is:     172.2

print('%-20s, your average score is:%1.1f' % (name, average)) 
# Peter               , your average score is:172.2

print('%-20s, your average score is:%.1f' % (name, average)) 
# Peter               , your average score is:172.2


print('%-20s, your average score is: %1.5s' % (name, average)) # is: %1.5s =  5 curseurs entre ": " et dernier caractere 
# Peter               , your average score is: 172.2

print('%-20s, your average score is: %1.20s' % (name, average)) 
# Peter               , your average score is: 172.25

print('%-20s, your average score is: %1.5f' % (name, average))   
# Peter               , your average score is: 172.25000


print('%-20s, your average score is: %5.1s' % (name, average))   
# Peter               , your average score is:     1

print('%20s, your average score is: %5.1f' % (name, average)) # %20 ou %+20 = centré à droite
#                Peter, your average score is: 172.2

print('%20s, your average score is: %1.5s' % (name, average))   
#                Peter, your average score is: 172.2

print('%20s, your average score is: %1.5f' % (name, average))   
#                Peter, your average score is: 172.25000

print('%20s, your average score is: %5.1s' % (name, average))   
#                Peter, your average score is:     1