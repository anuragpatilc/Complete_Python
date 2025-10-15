# Addition
result = 10 + 5
print(f"10 + 5 = {result}")  # Output: 10 + 5 = 15

# Subtraction
result = 10 - 5
print(f"10 - 5 = {result}")  # Output: 10 - 5 = 5

# Multiplication
result = 10 * 5
print(f"10 * 5 = {result}")  # Output: 10 * 5 = 50

# Division (returns float)
result = 10 / 5
print(f"10 / 5 = {result}")  # Output: 10 / 5 = 2.0
print(f"Type: {type(result)}")  # Output: Type: <class 'float'>

# Floor Division (returns integer, rounds down)
result = 10 // 3
print(f"10 // 3 = {result}")  # Output: 10 // 3 = 3

result = -10 // 3
print(f"-10 // 3 = {result}")  # Output: -10 // 3 = -4 (rounds toward negative infinity)

# Modulo (remainder after division)
result = 10 % 3
print(f"10 % 3 = {result}")  # Output: 10 % 3 = 1

# Negative modulo
result = -10 % 3
print(f"-10 % 3 = {result}")  # Output: -10 % 3 = 2

# Exponentiation (power)
result = 2 ** 3
print(f"2 ** 3 = {result}")  # Output: 2 ** 3 = 8

# Bitwise operations (new importance in latest Python)
print(f"5 & 3 = {5 & 3}")      # AND: Output: 1
print(f"5 | 3 = {5 | 3}")      # OR: Output: 7
print(f"5 ^ 3 = {5 ^ 3}")      # XOR: Output: 6
print(f"~5 = {~5}")            # NOT: Output: -6
print(f"5 << 1 = {5 << 1}")    # Left shift: Output: 10
print(f"5 >> 1 = {5 >> 1}")    # Right shift: Output: 2

print(5 != 3)       # Output: True (5 and 3 are different)
print(5 != 5)       # Output: False (5 and 5 are the same)
print("hello" != "world")  # Output: True (different strings)


## Visual Comparison Table
"""
Operator | Meaning              | Example    | Result
---------|----------------------|------------|--------
>        | Greater than         | 5 > 3      | True
<        | Less than            | 5 < 3      | False
>=       | Greater or equal     | 5 >= 5     | True
<=       | Less or equal        | 5 <= 4     | False
==       | Equal to             | 5 == 5     | True
!=       | Not equal to         | 5 != 5     | False
"""

# Understanding Bitwise Operaations in Python 
"""
Bitwise operations work directly on the binary representations of numbers.
Let me explain each one in detail 

First, Let's Understand Binary
-> Before we dive into bitwise operations, you need to understand how numbers are represented in binary:
"""

# Decimal to Binary conversion
print(f"5 in binary: {bin(5)}")      # Output: 5 in binary: 0b101
print(f"3 in binary: {bin(3)}")      # Output: 3 in binary: 0b11

# Let's pad them for easier visualization
# 5 = 0101 (4 bits)
# 3 = 0011 (4 bits)

"""
**Visual representation:**

5 in binary: 0 1 0 1
3 in binary: 0 0 1 1


Each digit is called a **bit**, and they represent powers of 2 from right to left:

Position:   3  2  1  0
Value:      8  4  2  1
5 (0101):   0  1  0  1  = 0×8 + 1×4 + 0×2 + 1×1 = 5
3 (0011):   0  0  1  1  = 0×8 + 0×4 + 1×2 + 1×1 = 3
"""