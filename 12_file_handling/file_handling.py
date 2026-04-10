# file handling - reading and writing files
# this is useful for saving data!

# WRITING TO FILES

# write mode - creates new file or overwrites existing
file = open("test.txt","w")
file.write("Hello, World!\n")
file.write("This is a test file.\n")
file.close()  # important! always close files

# better way - using with statement (auto closes)
with open("test.txt","w") as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")
# file closes automatically here

# append mode - adds to end of file
with open("test.txt","a") as file:
    file.write("This line was appended.\n")

# writing multiple lines
lines = ["Line 1\n","Line 2\n","Line 3\n"]
with open("test.txt","w") as file:
    file.writelines(lines)

# READING FROM FILES

# read entire file
with open("test.txt","r") as file:
    content = file.read()
    print(content)

# read line by line
with open("test.txt","r") as file:
    for line in file:
        print(line.strip())  # strip removes \n

# read all lines into list
with open("test.txt","r") as file:
    lines = file.readlines()
    print(lines)

# read one line at a time
with open("test.txt","r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(line1)
    print(line2)

# checking if file exists
import os
if os.path.exists("test.txt"):
    print("File exists!")
else:
    print("File not found!")

# deleting file
# os.remove("test.txt")  # be careful with this!

# working with paths
# os.path.join("folder","file.txt")  # creates proper path
# os.makedirs("new_folder")  # create directory

# exception handling with files
try:
    with open("nonexistent.txt","r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# reading and writing together
# read file, modify, write back
try:
    with open("test.txt","r") as file:
        lines = file.readlines()
    
    # modify lines
    lines.append("New line added!\n")
    
    with open("test.txt","w") as file:
        file.writelines(lines)
except FileNotFoundError:
    print("File not found!")

# working with CSV (comma separated values)
# write CSV
with open("data.csv","w") as file:
    file.write("name,age,city\n")
    file.write("Alice,25,NYC\n")
    file.write("Bob,30,LA\n")

# read CSV
with open("data.csv","r") as file:
    for line in file:
        data = line.strip().split(",")
        print(data)

# file modes:
# "r" - read (default)
# "w" - write (overwrites)
# "a" - append
# "r+" - read and write
# "x" - create new file (error if exists)

# always use 'with' statement - it handles closing automatically
# i forgot to close a file once and it caused problems
