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

MA[1] = np.array([10, 10, 10]) # --> remplace toute les valeurs de la ligne en précisant chaque valeur
print(MA)
# [[ 1,  2,  3],
#  [10, 10, 10],
#  [ 7,  8,  9]]

MA[2] = 99
print(MA)
# [[ 1,  2,  3],
#  [10, 10, 10],
#  [99, 99, 99]]  --> remplace toute les valeurs de la ligne

MA[1] = np.array([10, 9]) # --> si on met un nombre de valeurs autre 1 ou le nombre exact --> VelueError
print(MA)
# ValueError: could not broadcast input array from shape (2,) into shape (3,)



### Arrays STATISTICS

a = np.array([1, 2, 3, 4])
print(a.sum())
10

print(a.mean())
2.5

print(a.std()) # calcule l'écart-type (standard deviation) des éléments du tableau
1.118033988749895
# 1. **Calcul de la moyenne** :
(1 + 2 + 3 + 4) / 4 = 10/4 = 2.5

# 2. **Calcul des écarts à la moyenne au carré** :
(1 - 2.5)² = (-1.5)² = 2.25
(2 - 2.5)² = (-0.5)² = 0.25
(3 - 2.5)² = (0.5)² = 0.25
(4 - 2.5)² = (1.5)² = 2.25

# 3. **Calcul de la variance** :
(2.25 + 0.25 + 0.25 + 2.25) / 4 = 5/4 = 1.25

# 4. **Calcul de l'écart-type** :
√1.25 ≈ 1.118

## Résultat :
1.1180339887498949

print(a.var()) # calcule l'écart type au carré
1.25
## Calcul de la variance :

# 1. **Calcul de la moyenne** :
(1 + 2 + 3 + 4) / 4 = 2.5

# 2. **Calcul des écarts à la moyenne au carré** :
(1 - 2.5)² = 2.25
(2 - 2.5)² = 0.25
(3 - 2.5)² = 0.25
(4 - 2.5)² = 2.25

# 3. **Calcul de la variance** :
(2.25 + 0.25 + 0.25 + 2.25) / 4 = 5/4 = 1.25

## Résultat :
1.25

# La variance est utile pour les calculs statistiques, 
# mais l'écart-type est souvent plus facile à interpréter car il est 
# dans la même unité que les données originales.

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print (A.sum())
45
print(A.sum(axis=0)) # 0 = lignes, vertical
[12, 15, 18]
print(A.sum(axis=1)) # 1 = colonnes, horizontal
[6, 15, 24]

print(A.mean())
5
print(A.mean(axis=0))
[4., 5., 6.]
print(A.mean(axis=1))
[2., 5., 8.]

print(A.std())
2.581988897471611
print(A.std(axis=0))
[2.44948974, 2.44948974, 2.44948974]
print(A.std(axis=1))
[0.81649658, 0.81649658, 0.81649658]



### Arrays BROADCASTING & VECTORIZED OPERATIONS

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]
print(a+10)
# [10 11 12 13 14 15 16 17 18 19] # ne change pas la valeur de a
print(a)
# [0 1 2 3 4 5 6 7 8 9] 
a =a + 4
print(a)
# [ 4  5  6  7  8  9 10 11 12 13] # change la valeur de a

a = np.arange(4)
print(a)
# [0,1,2,3]
b = np.arange([10,10,10,10])
print(b)
# [10,10,10,10]
print(a+b)
[10, 11, 12, 13]
print(a*b)
[ 0, 10, 20, 30]



### Arrays BOOLEAN 

a = np.arange(4)
print(a)
[0,1,2,3]

print(a[0],a[-1])
# 0 3

print(a[[0,-1]])
# [0 3]

print(a[[True, False, False, True]]) # True = selectionne vs False = ignore
# [0 3]

print(a >= 2)
# [False, False,  True,  True]

print(a[a >= 2])
# [2, 3]

print(a[a > a.mean()]) # a.mean() = 1.5
# [2, 3]

print(a[~(a > a.mean())]) # ~ = inverse de 
# [0, 1]

print(a[(a == 0) | (a == 1)])
# [0, 1]

print(a[(a <= 2) & (a % 2 == 0)])
# [0, 2]

A = np.random.randint(100, size=(3, 3)) # génère 3 lignes de 3 colonnes avec des nombres de 0 à 99
print(A)
# [[12 40 67]
#  [61  8 29]
#  [77  0 83]]

print(A[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
])])
# [12, 67, 8, 77, 83]

print(A<30)
# [[False  True  True]
#  [ True False False]
#  [True False  True]]

print(A[A > 30])
# [40, 67, 61, 77, 83]



### Arrays LINEAR ALGEBRA

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

print(A.dot(B)) # .dot() = multiplication matricielle
# Calcul de l'élément [0,0] (première ligne de A, première colonne de B)
(1*6) + (2*4) + (3*2) = 6 + 8 + 6 = 20
# Calcul de l'élément [0,0] (première ligne de A, deuxième colonne de B)
(1*5) + (2*3) + (3*1) = 5 + 6 + 3 = 14
# Calcul de l'élément [0,0] (deuxième ligne de A, première colonne de B)
(4*6) + (5*4) + (6*2) = 24 + 20 + 12 = 56
# Calcul de l'élément [0,0] (deuxième ligne de A, deuxième colonne de B)
(4*5) + (5*3) + (6*1) = 20 + 15 + 6 = 41
# Calcul de l'élément [2,0] (troisième ligne de A, première colonne de B)
(7*6) + (8*4) + (9*2) = 42 + 32 + 18 = 92
# Calcul de l'élément [2,1] (troisième ligne de A, deuxième colonne de B)
(7*5) + (8*3) + (9*1) = 35 + 24 + 9 = 68
# [[20 14]
#  [56 41]
#  [92 68]]

print(A@B) # = multiplication
# [[20 14]
#  [56 41]
#  [92 68]]

print(B.T) # .T transpose lines in colonns and reversely
# [[20 56 92]
#  [14 41 68]]

print(B.T @ A)
# [[36, 48 , 60]
#   [24, 33, 42]]


















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

