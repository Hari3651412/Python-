# 🔹 PYTHON SETS - FULL GUIDE

# ✅ What is a Set?
# - A set is an unordered, unindexed collection of **unique** elements.
# - Defined using curly braces `{}` or the `set()` constructor.
# - Sets are mutable (can add/remove items), but only immutable (hashable) items can be added.

# ---------------------------
# 🔸 1. Creating Sets
# ---------------------------

# Set with numbers
num_set = {1, 2, 3, 4, 5}

# Set with mixed types
mixed_set = {1, "hello", 3.14, True}

# Empty set (must use set(), not {})
empty_set = set()
not_a_set = {}  # This creates an empty dictionary

print(type(empty_set))  # <class 'set'>

# Duplicate values are removed automatically
dup_set = {1, 2, 2, 3, 1}
print(dup_set)  # {1, 2, 3}

# ---------------------------
# 🔸 2. Accessing Set Items
# ---------------------------

# ❌ Sets are unordered → can't use indexing like set[0]

# Loop through a set
for item in num_set:
    print(item)

# ---------------------------
# 🔸 3. Adding Items to a Set
# ---------------------------

s = {1, 2, 3}

# add() → adds a single element
s.add(4)
print(s)  # {1, 2, 3, 4}

# update() → adds multiple elements
s.update([5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}

# ---------------------------
# 🔸 4. Removing Items from a Set
# ---------------------------

s = {1, 2, 3, 4, 5}

# remove(value) → removes item; raises error if not found
s.remove(3)
print(s)

# discard(value) → removes item; does nothing if not found
s.discard(10)  # No error

# pop() → removes and returns a random element
removed = s.pop()
print("Popped:", removed)

# clear() → removes all elements
s.clear()
print(s)  # set()

# ---------------------------
# 🔸 5. Set Operations
# ---------------------------

a = {1, 2, 3}
b = {3, 4, 5}

# union() → combines sets
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a | b)             # same result

# intersection() → common elements
print(a.intersection(b)) # {3}
print(a & b)             # same result

# difference() → elements in a but not in b
print(a.difference(b))   # {1, 2}
print(a - b)

# symmetric_difference() → elements in a or b but not both
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)

# ---------------------------
# 🔸 6. Set Methods Summary
# ---------------------------

# add(elem)                    → Add a single element
# update(iterable)             → Add multiple elements
# remove(elem)                 → Remove item, error if not found
# discard(elem)                → Remove item, no error if not found
# pop()                        → Remove and return random element
# clear()                      → Remove all elements
# union(set) / |               → Combine sets
# intersection(set) / &        → Common elements
# difference(set) / -          → Elements in one set but not other
# symmetric_difference(set) / ^→ Elements in either set but not both
# issubset(set)                → a.issubset(b)
# issuperset(set)              → a.issuperset(b)
# isdisjoint(set)              → True if no elements in common

# ---------------------------
# 🔸 7. Set Comparisons
# ---------------------------

x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True
print(x.isdisjoint({4})) # True

# ---------------------------
# 🔸 8. Frozen Sets
# ---------------------------

# frozenset → immutable version of a set
fs = frozenset([1, 2, 3])
# fs.add(4) ❌ Error: frozenset does not support adding/removal

print(fs)
