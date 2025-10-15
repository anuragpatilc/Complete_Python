print(f"5 << 1 = {5 << 1}")  # Output: 10

"""
**Left Shift:** Shifts bits to the left by n positions, filling with 0s on the right.

**Step-by-step breakdown:**

5 = 0101
After left shift by 1 position:
5 << 1 = 1010 = 10

Visual:
Original:  0 1 0 1
Shift <<1: 1 0 1 0 (shift left, fill right with 0)
Result: 10
"""

# Formula: x << n = x * 2^n
print(f"5 << 1 = {5 << 1}")   # Output: 10  (5 * 2^1 = 10)
print(f"5 << 2 = {5 << 2}")   # Output: 20  (5 * 2^2 = 20)
print(f"5 << 3 = {5 << 3}")   # Output: 40  (5 * 2^3 = 40)

# More examples
print(f"3 << 2 = {3 << 2}")   # Output: 12  (3 * 4 = 12)
print(f"1 << 4 = {1 << 4}")   # Output: 16  (1 * 16 = 16)

# 3 = 0011
# 3 << 2 = 1100 = 12