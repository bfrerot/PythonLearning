########## Methods STRING ##########


### .capitalize()	
# Converts the FIRST character to upper case AND all others in lower case
# when first value is a letter set the first letter as Cap, others in min
# if first value is number, or space, all letters are set in min

print('aBcD'.capitalize())
# Abcd
print('1aBcD'.capitalize())
# 1abcd
print("Alpha".capitalize())
# Alpha
print('ALPHA'.capitalize())
# Alpha
print(' Alpha'.capitalize()) # espace en premier
#  alpha
print('123'.capitalize())
# 123
print("αβγδ".capitalize())
# Αβγδ



### .casefold()	
# Converts string into lower case

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
# hello, and welcome to my world!



### .center()	
# Returns a centered string

print('Hello'.center(20, '='))
# =======Hello======== # on voit que si besoin le mot va deborder a gauche (mot impair)

# on peut center sur moins que la taille du string sans erreur
print('[' + 'Beta'.center(2) + ']')
# [Beta]
print('[' + 'Beta'.center(4) + ']')
# [Beta]
print('[' + 'Beta'.center(6) + ']')
# [ Beta ]



## .count("x", index)	
# Returns the number of times a specified value occurs in a string, with option to start from an index

print("abcabc".count("b"))
# 2
print('abcabc'.count("d"))
# 0

data = 'abbabadaadbbaccabc'
print(data.count('ab', 1)) #on  commence à b , le 2ème caractère, index 1
# 2



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



### .endswith()	
# Returns true if the string ends with the specified value

t = "zeta"
print(t.endswith("a"))
# True
print(t.endswith("A"))
# False
print(t.endswith("et"))
# False
print(t.endswith("eta"))
# True



### .expandtabs()	
# Sets the tab size of the string, default = 8
txt = "H\te\tl\tl\to"
print(txt)
# H       e       l       l       o
x =  txt.expandtabs()
print(x)
# H       e       l       l       o
x =  txt.expandtabs(2)
print(x)
# H e l l o
x =  txt.expandtabs(0)
print(x)
# Hello



### .find("x", index)	
# Searches the string for a specified value and returns the position of where it was found first
print("Emamamatata".find("ta"))
# 7
print("Eta".find("mma"))
# -1 # Si la sous-chaîne n'existe pas, elle renvoie -1.
print("Etata".find("ta"))
# 1

print('kappa'.find('a', 2))
# on commence à chercher à partir du 2ème élément
# 4



### .format()	
# Formats specified values in a string
ipadr = '10.1.1.1'
vrf = 'notaires'
ping = 'ping {} vrf {}'.format(ipadr, vrf)
print (ping)
# ping 10.1.1.1 vrf notaires



### .format_map()	
# Formats specified values in a string
# mapping est un dictionnaire dont les clés correspondent aux noms dans les accolades
data = {"name": "Alice", "age": 30}
text = "My name is {name} and I am {age} years old."
print(text.format_map(data))
# My name is Alice and I am 30 years old.



### .index()	
# Searches the string for a specified value and returns the position of where it was found
# the element searched for must occur in the sequence – its absence will cause a ValueError exception
txt = "Hello, welcome to my world."
x = txt.index("w") # avec une lettre, prendra en compte la premiere occurence de la lettre presente dans le string
print(x)
# 7

txt = "Hello, welcome to my world."
x = txt.index("welcome") # avec un mot, prendra en compte la premiere lettre du mot
print(x)
# 7



### .isalnum()	
# Returns True if all characters in the string are alphanumeric: ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

print('lambda30'.isalnum())
# True
print('lambda'.isalnum())
# True
print('30'.isalnum())
# True
print('@'.isalnum())
# False
print('lambda_30'.isalnum())
# False
print(''.isalnum())
# False
print(' '.isalnum())
# False



### .isalpha()	
# Returns True if all characters in the string are in the ALPHABET
# SPACE is not an alphabetic character
print("Moooo".isalpha())
# True
print('Mu40'.isalpha())
# False



### .isascii()	
# Returns True if all characters in the string are ascii characters
# ASCII = American Standard Code for Information Interchange
txt = "Company123"
x = txt.isascii()
print(x)
# True
txt = "#@!*Company123"
x = txt.isascii()
print(x)
# True



### .isdecimal()	
# envoie True si tous les caractères de la chaîne sont des chiffres décimaux (0–9), SANS point ni virgule ni signe
txt = "1234"
x = txt.isdecimal()
print(x)
# True
txt = "1234.1"
x = txt.isdecimal()
print(x)
# False



### .isdigit()	
# Returns True if all characters in the string are digits

txt = "50800"
txt2 = '135abcd'
x = txt.isdigit()
y = txt2.isdigit()
print(x)
# True
print(y)
# False

foo = ("Mary has 21 little sheep")
print (foo.split())
# ['Mary', 'has', '21', 'little', 'sheep']
print (foo.split()[2].isdigit())
# True



### .isidentifier()	
# returns True if the string is a valid identifier, otherwise False
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_) 
# A valid identifier cannot start with a number, or contain any spaces
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
# True
print(b.isidentifier())
# True
print(c.isidentifier())
# False
print(d.isidentifier())
# False



### .islower()	
# Returns True if all characters in the string are lower case
s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.islower()) 
# False
print (M.islower())
# False
print (m.islower())
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



### .isnumeric()	
# Returns True if all characters in the string are numeric
txt = "50800"
txt2 = '135abcd'
x = txt.isnumeric()
y = txt2.isnumeric()
print(x)
# True
print(y)
# False



### .isprintable()	
# Returns True if all characters in the string are printable
# False s’il y a au moins un caractère non imprimable, comme : \n (saut de ligne), \t (tabulation), \r (retour chariot), etc.
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
# True
print(" ".isspace())
# True
print("mooo mooo mooo".isspace())
# False



### .istitle()	
# Returns True if the string follows the rules of a title: if all words in a text start with a upper case letter AND the rest of the word are lower case letters
# otherwise False
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# True
txt = "hello, And Welcome To My World!"
x = txt.istitle()
print(x)
# False



### .isupper()	
# Returns True if all characters in the string are upper case
s = "TrAvIaTa"
M = "MAJUSCULE"
m = "minuscule"
print (s.isupper()) 
# False
print (M.isupper())
# True
print (m.isupper())
# False



### .join()	
# Converts the elements of an iterable into a string
print(",".join(["omicron", "pi", "rho"]))
# omicron,pi,rho

print("".join(["omicron", "pi", "rho"]))
# omicronpirho

print("***".join(["omicron", "pi", "rho"]))
# omicron***pi***rho

print ('ABC'.join(['My', 'name', 'is', 'Simon']))
# MyABCnameABCisABCSimon

print (' '.join(['My', 'name', 'is', 'Simon']))
# My name is Simon 

the_string = ',,'.join({'alpha', 'omega'}) # ici l'iterable est un set
print(the_string)
# alpha,,omega



### .ljust(int, value)	
# Returns a left justified version of the string
print ('Hello'.ljust(20, '-'))
# Hello---------------



### .lower()	
# Converts a string into lower case
s = "TrAvIaTa"
print (s.lower())
# traviata



### .lstrip()	
# Returns a left trim version of the string

# La méthode .lstrip() sans argument supprime les espaces et autres caractères blancs
# uniquement au début (left strip) de la chaîne.
spam = '    Hello World    ' 
print (spam.lstrip())
# Hello World    # 

# .lstrip("xyz") supprime tous les caractères x y et z du début de la chaîne 
print("www.cisco.com".lstrip("w."))  
# cisco.com # supprime w. et TOUT ce qui est à gauche MAIS que la première occurence
print("www.cisco.com.www.".lstrip("w."))  
# cisco.com.www.



### .maketrans()	
# Returns a translation table to be used in translations

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



### .partition(sep)	
# coupe la chaîne au tout premier séparateur sep et retourne un tuple de trois éléments: (avant, sep, après)
s = "user:age:location"
print(s.partition(":"))
# ('user', ':', 'age:location')
s = "PasDeSeparateur"
print(s.partition(":"))
# ('PasDeSeparateur', '', '')
s = "clé=valeur=autre"
print(s.partition("="))
# ('clé', '=', 'valeur=autre')



### .replace(avant,après,nbre de rempacements)	
# Returns a string where a specified value is replaced with a specified value

print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# www.pythoninstitute.org

print("Apple juice".replace("juice", ""))
# Apple

# the three-parameter replace() variant uses the third argument (a number) to limit the number of replacements
print("This is it!".replace("is", "are", 1))
# Thare is it!
print("This is it!This is it!This is it!".replace("is", "are", 2))
# Thare are it!This is it!This is it!
print("This is it!This is it!This is it!".replace("is", "are", 4))
# Thare are it!Thare are it!This is it!



### .rfind(value,start,end exclu)	
# Searches the string for a specified value and returns the LAST position of where it was found

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



### .rindex()	
# Searches the string for a specified value and returns the last position of where it was found

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
# 12



### .rjust()	
# Returns a right justified version of the string avec par defaut ' '

print ('Hello'.rjust(20, '*'))
# ***************Hello

print ('Hello'.rjust(20))
#                Hello



### .rpartition()	
# Returns a tuple where the string is parted into three parts
# The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.
# --> first element contains the part before the specified string
# --> second element contains the specified string.
# --> third element contains the part after the string.

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
# ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')



### .rsplit()	
# Splits the string at the specified separator, and returns a list

txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
# ['apple', 'banana', 'cherry']



### .rstrip()	# Returns a right trim version of the string

spam = '    Hello World    ' 
print (spam.rstrip())
#     Hello World



### .split()	
# Splits the string at the specified separator, and returns a list

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



### .splitlines()	
# Splits the string at line breaks and returns a list

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
# ['Thank you for the music', 'Welcome to the jungle']



### .startswith()	
# Returns true if the string starts with the specified value

print("omega".startswith("meg"))
# False
print("omega".startswith("om"))
# True



### .strip()	
# Returns a trimmed version of the string
# The strip() method combines the effects caused by rstrip() and lstrip() 
# – it makes a new string lacking all the leading and trailing whitespaces
spam = '    Hello World    ' 
print (spam.strip())
# Hello World#



### .swapcase()	
# Swaps cases, lower case becomes upper case and vice versa
print("I know that I know nothing.".swapcase())
# i KNOW THAT i KNOW NOTHING.



### .title()	
# Converts the first character of each word to upper case
print("I know that I know nothing. Part 1.".title())
# I Know That I Know Nothing. Part 1.


### .translate()	
# Returns a translated string
# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
# Use the maketrans() method to create a mapping table
# If a character is not specified in the dictionary/table, the character will not be replaced
# If you use a dictionary, you must use ascii codes instead of characters

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
# Hello Pam!



### .upper()	
# Converts a string into upper case

s = "TrAvIaTa"
print (s.upper())
print (s)
# TRAVIATA
# TrAvIaTa # la variable n'est pas modifiée



### .zfill()	
# Fills the string with a specified number of 0 values at the beginning
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