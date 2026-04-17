# my own module - just testing this out
# creating reusable functions

def greet(name):
    """Says hello to someone"""
    return f"Hello, {name}!"

def add_numbers(a,b):
    """Adds two numbers"""
    return a + b

def is_even(number):
    """Checks if number is even"""
    return number % 2 == 0

# some constants
PI = 3.14159
DAYS_IN_WEEK = 7

# a simple class
class Calculator:
    def add(self,x,y):
        return x + y
    
    def subtract(self,x,y):
        return x - y
    
    def multiply(self,x,y):
        return x * y
    
    def divide(self,x,y):
        if y == 0:
            return "Cannot divide by zero!"
        return x / y

# this only runs if file is executed directly
if __name__ == "__main__":
    print("Testing my_utils module")
    print(greet("Test"))
    print(add_numbers(5,3))
    print(is_even(4))
