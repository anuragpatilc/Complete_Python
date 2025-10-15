print(f"~5 = {~5}")  # Output: -6

"""
**NOT operation:** Flips all bits (0 becomes 1, 1 becomes 0). But there's a catch with negative numbers!

**Why ~5 = -6?** Python uses **two's complement** representation for negative numbers.
5 in binary (8-bit): 00000101
After flipping:      11111010 = -6 (in two's complement)

The formula is: ~x = -(x + 1)
~5 = -(5 + 1) = -6

Understanding two's complement:
- In Python, negative numbers are represented using two's complement
- To get a negative number in two's complement: flip all bits and add 1
- To reverse it: subtract 1 and flip all bits
"""

print(f"~5 = {~5}")      # Output: -6  (-(5+1))
print(f"~0 = {~0}")      # Output: -1  (-(0+1))
print(f"~-1 = {~-1}")    # Output: 0   (-(-1+1))
print(f"~10 = {~10}")    # Output: -11 (-(10+1))

# Formula: ~x = -(x + 1)
for x in [0, 1, 5, 10]:
    print(f"~{x} = {~x} (which equals {-(x+1)})")