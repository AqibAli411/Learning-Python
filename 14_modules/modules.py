# modules and imports
# using code from other files

# importing built-in modules
import math
print(math.pi)  # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.pow(2,3))  # 8.0

# import specific functions
from math import sqrt,pi
print(sqrt(25))  # 5.0
print(pi)

# import with alias
import math as m
print(m.ceil(4.2))  # 5

# import everything (not recommended)
# from math import *

# random module
import random
print(random.randint(1,10))  # random int between 1 and 10
print(random.choice(["apple","banana","cherry"]))  # random choice
print(random.random())  # random float between 0 and 1

numbers = [1,2,3,4,5]
random.shuffle(numbers)  # shuffles in place
print(numbers)

# datetime module
import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

today = datetime.date.today()
print(today)

# os module - operating system stuff
import os
print(os.getcwd())  # current working directory
# os.mkdir("new_folder")  # create directory
# os.listdir()  # list files in directory

# sys module
import sys
print(sys.version)  # python version
# print(sys.argv)  # command line arguments

# creating your own module
# just create a .py file with functions/classes
# then import it!

# example: create mymodule.py with:
# def greet(name):
#     return f"Hello, {name}!"
# 
# PI = 3.14159

# then use it:
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.PI)

# or:
# from mymodule import greet
# print(greet("Bob"))

# checking available functions in module
print(dir(math))  # lists all functions/variables

# getting help
# help(math)  # shows documentation
# help(math.sqrt)  # help for specific function

# common useful modules:
# - math: mathematical functions
# - random: random numbers
# - datetime: dates and times
# - os: operating system interface
# - sys: system-specific parameters
# - json: JSON encoding/decoding
# - re: regular expressions
# - collections: specialized container datatypes
# - itertools: functions for iterators

# installing external modules with pip:
# pip install package_name
# then import package_name

# example with requests (need to install first):
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# i think i need to review this when i start using external packages
