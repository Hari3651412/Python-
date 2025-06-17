# 🔹 PYTHON DICTIONARIES - FULL GUIDE

# ✅ What is a Dictionary?
# - A dictionary is an **unordered**, **mutable** collection of key-value pairs.
# - Keys must be unique and immutable (e.g., strings, numbers, tuples).
# - Values can be any data type.

# ----------------------------
# 🔸 1. Creating a Dictionary
# ----------------------------

# Basic dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
info = dict(name="Bob", age=30)

# Empty dictionary
empty_dict = {}

# Dictionary with mixed keys
mixed = {
    1: "one",
    "two": 2,
    (3, 4): "tuple"
}

# ----------------------------
# 🔸 2. Accessing Values
# ----------------------------

print(person["name"])        # Alice
# print(person["gender"])    ❌ KeyError

# Using get() to avoid KeyError
print(person.get("gender"))       # None
print(person.get("gender", "N/A"))# N/A

# ----------------------------
# 🔸 3. Changing and Adding Items
# ----------------------------

person["age"] = 26              # Update
person["gender"] = "female"     # Add new key-value
print(person)

# ----------------------------
# 🔸 4. Removing Items
# ----------------------------

# pop(key)
person.pop("city")         # Removes and returns value
# popitem()
item = person.popitem()    # Removes and returns last item
print(item)

# del keyword
del person["age"]

# clear()
person.clear()             # Removes all items

# ----------------------------
# 🔸 5. Looping through a Dictionary
# ----------------------------

student = {
    "name": "John",
    "grade": "A",
    "age": 20
}

# Keys
for key in student:
    print(key, student[key])

# Values
for value in student.values():
    print(value)

# Key-Value Pairs
for key, value in student.items():
    print(f"{key}: {value}")

# ----------------------------
# 🔸 6. Dictionary Methods
# ----------------------------

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

# keys()
print(d.keys())    # dict_keys(['a', 'b', 'c'])

# values()
print(d.values())  # dict_values([1, 2, 3])

# items()
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

# get()
print(d.get("b"))        # 2
print(d.get("z", 0))     # 0

# update() → merge dictionaries or add items
d.update({"b": 20, "d": 4})
print(d)

# pop()
d.pop("a")               # removes key "a"

# popitem()
print(d.popitem())       # removes last inserted pair

# setdefault() → returns value if key exists, else inserts key with default
x = d.setdefault("e", 99)
print(x)                 # 99
print(d)

# copy()
new_d = d.copy()
print(new_d)

# clear()
d.clear()
print(d)  # {}

# ----------------------------
# 🔸 7. Nested Dictionaries
# ----------------------------

students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])  # Alice

# ----------------------------
# 🔸 8. Dictionary Comprehension
# ----------------------------

squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ----------------------------
# ✅ Summary:
# ----------------------------
# - Dictionaries store data as key-value pairs.
# - Keys must be unique and immutable.
# - Support adding, updating, deleting, and accessing values.
# - Very efficient for lookups.
# - Useful methods: get(), update(), pop(), popitem(), setdefault(), keys(), values(), items(), clear(), copy().
# - Can be nested and used in comprehensions.
