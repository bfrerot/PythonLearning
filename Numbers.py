###------- NUMBERS -------###

## ANY
# you can write this number either like this: 11111111, or like this: 11_111_111
# You can write: -11111111, or -11_111_111.
# Positive numbers do not need to be preceded by the plus sign, but it's permissible, +11111111 and 11111111

# Octal -> print(0o123) 
# Hexa -> print(0x123) 

# exposant: 300000000 = 3 *10^8 --> python --> 3E8
# the exponent (the value after the E) has to be an integer;
# the base (the value in front of the E) may be either an integer or a float.
# 6.62607 x 10-34 --> 6.62607E-34 in python
# print(0.0000000000000000000001) --> 1e-22 --> Python always chooses the more economical form of the number's presentation


## INTEGERS

#4 is an integer literal
#int("4") is not an integer literal
#integers = nbre entier negatif ou positif
#11,111,111, or  11.111.111 is prohibited.
#What Python does allow is the use of underscores in numeric literals: 11111111 or 11_111_111.
#We code negative numbers in Python? As usual - by adding a minus: -11111111 or -11_111_111.
#Octal value: 0o123 is an octal number with a (decimal) value equal to 83.
#8^n/...8^3,8^2,8^1,8^0
#Hexadecimal value: 0x123 is a hexadecimal number with a (decimal) value equal to 291
#16^n/...16¨3,16^2,16^1,16^0


## FLOATS

#4.0 is a floating-point literal
#float("4.0") is not
#floating point --> avec une virgule ou un exposant
# 4.0 = 4.
# 0.5 = .5
print (2/4)
0.5
print (2./4)
0.5


## INT vs FLOATS
# donner des operations enfonction de variables
a = float(input("give a float a:"))# input a float value for variable a here
b = float(input("give a float b:"))# input a float value for variable b here
print("a+b=",a+b)# output the result of addition here
print("a-b=",a-b)# output the result of subtraction here
print("a*b=",a*b)# output the result of multiplication here
print("a/b=",a+b)# output the result of division here
print("That's all, folks!")
# give a float a:2.0
# give a float b:4
# a+b= 6.0
# a-b= -2.0
# a*b= 8.0
# a/b= 6.0
# That's all, folks!


##COMPLEX NUMBERS

#(3x+2) is a complex number
# build with a imaginary (x) + real component


# Determiner type data (int ou float ?)

def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(isInt(5))
print(isInt(5.0))
print(isInt("5"))
True
False
None



## OPERATORS

# +, -, *, /, //, %, **

# Priorities and order

# Multiplications/divisions precede Addition/soustraction

# Modulo will precede if on the left
print(5%4**2//2)
# 2
# first 4**2 = 16
# second 5%16 = 5
# third 5//2 = 2


    #Modulo --> from Left to Right --> first 9 % 6 gives 3, and then 3 % 2 gives 1
print(9 % 6 % 2) 
#1

    #Exponent -> from Right to Left --> 2 ** 3 → 8; 2 ** 8 → 256
print(2 ** 2 ** 3)
256

# -
print(3-2)
1
print (3-4)
-1

# /  --> le resultat sera TOUJOURS une FLOAT
print (3/2)
1.5
print (3.0/2)
1.5
print (float(3)/2)
1.5

print(2 / 3)
0.6666666666666666
print(6 / 3) # le resultat d'une division est TOUJOURS un float
2.0
print(6 / 3.)
2.0
print(6. / 3)
2.0
print(6. / 3.)
2.0

# //
#integer divisional operator. It differs from the standard / operator in two details:
#ITS RESULT LACKS THE FRACTIONNAL PART - it's absent (for integers), or is always equal to zero (for floats); this means that the results are always rounded;
#it conforms to the integer vs. float rule.
print(1 // 2)
0
print(1 // 2.)
0.0
print(6 // 3)
2
print(6 // 3.)
2.0
print(6. // 3)
2.0
print(6. // 3.)
2.0

print((2 // 4), (-2 // 4))
0 -1
#--> This is very important: rounding always goes to the lesser integer
print(6 // 4)
print(6. // 4)
print(6 / 4)
print(6./ 4)
#1
#1.0
#1.5
#1.5


# puissance **
# RAPPEL:
# x**0=1
# 0**x=0

print (2**3)
8
print (4**5)
1024
print (2+10*10+3)  # suit la priorité */ sur +- --> mettre des virgules pour contourner comme en maths
105
print (2**2**3) #de droite à gauche
256


# racine --> on peut passer par une fonction du module math
import math
print(math.sqrt(16))
4.0
# ou passer par exponent 1/x
print(16**(1/2))
# 4

# modulo %
# 0%x = 0
print (7 % 3)
1 # si j'enleve des 3 combien me reste-t-il lorsque le restant est plus petit que 3 = mod
# modulo % from left to right
print(9 % 6 % 2)
1 # 9%6 = 3 ET 3%2 = 1
print ((3 % 6))
3
print(3 % 75)
3

x = 0
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1


#modulo with negative numbers: r = x - (y * (x // y))
print ((-3 % -6))
-3
print ((-3 % 6))
3
print ((3 % -6))
-3
print (1%2)
1
print(12 % 5)
2
print (12%4.5)
3.0

x = int(input())
# 11  
y = int(input())
# 4
x = x % y
print(x) # 3
x = x % y
print(x) # -1
y = y % x # -1 % 4
print(y)
# 1

# multiplication *
print(2 * 3)
6
print(2 * 3.)
6.0
print(2. * 3)
6.0
print(2. * 3.)
6.0

# modulo & multiplication
print(2 * 3 % 5)
1 # COMPRENDS PAS

# operations sur variables
a=5
print (a)
5
print(a+a)
10
a = 10
a=a+a
print (a)
20


#shortcup operator
x=x*2 = x*=2
x=x/2 = x/=2
b=b+10 = b+=10
i=i+2*x = i+=2*x


# assigner variable --> commence par une lettre / pas d'espace / pas de caractere "special"
my_income=100
tax_rate=0.1
my_taxes=my_income*tax_rate
print (my_taxes)
10.0


# pour interroger sur le type d'une variable, ici int ou float
a = 10
type(a) 
<type 'int'>
a =3.1
print (type(a))
<type 'float'>


# exposant
# 3*(10^8) = 3E8 ou 3e8
# ou xEy --> Y = integer et X = float ou integer et E(ou e) = positif ou negatif
1e-22 = 0.0000000000000000000001 #0 + 21 0 apres la virgule
print(0.0000000000000000000001)
1e-22 # Python utilise la forme la plus simple pour aficher une valeur

v=2e400
print (v)
inf # si la valeur est trop grande Python simplifie en l'infini
print type(v)
<class 'float'> # une int avec un exposant est une float



# float() error

print (float("1, 3"))
ValueError: could not convert string to float:


# octal & hexa values

print(0o123)
83
print(0x123)
291


# float approximation error

print (0,1 + 0,2)
0.30000000000000004 # correspond à la somme des approximations de 0,1 et de 0,2


# f-strings et numbers
# on pourra utiliser des raccourcis propres au f-strings pour agir sur les numbers
# que l'on veut inclure dans un string

n = 7.125
print (f"The value of n is {n:.2}")
n = 7.126
print (f"The value of n is {n:.2f}")
n = 7.1
print (f"The value of n is {n:.2f}") # on force à 2 chiffres après la virgule, quite à rajouter des 0
The value of n is 7.1 # ! devrait etre 7.12
The value of n is 7.13
The value of n is 7.10

# on peut aussi formatter les nombres
n = 1234567890
print (f"The value of n is {n:,}")
The value of n is 1,234,567,890
print (f"The value of n is {n:_}")
The value of n is 1_234_567_890

n = 1234.56
print (f"The value of n is {n:,.2f}")
The value of n is 1,234.56

n=150000
print (f"The value of n is {n:_.2f}")
The value of n is 150_000.00

# on peut aussi deduire un pourcentage à partir d'un ratio
ratio = 0.9
print (f"Over {ratio:.1%} of Pythonistas say 'Real Python rocks!'")
print (f"Over {ratio:.2%} of Pythonistas say 'Real Python rocks!'")
Over 90.0% of Pythonistas say 'Real Python rocks!'
Over 90.00% of Pythonistas say 'Real Python rocks!'

n=(2/10)
print (f"The value of n is {n:.0%}")
The value of n is 20%


# options complex numbers
n=1+2j
print (n)
print (n.real)
print (n.imag)
print (n.conjugate())
(1+2j)
1.0
2.0
(1-2j)

a = 1 + 2j
b = 3 - 4j
print (a + b)
print (a - b)
print (a * b)
print (a ** b)
print (a / b)
(4-2j)
(-2+6j)
(11+2j)
(932.1391946432212+95.9465336603415j)
(-0.2+0.4j)

x = 42
print (x.real)
print (x.imag)
print (x.conjugate())
42
0
42

y = 3.14
print (y.real)
print (y.imag)
print (y.conjugate())
3.14
0.0
3.14