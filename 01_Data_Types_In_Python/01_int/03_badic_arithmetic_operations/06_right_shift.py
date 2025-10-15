print(f"5 >> 1 = {5 >> 1}")  # Output: 2

"""
**Right Shift:** Shifts bits to the right by n positions, discarding bits on the right.

**Step-by-step breakdown:**

5 = 0101
After right shift by 1 position:
5 >> 1 = 0010 = 2

Visual:
Original:  0 1 0 1
Shift >>1: 0 0 1 0 (shift right, leftmost becomes 0)
Result: 2
"""

# Formula: x >> n = x // 2^n (floor division by 2^n)
print(f"5 >> 1 = {5 >> 1}")   # Output: 2  (5 // 2 = 2)
print(f"5 >> 2 = {5 >> 2}")   # Output: 1  (5 // 4 = 1)
print(f"16 >> 2 = {16 >> 2}") # Output: 4  (16 // 4 = 4)

# More examples
print(f"20 >> 1 = {20 >> 1}") # Output: 10
print(f"20 >> 2 = {20 >> 2}") # Output: 5

# 20 = 10100
# 20 >> 2 = 00101 = 5