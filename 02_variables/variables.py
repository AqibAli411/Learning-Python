# learning about variables and data types
# took me forever to figure out you dont need to declare types

# integers (whole numbers)
age = 25
year = 2024
print("Age:",age)

# floats (decimal numbers)
price = 19.99
temperature = -5.5
print("Price:",price)

# strings (text)
name = "Alex"
city = 'New York'  # single or double quotes both work i guess
print("Name:",name)

# booleans (True/False)
is_student = True
has_license = False
print("Student?",is_student)

# you can change variable types?? this is weird coming from other languages
x = 5
print(x)
x = "now im a string"
print(x)
x = 3.14
print(x)  # python just lets you do this

# checking types
print(type(age))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(name))  # <class 'str'>

# converting between types
num_string = "100"
num_int = int(num_string)  # this was giving error before i added the int() thing
print(num_int + 50)  # now it works!

# print(num_string + 50)  # this breaks - cant add string and number

# print('debug: variable is', x)  # forgot to remove
