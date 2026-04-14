# Classes and Objects (OOP)

object oriented programming - organizing code into objects

## key concepts:
- class = blueprint
- object = instance of class
- __init__ = constructor (runs when creating object)
- self = refers to the instance

## instance vs class variables:
- instance variables: unique to each object (self.variable)
- class variables: shared by all objects

## methods:
- regular methods: take self as first parameter
- @staticmethod: dont need self or cls
- @classmethod: take cls as first parameter

## inheritance:
- create new class based on existing class
- use super() to call parent methods
- can override parent methods

## special methods:
- __init__ - constructor
- __str__ - string representation
- __repr__ - official representation
- __len__, __add__, etc.

things that confused me:
- why do we need self everywhere??
- difference between @staticmethod and @classmethod
- when to use inheritance vs composition

this is a big topic, need more practice with real examples

todo:
- learn about multiple inheritance
- understand property decorators
- practice more with inheritance
