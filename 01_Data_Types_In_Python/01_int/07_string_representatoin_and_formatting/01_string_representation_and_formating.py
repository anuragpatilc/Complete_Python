num = 42

# Using f-strings (modern approach)
print(f"The answer is {num}")  # Output: The answer is 42
print(f"Binary: {num:b}")      # Output: Binary: 101010
print(f"Octal: {num:o}")       # Output: Octal: 52
print(f"Hex: {num:x}")         # Output: Hex: 2a
print(f"Hex (uppercase): {num:X}")  # Output: Hex (uppercase): 2A

# Padding with zeros
print(f"{num:05d}")  # Output: 00042

# With thousand separators
big_num = 1000000
print(f"Large number: {big_num:,}")  # Output: Large number: 1,000,000
print(f"Large number: {big_num:_}")  # Output: Large number: 1_000_000

# Using format() method
print("Binary: {}".format(bin(num)))  # Output: Binary: 0b101010