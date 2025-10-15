# Creating Integers

"""
You create an integer by simply assigning a whole number to a vaiable:
"""

age = 25
temperature = -10
count = 0
population = 800000000000

print(f"age: {age}, type: {type(age)}") # age: 25, type: <class 'int'>
print(f"temperature: {temperature}, type: {type(temperature)}") # temperature: -10, type: <class 'int'>
print(f"count: {count}, type: {count}") # count: 0, type: 0
print(f"population: {population}, type: {population}") # population: 800000000000, type: 800000000000

# You can also create integers from other types using the "int()" funcation 
# converting a string to integer
num_str = "45"
num = int(num_str)
print(f"num_str: {num_str}, type: {type(num_str)}") # num_str: 45, type: <class 'str'>
print(f"num: {num}, type: {type(num)}") # num: 45, type: <class 'int'>

# Converting a float to integer (Truncates decimal)
price = 19.99
whole_price = int(price)
print(f"price: {price}, type: {type(price)}") # price: 19.99, type: <class 'float'>
print(f"whole_price: {whole_price}, type: {type(whole_price)}") # whole_price: 19, type: <class 'int'>

# Converting a boolean to integer
is_active = True
num = int(is_active)
print(f"is_acive: {is_active}, type: {type(is_active)}") # is_acive: True, type: <class 'bool'>
print(f"num: {num}, type: {type(num_str)}") # num: 1, type: <class 'str'>

# Converting String with base specification 
binary_string = int("1010", 2)
print(f"binary_string: {binary_string}, type: {type(binary_string)}") # binary_string: 10, type: <class 'int'>

octal_string = int("12", 8)
print(f"octal_string: {octal_string}, type: {type(octal_string)}") # octal_string: 10, type: <class 'int'>

hex_string = int("A", 16)
print(f"hex_string: {hex_string}, type: {type(hex_string)}") # hex_string: 10, type: <class 'int'>
