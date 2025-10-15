"""
6) divmod() Division and Modulo
- The divmod() function returns both the quotient and remainder of division in a single operation 
"""

quotient, remainder = divmod(10, 3)
print(f"divmod(10, 3) = {quotient}, {remainder}")  # Output: divmod(10, 3) = 3, 1

# Understanding divmod()
"""
divmod(10, 3):
10 / 3 = 3 remainder 1
Quotient = 3
Remainder = 1

It's equivalent to:
quotient = 10 // 3  (floor division)
remainder = 10 % 3  (modulo)
"""

# Different Examples
# Basic examples
q, r = divmod(20, 6)
print(f"20 ÷ 6 = {q} remainder {r}")  # Output: 20 ÷ 6 = 3 remainder 2

q, r = divmod(100, 7)
print(f"100 ÷ 7 = {q} remainder {r}")  # Output: 100 ÷ 7 = 14 remainder 2

# With negative numbers
q, r = divmod(-10, 3)
print(f"divmod(-10, 3) = {q}, {r}")  # Output: divmod(-10, 3) = -4, 2

q, r = divmod(10, -3)
print(f"divmod(10, -3) = {q}, {r}")  # Output: divmod(10, -3) = -4, -2

# With floats
q, r = divmod(10.5, 2.5)
print(f"divmod(10.5, 2.5) = {q}, {r}")  # Output: divmod(10.5, 2.5) = 4.0, 0.5

# Practical Examples
# Convert minutes to hours and minutes
total_minutes = 125
hours, minutes = divmod(total_minutes, 60)
print(f"{total_minutes} minutes = {hours}h {minutes}m")  # Output: 125 minutes = 2h 5m

# Convert seconds to hours, minutes, seconds
total_seconds = 3665
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"{total_seconds}s = {hours}h {minutes}m {seconds}s")
# Output: 3665s = 1h 1m 5s

# Distribute items into groups
items = 47
items_per_group = 10
num_groups, extra_items = divmod(items, items_per_group)
print(f"{items} items in groups of {items_per_group}: {num_groups} groups + {extra_items} extra")
# Output: 47 items in groups of 10: 4 groups + 7 extra
