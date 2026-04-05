# if/elif/else statements
# making decisions in code!

# basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# comparison operators
x = 10
y = 5
print(x == y)  # equal to
print(x != y)  # not equal to
print(x > y)   # greater than
print(x < y)   # less than
print(x >= y)  # greater than or equal
print(x <= y)  # less than or equal

# logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

if age < 18 or not has_license:
    print("You cannot drive")

# checking multiple conditions
temperature = 75
if temperature > 80:
    print("Its hot")
elif temperature > 60:
    print("Its nice")
else:
    print("Its cold")

# nested if statements
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not positive")

# checking if value exists
my_list = [1,2,3,4,5]
if 3 in my_list:
    print("3 is in the list")

# checking empty/not empty
empty_list = []
if empty_list:
    print("List has items")
else:
    print("List is empty")  # this runs

# ternary operator (one line if-else)
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# this is confusing but kinda cool i guess
