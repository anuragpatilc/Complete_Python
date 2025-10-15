"""
8) int() - Convert to Integer
The int() function converts a value to an integer. It can also convert strings with different bases.
"""

print(int("FF", 16))   # Output: 255 (hex to decimal)
print(int("1010", 2))  # Output: 10 (binary to decimal)

# Basic Conversions
# From string
print(int("42"))       # Output: 42
print(int("-15"))      # Output: -15

# From float (truncates decimal part)
print(int(3.14))       # Output: 3
print(int(9.99))       # Output: 9
print(int(-2.99))      # Output: -2 (truncates toward zero)

# From boolean
print(int(True))       # Output: 1
print(int(False))      # Output: 0

# Convert from Different Bases
# Binary (base 2)
print(int("1010", 2))        # Output: 10
print(int("11111111", 2))    # Output: 255

# Octal (base 8)
print(int("12", 8))          # Output: 10
print(int("377", 8))         # Output: 255

# Hexadecimal (base 16)
print(int("A", 16))          # Output: 10
print(int("FF", 16))         # Output: 255
print(int("CAFE", 16))       # Output: 51966

# Any base (2 to 36)
print(int("1A", 16))         # Output: 26
print(int("10", 10))         # Output: 10
print(int("101", 5))         # Output: 26 (1×5² + 0×5¹ + 1×5⁰)

# Error Handling
# Invalid conversion will raise ValueError
try:
    print(int("hello"))  # This will fail
except ValueError:
    print("Error: Cannot convert 'hello' to integer")

try:
    print(int("12", 2))  # Invalid: 12 is not a valid binary number
except ValueError:
    print("Error: '12' is not valid in base 2")

# Practical Examples
# Convert user input to integer
age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old")

# Parse hex color code
hex_color = "FF5733"
r = int(hex_color[0:2], 16)
g = int(hex_color[2:4], 16)
b = int(hex_color[4:6], 16)
print(f"RGB: ({r}, {g}, {b})")  # Output: RGB: (255, 87, 51)

# Convert binary string to decimal
binary_num = "11010101"
decimal = int(binary_num, 2)
print(f"Binary {binary_num} = Decimal {decimal}")  # Output: Binary 11010101 = Decimal 213