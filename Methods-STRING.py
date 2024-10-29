########## Methods STRING ##########


## .capitalize()	# Converts the first character to upper case

# when first value is a letter set the first letter as Cap, others in min
# if first value is number, or space, all letters are set in min

print('aBcD'.capitalize())
Abcd

print('1aBcD'.capitalize())
1abcd

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
Alpha
Alpha
alpha
123
Αβγδ


## .casefold()	# Converts string into lower case

## .center()	# Returns a centered string

print('Hello'.center(20, '='))
=======Hello======== # on voit que si besoin le mot va deborder a gauche (mot impair)

## .count()	# Returns the number of times a specified value occurs in a string

print("abcabc".count("b"))
print('abcabc'.count("d"))
2
0


## .encode()	# Returns an encoded version of the string

## .endswith()	# Returns true if the string ends with the specified value

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
True
False
False
True


## .expandtabs()	# Sets the tab size of the string

## .find()	# Searches the string for a specified value and returns the position of where it was found

print("Emamamatata".find("ta"))
print("Eta".find("mma"))
print("Etata".find("ta"))
7
-1
1


## .format()	# Formats specified values in a string

ipadr = '10.1.1.1'
vrf = 'notaires'
ping = 'ping {} vrf {}'.format(ipadr, vrf)
print (ping)
ping 10.1.1.1 vrf notaires

## .format_map()	# Formats specified values in a string

## .index()	# Searches the string for a specified value and returns the position of where it was found

txt = "Hello, welcome to my world."
x = txt.index("w") # avec une lettre, prendra en compte la premiere occurence de la lettre presente dans le string
print(x)
7

txt = "Hello, welcome to my world."
x = txt.index("welcome") # avec un mot, prendra en compte la premiere lettre du mot
print(x)
7

## .isalnum()	# Returns True if all characters in the string are alphanumeric: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
True
True
True
False
False
False


## .isalpha()	# Returns True if all characters in the string are in the ALPHABET

print("Moooo".isalpha())
print('Mu40'.isalpha())
True
False


## .isascii()	# Returns True if all characters in the string are ascii characters

## .isdecimal()	# Returns True if all characters in the string are decimals

## .isdigit()	# Returns True if all characters in the string are digits

## .isidentifier()	# Returns True if the string is an identifier

## .islower()	# Returns True if all characters in the string are lower case

s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.islower()) # True si TOUT en minuscule sinon False
print (M.islower())
print (m.islower())
False
False
True


## .isnumeric()	# Returns True if all characters in the string are numeric

## .isprintable()	# Returns True if all characters in the string are printable

## .isspace()	# Returns True if all characters in the string are whitespaces

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
True
True
False


## .istitle()	# Returns True if the string follows the rules of a title

## .isupper()	# Returns True if all characters in the string are upper case

s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.isupper()) # True si TOUT en MAJUSCULE sinon False
print (M.isupper())
print (m.isupper())
False
True
False


## .join()	# Converts the elements of an iterable into a string

print(",".join(["omicron", "pi", "rho"]))
omicron,pi,rho

print("".join(["omicron", "pi", "rho"]))
omicronpirho

print("***".join(["omicron", "pi", "rho"]))
omicron***pi***rho

print("***".join(["1", "2", "3"]))
1***2***3


## .ljust()	# Returns a left justified version of the string

print ('Hello'.ljust(20, '-'))
Hello---------------


## .lower()	# Converts a string into lower case

s = "TrAvIaTa"
print (s.lower())
print (s)
traviata
TrAvIaTa # la variable n'est pas modifiée


## .lstrip()	# Returns a left trim version of the string

spam = '    Hello World    ' 
print (spam.lstrip())
Hello World    


## .maketrans()	# Returns a translation table to be used in translations

## .partition()	# Returns a tuple where the string is parted into three parts

## .replace()	# Returns a string where a specified value is replaced with a specified value

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
www.pythoninstitute.org

print("Apple juice".replace("juice", ""))
Apple

var1 = float((input ("Enter a number: ")).replace(",","."))
var2 = round(var1,2)
print (var1,"rounded to 2 decimals places is",var2)
Enter a number: 2,456
2.456 rounded to 2 decimals places is 2.46

## .rfind()	# Searches the string for a specified value and returns the LAST position of where it was found

print("tau tau tau".rfind("ta"))
8

print("Hello, welcome to my world.".rfind("e", 5, 10)) #on itére à partir du 5ème caractère donc ,=0 etc


print(x)

## .rindex()	# Searches the string for a specified value and returns the last position of where it was found

## .rjust()	# Returns a right justified version of the string

print ('Hello'.rjust(20, '*')) # par defaut ' '
***************Hello

print ('Hello'.rjust(20))
               Hello

## .rpartition()	# Returns a tuple where the string is parted into three parts

## .rsplit()	# Splits the string at the specified separator, and returns a list

## .rstrip()	# Returns a right trim version of the string

spam = '    Hello World    ' 
print (spam.rstrip())
    Hello World

## .split()	# Splits the string at the specified separator, and returns a list

print('MyABCnameABCisABCSimon'.split('ABC'))
['My', 'name', 'is', 'Simon']

## .splitlines()	# Splits the string at line breaks and returns a list

## .startswith()	# Returns true if the string starts with the specified value

print("omega".startswith("meg"))
print("omega".startswith("om"))
False
True


## .strip()	# Returns a trimmed version of the string

spam = '    Hello World    ' 
print (spam.strip())
Hello World


## .swapcase()	# Swaps cases, lower case becomes upper case and vice versa

print("I know that I know nothing.".swapcase())
i KNOW THAT i KNOW NOTHING.

## .title()	# Converts the first character of each word to upper case

print("I know that I know nothing. Part 1.".title())
I Know That I Know Nothing. Part 1.

## .translate()	# Returns a translated string

## .upper()	# Converts a string into upper case

s = "TrAvIaTa"
print (s.upper())
print (s)
TRAVIATA
TrAvIaTa # la variable n'est pas modifiée

## .zfill()	# Fills the string with a specified number of 0 values at the beginning