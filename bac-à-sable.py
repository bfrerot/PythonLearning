import numpy as np

c = np.full((2,2), 99, dtype='float')
print(c)
# [[99. 99.]
#  [99. 99.]]
d = np.full_like(c,(55,3)) # reprend c (shape & dim) = 2*rows de 2 *col avec des val définies 55 et 3
print(d)
e = np.full_like(c,4) # # reprend c (shape & dim) = 2*rows de 2 *col avec des 4 partout
print(e)
