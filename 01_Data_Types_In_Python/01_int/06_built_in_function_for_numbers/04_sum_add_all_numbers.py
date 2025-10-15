"""
3) sum() - add all Numbers
- The sum() function adds all numbers in a sequence and erturns the total.
"""

numbers = [3, 7, 2, 9, 1]
print(f"Sum: {sum(numbers)}")  # Output: Sum: 22

# Sum with start value
print(f"Sum with start: {sum(numbers, 10)}")  # Output: Sum with start: 32
# Explanation: 3 + 7 + 2 + 9 + 1 = 22, then 22 + 10 = 32

# Sum with Different Types
# Sum of integers
print(sum([1, 2, 3, 4, 5]))  # Output: 15

# Sum of floats
print(sum([1.5, 2.5, 3.5]))  # Output: 7.5

# Sum with negative numbers
print(sum([10, -5, 20, -3]))  # Output: 22

# Sum with Tuples and Ranges
# Sum of tuple
print(sum((10, 20, 30)))  # Output: 60

# Sum of range
print(sum(range(1, 11)))  # Output: 55 (1+2+3+...+10)

# Sum of range with step
print(sum(range(0, 11, 2)))  # Output: 30 (0+2+4+6+8+10)

print(sum(range(1, 10000 * 100000)))