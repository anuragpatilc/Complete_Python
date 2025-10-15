# isinstance() - Check Type

x = 42
print(isinstance(x, int))        # Output: True
print(isinstance(x, float))      # Output: False
print(isinstance(x, (int, float)))  # Output: True

## Summary Table of All Functions

"""
Function      | Purpose                    | Example
--------------|----------------------------|---------------------------
abs()         | Absolute value             | abs(-15) = 15
max()         | Maximum value              | max([1,5,3]) = 5
min()         | Minimum value              | min([1,5,3]) = 1
sum()         | Sum of all items           | sum([1,2,3]) = 6
len()         | Count items                | len([1,2,3]) = 3
pow()         | Power/Exponentiation       | pow(2,3) = 8
divmod()      | Quotient and remainder     | divmod(10,3) = (3,1)
round()       | Round to n decimals        | round(3.14159, 2) = 3.14
int()         | Convert to integer         | int("FF", 16) = 255
float()       | Convert to float           | float("3.14") = 3.14
hex()         | Convert to hexadecimal     | hex(255) = '0xff'
bin()         | Convert to binary          | bin(10) = '0b1010'
oct()         | Convert to octal           | oct(8) = '0o10'
"""