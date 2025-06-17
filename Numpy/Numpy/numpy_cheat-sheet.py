# numpy_cheatsheet.py

import numpy_creation as np

print("----- 1. ARRAY CREATION -----")
a = np.array([1, 2, 3])
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
empty = np.empty((2, 2))
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
eye = np.eye(3)
full = np.full((2, 2), 7)

print("Array:", a)
print("Zeros:\n", zeros)
print("Linspace:", linspace)

print("\n----- 2. ARRAY SHAPE & INSPECTION -----")
print("Shape:", a.shape)
print("Size:", a.size)
print("Dim:", a.ndim)
print("Dtype:", a.dtype)

print("\n----- 3. RESHAPING & FLATTENING -----")
b = np.arange(12).reshape((3, 4))
print("Reshaped:\n", b)
print("Flattened:", b.flatten())
print("Transposed:\n", b.T)

print("\n----- 4. INDEXING & SLICING -----")
print("b[1,2]:", b[1,2])
print("Slice:\n", b[:, 1:3])

print("\n----- 5. BOOLEAN MASKING -----")
c = np.array([10, 20, 30, 40])
print("Mask > 25:", c[c > 25])

print("\n----- 6. AGGREGATION FUNCTIONS -----")
d = np.array([[1, 2], [3, 4]])
print("Sum:", np.sum(d))
print("Mean:", np.mean(d))
print("Median:", np.median(d))
print("Std:", np.std(d))
print("Sum by column:", np.sum(d, axis=0))
print("Sum by row:", np.sum(d, axis=1))

print("\n----- 7. SORTING & SEARCHING -----")
e = np.array([4, 1, 9, 2])
print("Sorted:", np.sort(e))
print("Index of max:", np.argmax(e))
print("Where e == 2:", np.where(e == 2))

print("\n----- 8. RANDOM NUMBERS -----")
np.random.seed(42)
print("Random int:\n", np.random.randint(0, 100, size=(2, 3)))
print("Random float:", np.random.rand(3))

print("\n----- 9. NAN & INF HANDLING -----")
f = np.array([1, np.nan, np.inf, 3])
print("Is NaN:", np.isnan(f))
print("Is finite:", np.isfinite(f))
print("Replace NaN/Inf:", np.nan_to_num(f))

print("\n----- 10. MATHEMATICAL OPERATIONS -----")
g = np.array([1, 2, 3])
print("Squared:", np.square(g))
print("Sqrt:", np.sqrt(g))
print("Log:", np.log(g))
print("Exp:", np.exp(g))
print("Rounded:", np.round(np.pi, 3))

print("\n----- 11. LINEAR ALGEBRA -----")
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])
print("Dot:\n", np.dot(A, B))
print("Inverse:\n", np.linalg.inv(A))
print("Determinant:", np.linalg.det(A))

print("\n----- 12. SET OPERATIONS -----")
x = np.array([1, 2, 3, 4])
y = np.array([3, 4, 5, 6])
print("Union:", np.union1d(x, y))
print("Intersection:", np.intersect1d(x, y))
print("Set difference:", np.setdiff1d(x, y))

print("\n----- 13. LOGICAL OPERATIONS -----")
z = np.array([1, 2, 3])
print("z > 2:", np.greater(z, 2))
print("All > 0:", np.all(z > 0))
print("Any > 2:", np.any(z > 2))

print("\n----- 14. STACKING & SPLITTING -----")
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6]])
print("VStack:\n", np.vstack((a1, a2)))
print("HStack:\n", np.hstack((a1, a1)))

print("\n----- 15. COPY & BROADCASTING -----")
x = np.array([1, 2, 3])
y = x.copy()
y[0] = 100
print("Original x:", x)
print("Copied y:", y)

print("\n----- END OF NUMPY CHEATSHEET -----")
