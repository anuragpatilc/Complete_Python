# Binary (base 2) - prefix with 0b
binary_num = 0b1010
print(f"Binary 0b1010 - {binary_num}") # Binary 0b1010 - 10

# Octal (base 8) - perfix with 0o
octal_num = 0o12
print(f"Octal 0o12 = {octal_num}") # Octal 0o12 = 10

# Hexadecimal (base 16) - perfix with 0x
hex_num = 0xA
print(f"Hex 0xA = {hex_num}") # Hex 0xA = 10

# Decimal (base 10) - default
decimal_num = 10
print(f"Decimal 10 = {decimal_num}") # Decimal 10 = 10

# Converting integer back to different bases 
num = 255
print(f"Decimal: {num}") # Decimal: 255
print(f"Binary: {bin(num)}") # Binary: 0b11111111
print(f"Octal: {oct(num)}") # Octal: 0o377
print(f"Hexadecimal: {hex(num)}") # Hexadecimal: 0xff