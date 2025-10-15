"""
2) max() and min() - Find Maximum and Minimum
- max() returns the largest value from a sequence or multiple arguments. min() returns the samllest value from a sequence or multiple arguments.
"""

numbers = [3, 7, 2, 9, 1]
print(f"Max: {max(numbers)}")  # Output: Max: 9
print(f"Min: {min(numbers)}")  # Output: Min: 1

# Using with multiple Arguments 
print(max(3, 7, 2, 9, 1))  # Output: 9
print(min(3, 7, 2, 9, 1))  # Output: 1

# With different types
print(max(10, -5, 0, 20))  # Output: 20
print(min(10, -5, 0, 20))  # Output: -5

# Using with Custom key Function 
# Find word with maximum length
words = ["cat", "elephant", "dog"]
longest = max(words, key=len)
print(longest)  # Output: elephant

# Find person with minimum age
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]
youngest = min(people, key=lambda p: p["age"])
print(f"Youngest: {youngest['name']}")  # Output: Youngest: Charlie