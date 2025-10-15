# Basic Comparison Operation

# 1) Greater Than (>)
print(5 > 3)    # Output: True

"""
This checks if the number on the left is greater than the number on the right
-> Is 5 greater than 3? YES -> True
-> The expression evaluates to a boolean value (either True or False)
"""

print(5 > 10)   # Output: False (5 is NOT greater than 10)
print(10 > 3)   # Output: True (10 IS greater than 3)

# 2) LEss Than (<)
print(5 < 3)    # Output: False

"""
This checks if the number on the left is less than the number on the right.
-> IS 5 less than 3? NO -> False
-> 5 is actually greater than 3, so the result is False
"""

print(2 < 5)    # Output: True (2 IS less than 5)
print(10 < 3)   # Output: False (10 is NOT less than 3)

# 3) Greater Than or Equal To (>=)
print(5 >= 5)   # Output: True

"""
This checks if the number on the left is greater than OR equal to the number on the right.
- Is 5 greater than or equal to 5? YES (they're equal) → True
- This operator accepts both conditions: greater than AND equal to
"""

print(5 >= 3)   # Output: True (5 is greater than 3)
print(3 >= 3)   # Output: True (they are equal)
print(2 >= 3)   # Output: False (2 is neither greater nor equal to 3)

# 4) Less Than or Equal To (<=)
print(5 <= 4)   # Output: False

"""
This checks if the number on the left is less than OR equal to the number on the right.
- Is 5 less than or equal to 4? NO → False
- 5 is greater than 4, so neither condition is met
"""

# 5) Equal To (==)
print(5 == 5)   # Output: True

"""
This checks if the values on both sides are exactly equal.
- Are 5 and 5 the same value? YES → True
- This is used for comparison, not assignment (which uses =)
"""

print(5 == 5)       # Output: True
print(5 == 3)       # Output: False
print("hello" == "hello")  # Output: True
print(10 == 10.0)   # Output: True (different types, but same value)

# 6) Not Equal To (!=)
print(5 != 5)   # Output: False

"""
This checks if the values on both sides are NOT equal.
- Are 5 and 5 different? NO → False
- They are the same, so they are not different
"""

print(5 != 3)       # Output: True (5 and 3 are different)
print(5 != 5)       # Output: False (5 and 5 are the same)
print("hello" != "world")  # Output: True (different strings)

"""
Visual Comparison Table

Operator | Meaning              | Example    | Result
---------|----------------------|------------|--------
>        | Greater than         | 5 > 3      | True
<        | Less than            | 5 < 3      | False
>=       | Greater or equal     | 5 >= 5     | True
<=       | Less or equal        | 5 <= 4     | False
==       | Equal to             | 5 == 5     | True
!=       | Not equal to         | 5 != 5     | False
"""