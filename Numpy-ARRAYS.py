########## ARRAYS ##########


import sys
import numpy as np


### Array TYPES ########################################################################################################################################################
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



### Arrays DIMENSIONS & SHAPES #########################################################################################################################################

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



### Arrays INDEXING & SLICING #######################################################################################################################################


## Square matrix
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
print(MA[1,2][0,2]) # row1 col0 = 4 , row2 col2 = 9
# [4 9]

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

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
# [[1,2,3,4,5,6,7]
#  [8,9,10,11,12,13,14]]
print(a[0,1:6:2]) # with indexing (startswith:endswithsNON-INCLUS:interval)
# [2 4 6]

a=np.array([[1,2],[3,4]],[[5,6],[7,8]])
print(a[0,1,0])
# 3
print(a[:,0,:])
# [[1 2]
#  [5 6]]

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

a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a[1,5]=20
print(a)
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 20 14]]
a[:,2]=(100,200)
print(a)
print(a)
# [[  1   2 100   4   5   6   7]
#  [  8   9 200  11  12  20  14]]

## Indexing with a list
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[0,2,-1]])
# [1 3 9]



### Array INITIALIZATION #############################################################################################################################################

## .copy()
# copy an array
# if we just do a copy, ex b = a, a and b will share the same memory set, like lists etc

a = np.array([1,2,3])
b = a 
print(b)
# [1,2,3]

# so if we change something in b, it will change in a as well
b[0] = 100
print(a)
# [100   2   3]
,
,#,,,, to avoid we use .copy()
a = np.array([1,2,3])
b = a.copy()
print(b)
# [1 2 3]
b[0] = 100
print(b)
# [100   2   3]
print(a)
# [1 2 3]


## np.arrange()
a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]


## np.zeros

#1*D
a = np.zeros(5)
print(a)
# [0. 0. 0. 0. 0.]

#2*D
a = np.zeros((2,5))
print(a)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

#3*D
a = np.zeros((2,5,3)) # 2*elem de 5 rows et 3 col
print(a)
# [[[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
# 
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]]

#4*D
a = np.zeros((2,3,4,5)) # 2*elem composés de 3*elem de 4 rows et 5 col
print(a)
# [[[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]

#   [[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]

#   [[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]]

#  [[[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]

#   [[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]

#   [[0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]
#    [0. 0. 0. 0. 0.]]]]
 
 
## np.ones
# same principles with 1s
b = np.ones((2,5))
print(a)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]


## np.x
c = np.full((2,2), 99) # shape + number, 2*rows de 2*col, que des 99
print(c)
# [[99 99]
#  [99 99]]


## np.x + dtype
b = np.ones((2,5), dtype='int8')
print(a)
# [[1 1 1 1 1]
#  [1 1 1 1 1]]

c = np.full((2,2), 99, dtype='float')
print(c)
# [[99. 99.]
#  [99. 99.]]


## np.full_like
c = np.full((2,2), 99, dtype='float')
print(c)
# [[99. 99.]
#  [99. 99.]]
d = np.full_like(c.shape,55) # reprend la shape de c = 2*rows avec des 55, on est en 1*D ici
print(d)
# [55 55]
d = np.full_like(c.shape,(55,3)) # reprend la shape de c = 2*rows avec des val définies 55 et 3
print(d)
# [55 3]
d = np.full_like(c,(55,3)) # reprend c (shape & dim) = 2*rows de 2 *col avec des val définies 55 et 3
print(d)
# [[55.  3.]
#  [55.  3.]]
e = np.full_like(c,4) # # reprend c (shape & dim) = 2*rows de 2 *col avec des 4 partout
print(e)
# [[4. 4.]
#  [4. 4.]]


## np.random.random()
# randomise des floats entre 0 et <1
# ne prend qu'1 argument: (2,3) entre () est vu comme 1 argument
# sinon TypeError: random() takes at most 1 positional argument (2 given)
c = np.random.random((2,3))
print(c)
# [[0.92185347 0.93864465 0.71607922]
#  [0.93769782 0.97632957 0.37463711]]


## np.random.rand()
# meme fonction
# inversement si on met (2,3) entre () TypeError: 'tuple' object cannot be interpreted as an integer
c = np.random.rand(2,3)
print(c)
# [[0.53049429 0.34835506 0.25564455]
#  [0.99792738 0.31898804 0.28904718]]


## np.random.random_sample()
a=np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]])
c = np.random.random_sample(a.shape)
print(c)
# [[0.15281497 0.59934954 0.16863256 0.74217746]
#  [0.31460485 0.95896923 0.24720564 0.34505195]
#  [0.82068312 0.98950176 0.44584138 0.85810591]
#  [0.70819329 0.81301291 0.50197862 0.3917888 ]]


## np.random.randint(x)
# au moins 1 parameter
f = np.random.randint(1) # choisit une int entre 0 et..rien, 1 ==> on part de 0
print(f)
# 0
f = np.random.randint(8) # choisit une int entre 0 et 8 exclu
print(f)
# 3
f = np.random.randint(8,12) # choisit une int entre 8 et 12 exclu
print(f)

f = np.random.randint(8, size=(2,3,3)) # 2*dim, 3*rows, 3*col
# [[[1 1 5]
#   [0 4 0]
#   [0 3 4]]
#  [[5 1 5]
#   [7 5 4]
#   [7 1 2]]]


## np.identity(x)
# square matrix with ones on the main diagonal and zeros elsewhere.
identity_matrix = np.identity(3)
print(identity_matrix)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


## np.repeat()
k = np.array([1,2,3])
k2 = np.repeat(k,3) 
print(k2)
# [1 1 1 2 2 2 3 3 3]
k = np.array([[1,2,3]])
k2 = np.repeat(k,3,axis=0)
print(k2)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]
k2 = np.repeat(k,3,axis=1)
print(k2)
# [[1 1 1 2 2 2 3 3 3]]



### Arrays REORGANIZATION #############################################################################################################################################

## .reshape()
# il faut qu'il y ait de la proportionnalité entre before et after
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
print(A.shape)
# (2, 4) ==> 2*4 = 8
Abis = A.reshape((8,1)) # ==> 8*1 = 8
print(Abis)
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]

Abis = A.reshape((5,2)) # ==> 5*2 = 10 NOK !!
print(Abis)
# ValueError: cannot reshape array of size 8 into shape (5,2)

Abis = A.reshape((2,2,2)) # ==> 2*2*2 = 8
print(Abis)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]


## .vstack()
# vertical stacking
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1,v2]))
# [[1 2 3 4]
#  [5 6 7 8]]
print(np.vstack([v1,v2,v2, v1,v1]))
# [[1 2 3 4]
#  [5 6 7 8]
#  [5 6 7 8]
#  [1 2 3 4]
#  [1 2 3 4]]


## .hstack()
# horizontal stacking
h1 = np.ones((2,4))
print(h1)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
h2 = np.zeros((2,2))
print(h2)
# [[0. 0.]
#  [0. 0.]]
print(np.hstack([h1,h2]))
# [[1. 1. 1. 1. 0. 0.]
#  [1. 1. 1. 1. 0. 0.]]

# h1 et h2 doivent avoir le meme nombre de rows
h1 = np.ones((2,4))
h2 = np.zeros((3,2))
print(np.hstack([h1,h2]))
# ValueError: all the input array dimensions except for the concatenation
# axis, must match exactly, but along dimension 0, 
# the array at index 0 has size 2 and the array at index 1 
# has size 3



### Arrays STATISTICS #################################################################################################################################################

## .sum()
a = np.array([1, 2, 3, 4])
print(a.sum())
# 10
print(np.sum(a))
# 10


## .min()
print(a.min())
# 1
print(np.min(a))
# 1


## .max()
print(a.max())
# 4
print(np.max(a))
# 4


## .mean()
print(a.mean())
# 2.5
print(np.mean(a))
# 2.5


## .std()
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
# √1.25 ≈ 1.118

# Résultat :
1.1180339887498949


## .var()
print(a.var()) # calcule l'écart type au carré
1.25
# Calcul de la variance :

# 1. **Calcul de la moyenne** :
(1 + 2 + 3 + 4) / 4 = 2.5

# 2. **Calcul des écarts à la moyenne au carré** :
(1 - 2.5)² = 2.25
(2 - 2.5)² = 0.25
(3 - 2.5)² = 0.25
(4 - 2.5)² = 2.25

# 3. **Calcul de la variance** :
(2.25 + 0.25 + 0.25 + 2.25) / 4 = 5/4 = 1.25

# Résultat :
1.25

# La variance est utile pour les calculs statistiques, 
# mais l'écart-type est souvent plus facile à interpréter car il est 
# dans la même unité que les données originales.


## avec les matrices..

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

print(np.mean(A))
# 5.0
print(np.mean(A, axis=0))
# [4. 5. 6.]
print(np.mean(A, axis=0))
# [2. 5. 8.]

print(np.min(A, axis=0)) # pour chaque collone, donne le min
# [1 2 3]
print(np.min(A, axis=1)) # pour chaque rangée, donne le min
# [1 4 2]
print(np.max(A, axis=0)) # pour chaque collone, donne le max
# [7 8 9]
print(np.max(A, axis=1)) # pour chaque rangée, donne le max
# [8 6 9]

print(A.std())
2.581988897471611
print(A.std(axis=0))
[2.44948974, 2.44948974, 2.44948974]
print(A.std(axis=1))
[0.81649658, 0.81649658, 0.81649658]



### Arrays MATHEMATICs & BROADCASTING & VECTORIZED OPERATIONS #########################################################################################################

## array + - * / int

a = np.array([0,1,2,3])
print(a+2)
# [2 3 4 5]
print(a-2)
# [-2 -1  0  1]
print(a*2)
# [0 2 4 6]
print(a/2) # si  on veut de l'int il faut mettre //
# [0.  0.5 1.  1.5]


## array + - * / float

a = np.array([0,1,2,3])
print(a+2.)
# [2. 3. 4. 5.]
print(a-2.)
# [-2. -1.  0.  1.]
print(a*2.)
# [0. 2. 4. 6.]
print(a/2.)
# [0.  0.5 1.  1.5]
print(a**2)
# [ 0  1  4  9 16]


## sin
print(np.sin(a))
# [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025 ]


## cos
print(np.cos(a))
# [ 1.          0.54030231 -0.41614684 -0.9899925  -0.65364362]


## changer la valeur de l'array
print(a+10)
# [10 11 12 13 14 15 16 17 18 19] # ne change pas la valeur de a
print(a)
# [0 1 2 3 4 5 6 7 8 9] 
a =a + 4
print(a)
# [ 4  5  6  7  8  9 10 11 12 13] # change la valeur de a


## opérations entre arrays
a = np.array([0,1,2,3,4])
print(a)
# [0 1 2 3 4]
b = np.array([10,20,30,40,50])
print(b)
# [10 20 30 40 50]

print(a+b)
# [10 21 32 43 54]

print(a*b)
# [  0  20  60 120 200]

print(a/b)
# [0.         0.05       0.06666667 0.075      0.08      ]


## CAS DE LA DIVISION PAR 0

print(b/a)
# RuntimeWarning: divide by zero encountered in divide
#   print(b/a)
#[        inf 20.         15.         13.33333333 12.5       ] # ici inf = infini

# pour contourner, plusieurs possibilité
# 1 - ignorer le warning et ne pas l'afficher
np.seterr(divide='ignore')  # Ignore les avertissements de division par zéro
print(b/a)
# [        inf 20.         15.         13.33333333 12.5       ] # sans message de warning

# 2 - on définit en plus une valeur résultat en cas de division par 0
result = b / a
result[np.isinf(result)] = 0  # Remplacer inf par 0, par exemple
print(result)
# [ 0.         20.         15.         13.33333333 12.5       ]


## Arrays LINEAR ALGEBRA between matrixes

# On DOIT avoir autant de col en a que de row en b
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

# multiplication matricielle
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

# A.dot(B)
print(A.dot(B)) # .dot() = multiplication matricielle
# [[20 14]
#  [56 41]
#  [92 68]]

# .matmul()
p = np.matmul(A,B)
print(p)
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



### Arrays BOOLEAN #################################################################################################################################################### 

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

filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)
# [[  1.  13.  21.  11. 196.  75.   4.   3.  34.   6.   7.   8.   0.   1.   2.   3.   4.   5.]
#  [  3.  42.  12.  33. 766.  75.   4.  55.   6.   4.   3.   4.   5.   6.   7.   0.  11.  12.]
#  [  1.  22.  33.  11. 999.  11.   2.   1.  78.   0.   1.   2.   9.   8.   7.   1.  76.  88.]]
print(np.any(filedata >50, axis=0))  # on regarde dans chaque colonne si on a un check positif
# [False False False False  True  True False  True  True False False False False False False False  True  True]
print(np.any((filedata >50) & (filedata <100), axis=0)) 
# [False False False False False  True False  True  True False False False False False False False  True  True]
print(~(np.any((filedata >50) & (filedata <100), axis=0))) # ~ = NOT
# [ True  True  True  True  True False  True False False  True  True  True True  True  True  True False False]
print(np.all(filedata >50, axis=0))
# [False False False False  True False False False False False False False False False False False False False]





### DIVERS / MISCELLANEOUS ###########################################################################################################################################

## .genfromtxt()

filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)
# [[  1.  13.  21.  11. 196.  75.   4.   3.  34.   6.   7.   8.   0.   1.
#     2.   3.   4.   5.]
#  [  3.  42.  12.  33. 766.  75.   4.  55.   6.   4.   3.   4.   5.   6.
#     7.   0.  11.  12.]
#  [  1.  22.  33.  11. 999.  11.   2.   1.  78.   0.   1.   2.   9.   8.
#     7.   1.  76.  88.]]

# si on veut changer le type en int
print(filedata.astype('int'))
# [[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
#  [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
#  [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]


