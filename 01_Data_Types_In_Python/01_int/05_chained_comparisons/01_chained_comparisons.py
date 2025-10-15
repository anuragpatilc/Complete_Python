# Chained comparison 1
print(3 < 5 < 7)      # Output: True

"""
This checks multiple conditions at once in a single expression.

How it works:
Python reads this as: "Is 3 less than 5 AND is 5 less than 7?"
It's equivalent to: (3 < 5) and (5 < 7)
"""

# step-by-step breakdown:

# Step 1: Is 3 < 5?
step1 = 3 < 5    # True

# Step 2: Is 5 < 7?
step2 = 5 < 7    # True

# Step 3: Are both True?
result = step1 and step2  # True and True = True

# Examples:
print(1 < 2 < 3)        # Output: True (all conditions met)
print(1 < 2 < 2)        # Output: False (2 is NOT less than 2)
print(5 < 10 < 8)       # Output: False (10 is NOT less than 8)
print(0 < 5 < 10 < 15)  # Output: True (all conditions met)

# Chained Comparison 2
print(10 > 5 >= 5)    # Output: True

"""
This checks multiple conditions with different operators.

How it works:
Python reads this as: "Is 10 greater than 5 AND is 5 greater than or equal to 5?"
It's equivalent to: (10 > 5) and (5 >= 5)
"""

# step-by-step breakdown:
# Step 1: Is 10 > 5?
step1 = 10 > 5    # True

# Step 2: Is 5 >= 5?
step2 = 5 >= 5    # True

# Step 3: Are both True?
result = step1 and step2  # True and True = True

# Examples
print(10 > 5 >= 5)       # Output: True (both conditions met)
print(10 > 5 > 3)        # Output: True (10 > 5 is True, 5 > 3 is True)
print(10 > 5 > 8)        # Output: False (10 > 5 is True, but 5 > 8 is False)
print(20 >= 10 > 5 >= 5) # Output: True (all four conditions met)