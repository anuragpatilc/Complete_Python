"""
1) abs() - Absolute Value
- The abs() function returns the absolute value (distance from zero) of a number, always returning a positive value.
"""
print(abs(-15))  # Output: 15
print(abs(15))   # Output: 15
print(abs(0))    # Output: 0

"""
How it works:
- For negative numbers: removes the minus sign
- For positive numbers: returns the number as is
- For zero: returns zero
"""

# More examples with different types
print(abs(-3.14))        # Output: 3.14
print(abs(-100))         # Output: 100
print(abs(5))            # Output: 5

# Practical use case: calculating distance
current_position = 5
target_position = 12
distance = abs(target_position - current_position)
print(f"Distance: {distance}")  # Output: Distance: 7