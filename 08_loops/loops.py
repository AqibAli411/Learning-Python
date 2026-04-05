# loops - for and while
# repeating code without copy-pasting

# FOR LOOPS

# looping through list
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)

# looping through range
for i in range(5):  # 0 to 4
    print(i)

for i in range(2,8):  # 2 to 7
    print(i)

for i in range(0,10,2):  # 0 to 9, step by 2
    print(i)  # 0,2,4,6,8

# looping through string
for char in "Python":
    print(char)

# looping through dictionary
person = {"name": "Alex","age": 25,"city": "NYC"}
for key in person:
    print(key,person[key])

# better way:
for key,value in person.items():
    print(f"{key}: {value}")

# enumerate - get index and value
fruits = ["apple","banana","cherry"]
for index,fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# WHILE LOOPS

# basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # dont forget this or infinite loop!

# while with condition
password = ""
while password != "python":
    password = input("Enter password: ")
    if password != "python":
        print("Wrong password, try again")
print("Access granted!")

# BREAK - exit loop early
for i in range(10):
    if i == 5:
        break  # stops loop when i is 5
    print(i)  # prints 0,1,2,3,4

# CONTINUE - skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)  # prints 1,3,5,7,9

# nested loops
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# practical example - multiplication table
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} x {j} = {i*j}")
    print()  # blank line

# while True with break (common pattern)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# else with loops (weird but exists)
# runs if loop completes without break
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # this runs

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")  # this DOESNT run because of break

# i dont know why this works but it does

# TODO: figure out enumerate() tomorrow
