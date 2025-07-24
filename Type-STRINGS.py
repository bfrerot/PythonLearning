########## STRINGS ##########

## Immutability: on ne peut changer les itérations d'un string ex Paris --> Karis 
name = "Paris"
name[0] = 'K'
# Traceback (most recent call last):
#   File "main.py", line 1, in <module>
#     name = Paris
# NameError: name 'Paris' is not defined


## Guillemets
'string'
"string" # pareil mais fera la difference si apostrophes dans la string

print("""red roses and violet roses""")
# red roses and violet roses
# Les triple guillemets """ ... """ permettent d'écrire des chaînes multilignes
# mais si tu écris une phrase sur une seule ligne à l'intérieur
# elle est affichée normalement
print("""red roses 
      
      
      
      and violet roses""")
# red roses 
# 
# 
# 
#       and violet roses

# " I'm going on a run " # ok

# ' I'm going on a run ' # nok
# SyntaxError: invalid syntax


## Concatenation
# on peut additioner des str entre elles MAIS PAS des str ET des int/float
s="hello"
print(s + ' concatenate me!')
# hello concatenate me!


## Multiplication
letter = 'z'
L=letter*10 
print (L)
# zzzzzzzzzz


## Multilignes - ''' 

texte_multiligne = """Ceci est un exemple
de chaîne de caractères
sur plusieurs lignes."""
print(texte_multiligne)
# Ceci est un exemple
# de chaîne de caractères
# sur plusieurs lignes.


## Print
print ('string')
# string

print ('string' 'string2') # SANS VIRGULE POUR SEPARER = affiche à la suite , sans espace..
# stringstring2

print ('string'' ''string2') # contourne le 'probleme', l'espace est un string
# string string2

print ('string \n string2') # \n pour retourner à la ligne, si espace il y aura un decalage
# string 
#  string2

print ('string \nstring2') # coller au string suivant pour affichage coherent
# string 
# string2

print ('first part \t second part') # tabulation = 2*espaces
# first part 	 second part

print("I like \"Monty Python\"") # \ suivi d'un signe special à ignorer qui sera traité comme un string normal
# I like "Monty Python"

print('I like "Monty Python"') # toujours attention aux types de guillemets
print("I like 'Monty Python'")
# I like "Monty Python"
# I like 'Monty Python'


## Indexing & Slicing

s='hello'

s[0] # indexation commence à 0 --> le 1er caractere est indexé 0
# h
s[1]
# e

s[1:] # affiche TOUT à parir du 2nd
# ello

s[1:3] # affiche du 1er au 2nd, LE DERNIER EST EXCLU
# el
s[1:4] # affiche du 1er au 3eme
# ell

s[:3] # ici affiche tout jusqu'au 3eme non-inclus, L'INDEXATION COMMENCE A 0
# hel
s[:20] # affiche ET PAS D ERREUR si chiffre > au nombre réel de caractères du string
# hello
s[14:20]
# = rien  mais pas d'erreur

s[-1] # recule pour afficher le dernier caractere
# o
s[-5:-1]
# hello
s[-5:0] # n'affiche rien car dans ce cas la boundary doit exister
# rien à afficher mais pas d'erreur; le premier est EGAL au second
s = "Bonjour"
print(s[-5:0])
# rien à afficher mais pas d'erreur, le premier est APRES le second

s[:-1] # affiche tout sauf le dernier caractere
# hell
s[:] # affiche tout
# hello
s[::1] # affiche tout, le 1 est par défaut
# hello
s[::2] # affiche tout mais saute 1 sur 2 caracteres
# hlo
s[::-1] # affiche tout mais à l'envers
# olleh
s[::-2] # affiche 1 character sur 2 mais à l'envers
# olh


mystring = "abcdefgijk"
mystring[2:7:2] # commence a l'indexé 2 (c), jusqu'à l'indexé 7 (mais non inclus g) et saute 1 lettre sur 2
# ceg
mystring[0:9:3] # commence a l'indexé 0 (a), jusqu'à l'indexé 9 (mais non inclus k) et saute 1 lettre sur 3
# adg


# SUMMARY

# | Expression    | Résultat  | Explication                              |
# | ------------- | --------- | ---------------------------------------- |
# | `s[1:4]`      | `'ell'`   | De `'e'` à `'l'`, sans inclure l'index 4 |
# | `s[-4:-1]`    | `'ell'`   | Même chose, avec indices négatifs        |
# | `s[:3]`       | `'hel'`   | Début jusqu’à l’index 3 (exclu)          |
# | `s[2:]`       | `'llo'`   | De l'index 2 à la fin                    |
# | `s[::-1]`     | `'olleh'` | Chaîne inversée                          |
# | `s[-1:-5:-1]` | `'olle'`  | De `'o'` vers `'e'` (ordre inverse)      |


##  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" not in alphabet)
# True
# True

# funny thing
# ==> "", empty string is a part of any string
print ("" in "nimportequ'elle string")
# True
print ("" in "")
# True


## f-strings ou formatted strings litterals - python 3.6 and above

n = 3
m = 4
print (f"{n} times {m} is {n*m}")
# 3 times 4 is 12

# AVANT PYTHON 3.6 

# on utilise .format()
n = 3
m = 4
print ("{} has {} heads and {} arms".format(name, heads, arms))

# ou encore %
print('%(language)s has %(number)03d quote types.' %{'language': "Python", "number": 2})
# Python has 002 quote types.


## Strings à partir d'une List

# on peut attribuer des valeurs à des variables à partir d'une list
# attention le nombre des variables doit corroborer le nombre d'éléments de la list

fruits = ("Apples", "Oranges", "Bananas")
a, b, c = fruits
print(b)
# Oranges

fruits = ("Apples", "Oranges", "Bananas")
a, b, c, d = fruits # d est en trop
print(b)
# Traceback (most recent call last):
#   File "c:\PythonLearning\bac-à-sable.py", line 2, in <module>
#     a, b, c, d = fruits
#     ^^^^^^^^^^
# ValueError: not enough values to unpack (expected 4, got 3)


## List à partir d'une string

first_greek_3 = sorted('omega')
print(first_greek_3)
# ['a', 'e', 'g', 'm', 'o']