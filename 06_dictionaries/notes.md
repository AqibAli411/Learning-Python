# Dictionaries

key-value pairs! super useful for storing related data

## syntax:
```
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
```

## important methods:
- .get(key) - safe access
- .keys() - all keys
- .values() - all values  
- .items() - key-value pairs
- .pop(key) - remove and return
- .update() - merge dictionaries

## notes:
- keys must be unique
- keys must be immutable (strings, numbers, tuples ok)
- values can be anything
- unordered (well, ordered since python 3.7 but dont rely on it?)

mistakes:
- tried to use list as key = ERROR
- forgot that dict["key"] crashes if key doesnt exist (use .get() instead)

todo: learn about defaultdict and Counter (saw these mentioned)
