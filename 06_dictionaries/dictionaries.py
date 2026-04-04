# dictionaries - key:value pairs
# like a real dictionary where you look up words (keys) to get definitions (values)

# creating dictionary
person = {
    "name": "Alex",
    "age": 25,
    "city": "New York",
    "is_student": True
}
print(person)

# accessing values
print(person["name"])  # Alex
print(person["age"])  # 25

# safer way to access (doesnt crash if key missing)
print(person.get("name"))  # Alex
print(person.get("country"))  # None (instead of error)
print(person.get("country","USA"))  # USA (default value)

# adding/updating
person["email"] = "alex@email.com"  # adds new key
person["age"] = 26  # updates existing key
print(person)

# removing
del person["is_student"]
print(person)

# or use pop
email = person.pop("email")
print(email)
print(person)

# checking if key exists
print("name" in person)  # True
print("phone" in person)  # False

# getting all keys, values, items
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alex', 26, 'New York'])
print(person.items())  # dict_items([('name', 'Alex'), ('age', 26), ('city', 'New York')])

# looping through dictionary
for key in person:
    print(key,person[key])

# better way:
for key,value in person.items():
    print(f"{key}: {value}")

# nested dictionaries
students = {
    "student1": {"name": "Alice","grade": 90},
    "student2": {"name": "Bob","grade": 85},
    "student3": {"name": "Charlie","grade": 95}
}
print(students["student1"]["name"])  # Alice
print(students["student2"]["grade"])  # 85

# dictionary from lists
keys = ["name","age","city"]
values = ["Alex",25,"NYC"]
combined = dict(zip(keys,values))
print(combined)  # why does this work??

# copying dictionaries
original = {"a": 1,"b": 2}
copy = original.copy()
copy["c"] = 3
print(original)  # {'a': 1, 'b': 2}
print(copy)  # {'a': 1, 'b': 2, 'c': 3}
