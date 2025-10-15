def toggle_bit(num, position):
    """Flip bit at position"""
    return num ^ (1 << position)

num = 5  # 0101
result = toggle_bit(num, 1)  # Toggle bit 1
print(f"{num} -> {result}")  # Output: 5 -> 7
# 0101 ^ 0010 = 0111 = 7