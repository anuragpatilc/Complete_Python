"""
2. Format Specifiers - Number Base Conversions

- After the variable inside {}, You can add a colon : followed by format specifiers.

"""

# Binary Format (:b)

num = 42
print(f"Binary: {num:b}")  # Output: Binary: 101010

"""
Explanation:
- :b converts the number to binary (base 2)
- 42 in decimal = 101010 in binary 
- No prefix (no 0b)
"""

# Step-by-step conversion
# 42 = 32 + 8 + 2
# 42 = 2^5 + 2^3 + 2^1
# 42 = 101010 in binary

print(f"5 in binary: {5:b}")      # Output: 5 in binary: 101
print(f"255 in binary: {255:b}")  # Output: 255 in binary: 11111111

# Octal Format (:o)
num = 42
print(f"Octal: {num:o}")  # Output: Octal: 52

"""
Explanation:
- :o converts the number to octal (base 8)
- 42 in decimal = 52 in octal 
- No prefix (no 0o)
"""

# Step-by-step conversion
# 42 = 5×8 + 2
# 42 = 52 in octal

print(f"8 in octal: {8:o}")      # Output: 8 in octal: 10
print(f"64 in octal: {64:o}")    # Output: 64 in octal: 100

# Hexadecimal Format (:x or :X)
num = 42
print(f"Hex: {num:x}")              # Output: Hex: 2a
print(f"Hex (uppercase): {num:X}")  # Output: Hex (uppercase): 2A

"""
Explanation:
- :x converts to hexadecimal (base 16) in lowercase
- :X converts to hexadecimal in UPPERCASE
- 42 in decimal = 2A in hexadecimal
- No prefix (no 0x)
"""

# Step-by-step conversion
# Hex digits: 0-9, A(10), B(11), C(12), D(13), E(14), F(15)
# 42 = 2×16 + 10
# 42 = 2A in hexadecimal (A represents 10)

print(f"255 in hex: {255:x}")    # Output: 255 in hex: ff
print(f"255 in hex: {255:X}")    # Output: 255 in hex: FF
print(f"16 in hex: {16:x}")      # Output: 16 in hex: 10

# complete Example - All Bases
num = 100

print(f"Decimal: {num}")       # Output: Decimal: 100
print(f"Binary: {num:b}")      # Output: Binary: 1100100
print(f"Octal: {num:o}")       # Output: Octal: 144
print(f"Hex: {num:x}")         # Output: Hex: 64
print(f"Hex (upper): {num:X}") # Output: Hex (upper): 64