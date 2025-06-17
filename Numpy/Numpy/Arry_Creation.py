"""
creating test arrys
predefining arry structures for large data files

"""
import numpy as np

np.array([1,2,3,4,5,6,7,8,9,10])  # crate array

print(np.zeros((2,3)))  # create  2dimentions 3 values  array of zeros

print(np.ones((3,2)))  # create 3dimentions 2 values array of ones

#print(np.empty((2,3)))

print(np.arange(0,10,2))  #(start, stop, step)Creates numbers from 0 to 10 (excluding 10) with a step of 2.

print(np.linspace(0,1,5))  #Divides the interval from 0 to 1 into 5 evenly spaced points.

print(np.logspace(0,1,5))  #Creates 5 values evenly spaced on a log scale from 10¹ to 10²

print(np.random.rand(2,3))  #creates a 2x3 matrix of random numbers

print(np.eye(3))

print(np.identity(3))

print(np.full((3,3),5))  #creates a 3x3 matrix of 5s

print(np.repeat([1,2],2))   #Repeats each element 3 times

print(np.tile([1,2],(2,3)))  #Creates a 2x3 matrix of 1s and 2s

print
