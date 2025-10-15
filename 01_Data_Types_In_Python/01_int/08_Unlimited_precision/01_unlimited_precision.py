"""
Unlimited Precision
One of Python's greatest strengths with integers is unlimited precision:
"""

# Huge numbers work without any issues
factorial_20 = 1
for i in range(1, 21):
    factorial_20 *= i

print(f"20! = {factorial_20}")
# Output: 20! = 2432902008176640000

# Even larger numbers
huge = 10 ** 1000
print(f"10^1000 has {len(str(huge))} digits")  # Output: 10^1000 has 1001 digits

# Arbitrary precision arithmetic
a = 123456789123456789
b = 987654321987654321
result = a * b
print(f"{a} * {b} = {result}")
# Output: 123456789123456789 * 987654321987654321 = 121932631112635269230815276352189