print(f"5 & 3 = {5 & 3}")  # Output: 1

"""
**AND operation:** Returns 1 only if **both bits are 1**, otherwise returns 0.

**Step-by-step breakdown:**

5 = 0101
3 = 0011
    ----
& = 0001 = 1

Position 0: 1 & 1 = 1 ✓
Position 1: 0 & 1 = 0
Position 2: 1 & 0 = 0
Position 3: 0 & 0 = 0

Result = 0001 = 1
"""

# Real-world analogy: It's like an "AND gate" in electronics. Both switches must be ON for the light to turn ON.
# More examples
print(f"12 & 10 = {12 & 10}")  # Output: 8
# 12 = 1100
# 10 = 1010
#      1000 = 8

print(f"15 & 7 = {15 & 7}")    # Output: 7
# 15 = 1111
#  7 = 0111
#      0111 = 7