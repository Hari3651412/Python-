# 🔹 PYTHON VARIABLES - COMPLETE GUIDE

# ------------------------------
# 🔸 What is a Variable?
# ------------------------------
# A variable is a **name** that refers to a value stored in memory.
# You use variables to store data that you want to use later.

# Think of it like a labeled box that holds something.

# Syntax:
# variable_name = value

# ------------------------------
# 🔸 Example: Basic Variables
# ------------------------------

name = "Alice"       # string
age = 25             # integer
height = 5.7         # float
is_student = True    # boolean

print(name)
print(age)
print(height)
print(is_student)

# ------------------------------
# 🔸 Variable Naming Rules
# ------------------------------
# ✅ Valid:
# - Starts with a letter or underscore (_)
# - Can contain letters, digits, and underscores
# ❌ Invalid:
# - Can't start with a number
# - Can't use special characters (!, @, $, etc.)
# - Can't use Python keywords (like `if`, `for`, `class`, etc.)

# Valid examples
first_name = "John"
_age = 30
user2 = "Mike"

# Invalid examples (will cause errors if uncommented)
# 2user = "Jack"
# user-name = "Sarah"
# class = "Math"

# ------------------------------
# 🔸 Dynamic Typing in Python
# ------------------------------
# Python variables are **dynamically typed**, meaning you don’t need to declare a type.

x = 10       # x is int
x = "hello"  # now x is string
print(x)

# ------------------------------
# 🔸 Multiple Assignments
# ------------------------------

a, b, c = 1, 2, 3
print(a, b, c)

# Assigning same value to multiple variables
x = y = z = 100
print(x, y, z)

# ------------------------------
# 🔸 Variable Types and type() Function
# ------------------------------

a = 10
b = 3.14
c = "Python"
d = True

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

# ------------------------------
# 🔸 Constants (By Convention)
# ------------------------------
# Python doesn't have true constants, but we use UPPERCASE names to show that a value should not change.

PI = 3.14159
MAX_USERS = 100

print(PI, MAX_USERS)

# ------------------------------
# 🔸 Memory Reference Concept
# ------------------------------
# Variables point to data in memory. When you assign one variable to another, they both refer to the same data.

x = [1, 2, 3]
y = x
y.append(4)
print(x)  # [1, 2, 3, 4] — x is also changed
