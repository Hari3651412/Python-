import numpy as np
print(np.__version__)

a=np.array([[1,2,3],[4,5,6]])
print(np.zeros((2,3)))
print(np.ones((1,3)))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
print(np.logspace(0,1,5))
print(np.random.rand(3,2))
print(np.eye(3))
print(np.repeat([1,2],2))
print(np.full((3,3),5))
print(np.tile([1,2],(2,3)))
