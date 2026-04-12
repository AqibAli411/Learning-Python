# exception handling - dealing with errors
# try/except blocks

# without exception handling - program crashes
# print(10 / 0)  # ZeroDivisionError!

# with exception handling
try:
    result = 10 / 0
except:
    print("An error occurred!")

# catching specific exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# multiple except blocks
try:
    numbers = [1,2,3]
    print(numbers[10])  # IndexError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except IndexError:
    print("Index out of range!")

# catching multiple exceptions in one block
try:
    # some code
    x = int("hello")  # ValueError
except (ValueError,TypeError):
    print("Value or Type error occurred!")

# getting error message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: division by zero

# else block - runs if no exception
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # this runs

# finally block - always runs (cleanup code)
try:
    file = open("test.txt","r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs")
    # file.close()  # cleanup

# practical example - user input
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative!")
            continue
        break
    except ValueError:
        print("Please enter a valid number!")

print(f"Your age is {age}")

# raising exceptions
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive!")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(e)

# custom exceptions (advanced)
class TooYoungError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise TooYoungError("Must be 18 or older!")
    return True

try:
    check_age(15)
except TooYoungError as e:
    print(e)

# common exceptions:
# ValueError - invalid value
# TypeError - wrong type
# IndexError - index out of range
# KeyError - key not in dictionary
# FileNotFoundError - file doesnt exist
# ZeroDivisionError - division by zero
# AttributeError - attribute doesnt exist

# nested try-except
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner exception caught")
        raise  # re-raise the exception
except:
    print("Outer exception caught")

# this was giving error before i added the int() thing
