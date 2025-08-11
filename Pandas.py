########## PANDAS ##########

import pandas as pd



### SERIES


## create a serie

# from a list
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)
'''
0     35.467
1     63.951
2     80.940
3     60.665
4    127.061
5     64.511
6    318.523
dtype: float64
'''

# from a dictionnary

g7_pop = pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')
print(g7_pop)
'''
Canada             35.467
France             63.951
Germany            80.940
Italy              60.665
Japan             127.061
United Kingdom     64.511
United States     318.523
Name: G7 Population in millions, dtype: float64
'''

# from another serie

new_g4_pop = pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])
print(new_g4_pop)
'''
France     63.951
Germany    80.940
Italy      60.665
Spain         NaN
Name: G7 Population in millions, dtype: float64
'''


## giving a name to a serie

g7_pop.name = 'G7 Population in millions'
print(g7_pop)
'''
0     35.467
1     63.951
2     80.940
3     60.665
4    127.061
5     64.511
6    318.523
Name: G7 Population in millions, dtype: float64
'''


## print attributes from a serie

print(g7_pop.dtype)
# float64

print(g7_pop.mean()) # moyenne
# 107.30257142857144

print(g7_pop.std()) # écart type
# 97.24996987121581

print(g7_pop.values)
# [ 35.467  63.951  80.94   60.665 127.061  64.511 318.523]

print(type(g7_pop.values))
# <class 'numpy.ndarray'>



## index

# series are iterable

# ==> Un seul index : pandas retourne une Serie
#     Plusieurs indexes** : pandas retourne un DataFrame

# IMPORTANT, in PANDAS upper limits is INCLUDED


print(g7_pop[0])
# 35.467

print(g7_pop.index)
# RangeIndex(start=0, stop=7, step=1)

# in contrast to lists, we can explicitly define the index:
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

print(g7_pop)
'''
Canada             35.467
France             63.951
Germany            80.940
Italy              60.665
Japan             127.061
United Kingdom     64.511
United States     318.523
Name: G7 Population in millions, dtype: float64
'''

print(g7_pop['Canada'])
# 35.467

print(g7_pop[['Italy', 'France']])
'''
Italy     60.665
France    63.951
'''


# Numeric positions can also be used, with the "iloc" attribute

print(g7_pop.iloc[0])
# 35.467

print(g7_pop.iloc[-1])
# 318.523

print(g7_pop.iloc[[0, 1]])
'''
Canada    35.467
France    63.951
Name: G7 Population in millions, dtype: float64
'''


## slicing
# LAST index INCLUDED !!!

print(g7_pop['Canada': 'Italy'])
'''
Canada     35.467
France     63.951
Germany    80.940
Italy      60.665  # LAST index INCLUDED !!!
Name: G7 Population in millions, dtype: float64
'''


## modifying series

g7_pop['Canada'] = 40.5
print(g7_pop)
'''
Canada             40.500 # value replaced
France             63.951
Germany            80.940
Italy              60.665
Japan             127.061
United Kingdom     64.511
United States     318.523
Name: G7 Population in millions, dtype: float64
'''

g7_pop.iloc[-1] = 500
print(g7_pop)
'''
Canada             40.500
France             63.951
Germany            80.940
Italy              60.665
Japan             127.061
United Kingdom     64.511
United States     500.000 # value replaced
Name: G7 Population in millions, dtype: float64
'''

g7_pop[g7_pop < 70] = 99.99
print(g7_pop)
'''
Canada             99.990
France             99.990
Germany            80.940
Italy              99.990
Japan             127.061
United Kingdom     99.990
United States     318.523
Name: G7 Population in millions, dtype: float64
'''



### Conditional selection - boolean arrays

print(g7_pop > 70)
'''
Canada            False
France            False
Germany            True
Italy             False
Japan              True
United Kingdom    False
United States      True
Name: G7 Population in millions, dtype: bool
'''

print(g7_pop[g7_pop > 70])
'''
Germany           80.940
Japan            127.061
United States    318.523
Name: G7 Population in millions, dtype: float64
'''

print(g7_pop[g7_pop > g7_pop.mean()])
'''
Japan            127.061
United States    318.523
Name: G7 Population in millions, dtype: float64
'''

print(g7_pop[(g7_pop > 80) | (g7_pop < 40)])
'''
Canada            35.467
Germany           80.940
Japan            127.061
United States    318.523
Name: G7 Population in millions, dtype: float64
'''

print(g7_pop[(g7_pop > 80) & (g7_pop < 200)])
'''
Germany     80.940
Japan      127.061
Name: G7 Population in millions, dtype: float64
'''



### Operations and methods

print(g7_pop * 1_000_000)
'''
Canada             35467000.0
France             63951000.0
Germany            80940000.0
Italy              60665000.0
Japan             127061000.0
United Kingdom     64511000.0
United States     318523000.0
Name: G7 Population in millions, dtype: float64
'''

print(g7_pop['France': 'Italy'].mean())
# 68.51866666666666