"""
Understanding String Formatting in Python
1) F - String (Formatted String Literals) - Modern Approach 
- F - string were introduced in Python 3.6 and are the most modern readable way to formate strings.
"""

# Basic F-String Syntax 

num = 42
print(f"The answer is {num}")  # Output: The answer is 42

"""
How it works:
- Start the string f or F before the quotes 
- Put variables or expressions inside curly braces {}
- Python evaluates the expression and inserts the result 
"""

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
# Output: My name is Alice and I am 25 years old

# You can also use expressions
print(f"Next year I will be {age + 1}")  # Output: Next year I will be 26