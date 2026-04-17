# testing my own module
# importing from my_utils.py

import my_utils

# using functions from module
print(my_utils.greet("Alice"))
print(my_utils.add_numbers(10,5))
print(my_utils.is_even(7))

# using constants
print(f"Pi is approximately {my_utils.PI}")

# using class from module
calc = my_utils.Calculator()
print(calc.add(5,3))
print(calc.multiply(4,7))

# alternative import style
from my_utils import greet,is_even

print(greet("Bob"))
print(is_even(10))

# this is pretty cool! i can organize my code better now
