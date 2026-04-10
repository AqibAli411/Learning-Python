# File Handling

reading and writing files in python

## file modes:
- "r" - read only
- "w" - write (overwrites!)
- "a" - append to end
- "r+" - read and write
- "x" - create new (error if exists)

## important:
- ALWAYS close files after opening
- use `with` statement - auto closes
- use try/except for FileNotFoundError

## reading:
- .read() - entire file as string
- .readline() - one line
- .readlines() - all lines as list
- can iterate with for loop

## writing:
- .write(string) - write string
- .writelines(list) - write list of strings

mistakes i made:
- forgot to close file = bad!
- used "w" mode and accidentally deleted file contents
- forgot \n for new lines

the with statement is way better than manually closing files

todo:
- learn about json files
- learn about pickle for saving python objects
- understand binary file modes (rb, wb)
