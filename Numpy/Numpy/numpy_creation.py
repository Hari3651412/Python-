#What is numpy(Numarical Python)
#it is open source python library
#user for:
 # > numarical computations
 # > Large data handling
 # > Matrix opertaions
 # > Linear algebra, statastics, and more

# why Do Data Analysts Use NumPy
# for fast performence
# Memory efficient
# procewsses entire arrys without loops
# Great for numerical analysis, data transformation, pre processing


#1) N- Dimentional arry

import numpy as np

arr = np.array([1,10,20,50,100])
print(arr)
print(type(arr))

#2) 2D arrar

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(type(arr2))

# NUmpy array properties
a = np.array([[1,2,3],[4,5,6]])
print(a.shape) # output:(2,3)   ->2 rows 3 columns
print(a.ndim)  # output:2  --> dimentions
print(a.size)  # output:6  --> total elements
print(a.dtype) # output:int64 --> data type

# Creating arrays

print(np.zeros((2,3))) # 2 is dimention , and 3 is total elements

print(np.ones((3,2)))

print(np.zeros((2,2),dtype=int))

print(np.ones((2,3),dtype=float))

print(np.ones((2,3),dtype=bool))


#Using arange and linspace

print(np.arange(0,10,2))  #(start,stop,step)
"""
start = 0
stop = 10(exclusive)
step = 2(how many steps)"""

print(np.linspace(0,1,5)) #(start,stop,number of elements)

"""
start = 0
stop = 1(inclusive - includes 1)
step = 5(how many steps)
"""
# random numbers
#generates a 2x3 matrix of random numbers
print(np.random.rand(2,3))

print(np.random.randint(0,100,size=(2,3)))
"""
low = 0
high = 100
size = (2,3)
"""

