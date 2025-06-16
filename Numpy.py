########## Numpy ##########


https://numpy.org/doc/stable/user/whatisnumpy.html

### NumPy is the fundamental package for scientific computing in Python. 

# It is a Python library that provides a multidimensional array object, 
# various derived objects (such as masked arrays and matrices), 
# and an assortment of routines for fast operations on arrays, 
# including mathematical, logical, shape manipulation, sorting, selecting, I/O, 
# discrete Fourier transforms, basic linear algebra, basic statistical operations, 
# random simulation and much more.

# At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays
# of homogeneous data types, with many operations being performed in compiled code for performance. 
# There are several important differences between NumPy arrays and the standard Python sequences:
#       NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). 
#       Changing the size of an ndarray will create a new array and delete the original.
#       The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. 
#           The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.
#       NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. 
#           Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

# A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; 
# though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, 
# and they often output NumPy arrays. 
# In other words, in order to efficiently use much (perhaps even most) of today’s scientific/mathematical Python-based software, 
# just knowing how to use Python’s built-in sequence types is insufficient - one also needs to know how to use NumPy arrays.

# Why is NumPy fast?
# Vectorization describes the absence of any explicit looping, indexing, etc., 
# in the code - these things are taking place, of course, just “behind the scenes” in optimized, pre-compiled C code. 
# Vectorized code has many advantages, among which are:
#       vectorized code is more concise and easier to read
#       fewer lines of code generally means fewer bugs
#       the code more closely resembles standard mathematical notation (making it easier, typically, to correctly code mathematical constructs)
#       vectorization results in more “Pythonic” code. Without vectorization, our code would be littered with inefficient and difficult to read for loops.

# Rappel on peut stocker par nombre de bits --> n^2 possibilités

# An integer in Python is > 24bytes
import sys
print(sys.getsizeof(1)) 
# 28
print(sys.getsizeof(10**100)) 
# 72

# Lists are even larger
print(sys.getsizeof([1]))
# 64

# Performance is not the best 
import time
l = list(range(100000))
start = time.time()
result = sum([x ** 2 for x in l])
end = time.time()
print(f"Result: {result}")
print(f"Time taken: {end - start:.6f} seconds")
# Result: 333328333350000
# Time taken: 0.014646 seconds

# Numpy size is much smaller
import numpy as np
print(np.dtype(int).itemsize)
# 8
print(np.dtype(np.int8).itemsize)
# 1
print(np.array([1]).nbytes)
# 8

# Numpy offers more performance
import numpy as np
import time
a = np.arange(100000)
start = time.time()
result = np.sum(a ** 2)
end = time.time()
print(f"Result: {result}")
print(f"Time taken: {end - start:.6f} seconds")
# Result: 333328333350000
# Time taken: 0.001936 seconds