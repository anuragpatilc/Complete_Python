print(f"5 | 3 = {5 | 3}")  # Output: 7

"""
**OR operation:** Returns 1 if **at least one bit is 1**, otherwise returns 0.

**Step-by-step breakdown:**

5 = 0101
3 = 0011
    ----
| = 0111 = 7

Position 0: 1 | 1 = 1 ✓
Position 1: 0 | 1 = 1 ✓
Position 2: 1 | 0 = 1 ✓
Position 3: 0 | 0 = 0

Result = 0111 = 7
"""

# Real-world analogy: It's like an "OR gate". If either switch is ON, the light turns ON.
# More examples
print(f"12 ^ 10 = {12 ^ 10}")  # Output: 6
# 12 = 1100
# 10 = 1010
#      0110 = 6

print(f"7 ^ 7 = {7 ^ 7}")      # Output: 0
# 7 = 0111
# 7 = 0111
#     0000 = 0 (same bits = 0)