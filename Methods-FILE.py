########## METHOD FILES ##########



### close()
# Ferme le fichier

f = open('exemple.txt', 'w')
f.write('Bonjour')
f.close()  # Fermeture du fichier



### detach()
# Sépare le flux brut (stream) du buffer (utile avec certains types de fichiers, notamment avec io.BufferedWriter)

import io
buffer = io.BytesIO(b"donnees binaires")
raw_stream = buffer.detach()  # Sépare le flux brut



### fileno()
# Donne le numéro du fichier selon le système d'exploitation.

f = open('exemple.txt', 'r')
print(f.fileno())  # Affiche le numéro du fichier
# 3
f.close()



### flush()
# Vérifie que tout est écrit dans le fichier (force l'écriture).

f = open('exemple.txt', 'w')
f.write('Texte')
f.flush()  # Force l'écriture dans le fichier avent le close()
f.close()



### isatty()
# Vérifie si le flux est interactif (typiquement si c'est le terminal)

import sys
print(sys.stdin.isatty())  # True si le terminal est interactif
# True



### read()
# Lit tout le contenu du fichier

f = open('exemple.txt', 'r')
contenu = f.read()
print(contenu)
# Texte
f.close()



### readable()
# Vérifie si le fichier peut être lu.

f = open('exemple.txt', 'r')
print(f.readable())  
# True
f.close()



### readline()
# Lit une ligne à la fois.

f = open('exemple.txt', 'r')
ligne = f.readline()
print(ligne)
# Ligne1
#
f.close()



### readlines()
# Lit toutes les lignes dans une liste.

f = open('exemple.txt', 'r')
lignes = f.readlines()
print(lignes)
# ['Ligne1\n', 'Ligne2\n', 'Ligne3\n', 'Ligne4']
f.close()



### seek(INT)
# Change la position de lecture/écriture dans le fichier.

# exemple.txt AVANT
'''Ligne1
Ligne2
Ligne3
Ligne4'''

f = open('exemple.txt', 'r+')
f.seek(0)  # Retour au 1er caractère
f.write('Bonjour Madame') # Ecrase ne s'inclut pas
f.close()

# exemple.txt APRES
'''Bonjour Madame
Ligne3
Ligne4'''



### seekable()
# Vérifie si le fichier permet de changer la position

f = open('exemple.txt', 'r')
print(f.seekable())  
# True
f.close()



### tell()
# Donne la position actuelle dans le fichier

f = open('exemple.txt', 'r')
print(f.tell())  
# 0 au début
f.read(5)
print(f.tell())  
# 5 == > Position après lecture
f.close()



### truncate()
# Redimensionne le fichier à une taille donnée

# exemple.txt AVANT
'''Ligne1
Ligne2
Ligne3
Ligne4'''

f = open('exemple.txt', 'w')
f.write('12345678') # écrase et met '12345678'

# exemple.txt
'''12345678'''

f.truncate(5)  # Garde seulement '12345'
f.close()

# exemple.txt APRES
'''12345'''



### writable()
# Vérifie si le fichier peut être écrit

f = open('exemple.txt', 'w')
print(f.writable())  
# True
f.close()



### write()
# Écrit une chaîne dans le fichier

f = open('exemple.txt', 'w')
f.write('Bonjour')
f.close()



### writelines()
# Écrit une liste de chaînes dans le fichier

f = open('exemple.txt', 'w')
f.writelines(['Ligne 1\n', 'Ligne 2\n', 'Ligne 3\n'])
f.close()

# exemple.txt APRES
'''Ligne 1
Ligne 2
Ligne 3'''