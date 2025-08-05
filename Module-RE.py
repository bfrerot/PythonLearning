##########  RE MODULE ##########


# RE module in Python is a built-in library that provides support for regular expressions
# Regular expressions (often called regex) are patterns used to match and manipulate strings based on specific rules


# RE module is used for:
#   Searching for patterns within strings
#   Validating string formats (e.g., email, phone numbers)
#   Replacing parts of strings
#   Splitting strings based on patterns
#   Extracting specific parts of strings


## ==> Tableau des métacaractères et classes en regex
''' 
Métacaractère / Classe	Signification	Exemple / Description
.	n'importe quel caractère sauf le saut de ligne (\n)
\d	chiffre (0-9)	
\d+ : une ou plusieurs chiffres
\D	non-chiffre	\D+ : une ou plusieurs caractères non-chiffres
\w	caractère alphanumérique ou underscore (a-z, A-Z, 0-9, _)	
\w+ : un mot
\W	caractère non alphanumérique	
\W+ : séparateurs ou ponctuations
\s	espace blanc (espace, tab, saut de ligne)	
\s+ : espaces multiples
\S	caractère non-espace	
\S+ : non-espaces
[...]	classe de caractères (un seul caractère parmi ceux listés)
[^...]	classe négative (tout sauf ceux listés)	[^abc] : tout sauf a, b, c
^	début de la chaîne (ou début d’une ligne en mode multiligne)	^Bonjour : commence par "Bonjour"
$	fin de la chaîne (ou fin d’une ligne en mode multiligne)	mon$ : se termine par "mon"
*	zéro ou plusieurs répétitions	a* : zéro ou plusieurs a
+	une ou plusieurs répétitions	a+ : une ou plusieurs a
?	zéro ou une répétition (optionnel)	colou?r : color ou colour
{n}	exactement n répétitions	\d{3} : 3 chiffres consécutifs
{n,}	n ou plus répétitions	\d{2,} : au moins 2 chiffres
{n,m}	entre n et m répétitions	\d{2,4} : 2 à 4 chiffres
'''



### re.match()	
# Checks for a match only at the beginning of the string
import re

texte = "Python 3.8 est cool"
resultat = re.match(r"Python", texte) # Vérifie si le texte commence par "Python"

if resultat:
    print("Match trouvé :", resultat.group())
else:
    print("Aucun match")
# Match trouvé : Python



### re.search()	
# Searches for a pattern anywhere in the string	re.search
import re

texte = "J’aime le langage Python."
resultat = re.search(r"Python", texte) # Cherche "Python" n’importe où dans la chaîne

if resultat:
    print("Motif trouvé à la position :", resultat.start())
else:
    print("Motif non trouvé")
# Motif trouvé à la position : 18



### re.findall()	
# Finds all non-overlapping matches of a pattern in the string
import re
texte = "Il y a 3 pommes, 5 oranges et 2 bananes." 
nombres = re.findall(r"\d+", texte) # Trouver tous les chiffres dans le texte
print(nombres)  
# ['3', '5', '2']



### re.finditer()	
# Returns an iterator of match objects for all matches	
import re
texte = "Les couleurs : rouge, vert, bleu."

# Trouver toutes les couleurs (motifs après les deux points)
for match in re.finditer(r"\b\w+\b", texte):
    print("Mot trouvé :", match.group(), "à la position :", match.start())
# Mot trouvé : Les à la position : 0
# Mot trouvé : couleurs à la position : 4
# Mot trouvé : rouge à la position : 14
# Mot trouvé : vert à la position : 20
# Mot trouvé : bleu à la position : 26



### re.sub()	
# Replaces matches of a pattern with a string
import re
texte = "Je suis né en 1990, et en 2020 je suis toujours là."
nouveau_texte = re.sub(r"\d{4}", "année", texte) # Remplacer tous les années par "année"
print(nouveau_texte)  
# Je suis né en année, et en année je suis toujours là.



### re.split()	
# Splits a string by the occurrences of a pattern
import re
texte = "pomme, banane; orange|kiwi"
morceaux = re.split(r"[;,|]\s*", texte) # Diviser en utilisant la virgule, le point-virgule ou la barre verticale
print(morceaux)  
# ['pomme', 'banane', 'orange', 'kiwi']
