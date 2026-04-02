# tuples and sets - still figuring these out

# TUPLES - like lists but immutable (cant change them)
# use parentheses instead of brackets

my_tuple = (1,2,3,4,5)
print(my_tuple)

# accessing works same as lists
print(my_tuple[0])  # 1
print(my_tuple[-1])  # 5

# but you CANT change them
# my_tuple[0] = 10  # this gives error!

# why use tuples?
# - faster than lists
# - protect data from being changed
# - can use as dictionary keys (lists cant)

coordinates = (10.5, 20.3)
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# tuple unpacking - this is cool!
x,y = coordinates
print(x)  # 10.5
print(y)  # 20.3

# single element tuple needs comma (weird)
single = (5,)  # without comma its just a number in parentheses
print(type(single))

# SETS - unordered collection of unique items
# use curly braces

my_set = {1,2,3,4,5}
print(my_set)

# no duplicates allowed!
numbers = {1,2,2,3,3,3,4,5}
print(numbers)  # {1, 2, 3, 4, 5} - duplicates removed automatically

# adding to sets
my_set.add(6)
print(my_set)

# removing from sets
my_set.remove(3)  # error if not found
# my_set.discard(100)  # no error if not found
print(my_set)

# set operations (like math class)
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# union - all elements from both
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))  # same thing

# intersection - only common elements
print(set1 & set2)  # {3, 4}
print(set1.intersection(set2))  # same thing

# difference - in first but not second
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))  # same thing

# checking membership (fast!)
print(3 in my_set)  # True

# converting between types
list_with_dupes = [1,1,2,2,3,3]
unique_set = set(list_with_dupes)
print(unique_set)  # {1, 2, 3}
back_to_list = list(unique_set)
print(back_to_list)  # [1, 2, 3]

# note: sets are unordered so you cant index them
# print(my_set[0])  # this breaks!
