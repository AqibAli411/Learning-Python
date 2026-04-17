# Modules and Imports

using code from other files/libraries

## importing:
```
import module_name
from module_name import function_name
import module_name as alias
from module_name import *  # dont do this
```

## useful built-in modules:
- math - mathematical functions
- random - random numbers
- datetime - dates and times
- os - file system operations
- sys - system stuff
- json - working with JSON

## creating your own modules:
- just make a .py file
- put functions/classes in it
- import it in other files

## external packages:
- install with pip: `pip install package_name`
- then import normally

## useful functions:
- dir(module) - see whats in module
- help(module) - get documentation

mistakes:
- tried to import module that wasnt installed
- circular imports (file A imports B, B imports A) = bad!
- forgot that module name = file name

todo:
- learn about __name__ == "__main__"
- understand packages vs modules
- learn about virtual environments (venv)
