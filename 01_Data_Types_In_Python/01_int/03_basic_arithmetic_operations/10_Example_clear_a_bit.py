def clear_bit(num, position):
    """Set bit at position to 0"""
    return num & ~(1 << position)

num = 5  # 0101
result = clear_bit(num, 0)  # Clear bit 0 (set to 0)
print(f"{num} -> {result}")  # Output: 5 -> 4
# 0101 & ~0001 = 0101 & 1110 = 0100 = 4