# classes and objects - OOP basics
# still wrapping my head around this

# defining a class
class Dog:
    # constructor - runs when creating new object
    def __init__(self,name,age):
        self.name = name  # instance variable
        self.age = age
    
    # method
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def get_age(self):
        return self.age

# creating objects (instances)
dog1 = Dog("Buddy",3)
dog2 = Dog("Max",5)

print(dog1.name)  # Buddy
print(dog2.name)  # Max

dog1.bark()  # Buddy says Woof!
dog2.bark()  # Max says Woof!

# class with more features
class Person:
    # class variable (shared by all instances)
    species = "Human"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
    
    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now {self.age} years old")

person1 = Person("Alice",25)
person1.greet()
person1.have_birthday()

# accessing class variable
print(Person.species)  # Human
print(person1.species)  # Human

# inheritance - creating class based on another class
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)  # call parent constructor
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying")
    
    # overriding parent method
    def greet(self):
        print(f"Hi, I'm {self.name}, student ID: {self.student_id}")

student1 = Student("Bob",20,"S12345")
student1.greet()  # uses overridden method
student1.study()
student1.have_birthday()  # inherited from Person

# another example - bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        return self.balance

account = BankAccount("Alice",1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")

# private variables (sort of)
class MyClass:
    def __init__(self):
        self.public = "I'm public"
        self._protected = "I'm protected"  # convention: dont access directly
        self.__private = "I'm private"  # name mangling
    
    def get_private(self):
        return self.__private

obj = MyClass()
print(obj.public)
print(obj._protected)  # can still access but shouldnt
# print(obj.__private)  # this breaks!
print(obj.get_private())  # proper way

# string representation
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

book = Book("Python Basics","John Doe")
print(book)  # uses __str__
print(repr(book))  # uses __repr__

# static methods and class methods
class MathOperations:
    @staticmethod
    def add(x,y):
        return x + y
    
    @classmethod
    def multiply(cls,x,y):
        return x * y

print(MathOperations.add(5,3))  # 8
print(MathOperations.multiply(5,3))  # 15

# why does this work??
# still confused about when to use @staticmethod vs @classmethod
# i have no idea if this is the 'pythonic' way
