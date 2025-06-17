# 🔹 PYTHON STRINGS FULL GUIDE

# ------------------------------
# 🔸 String Creation
# ------------------------------

str1 = 'Hello'
str2 = "World"
multiline = """This is
a multiline
string."""

print(str1)
print(str2)
print(multiline)

# ------------------------------
# 🔸 String Indexing and Slicing
# ------------------------------

s = "Python"

print(s[0])    # P
print(s[-1])   # n

print(s[1:4])  # yth
print(s[:3])   # Pyt
print(s[3:])   # hon

# ------------------------------
# 🔸 String Immutability
# ------------------------------

# Strings cannot be changed directly
# s[0] = 'J'  # ❌ Error

# ------------------------------
# 🔸 Common String Methods
# ------------------------------

text = "  Hello World  "

# Length
print(len(text))  # 15

# Case conversion
print(text.lower())       # "  hello world  "
print(text.upper())       # "  HELLO WORLD  "
print("hello world".capitalize())  # "Hello world"
print("hello world".title())       # "Hello World"

# Stripping whitespaces
print(text.strip())   # "Hello World"
print(text.lstrip())  # "Hello World  "
print(text.rstrip())  # "  Hello World"

# Replace
print(text.replace("World", "Python"))  # "  Hello Python  "

# Split and Join
print("one,two,three".split(','))   # ['one', 'two', 'three']
print(",".join(['a', 'b', 'c']))    # 'a,b,c'

# Find and Index
print("hello".find('e'))     # 1
print("hello".index('l'))    # 2

# Startswith and Endswith
print("hello".startswith('he'))  # True
print("hello".endswith('lo'))    # True

# Count
print("banana".count('a'))  # 3

# Character checks
print("abc123".isalnum())   # True
print("abc".isalpha())      # True
print("123".isdigit())      # True

# ------------------------------
# 🔸 String Formatting
# ------------------------------

name = "Alice"
age = 25

# Old-style
print("Hello, %s!" % name)            # 'Hello, Alice!'

# str.format()
print("Hello, {}!".format(name))     # 'Hello, Alice!'

# f-strings
print(f"My name is {name} and I'm {age} years old.")  # 'My name is Alice and I'm 25 years old.'

# ------------------------------
# 🔸 String Tricks
# ------------------------------

# Reverse a string
s = "Python"
print(s[::-1])  # 'nohtyP'

# Palindrome check
s = "madam"
print(s == s[::-1])  # True

# Escape characters
print("He said, \"Hello!\"")  # He said, "Hello!"
print("Line1\nLine2")         # Line break

# Raw string
print(r"C:\new_folder\test")  # C:\new_folder\test

# String comparison
print("apple" == "Apple")     # False
print("apple" > "banana")     # False

# ------------------------------
# 🔸 Practice Example
# ------------------------------

text = " Python programming is powerful. "

# Step-by-step manipulation
clean = text.strip()                     # "Python programming is powerful."
clean = clean.replace("powerful", "awesome")  # "Python programming is awesome."
clean = clean.upper()                    # "PYTHON PROGRAMMING IS AWESOME."

print(clean)
