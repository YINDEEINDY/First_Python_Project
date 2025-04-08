# Variables
x = 5
y = "Hello, World!"

# Basic Data Types
integer = 10
floating_point = 20.5
string = "Python"
boolean = True

# Lists
fruits = ["apple", "banana", "cherry"]

# Tuples
coordinates = (10.0, 20.0)

# Sets
unique_numbers = {1, 2, 3}

# Dictionaries
person = {"name": "Alice", "age": 25}

# Conditional Statements
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Loops
for fruit in fruits:
    print(fruit)

i = 0
while i < 5:
    print(i)
    i += 1

# Functions
def greet(name):
    return f"Hello, {name}!"

# Classes
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Instantiating a class
dog = Animal("Dog")
print(dog.speak())

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")

