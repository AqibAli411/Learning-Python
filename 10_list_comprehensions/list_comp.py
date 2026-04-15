# list comprehensions - shorter way to create lists
# took me forever to figure this out

# OLD WAY - using loop
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# NEW WAY - list comprehension
squares = [i ** 2 for i in range(10)]
print(squares)  # same result, one line!

# basic syntax: [expression for item in iterable]

# more examples
numbers = [1,2,3,4,5]
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# with strings
fruits = ["apple","banana","cherry"]
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)  # ['APPLE', 'BANANA', 'CHERRY']

# with condition (filtering)
# syntax: [expression for item in iterable if condition]

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# only squares of even numbers
squares_of_evens = [n ** 2 for n in range(10) if n % 2 == 0]
print(squares_of_evens)  # [0, 4, 16, 36, 64]

# with if-else
# syntax: [expression_if_true if condition else expression_if_false for item in iterable]
numbers = [1,2,3,4,5]
result = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(result)  # ['odd', 'even', 'odd', 'even', 'odd']

# nested list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# creating matrix
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# dictionary comprehension (yes this exists too!)
numbers = [1,2,3,4,5]
squared_dict = {n: n**2 for n in numbers}
print(squared_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# set comprehension
numbers = [1,1,2,2,3,3,4,4]
unique_squares = {n**2 for n in numbers}
print(unique_squares)  # {1, 4, 9, 16}

# practical examples

# get lengths of words
words = ["hello","world","python","programming"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6, 11]

# filter and transform
words = ["hello","world","python","hi","programming"]
long_words = [word.upper() for word in words if len(word) > 4]
print(long_words)  # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# extract numbers from mixed list
mixed = [1,"hello",3.14,"world",5,True,"python",10]
numbers_only = [x for x in mixed if type(x) == int or type(x) == float]
print(numbers_only)  # [1, 3.14, 5, 10]

# this is so much cleaner than regular loops!
# but can get confusing if too complex
