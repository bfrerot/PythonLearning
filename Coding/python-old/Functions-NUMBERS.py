### fonctions pour changer de type

# de float ou int vers str
a= 2.2
print (str(a))
2.2
d= 4
print (str(d))
4 # en fait "4"

b = "20.2"
print (str(int(float(b))))
20

total_pancakes = 10
pancakes_eaten = 5
print ("Only " + str(total_pancakes - pancakes_eaten) + " pancakes left.")
Only 5 pancakes left.# on a changé le resultat d'une operation en str

# de string vers int, attention si virgule on ne pourra pas convertir en int
# par contre possible dans l'autre sens de float vers int vers str (cf au-dessus)
b = "20.2"
print (int(b))
Traceback (most recent call last):
  File "C:\Users\bfrerot\OneDrive - ID Logistics\Documents\Python\IDLE.py", line 2, in <module>
    print (int(b))
ValueError: invalid literal for int() with base 10: '20.2'

e = float(b)
print (e)
20.2


### round()
# arrondit au nombre entier le plus près
print (round(1.1))
print (round(1.9))
print (round(1.5))
print (round(2.5))
print (round(3.5))
print (round(10.5))
1
2
2
2
4 # arrondit au supérieur, pourquoi ? Rounding ties rule
10

# A tie is any number whose last digit is a five. 2.5 and
# 3.1415 are ties, but 1.37 is not.
# When you round ties to even, you first look at the digit one decimal
# place to the left of the last digit in the tie. If that digit is even, you
# round down. If the digit is odd, you round up. That’s why 2.5 rounds
# down to 2 and 3.5 round up to 4 ###

# 2ème argument pour limiter le nombre de chiffres après la virgule, doit etre un nbre entier
print (round(2.56789, 2))
print (round(3.543219876, 4))
2.57
3.5432

# contradiction avec la Round Ties Rule qui veut arrondir au nombre ENTIER even le plus près
print (round(2.675))
print (round(2.675, 2))
3
2.67

var1 = float((input ("Enter a number: ")).replace(",","."))
var2 = round(var1,2)
print (var1,"rounded to 2 decimals places is",var2)
Enter a number: 2,456
2.456 rounded to 2 decimals places is 2.46

print (round(pow(3,0.125),3))
1.147


### abs()

# The absolute value of a number n is just n if n is positive, and -n
# if n is negative. For example, the absolute value of 3 is 3, while the
# absolute value of -5 is 5
print (abs(5))
print (abs(-5.780))
print (abs(-5.608))
5
5.78
5.608

var1 = float((input ("Enter a number: ")).replace(",","."))
var2 = abs(var1)
print ("The absolute value of",var1,"is",var2)
Enter a number: 5,456
The absolute value of 5.456 is 5.456


### pow()

# You can also use the pow() function. pow() takes two
# arguments. The first is the base, that is the number to be raised to a
# power, and the second argument is the exponent
print (pow(2, 3))
print (pow(-2, 3))
print (pow(2, -3))
print (pow(2.5, 3))
print (pow(2, 3.5))
print (pow(2.5, -3))
print (pow(2, -3.5))
print (pow(-2.5, 3))
print (pow(-2, 3.5))
8
-8
0.125
15.625
11.313708498984761
0.064
0.08838834764831845
-15.625
(-4.849353914918763e-15-11.313708498984761j)

# avec un troisieme argument pour obtenir le modulo en rapport avec ce troisième argument
print (pow(2, 3, 2))
print (pow(2, 3, 3))
0
2

