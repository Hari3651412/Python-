# 🔹 PYTHON OPERATORS - COMPLETE GUIDE

# ------------------------------
# 🔸 What are Operators?
# ------------------------------
# Operators are special symbols used to perform operations on variables and values.

# ------------------------------
# 🔸 1. Arithmetic Operators
# ------------------------------

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333...
print(a % b)   # Modulus → 1
print(a ** b)  # Exponent → 1000 (10^3)
print(a // b)  # Floor Division → 3

# ------------------------------
# 🔸 2. Comparison Operators
# ------------------------------
# Return True or False

x = 5
y = 10

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True

# ------------------------------
# 🔸 3. Assignment Operators
# ------------------------------

x = 5
x += 2   # Same as x = x + 2 → 7
x -= 1   # x = 6
x *= 3   # x = 18
x /= 2   # x = 9.0
x %= 4   # x = 1.0
x //= 2  # x = 0.0
x **= 3  # x = 0.0

print(x)

# ------------------------------
# 🔸 4. Logical Operators
# ------------------------------
# Used with boolean values

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# ------------------------------
# 🔸 5. Identity Operators
# ------------------------------
# Check memory location (object identity)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (same object)
print(a is not c)  # True (different objects, even though contents same)

# ------------------------------
# 🔸 6. Membership Operators
# ------------------------------
# Check presence of value in sequence

fruits = ['apple', 'banana', 'cherry']

print('banana' in fruits)     # True
print('orange' not in fruits) # True

# ------------------------------
# 🔸 7. Bitwise Operators
# ------------------------------

x = 5     # 0101 in binary
y = 3     # 0011 in binary

print(x & y)   # AND → 1  (0001)
print(x | y)   # OR → 7   (0111)
print(x ^ y)   # XOR → 6  (0110)
print(~x)      # NOT → -6
print(x << 1)  # Left Shift → 10 (1010)
print(x >> 1)  # Right Shift → 2 (0010)

# ------------------------------
# 🔸 Combined Example
# ------------------------------

a = 4
b = 2

# Arithmetic
add = a + b
sub = a - b
mul = a * b
div = a / b

# Comparison
is_equal = (a == b)

# Logical
result = (a > 1 and b < 5)

# Bitwise
bit = a & b

print(f"Add: {add}, Sub: {sub}, Mul: {mul}, Div: {div}")
print(f"Equal: {is_equal}, Logical Result: {result}, Bitwise AND: {bit}")
