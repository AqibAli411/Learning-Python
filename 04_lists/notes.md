# Lists

lists are super useful! ordered and changeable

## creating:
- square brackets []
- can have any types mixed together

## common methods:
- .append(item) - add to end
- .insert(index,item) - add at position
- .remove(item) - remove first match
- .pop() - remove last (or at index)
- .sort() - sort in place
- .reverse() - reverse order
- .count(item) - count occurrences
- .index(item) - find position

## important:
- indexing starts at 0
- negative indices count from end
- slicing works like strings
- use .copy() to actually copy a list

mistakes i made:
- forgot that list2=list1 doesnt copy, they share same data
- tried to use .append() with multiple items (use .extend() for that)
- confused .sort() and sorted() - one modifies original, one returns new

todo:
- learn about list comprehensions (saw this mentioned somewhere)
- understand when to use lists vs tuples
