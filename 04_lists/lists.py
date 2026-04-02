# lists - ordered, mutable collections
# basically arrays but python calls them lists

# creating lists
my_list = [1,2,3,4,5]
names = ["Alice","Bob","Charlie"]
mixed = [1,"hello",3.14,True]  # can mix types!
print(my_list)
print(names)

# accessing elements
print(names[0])  # Alice
print(names[-1])  # Charlie (last element)

# changing elements
names[1] = "Bobby"
print(names)  # ['Alice', 'Bobby', 'Charlie']

# adding elements
names.append("David")  # adds to end
print(names)

names.insert(1,"Eve")  # insert at position 1
print(names)

# removing elements
names.remove("Eve")  # removes first occurrence
print(names)

popped = names.pop()  # removes and returns last element
print(popped)
print(names)

# list methods
numbers = [3,1,4,1,5,9,2,6]
print(numbers)

numbers.sort()  # sorts in place
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.reverse()
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

print(numbers.count(1))  # how many 1s? = 2
print(numbers.index(5))  # position of 5? = 2

# length
print(len(numbers))

# checking if element exists
print(5 in numbers)  # True
print(100 in numbers)  # False

# slicing (same as strings)
print(numbers[2:5])  # [5, 4, 3]
print(numbers[:3])  # first 3 elements
print(numbers[-2:])  # last 2 elements

# copying lists
# list2 = list1  # this doesnt copy! both point to same list
original = [1,2,3]
copy = original.copy()  # proper way to copy
# or: copy = original[:]  # this also works apparently
copy.append(4)
print(original)  # [1, 2, 3]
print(copy)  # [1, 2, 3, 4]

# concatenating lists
list1 = [1,2,3]
list2 = [4,5,6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# nested lists (lists inside lists)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])  # [1, 2, 3]
print(matrix[0][1])  # 2 - maybe theres a better way but okay
