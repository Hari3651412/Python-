"""
"Data comes in wrong shape" — Time Series Needs 2D Shape
"Preparing features for ML models" — Models Need 2D Arrays

"""
import numpy as np
a =np.array([[1, 2, 3], [4, 5, 6]])
print(a)

reshaped = a.reshape(3,2)
print(a)

#flatten() Converts array to 1D, Returns a copy

print(reshaped.flatten())

#ravel() Also makes a 1D array, But returns a view (not a copy) — so changing it may affect original

print(a.ravel())
print(a)

#transpose or .T  #Swaps rows and columns (like flipping diagonally)

print(reshaped.transpose())

print(reshaped.T)

#squeeze Remove axes with length 1 (i.e., unnecessary dimensions).
b = np.array([[[1, 2, 3], [4, 5, 6]]])
print("Original shape:", b.shape)
# Output: (1, 2, 3)

squeezed = np.squeeze(b)
print("Shape after squeeze:", squeezed.shape)
# Output: (2, 3)

#np.expand_dims()






