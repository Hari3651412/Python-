# 🔹 PYTHON TYPE CASTING - COMPLETE GUIDE

# ------------------------------
# 🔸 What is Type Casting?
# ------------------------------
# Type casting means converting one data type to another.
# Example: converting a string to an integer or float.

# Python provides built-in functions for casting:
# - int()
# - float()
# - str()
# - bool()
# - list(), tuple(), set()

# ------------------------------
# 🔸 int() - Convert to Integer
# ------------------------------

a = "10"
b = int(a)     # string to int
print(b)       # 10
print(type(b)) # <class 'int'>

x = 5.9
y = int(x)     # float to int (truncates decimals)
print(y)       # 5

# ------------------------------
# 🔸 float() - Convert to Float
# ------------------------------

a = "3.14"
b = float(a)   # string to float
print(b)       # 3.14

x = 7
y = float(x)   # int to float
print(y)       # 7.0

# ------------------------------
# 🔸 str() - Convert to String
# ------------------------------

a = 100
b = str(a)     # int to string
print(b)       # "100"
print(type(b)) # <class 'str'>

pi = 3.14
print(str(pi)) # "3.14"

# ------------------------------
# 🔸 bool() - Convert to Boolean
# ------------------------------
# Rules:
# - 0, 0.0, "", [], {}, None → False
# - everything else → True

print(bool(0))         # False
print(bool(1))         # True
print(bool(""))        # False
print(bool("hello"))   # True
print(bool([]))        # False

# ------------------------------
# 🔸 list(), tuple(), set() - Convert to Collection Types
# ------------------------------

s = "abc"
print(list(s))   # ['a', 'b', 'c']
print(tuple(s))  # ('a', 'b', 'c')
print(set(s))    # {'a', 'b', 'c'} (unordered)

# From tuple to list
t = (1, 2, 3)
print(list(t))   # [1, 2, 3]

# From list to tuple
l = [4, 5, 6]
print(tuple(l))  # (4, 5, 6)

# ------------------------------
# 🔸 Invalid Casting (Causes Error)
# ------------------------------

# int("abc")   → ValueError
# float("xyz") → ValueError
# int("3.5")   → ValueError (string must be whole number)

# Example:
# print(int("abc"))  # ❌ Will cause error

# ------------------------------
# 🔸 Practical Example
# ------------------------------

num1 = input("Enter a number: ")   # input gives string
num2 = input("Enter another: ")

total = int(num1) + int(num2)      # convert before adding
print("Sum:", total)
