def set_bit(num, position):
    """Set bit at position to 1"""
    return num | (1 << position)

num = 5  # 0101
result = set_bit(num, 1)  # Set bit 1 to 1
print(f"{num} -> {result}")  # Output: 5 -> 7
# 0101 | 0010 = 0111 = 7