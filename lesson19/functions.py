"""
- Functions -
A. Define a Python function named greet_user that takes a user's name as a parameter 
and prints a greeting message. Call the function to greet the user by their name.
B. Write a function named calculate_area that takes the radius of a circle as a parameter 
and returns the area of the circle. Print the area of a circle with radius 5 using this function.
C. Create a function named calculate_total_cost that takes the price and quantity of an 
item as parameters and returns the total cost. Print the total cost for an item with a 
price of $10 and a quantity of 3 using this function.
D. Write a function named 'hello' that prints "Hello world". Call this function two times.

Quiz.
1. What is a function in Python?
    a) A named sequence of statements that can be reused.
    b) A built-in data type in Python.
    c) A special type of loop in Python.
    d) A conditional statement in Python.

2. How do you define a function in Python?
    a) Using the def keyword followed by the function name and parameters.
    b) Using the function keyword followed by the function name and parameters.
    c) Using the define keyword followed by the function name and parameters.
    d) Using the func keyword followed by the function name and parameters.

3. What is the purpose of parameters in a Python function?
    a) Parameters define the return value of the function.
    b) Parameters specify the input values that the function expects.
    c) Parameters define the scope of the function.
    d) Parameters are used to create local variables within the function.

4. What is a return statement in a Python function?
    a) It exits the function and returns a value to the calling code.
    b) It prints a value to the console.
    c) It defines the parameters of the function.
    d) It defines a loop inside the function.
    
5. How can you call a function in Python?
    a) Using the call keyword followed by the function name and arguments.
    b) Using the execute keyword followed by the function name and arguments.
    c) Using the function name followed by parentheses and providing the required arguments.
    d) Using the run keyword followed by the function name and arguments.

6. What is the difference between parameters and arguments in a Python function?
    a) Parameters are values passed to a function when calling it, and arguments are 
    the values specified in the function definition.
    b) Parameters and arguments are the same.
    c) Parameters are the values specified in the function definition, and arguments 
    are the values passed to a function when calling it.
    d) Parameters are used in Python 2, and arguments are used in Python 3.

7. Write a Python function named add_numbers that takes two parameters a and b and returns their sum.
    a)
    def add_numbers(a, b):
        return a * b
    b)
    def add_numbers(a, b):
        return a - b
    c)
    def add_numbers(a, b):
        return a + b
    d)
    def add_numbers(a, b):
        return a / b

8. Write a Python function named is_even that takes a single parameter num and returns True if the number
is even and False otherwise.
    a)
    def is_even(num):
        return num % 2 == 0
    b)
    def is_even(num):
        return num / 2 == 0
    c)
    def is_even(num):
        return num * 2 == 0
    d)
    def is_even(num):
        return num + 2 == 0

9. Write a Python function named greet that takes a single parameter name and prints a greeting message.
    a)
    def greet(name):
        print("Hello, " + name + "!")
    b)
    def greet(name):
        return "Hello, " + name + "!"
    c)
    def greet(name):
        return "Hi there!"
    d)
    def greet(name):
        print("Hi there!")

10. Write a Python function named calculate_average that takes a list of numbers and returns their average.
    a)
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)
    b)
    def calculate_average(numbers):
        return sum(numbers) * len(numbers)
    c)
    def calculate_average(numbers):
        return sum(numbers)
    d)
    def calculate_average(numbers):
        return len(numbers) / sum(numbers)

11. Write a Python function named calculate_power that takes two parameters base and exponent 
and returns the result of base raised to the power of exponent.
    a)
    def calculate_power(base, exponent):
        return base**exponent
    b)
    def calculate_power(base, exponent):
        return base*exponent
    c)
    def calculate_power(base, exponent):
        return exponent**base
    d)
    def calculate_power(base, exponent):
        return base^exponent

12. Consider the following Python program:
    def print_greeting():
        print("Hello, world!")

    print_greeting()

    What will this program print?
    a) Hello, world!
    b) print_greeting()
    c) Hello,
    d) world!

13. Consider the following Python program:
    def print_numbers():
        print(1)
        print(2)
        print(3)

    print_numbers()

    What will this program print?
    a)
    1
    2
    3
    b)
    123
    c)
    1
    2
    d)
    3
    2
    1
    
14. Consider the following Python program:
    def print_multiple_messages():
        print("Hello!")
        print("How are you?")
        print("Goodbye!")

    print_multiple_messages()

    What will this program print?
    a)
    Hello!
    How are you?
    Goodbye!
    b)
    Hello!How are you?Goodbye!
    c)
    Hello!How are you?
    Goodbye!
    d)
    Hello!
    How are you?Goodbye!

15. Consider the following Python program:
    def print_values():
        print("Value 1")
        print("Value 2")
        print("Value 3")

    print_values()

    What will this program print?
    a)
    Value 1
    Value 2
    Value 3
    b)
    Value 1Value 2Value 3
    c)
    Value 1
    Value 2
    d)
    Value 3
    Value 2
    Value 1

16. Consider the following Python program:
    def print_repeated_message():
    for _ in range(3):
        print("This is a repeated message.")

    print_repeated_message()

    What will this program print?
    a)
    This is a repeated message.
    This is a repeated message.
    This is a repeated message.
    b)
    This is a repeated message.This is a repeated message.This is a repeated message.
    c)
    This is a repeated message.
    d)
    This is a repeated message.
    This is a repeated message.

17. What is the purpose of the return keyword in a Python function?
    a) To exit the function and return to the calling code.
    b) To return a value or object from the function to the caller.
    c) To define a new variable within the function.
    d) To print a message to the console.

18. What happens if a function in Python does not contain a return statement?
    a) An error is raised, indicating a missing return statement.
    b) The function automatically returns None if there is no return statement.
    c) The function will not execute and throw an exception.
    d) The function will exit without returning anything.

19. What does the return statement without a value return in Python?
    a) It returns the value 0.
    b) It returns an empty string.
    c) It returns None.
    d) It is not valid to have a return statement without a value.

20. What is the data type of the value that can be returned by a Python function?
    a) The data type is determined by the function's name.
    b) The data type is always str (string).
    c) The data type is determined by the return statement.
    d) The data type is always int (integer).

21. Consider the following function:
    def greet():
        print("Hello, world!")

    result = greet()

    What will be the value of result after calling greet()?
    a) None
    b) Hello, world!
    c) An error will occur.
    d) result will not have a value.

22. Can a Python function have both a return statement and print statements inside it?
    a) Yes
    b) No
"""

import math

# - Functions -
# Exercise A
# METHOD 1
def greet_user():
    name = input("Please enter your name:\n>> ")
    print(f"Hello {name.capitalize()}!")

greet_user()
print("-------------------------------------")

# METHOD 2
user_name = input("Please enter your name:\n>> ")

def greet_user(name):
    print(f"Hello {name.capitalize()}!")

greet_user(user_name)
print("-------------------------------------")



# Exercise B
# METHOD 1
def calculate_area():
    radius = int(input("Please enter the value of the circle radius:\n>> "))
    s = round(math.pi * (radius ** 2), 1)
    print(f"The area of the circle with radius {radius} = {s}")

calculate_area()
print("-------------------------------------")

# METHOD 2
radius = int(input("Please enter the value of the circle radius:\n>> "))

def calculate_area(radius):
    s = round(math.pi * (radius ** 2), 1)
    print(f"The area of the circle with radius {radius} = {s}")

calculate_area(radius)
print("-------------------------------------")

# METHOD 3
radius = int(input("Please enter the value of the circle radius:\n>> "))

def calculate_area(radius):
    return round(math.pi * radius ** 2, 1)

area = calculate_area(radius)
print(f"The area of the circle with radius {radius} = {area}")
print("-------------------------------------")



# Exercise C
# METHOD 1
def calculate_total_cost():
    price = int(input("Please enter the price of the product:\n>> "))
    quantity = int(input("Please enter the quantity of the product:\n>> "))
    total_price = price * quantity
    print(f"Total cost of the product: {total_price}$")

calculate_total_cost()
print("-------------------------------------")

# METHOD 2
price = int(input("Please enter the price of the product:\n>> "))
quantity = int(input("Please enter the quantity of the product:\n>> "))

def calculate_total_cost(price, quantity):
    total_price = price * quantity
    print(f"Total cost of the product: {total_price}$")

calculate_total_cost(price, quantity)
print("-------------------------------------")

# METHOD 3
price = int(input("Please enter the price of the product:\n>> "))
quantity = int(input("Please enter the quantity of the product:\n>> "))

def calculate_total_cost(price, quantity):
    return price * quantity

total_price = calculate_total_cost(price, quantity)
print(f"Total cost of the product: {total_price}$")
print("-------------------------------------")



# Exercise D
# METHOD 1
def hello():
    print("Hello world")

hello()
hello()
print("-------------------------------------")

# METHOD 2
def hello():
    print("Hello world")

for i in range(2):
    hello()
print("-------------------------------------")

# METHOD 3
def hello():
    for i in range(2):
        print("Hello world")

hello()



# Quiz.
# 1. a
# 2. a
# 3. b
# 4. a
# 5. c
# 6. c
# 7. c
# 8. a
# 9. a
# 10. a
# 11. a
# 12. a
# 13. a
# 14. a
# 15. a
# 16. a
# 17. b
# 18. b
# 19. c
# 20. c
# 21. a
# 22. a


