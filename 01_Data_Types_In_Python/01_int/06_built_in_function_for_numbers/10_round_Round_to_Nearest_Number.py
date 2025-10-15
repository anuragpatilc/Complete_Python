"""
7) round() - Round to Nearest Number
- The round() function rounds a number to the nearest integer or to a specified number of decimal places.
"""

print(f"round(4.5) = {round(4.5)}")  # Output: round(4.5) = 4
print(f"round(5.5) = {round(5.5)}")  # Output: round(5.5) = 6

"""
Understanding Banker's Rounding 
Python uses banker's rounding ( round half to even):
- If the value is exactly halfway between two numbers, it rounds ot the nearest even number
"""

print(round(0.5))   # Output: 0 (rounds to nearest even)
print(round(1.5))   # Output: 2 (rounds to nearest even)
print(round(2.5))   # Output: 2 (rounds to nearest even)
print(round(3.5))   # Output: 4 (rounds to nearest even)
print(round(4.5))   # Output: 4 (rounds to nearest even)
print(round(5.5))   # Output: 6 (rounds to nearest even)

# Rounding to Decimal Places 
# Round to 2 decimal places
print(round(3.14159, 2))   # Output: 3.14

# Round to 1 decimal place
print(round(2.678, 1))     # Output: 2.7

# Round to 0 decimal places (returns integer)
print(round(4.6))          # Output: 5

# Round to negative places (rounds to tens, hundreds, etc.)
print(round(1234, -1))     # Output: 1230 (rounds to nearest 10)
print(round(1234, -2))     # Output: 1200 (rounds to nearest 100)
print(round(1234, -3))     # Output: 1000 (rounds to nearest 1000)

# Practical Examples 
# Round prices
price = 19.456
rounded_price = round(price, 2)
print(f"Price: ${rounded_price}")  # Output: Price: $19.46

# Round percentages
percentage = 85.678
rounded_percentage = round(percentage, 1)
print(f"Score: {rounded_percentage}%")  # Output: Score: 85.7%

# Round to significant figures
numbers = [1.234, 0.005678, 456.789]
for num in numbers:
    print(f"{num} rounded to 2 decimals: {round(num, 2)}")

"""
Output:
1.234 rounded to 2 decimals: 1.23
0.005678 rounded to 2 decimals: 0.01
456.789 rounded to 2 decimals: 456.79
"""