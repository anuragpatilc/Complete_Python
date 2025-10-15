def is_bit_set(num, position):
    """Check if bit at position is 1"""
    return (num & (1 << position)) != 0

# Check if bit 0 is set in 5 (0101)
print(is_bit_set(5, 0))  # Output: True (rightmost bit is 1)
print(is_bit_set(5, 1))  # Output: False (second bit is 0)
print(is_bit_set(5, 2))  # Output: True (third bit is 1)