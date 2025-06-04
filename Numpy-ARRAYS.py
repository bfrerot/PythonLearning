########## ARRAYS ##########


import sys
import numpy as np

### Array TYPES
# Tous les éléments doivent être du même type (int, float, etc.)
# Plus efficace en mémoire que les listes Python

a = np.array([1, 2, 3, 4])
print(a.dtype)
# int64

b = np.array([0, .5, 1, 1.5, 2])
print(b.dtype)
# float64 --> si mélange de int et float, l'arrray retient le float pour tous les éléments

c = np.array(['a', 'b', 'c'])
print(c.dtype)
# <U1

d = np.array([{'a': 1}, sys])
print(d.dtype)
# object --> signifie qu'il stocke des références vers des objets Python plutôt que des données numériques
# NON RECOMMANDE

z = np.array(['a', 1, 2.5, [1,2,3]]) # pas homogène --> ValueError
print(z.dtype)
# ValueError: setting an array element with a sequence. The requested array has an 
# inhomogeneous shape after 1 dimensions. The detected shape was (4,) + inhomogeneous part.


### Arrays DIMENSIONS & SHAPES

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])

C = np.array([
    [
        [12, 11, 10],
        [9, 8, 7],
    ],
    [       
        [6, 5, 4]
    ]
])

## .shape
print(A.shape)
# (2, 3) --> 2 rangées horizontales , 3 colonnes vericales
print(B.shape)
# (2, 2, 3) --> 2?,  2 rangées horizontales , 3 colonnes vericales
print(C.shape)
# (2,) --> # If the shape isn't consistent, it'll just fall back to regular Python objects

## .ndim
print(A.ndim)
# 2 --> 2 dimensions : 1st = [1,2,3] + 2nd = [4,5,6]
print(B.ndim)
# 3
print(C.ndim)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. 
# The detected shape was (2,) + inhomogeneous part.

## .size
print(A.size)
# 6 --> 6 éléments : 1,2,3,4,5 et 6
print(B.size)
# 12
print(C.size)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. 
# The detected shape was (2,) + inhomogeneous part.


### Arrays INDEXING & SLICING

# Square matrix
MA = np.array([
#    0. 1. 2
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
])

print(MA[1])
# [4,5,6]

print(MA[1][0]) # ou print([1,0])
# 4

print(MA[0:2])
# [[1, 2, 3],
#  [4, 5, 6]]

print(MA[:, :2])
# [[1 2]
#  [4 5]
#  [7 8]]

print(MA[:2, :2])
# [[1 2]
#  [4 5]]

print(MA[:2, 2:])
# [[3]
#  [6]]
























2. Performance optimisée


Opérations vectorisées (calculs sur tout l'array en une fois)

Implémentation en C, donc beaucoup plus rapide pour les calculs mathématiques


3. Multi-dimensionnel


Supporte les tableaux 1D, 2D, 3D, etc.

Forme définie par l'attribut shape


4. Taille fixe


Une fois créé, la taille ne peut pas changer (pas d'append/remove)



Comparaison avec les autres structures

Critère	Array NumPy	Liste	Tuple	Dictionnaire
Type de données	Homogène	Hétérogène	Hétérogène	Clé-valeur
Mutabilité	Modifiable*	Modifiable	Immutable	Modifiable
Performance calculs	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐	⭐
Mémoire	Très efficace	Moins efficace	Efficace	Variable
Multi-dimensionnel	✅ Natif	❌ (listes imbriquées)	❌	❌
Indexation	Par position	Par position	Par position	Par clé
Opérations mathématiques	✅ Intégrées	❌ Manuel	❌ Manuel	❌

*Contenu modifiable, taille fixe

