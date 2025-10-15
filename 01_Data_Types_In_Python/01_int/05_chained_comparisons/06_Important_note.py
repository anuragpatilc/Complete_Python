# Important Notes

# 1) Orfer matters in chained comparisons:
print(3 < 5 < 7)   # Output: True
print(7 < 5 < 3)   # Output: False (reads left to right)

#) 2) Each condition is evaluated:
# Only evaluates 5 < 7 once, not twice
print(1 < 5 < 7)  # Efficient in Python! # Output: True

# 3) Mixed operators work:
print(1 < 5 >= 5 > 3)  # Output: True (all conditions met)

# 4) Be careful with strings:
print("a" < "b" < "c")  # Output: True (alphabetical comparison)
print("apple" < "banana" < "cherry")  # Output: True

"""
Summary
- Comparison operators return True or False
- Chained comparisons let you check multiple conditions in one line
- They make code more readable and Pythonic
- They're efficient because Python evaluates them smartly
"""