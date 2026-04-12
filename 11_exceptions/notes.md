# Exception Handling

try/except to handle errors without crashing

## syntax:
```
try:
    # code that might fail
except ExceptionType:
    # handle error
else:
    # runs if no error
finally:
    # always runs
```

## common exceptions:
- ValueError
- TypeError  
- IndexError
- KeyError
- FileNotFoundError
- ZeroDivisionError

## important:
- can catch multiple exception types
- use `as e` to get error message
- finally block for cleanup code
- can raise exceptions with `raise`
- can create custom exceptions

mistakes i made:
- using bare except (should specify exception type)
- forgetting that finally always runs even if return in try

the else block is useful but i keep forgetting about it

todo: learn more about custom exceptions and when to use them
