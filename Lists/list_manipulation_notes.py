# 🔹 PYTHON LISTS - COMPLETE GUIDE

# ------------------------------
# 🔸 What is a List?
# ------------------------------
# A list is an ordered, mutable (changeable) collection of items in Python.
# Lists can contain items of different data types.

# Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "hello", 3.5, True]

print(fruits)
print(numbers)
print(mixed)

# ------------------------------
# 🔸 List Indexing & Slicing
# ------------------------------

my_list = ['a', 'b', 'c', 'd', 'e']

print(my_list[0])     # 'a'
print(my_list[-1])    # 'e'
print(my_list[1:4])   # ['b', 'c', 'd']
print(my_list[:3])    # ['a', 'b', 'c']
print(my_list[2:])    # ['c', 'd', 'e']
print(my_list[::-1])  # Reverse the list

# ------------------------------
# 🔸 Updating and Modifying Lists
# ------------------------------

my_list[0] = 'z'     # Replace 'a' with 'z'
print(my_list)       # ['z', 'b', 'c', 'd', 'e']

# ------------------------------
# 🔸 List Methods
# ------------------------------

nums = [10, 20, 30, 40]

# append(): Add to end
nums.append(50)
print(nums)  # [10, 20, 30, 40, 50]

# extend(): Add multiple elements
nums.extend([60, 70])
print(nums)  # [10, 20, 30, 40, 50, 60, 70]

# insert(): Insert at position
nums.insert(2, 25)  # Insert 25 at index 2
print(nums)

# remove(): Remove specific value
nums.remove(40)
print(nums)

# pop(): Remove last or specific index
nums.pop()       # Removes last
nums.pop(1)      # Removes element at index 1
print(nums)

# index(): First index of value
print(nums.index(30))  # Index of 30

# count(): Number of times value appears
print(nums.count(10))  # 1

# reverse(): Reverse the list
nums.reverse()
print(nums)

# sort(): Sort list (ascending)
nums.sort()
print(nums)

# sort(reverse=True): Descending sort
nums.sort(reverse=True)
print(nums)

# copy(): Creates a copy
new_nums = nums.copy()
print(new_nums)

# clear(): Removes all elements
new_nums.clear()
print(new_nums)  # []

# ------------------------------
# 🔸 List Operations
# ------------------------------

a = [1, 2, 3]
b = [4, 5]

# Concatenation
c = a + b
print(c)

# Repetition
d = a * 2
print(d)

# Membership
print(2 in a)      # True
print(6 not in a)  # True

# ------------------------------
# 🔸 Looping Through Lists
# ------------------------------

colors = ["red", "green", "blue"]

# Using for loop
for color in colors:
    print(color)

# Using index
for i in range(len(colors)):
    print(f"Index {i} has value {colors[i]}")

# ------------------------------
# 🔸 Nested Lists
# ------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # First row
print(matrix[1][2])    # 6

# ------------------------------
# 🔸 List Comprehensions
# ------------------------------

# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# ------------------------------
# 🔸 Practice Example
# ------------------------------

data = [5, 3, 8, 1, 9]

# Step-by-step manipulations
data.append(4)      # Add 4
data.sort()         # Sort ascending
data.remove(1)      # Remove 1
data.insert(0, 100) # Insert 100 at start
data.reverse()      # Reverse list

print(data)

