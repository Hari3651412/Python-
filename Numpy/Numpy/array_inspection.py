import numpy as np
"""
Understand shape, size, memory usage
Optimize data processing

optimise data processing means improving how effectively and efficiently
datA IS collectef, transformed, analyzed, and stored  . with the goal of 
reducing processing time, memory usage, and resource consuption , while 
maintaing or improving accuracy and reliability
"""
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape) # Returns the dimensions of the array

b = np.array([[1,2,3,4,5],[7,9,15,16,17]])
print(b.ndim) # Returns the number of dimensions of the array

print(b.size) # Returns the total number of elements in the array

print(b.dtype) # Returns the data type of the array elements

print(b.itemsize) # Returns the size of each array element in bytes

print(b.nbytes) # each element size = 8 bytes Returns the total number of bytes consumed by the elements of the array