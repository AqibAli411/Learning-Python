# string methods and manipulation
# strings are way more powerful than i thought

text = "hello world"
print(text)

# string methods
print(text.upper())  # HELLO WORLD
print(text.lower())  # hello world  
print(text.capitalize())  # Hello world
print(text.title())  # Hello World - capitalizes each word

# length
print(len(text))  # 11 characters

# replacing
new_text = text.replace("world","python")
print(new_text)  # hello python

# splitting - this is useful!
words = text.split()  # splits by space
print(words)  # ['hello', 'world']

# joining
joined = "-".join(words)
print(joined)  # hello-world

# string indexing (starts at 0!)
first_char = text[0]  # h
print(first_char)
last_char = text[-1]  # d - negative index from end
print(last_char)

# slicing [start:end]
print(text[0:5])  # hello
print(text[6:])  # world
print(text[:5])  # hello

# checking if substring exists
print("world" in text)  # True
print("python" in text)  # False

# f-strings - finally figured these out!
name = "Alex"
age = 25
# old way:
print("My name is " + name + " and I am " + str(age))
# new way (so much better):
print(f"My name is {name} and I am {age}")  # i dont know why this works but it does

# multiline strings
long_text = """This is a 
multiline string
pretty cool"""
print(long_text)

# strip whitespace
messy = "  hello  "
print(messy.strip())  # removes spaces from ends
