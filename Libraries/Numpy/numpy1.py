# NUMPY NOTES
import numpy as np
import time
import sys

# One dimensional array
a = np.array([1, 2, 3])
print(a)

# Two dimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Numpy Arrays are greatly superior to the usual python lists. They consume less memory, are fast and flexible
# Memory difference can be observed here
s = [x for x in range(1000)]
print(sys.getsizeof(s[0])*len(s))  # Storage required by a list - 12000
arr = np.arange(1000)
print(arr.size*arr.itemsize)  # Storage required by numpy array - 4000

# Shape of an array - rows and columns
c = np.array([[1, 5, 7], [4, 8, 9]])
print(c.shape)  # Prints out a tuple of rows and columns (2, 3)

# Reshape an array - (rows x columns) -> (columns x rows)
d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
d_modified = d.reshape(4, 2)
print(d_modified)  #[[1, 2], [3, 4], [5, 6], [7, 8]]

# Slicing
print(d[0, 2])  # 0th row, 3rd element
print(d[0:, 2])  # All rows starting from 0 and their respective 3rd elements

e = np.linspace(1, 3, 5)
print(e)  # Prints out five equally spaced numbers between 1 and 3 (both included)

# Basic Math
f = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.sum(f))
print(np.sum(f, axis=0))  # 0 is columns and 1 is rows
print(np.mean(f))
print(np.median(f))
print(np.std(f))  # Standard deviation
# Numpy performs element wise operations when we do +, -, *, / on two numpy arrays
# To concatenate two arrays we can use np.vstack() and np.hstack() and concatenate horizantally or vertically

print(np.arange(1, 10, 2))  # arange(start, stop, steps) -> [1, 3, 5, 7, 9]
# arange doesn't take upper limit (10) into consideration

print(np.linspace(1, 10, 4))  #linspace(start, stop, N) -> [1, 4, 7, 10]
# It roughly translates to 'Give me an array with N evenly spcaed numbers between 1 and 10(inclusive).

g = np.arange(12)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
gs = g.reshape(3, 4)  #[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]


