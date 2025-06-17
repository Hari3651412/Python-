# 🔹 PYTHON TUPLES - FULL GUIDE

# ✅ What is a Tuple?
# - A tuple is an ordered, immutable (unchangeable) collection in Python.
# - Defined using parentheses ().
# - Can store multiple types of data.
# - Items can be accessed using index (like lists).

# ---------------------------
# 🔸 1. Creating Tuples
# ---------------------------

# Empty tuple
empty = ()

# Tuple with integers
nums = (1, 2, 3)

# Tuple with mixed data types
mixed = ("apple", 3.14, True, 42)

# Tuple without parentheses (comma is enough)
no_parens = "a", "b", "c"

# Single-element tuple (IMPORTANT: needs a trailing comma)
one_item = (5,)
not_a_tuple = (5)  # Just an int

print(type(one_item))      # <class 'tuple'>
print(type(not_a_tuple))   # <class 'int'>

# ---------------------------
# 🔸 2. Accessing Tuple Elements
# ---------------------------

t = ("red", "green", "blue")

print(t[0])      # red
print(t[-1])     # blue
print(t[1:])     # ('green', 'blue') — slicing works

# ---------------------------
# 🔸 3. Tuple is Immutable
# ---------------------------

# t[0] = "yellow"  ❌ Error: Tuples cannot be modified

# ---------------------------
# 🔸 4. Looping through Tuple
# ---------------------------

for color in t:
    print(color)

# ---------------------------
# 🔸 5. Tuple Methods
# ---------------------------

tup = (1, 2, 3, 2, 4, 2)

# count(value) → returns how many times a value appears
print(tup.count(2))  # 3

# index(value) → returns the index of first occurrence
print(tup.index(3))  # 2

# ---------------------------
# 🔸 6. Tuple Operations
# ---------------------------

a = (1, 2)
b = (3, 4)

# Concatenation
c = a + b
print(c)  # (1, 2, 3, 4)

# Repetition
d = a * 3
print(d)  # (1, 2, 1, 2, 1, 2)

# Membership
print(2 in a)      # True
print(5 not in a)  # True

# ---------------------------
# 🔸 7. Tuple Unpacking
# ---------------------------

person = ("Alice", 25, "Engineer")

name, age, job = person

print(name)  # Alice
print(age)   # 25
print(job)   # Engineer

# ---------------------------
# 🔸 8. Tuples with Nested Data
# ---------------------------

nested = (1, 2, (3, 4), ["a", "b"])

print(nested[2])       # (3, 4)
print(nested[3][0])    # a

# Though tuple itself is immutable, if it contains mutable items (like lists), those can be changed:
nested[3][1] = "z"
print(nested)  # (1, 2, (3, 4), ['a', 'z'])

# ---------------------------
# 🔸 9. Converting Between Tuples and Lists
# ---------------------------

# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# List to tuple
new_t = tuple(lst)
print(new_t)  # (1, 2, 3, 4)

# ---------------------------
# ✅ Summary:
# ---------------------------
# - Tuples are ordered and immutable.
# - Defined with (), or just commas.
# - Support indexing, slicing, unpacking, and two methods: count() and index().
# - Use tuples for fixed collections or where immutability is important (e.g., coordinates, config data).
