# Useful for bit manipulation, flags, and performance
a = 5      # Binary: 101
b = 3      # Binary: 011

# AND - both bits must be 1
result = a & b
print(f"{a} & {b} = {result}")  # Output: 5 & 3 = 1 (Binary: 001)

# OR - at least one bit must be 1
result = a | b
print(f"{a} | {b} = {result}")  # Output: 5 | 3 = 7 (Binary: 111)

# XOR - bits must be different
result = a ^ b
print(f"{a} ^ {b} = {result}")  # Output: 5 ^ 3 = 6 (Binary: 110)

# NOT - flip all bits
result = ~a
print(f"~{a} = {result}")  # Output: ~5 = -6

# Left shift (multiply by 2^n)
result = a << 1
print(f"{a} << 1 = {result}")  # Output: 5 << 1 = 10

# Right shift (divide by 2^n)
result = a >> 1
print(f"{a} >> 1 = {result}")  # Output: 5 >> 1 = 2

# Bit length (number of bits needed to represent)
print(f"Bit length of {a}: {a.bit_length()}")  # Output: Bit length of 5: 3