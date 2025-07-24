########## Methods STRING ##########


### .capitalize()	# Converts the first character to upper case

# when first value is a letter set the first letter as Cap, others in min
# if first value is number, or space, all letters are set in min

print('aBcD'.capitalize())
# Abcd

print('1aBcD'.capitalize())
# 1abcd

print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())
# Alpha
# Alpha
#  alpha
# 123
# Αβγδ


### .casefold()	# Converts string into lower case IN THE WHOLE STRING

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
# hello, and welcome to my world!


### .center()	# Returns a centered string

print('Hello'.center(20, '='))
# =======Hello======== # on voit que si besoin le mot va deborder a gauche (mot impair)

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
# [Beta]
# [Beta]
# [ Beta ]


## .count()	# Returns the number of times a specified value occurs in a string

print("abcabc".count("b"))
print('abcabc'.count("d"))
# 2
# 0


## .decode() / .encode()	# Returns an decoded/encoded version of the string

txt = "My name is Ståle"
x = txt.encode()
print(x)
# b'My name is St\xc3\xa5le' 

# Le préfixe b'...' indique que c’est un objet bytes, pas une str.
# \xc3\xa5 est la représentation UTF-8 du caractère å.
# En UTF-8, å est encodé en deux octets : 0xC3 et 0xA5

# pour revenir en arrière on utilise .decode()
print(x.decode())
# My name is Ståle


### .endswith()	# Returns true if the string ends with the specified value

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
# True
# False
# False
# True


### .expandtabs()	# Sets the tab size of the string, default = 8

txt = "H\te\tl\tl\to"
x =  txt.expandtabs()
print(x)
# H      e       l       l       o
x =  txt.expandtabs(2)
print(x)
# H e l l o


### .find()	# Searches the string for a specified value and returns the position of where it was found
            # If many, CONSIDER ONLY THE FIRST

print("Emamamatata".find("ta"))
print("Eta".find("mma"))
print("Etata".find("ta"))
# 7
# -1 # Si la sous-chaîne n'existe pas, elle renvoie -1.
# 1

print('kappa'.find('a', 2))
# on commence à chercher à partir du 2ème élément
# 4

# autre exemple
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
# 15
# 80
# 198
# 221
# 238


### .format()	# Formats specified values in a string

ipadr = '10.1.1.1'
vrf = 'notaires'
ping = 'ping {} vrf {}'.format(ipadr, vrf)
print (ping)
# ping 10.1.1.1 vrf notaires


### .format_map()	# Formats specified values in a string
                    # mapping est un dictionnaire dont les clés correspondent aux noms dans les accolades

data = {"name": "Alice", "age": 30}
text = "My name is {name} and I am {age} years old."
print(text.format_map(data))
# My name is Alice and I am 30 years old.


### .index()	# Searches the string for a specified value and returns the position of where it was found
# the element searched for must occur in the sequence – its absence will cause a ValueError exception

txt = "Hello, welcome to my world."
x = txt.index("w") # avec une lettre, prendra en compte la premiere occurence de la lettre presente dans le string
print(x)
# 7

txt = "Hello, welcome to my world."
x = txt.index("welcome") # avec un mot, prendra en compte la premiere lettre du mot
print(x)
# 7


### .isalnum()	# Returns True if all characters in the string are alphanumeric: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
# True
# True
# True
# False
# False
# False


### .isalpha()	# Returns True if all characters in the string are in the ALPHABET
# SPACE is not an alphabetic character


print("Moooo".isalpha())
print('Mu40'.isalpha())
# True
# False


### .isascii()	# Returns True if all characters in the string are ascii characters
# ASCII = American Standard Code for Information Interchange

txt = "Company123"
x = txt.isascii()
print(x)
# True
txt = "#@!*Company123"
x = txt.isascii()
print(x)
# True


### .isdecimal()	# envoie True si tous les caractères de la chaîne sont des chiffres décimaux (0–9), SANS point, virgule ni signe.

txt = "1234"
x = txt.isdecimal()
print(x)
# True

txt = "1234.1"
x = txt.isdecimal()
print(x)
# False


### .isdigit()	# Returns True if all characters in the string are digits

txt = "50800"
txt2 = '135abcd'
x = txt.isdigit()
y = txt2.isdigit()
print(x)
print(y)
# True
# False

foo = ("Mary has 21 little sheep")
print (foo.split())
# ['Mary', 'has', '21', 'little', 'sheep']
print (foo.split()[2].isdigit())
# True


### .isidentifier()	# Returns True if the string is an identifier
# returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), 
# or underscores (_). A valid identifier cannot start with a number, or contain any spaces.

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
# True
# True
# False
# False


### .islower()	# Returns True if all characters in the string are lower case

s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.islower()) # True si TOUT en minuscule sinon False
print (M.islower())
print (m.islower())
# False
# False
# True

strng = '\''.join(("Mary", "had", "21", "sheep"))
print(strng)
# Mary'had'21'sheep
print(strng[0:1])
# M
print(strng[0:2])
# Ma
print(strng[0:1].islower())
# False


### .isnumeric()	# Returns True if all characters in the string are numeric

txt = "50800"
txt2 = '135abcd'
x = txt.isnumeric()
y = txt2.isnumeric()
print(x)
print(y)
# True
# False


### .isprintable()	# Returns True if all characters in the string are printable
# False s’il y a au moins un caractère non imprimable, comme : \n (saut de ligne),
# \t (tabulation), \r (retour chariot), etc.

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
# True

txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x)
# False


### .isspace()	# Returns True if all characters in the string are whitespaces

print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
# True
# True
# False


### .istitle()	# Returns True if the string follows the rules of a title
# returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters,
# otherwise False.

txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# True

txt = "hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# False


### .isupper()	# Returns True if all characters in the string are upper case

s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.isupper()) # True si TOUT en MAJUSCULE sinon False
print (M.isupper())
print (m.isupper())
# False
# True
# False


### .join()	# Converts the elements of an iterable into a string

print(",".join(["omicron", "pi", "rho"]))
# omicron,pi,rho

print("".join(["omicron", "pi", "rho"]))
# omicronpirho

print("***".join(["omicron", "pi", "rho"]))
# omicron***pi***rho

print("***".join(["1", "2", "3"]))
# 1***2***3

print ('ABC'.join(['My', 'name', 'is', 'Simon']))
# MyABCnameABCisABCSimon

print (' '.join(['My', 'name', 'is', 'Simon']))
# My name is Simon 

commands = ['conf t', 'int gi0/0', 'shut', 'no shut']
print('\n'.join(commands)) # on va sauter une ligne
# conf t
# int gi0/0
# shut
# no shut


### .ljust()	# Returns a left justified version of the string

print ('Hello'.ljust(20, '-'))
# Hello---------------


### .lower()	# Converts a string into lower case

s = "TrAvIaTa"
print (s.lower())
print (s)
# traviata
# TrAvIaTa # la variable n'est pas modifiée


### .lstrip()	# Returns a left trim version of the string

# La méthode .lstrip() sans argument supprime les espaces et autres caractères blancs
# uniquement au début (left strip) de la chaîne.
spam = '    Hello World    ' 
print (spam.lstrip())
# Hello World    # 

#lstrip("xyz") supprime tous les caractères x y et z du début de la chaîne 
print("www.cisco.com".lstrip("w."))  
# cisco.com # supprime les w et les .


### .maketrans()	# Returns a translation table to be used in translations

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
# Hello Pam!

txt = "Hi Alice! Are you excited?"
remplacements = str.maketrans(
    {"a": "@", "e": "3", "i": "1", "!": None, "?": None}
)
resultat = txt.translate(remplacements)
print(resultat)
# H1 @l1c3 Ar3 you 3xc1t3d


### .partition()	# Returns a tuple where the string is parted into three parts


### .replace()	# Returns a string where a specified value is replaced with a specified value

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# www.pythoninstitute.org

print("Apple juice".replace("juice", ""))
# Apple

var1 = float((input ("Enter a number: ")).replace(",","."))
var2 = round(var1,2)
print (var1,"rounded to 2 decimals places is",var2)
# Enter a number: 2,456
# 2.456 rounded to 2 decimals places is 2.46

# the three-parameter replace() variant uses the third argument (a number) to limit the number of replacements
print("This is it!".replace("is", "are", 1))
# Thare is it!
print("This is it!".replace("is", "are", 2))
# Thare are it!


### .rfind()	# Searches the string for a specified value and returns the LAST position of where it was found

print("tau tau tau".rfind("ta"))
# 8
print("tau tau tau".rfind("ta", 9))
# -1
print("tau tau tau".rfind("ta", 3, 9))
# 4

print("Welcome to my world.".rfind("e", 5, 10))
# Cherche la dernière occurrence de la sous-chaîne "e" entre les indices 5 (start) et 10 (end exclusif, donc 9).
# 6

print("Welcome to my world.".rfind("z", 5, 10))
# si pas d'occurence, affiche -1
# -1


### .rindex()	# Searches the string for a specified value and returns the last position of where it was found

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
# 12


### .rjust()	# Returns a right justified version of the string

print ('Hello'.rjust(20, '*')) # par defaut ' '
# ***************Hello

print ('Hello'.rjust(20))
#                Hello


### .rpartition()	# Returns a tuple where the string is parted into three parts
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# --> first element contains the part before the specified string
# --> second element contains the specified string.
# --> third element contains the part after the string.

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
# ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')


### .rsplit()	# Splits the string at the specified separator, and returns a list

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
# ['apple', 'banana', 'cherry']


### .rstrip()	# Returns a right trim version of the string

spam = '    Hello World    ' 
print (spam.rstrip())
#     Hello World


### .split()	# Splits the string at the specified separator, and returns a list

print('MyABCnameABCisABCSimon'.split('ABC'))
# ['My', 'name', 'is', 'Simon']

print("phi       chi\npsi")
# phi       chi
# psi
print("phi       chi\npsi".split())
# ['phi', 'chi', 'psi']

foo = ("Mary has 21 little sheep")
print (foo.split())
# ['Mary', 'has', '21', 'little', 'sheep']
print (foo.split()[2].isdigit())
# True


### .splitlines()	# Splits the string at line breaks and returns a list

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
# ['Thank you for the music', 'Welcome to the jungle']


### .startswith()	# Returns true if the string starts with the specified value

print("omega".startswith("meg"))
print("omega".startswith("om"))
# False
# True


### .strip()	# Returns a trimmed version of the string
# The strip() method combines the effects caused by rstrip() and lstrip() 
# – it makes a new string lacking all the leading and trailing whitespaces
spam = '    Hello World    ' 
print (spam.strip())
# Hello World#


### .swapcase()	# Swaps cases, lower case becomes upper case and vice versa

print("I know that I know nothing.".swapcase())
# i KNOW THAT i KNOW NOTHING.


### .title()	# Converts the first character of each word to upper case

print("I know that I know nothing. Part 1.".title())
# I Know That I Know Nothing. Part 1.


### .translate()	# Returns a translated string
# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
# Use the maketrans() method to create a mapping table
# If a character is not specified in the dictionary/table, the character will not be replaced
# If you use a dictionary, you must use ascii codes instead of characters

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
# Hello Pam!


### .upper()	# Converts a string into upper case

s = "TrAvIaTa"
print (s.upper())
print (s)
# TRAVIATA
# TrAvIaTa # la variable n'est pas modifiée


### .zfill()	# Fills the string with a specified number of 0 values at the beginning
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.

txt = "50"
x = txt.zfill(10)
print(x)
# 0000000050

txt = "0000000050"
x = txt.zfill(5) # 5 < len(txt) = 10
print(x)
# 0000000050 # inchangé