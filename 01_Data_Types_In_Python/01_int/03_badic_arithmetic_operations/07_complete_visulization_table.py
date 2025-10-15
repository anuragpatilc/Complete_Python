a = 5   # 0101
b = 3   # 0011

print("Operation | Result | Explanation")
print("-" * 50)
print(f"5 & 3     | {5 & 3}      | Both bits must be 1")
print(f"5 | 3     | {5 | 3}      | At least one bit is 1")
print(f"5 ^ 3     | {5 ^ 3}      | Bits are different")
print(f"~5        | {~5}     	 | Flip all bits")
print(f"5 << 1    | {5 << 1}     | Shift left, multiply by 2")
print(f"5 >> 1    | {5 >> 1}     | Shift right, divide by 2")