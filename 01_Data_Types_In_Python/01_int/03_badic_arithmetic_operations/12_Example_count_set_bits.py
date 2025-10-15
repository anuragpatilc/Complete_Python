def count_set_bits(num):
    """Count number of 1s in binary representation"""
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

print(count_set_bits(5))   # Output: 2 (0101 has two 1s)
print(count_set_bits(7))   # Output: 3 (0111 has three 1s)
print(count_set_bits(15))  # Output: 4 (1111 has four 1s)

# Built-in method
print(bin(5).count('1'))   # Output: 2


## Real-World Applications
"""
1. **File Permissions:** Unix file permissions use bitwise operations
2. **Graphics Programming:** Pixel operations often use bitwise operations
3. **Network Programming:** IP addresses and subnets use bitwise operations
4. **Game Development:** Collision detection and flags use bitwise operations
5. **Cryptography:** Many encryption algorithms use bitwise operations
"""

## Summary Table
"""
Operator | Name            | Operation
---------|-----------------|---------------------
&        | AND             | Both bits must be 1
|        | OR              | At least one bit is 1
^        | XOR             | Bits must be different
~        | NOT             | Flip all bits
<<       | Left Shift      | Shift left, multiply by 2^n
>>       | Right Shift     | Shift right, divide by 2^n
"""