# functions - reusable blocks of code
# def keyword to define

# basic function
def greet():
    print("Hello!")

greet()  # calling the function

# function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alex")
greet_person("Bob")

# function with return value
def add(a,b):
    return a + b

result = add(5,3)
print(result)  # 8

# multiple parameters
def calculate(x,y,operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y

print(calculate(10,5,"add"))  # 15
print(calculate(10,5,"multiply"))  # 50

# default parameters
def greet_with_title(name,title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")  # Hello, Mr. Smith
greet_with_title("Smith","Dr.")  # Hello, Dr. Smith

# return multiple values
def get_name():
    first = "John"
    last = "Doe"
    return first,last  # returns tuple

first_name,last_name = get_name()
print(first_name,last_name)

# arbitrary number of arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1,2,3))  # 6
print(sum_all(1,2,3,4,5))  # 15

# keyword arguments (**kwargs)
def print_info(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

print_info(name="Alex",age=25,city="NYC")

# docstrings - documentation for functions
def multiply(a,b):
    """
    Multiplies two numbers and returns the result.
    
    Parameters:
    a: first number
    b: second number
    
    Returns:
    product of a and b
    """
    return a * b

print(multiply(4,5))
# print(multiply.__doc__)  # prints the docstring

# scope - variables inside function are local
def test_scope():
    x = 10  # local variable
    print(x)

test_scope()
# print(x)  # this would error - x doesnt exist outside function

# global variables
counter = 0

def increment():
    global counter  # need this to modify global variable
    counter += 1

increment()
increment()
print(counter)  # 2

# lambda functions - one line anonymous functions
square = lambda x: x ** 2
print(square(5))  # 25

add = lambda x,y: x + y
print(add(3,4))  # 7

# lambda with map
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2,numbers))
print(squared)  # [1, 4, 9, 16, 25]

# lambda with filter
numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)  # [2, 4, 6, 8, 10]

# maybe theres a better way but okay
