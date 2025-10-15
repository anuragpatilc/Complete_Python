"""
5) pow() - Power / Exponentiation 
The pow() function raises a number to a power. It has two forms:
- pow(base, exponent) - returns base ^ exponent
- pow(base, exponent, modulo) - retirms (base ^ exponent) % modulo
"""

print(f"pow(2, 3) = {pow(2, 3)}")  # Output: pow(2, 3) = 8
print(f"pow(2, 3, 5) = {pow(2, 3, 5)}")  # Output: pow(2, 3, 5) = 3

# Understanding pow() with Modulo
# pow(2, 3, 5) explanation:
# 2^3 = 8
# 8 % 5 = 3
print(pow(2, 3, 5))  # Output: 3

# Different Examples

# Basic power
print(pow(2, 4))     # Output: 16 (2^4)
print(pow(3, 3))     # Output: 27 (3^3)
print(pow(10, 2))    # Output: 100 (10^2)

# With decimal numbers
print(pow(2.5, 2))   # Output: 6.25

# Negative exponent (fraction)
print(pow(2, -1))    # Output: 0.5 (1/2)
print(pow(2, -2))    # Output: 0.25 (1/4)

# With modulo
print(pow(2, 10, 1000))   # Output: 24 (2^10 % 1000 = 1024 % 1000 = 24)
print(pow(5, 3, 7))       # Output: 6 (5^3 % 7 = 125 % 7 = 6)

# Practical Examples

# Calculate area of square
side = 5
area = pow(side, 2)
print(f"Area: {area} square units")  # Output: Area: 25 square units

# Calculate volume of cube
side = 3
volume = pow(side, 3)
print(f"Volume: {volume} cubic units")  # Output: Volume: 27 cubic units

# Exponential growth
initial = 2
generations = 5
population = pow(initial, generations)
print(f"Final population: {population}")  # Output: Final population: 32