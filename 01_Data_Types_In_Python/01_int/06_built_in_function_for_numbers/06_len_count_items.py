"""
4) len() - Count Items
- The len() function returns the number of items in a sequence.
"""

items = [1, 2, 3, 4, 5]
print(f"Length: {len(items)}")  # Output: Length: 5

# Using with different Sequences

# List
print(len([1, 2, 3]))  # Output: 3

# String
print(len("hello"))  # Output: 5

# Tuple
print(len((10, 20, 30)))  # Output: 3

# Dictionary
print(len({"a": 1, "b": 2, "c": 3}))  # Output: 3

# Range
print(len(range(10)))  # Output: 10