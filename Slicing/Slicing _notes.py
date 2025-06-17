# 🔹 PYTHON SLICING - FULL GUIDE

# Slicing means extracting a portion (sublist or substring) from a sequence like:
# - List
# - String
# - Tuple

# The syntax is:
# sequence[start:stop:step]

# ------------------------------
# 🔸 Slicing with Strings
# ------------------------------

text = "Python"

print(text[0:2])     # 'Py' → index 0 to 1
print(text[2:5])     # 'tho' → index 2,3,4
print(text[:4])      # 'Pyth' → from beginning to index 3
print(text[2:])      # 'thon' → from index 2 to end
print(text[:])       # 'Python' → full string
print(text[::2])     # 'Pto' → every 2nd character
print(text[::-1])    # 'nohtyP' → reversed string

# ------------------------------
# 🔸 Slicing with Lists
# ------------------------------

nums = [10, 20, 30, 40, 50, 60]

print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]
print(nums[3:])      # [40, 50, 60]
print(nums[::2])     # [10, 30, 50]
print(nums[::-1])    # [60, 50, 40, 30, 20, 10]

# ------------------------------
# 🔸 Negative Index Slicing
# ------------------------------

letters = ['a', 'b', 'c', 'd', 'e']

print(letters[-3:])      # ['c', 'd', 'e']
print(letters[-4:-1])    # ['b', 'c', 'd']
print(letters[::-1])     # ['e', 'd', 'c', 'b', 'a']

# ------------------------------
# 🔸 Using Step Values
# ------------------------------

nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[::2])    # [0, 2, 4, 6] → every 2nd element
print(nums[1::2])   # [1, 3, 5] → every 2nd element starting from index 1
print(nums[::-1])   # [6, 5, 4, 3, 2, 1, 0] → reversed list

# ------------------------------
# 🔸 Practice Examples
# ------------------------------

data = "HelloWorld"

print(data[1:8:2])     # 'elWr' (1 to 7 with step 2)
print(data[-5:-1])     # 'Worl'
print(data[::-2])      # 'drloH' (reverse every 2nd char)

# ------------------------------
# 🔸 Use Cases
# ------------------------------

# Copy a list
original = [1, 2, 3]
copy = original[:]
print(copy)  # [1, 2, 3]

# Reverse a string
s = "python"
print(s[::-1])  # 'nohtyp'

# Get every 3rd element from a list
sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sample[::3])  # [0, 3, 6, 9]
