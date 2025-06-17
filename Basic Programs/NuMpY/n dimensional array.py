import numpy as np
from numpy.ma.core import zeros

arr=np.array([10,20,40,50,20])
print(arr)
print(type(arr))

#2) 2 dimensional array

arr2=np.array([[1,3,2],[1,3,4]])
print(arr2)

#3)array properties
a=np.array([[1,2,3],[4,5,6]])
print(a.size)
print(a.shape)
print(a.ndim)
print(a.dtype)


#how to create arrays

print(np.zeros([2,3]))
print(np.ones([2,3]))

print(np.ones((2,3),dtype=int))
print(np.ones((2,3),dtype=float))
print(np.zeros((2,3),dtype=bool))
print(np.ones((2,4),dtype=int))

#using arange and linspace

print(np.arange(0,10,2))

print(np.linspace(0,1,5))

print(np.random.rand(2,4))

print(np.random.randint(0,100,4))
