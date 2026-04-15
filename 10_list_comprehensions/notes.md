# List Comprehensions

shorter syntax for creating lists from other iterables

## basic syntax:
`[expression for item in iterable]`

## with condition:
`[expression for item in iterable if condition]`

## with if-else:
`[expr_if_true if condition else expr_if_false for item in iterable]`

## also works for:
- dictionary comprehensions: `{key: value for item in iterable}`
- set comprehensions: `{expression for item in iterable}`

## pros:
- more concise
- faster than regular loops
- more "pythonic"

## cons:
- can be hard to read if too complex
- dont overuse - sometimes regular loop is clearer

took me a while to understand the syntax, especially with if-else

the order is weird: [WHAT_TO_DO for ITEM in LIST if CONDITION]

todo: practice more complex comprehensions
