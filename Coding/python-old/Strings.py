########## STRINGS #########

# Immutability: on ne peut changer les itérations d'un string ex Paris --> Karis 
name = "Paris"
name[0] = 'K'
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    name = Paris
NameError: name 'Paris' is not defined

s[0] = 'x' # NOK - ON NE PEUT PAS CHANGER UNE LETTRE D'UN STRING SEULEMENT

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[0] = 'x'
TypeError: 'str' object does not support item assignment

# Guillemets
'string'
"string" --> pareil mais fera la difference si apostrophes dans la string

" I'm going on a run "
" I'm going on a run " # ok
' I'm going on a run ' # nok
SyntaxError: invalid syntax


# Concatenation
# on peut additioner des str entre elles MAIS PAS des str ET des int/float
s + ' concatenate me!' 
'hello concatenate me!'
s = s + ' concatenate me!' # on peut lui ajouter des caracteres
print("s")
hello concatenate me!



# Multiplication
letter = 'z'
L=letter*10 
print (L)
zzzzzzzzzz


# Multilignes - ''' 

multiLine = '''Line #comment1
Line '''

print(multiLine)
print(len(multiLine))
Line #comment
Line 




# Print
print ('string')
string

print ('string' 'string2') # affiche à la suite , sans espace..
stringstring2

print ('string'' ''string2') # contourne le 'probleme', l'espace est un string
string string2

print ('string \n string2') # \n pour retourner à la ligne, si espace il y aura un decalage
string 
 string2

print ('string \nstring2') # coller au string suivant pour affichage coherent
string 
string2

print ('first part \t second part') # tabulation = 2*espaces
first part 	 second part

print("I like \"Monty Python\"") # \ suivi d un signe special a ignorer qui sera traite comme un string normal
I like "Monty Python"

print('I like "Monty Python"') # toujours attention aux types de guillemets
print("I like 'Monty Python'")
I like "Monty Python"
I like 'Monty Python'


# Indexing & Slicing

s='hello'

s[0] # indexation commence à 0 --> le 1er caractere est indexé 0
'h'
s[1]
'e'
s[1:] # affiche à parir du 2nd
'ello'
s[1:3] # affiche du 1er au 2nd, le dernier n'est pas inclus
'el'
s[1:4] # affiche du 1er au 3eme
'ell'
s[:3] # ici affiche tout jusqu'au 3eme non-inclus, L'INDEXATION COMMENCE A 0
'hel'
s[:20] # affiche ET PAS D ERREUR si chiffre > au nombre réel de caractères du string
'hello'
s[14:20]
# rien à afficher mais pas d'erreur
s[-1] # recule pour afficher le dernier caractere
'o'
s[-5:-1]
'hello'
s[-5:0] # n'affiche rien car dans ce cas la boundary doit exister
# rien à afficher mais pas d'erreur
s[:-1] # affiche tout sauf le dernier caractere
'hell'
s[:] # affiche tout
'hello'
s[::1] # affiche tout
'hello'
s[::2] # affiche tout mais saute 1 sur 2 caracteres
'hlo'
s[::-1] # affiche tout mais à l'envers
'olleh'


mystring = "abcdefgijk"

mystring[2:7:2] # commence a l'indexé 2 (c), jusqu'à l'indexé 7 (mais non inclus g) et saute 1 lettre sur 2
'ceg'
mystring[0:9:3] # commence a l'indexé 0 (a), jusqu'à l'indexé 9 (mais non inclus k) et saute 1 lettre sur 3
'adg'


#  in, not in 

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" not in alphabet)
True
True


## f-strings ou formatted strings litterals - python 3.6 and above

print(name, "has", str(heads), "heads and", str(arms), "arms")
print(name + " has " + str(heads) + " heads and " + str(arms) + " arms")
f"{name} has {heads} heads and {arms} arms" # f-string

n = 3
m = 4
print (f"{n} times {m} is {n*m}")
3 times 4 is 12

# avant python 3.6 on utilise .format()

n = 3
m = 4
print ("{} has {} heads and {} arms".format(name, heads, arms))

# ou encore %

print('%(language)s has %(number)03d quote types.' %{'language': "Python", "number": 2})
Python has 002 quote types.