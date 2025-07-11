"""
- Functions -
A. Create a function named add_numbers that takes two parameters, a and b, and 
returns their sum. Test the function with values 10 and 15.
B. Create a function named calculate_area that calculates the area of a rectangle. 
Add a docstring explaining what the function does and use type annotations for parameters 
and the return value.
C. Write a function that takes a string as a parameter and returns the count of vowels (a, e, i, o, u)
in the string.
D. Write a function that calculates the factorial of a given number n using a for loop.
E. Write a function that takes a string as a parameter and returns True if the string is a palindrome 
(reads the same forwards and backwards), and False otherwise.
F. Write a function that takes a string as a parameter and returns the reverse of the string. 
Use a for loop to iterate through the characters in the string.
G. Write a function that takes a number as a parameter and prints whether it's positive, negative, 
or zero using if-elif-else statements.
H. Write a function that takes a list of boolean values as a parameter and returns the count of True
and False values in the list. Use a for loop and if statements.
I. Write a function that checks if a given number is a prime number. Return True if it's prime, and 
False if it's not. Use a for loop and conditionals.
J. Write a function that takes a list of numbers as a parameter and returns the largest number in the 
list. Use an if statement to track the largest number.
K. Write a program that calculates the sum of all even numbers from 1 to a given number n. Use a for 
loop and an if statement.
L. Write a program that prints numbers from 1 to 10. For multiples of 3, print "Fizz" instead of the 
number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

Quiz.
1. What is a function in Python?
    a) A variable
    b) A block of reusable code
    c) A loop construct
    d) An if-else statement

2. How do you define a function in Python?
    a) def function_name()
    b) function function_name()
    c) define function_name()
    d) define function_name:

3. What is the purpose of a return statement in a function?
    a) To terminate the function
    b) To print a message
    c) To return a value from the function
    d) To define the function's name

4. Can a Python function return multiple values?
    a) Yes
    b) No

5. What is a docstring in Python?
    a) A debugging tool
    b) A function that prints debugging information
    c) A comment used for explaining the purpose and usage of a function, class or module
    d) A data type

6. How do you write a docstring in a Python function?
    a) Using triple single-quotes or triple double-quotes at the beginning of the function
    b) Using the docstring keyword
    c) Using a single quote at the beginning of the function
    d) Using the doc keyword

7. What is the purpose of type annotations in Python?
    a) To enforce strict data types in Python programs
    b) To improve the performance of functions
    c) To provide hints about the expected types of arguments and return values
    d) To comment on the function's implementation

8. How do you add type annotations to a function in Python?
    a) By using the type keyword
    b) By writing the types as comments next to the variables
    c) By using the annotate keyword
    d) By using a colon after the variable name

9. What is a type hint in Python?
    a) A mandatory type requirement for function parameters
    b) A suggestion for the expected type of a variable or expression
    c) A data type in Python
    d) A keyword to define custom types

10. What is the benefit of using type hints in Python?
    a) It improves the performance of functions
    b) It makes the code more readable and self-explanatory
    c) It enforces strict data types in Python programs
    d) It is a requirement for all Python functions

11. How do you specify the return type of a function in a type hint?
    a) By using -> followed by the return type
    b) By using return_type = followed by the return type
    c) By using returns followed by the return type
    d) By using return: followed by the return type

12. What is the purpose of using type annotations for function parameters and return values?
    a) To enforce type casting
    b) To improve the speed of execution
    c) To make the code more understandable and maintainable
    d) To reduce the need for testing

13. What does the following Python code snippet do?
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")

    a) Defines a function to greet a person by name
    b) Prints the word "Alice"
    c) Prints "Hello, world!"
    d) Defines a loop to greet multiple people

14. What is the primary purpose of the following Python function?
    def calculate_average(numbers):
        \"\"\"Calculates the average of a list of numbers.\"\"\"
        total = sum(numbers)
        count = len(numbers)
        return total / count

    a) To calculate the sum of a list of numbers
    b) To calculate the median of a list of numbers
    c) To calculate the average of a list of numbers
    d) To calculate the maximum number in a list

15. What is the output of the following Python code snippet?
    def is_even(num):
        return num % 2 == 0

    print(is_even(4))

    a) True
    b) False
    c) 4
    d) Error

16. How do you call the function is_even from question 15 to check if the number 7 is even?
    a) is_even(7)
    b) is_even(num=7)
    c) is_even(num)
    d) is_even(is_even(7))

17. What does the following Python code snippet do?
    def print_numbers(n):
        for i in range(n):
            print(i)

    print_numbers(5)

    a) Prints the numbers 0 to 4
    b) Prints the number 5
    c) Prints the numbers 1 to 5
    d) Prints the numbers 0 to 5

18. What does the following Python code snippet do?
    def absolute_value(num):
        if num >= 0:
            return num
        else:
            return -num

    result = absolute_value(-5)

    a) Calculates the square root of a number
    b) Calculates the absolute value of a number
    c) Calculates the factorial of a number
    d) Calculates the exponentiation of a number

19. What is the output of the following Python code snippet?
    def greet(time):
        if time < 12:
            return "Good morning!"
        elif time < 17:
            return "Good afternoon!"
        else:
            return "Good evening!"

    print(greet(10))

    a) Good morning!
    b) Good afternoon!
    c) Good evening!
    d) Error

20. What does the following Python code snippet do?
    def square(num):
        return num ** 2

    numbers = [1, 2, 3, 4]
    squared_numbers = [square(num) for num in numbers]

    a) Doubles each number in the list numbers
    b) Squares each number in the list numbers
    c) Computes the square root of each number in the list numbers
    d) Adds 1 to each number in the list numbers

21. What is the purpose of using functions with loops in Python?
    a) To define the loop's condition
    b) To modularize code and avoid repetition
    c) To improve the loop's performance
    d) To define the loop's increment

22. What is the purpose of using functions with if statements in Python?
    a) To define the if statement's condition
    b) To modularize code and avoid repetition
    c) To improve the if statement's performance
    d) To define the if statement's action
"""


# - Functions -
# Exercise A
# METHOD 1
a = int(input("Please enter the first summand:\n>> "))
b = int(input("Please enter the second summand:\n>> "))

def add_numbers(a,b):
    return a + b 

sum = add_numbers(a, b)
print(f"The sum of the two numbers: {sum}")
print("-------------------------------------")

# METHOD 2
def add_numbers():
    a = int(input("Please enter the first summand:\n>> "))
    b = int(input("Please enter the second summand:\n>> "))
    sum = a + b
    print(f"The sum of the two numbers: {sum}")

add_numbers()
print("-------------------------------------")

# METHOD 3
a = int(input("Please enter the first summand:\n>> "))
b = int(input("Please enter the second summand:\n>> "))

def add_numbers(a,b):
    sum = a + b 
    print(f"The sum of the two numbers: {sum}")

add_numbers(a, b)
print("-------------------------------------")



# Exercise B
# METHOD 1
c = int(input("Please enter the first side of the rectangle:\n>> "))
d = int(input("Please enter the second side of the rectangle:\n>> "))

def calculate_area(c, d):
    s = c * d
    print(f"The area of a rectangle = {s}")

calculate_area(c, d)
print("-------------------------------------")

# METHOD 2
def calculate_area():
    c = int(input("Please enter the first side of the rectangle:\n>> "))
    d = int(input("Please enter the second side of the rectangle:\n>> "))
    s = c * d
    print(f"The area of a rectangle = {s}")

calculate_area()
print("-------------------------------------")

# METHOD 3
c = int(input("Please enter the first side of the rectangle:\n>> "))
d = int(input("Please enter the second side of the rectangle:\n>> "))

def calculate_area(c, d):
    return c * d

s = calculate_area(c, d)
print(f"The area of a rectangle = {s}")
print("-------------------------------------")



# Exercise C
# METHOD 1
string = input("Please enter any string:\n>> ")
vowels = "aeiouAEIOU"

def count_of_vowels(string, vowels):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

sum = count_of_vowels(string, vowels)
print(f"There are {sum} vowels in this stringer!")
print("-------------------------------------")

# METHOD 2
def count_of_vowels():
    string = input("Please enter any string:\n>> ")
    vowels = "aeiouAEIOU"
    count = 0
    
    for i in string:
        if i in vowels:
            count += 1
    print(f"There are {count} vowels in this stringer!")

count_of_vowels()
print("-------------------------------------")

# METHOD 3
string = input("Please enter any string:\n>> ")
vowels = "aeiouAEIOU"

def count_of_vowels(string, vowels):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print(f"There are {count} vowels in this stringer!")

count_of_vowels(string, vowels)
print("-------------------------------------")


    
# Exercise D
# METHOD 1
def factorial():
    num = int(input("Please enter the number whose factorial you want to know:\n>> "))
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial {num} = {result}")

factorial() 
print("-------------------------------------")

# METHOD 2
num = int(input("Please enter the number whose factorial you want to know:\n>> "))
result = 1

def factorial(num, result):
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial {num} = {result}")

factorial(num, result) 
print("-------------------------------------")

# METHOD 3
num = int(input("Please enter the number whose factorial you want to know:\n>> "))
result = 1

def factorial(num, result):
    for i in range(1, num + 1):
        result *= i
    return result

multiplication = factorial(num, result)
print(f"Factorial {num} = {multiplication}")
print("-------------------------------------")



# Exercise E
strong = input("Please enter any srting:\n>> ")

def palindrome_string(strong):
    return strong == strong[::-1]
    
print(palindrome_string(strong))
print("-------------------------------------")



# Exercise F
string = input("Please enter any string:\n>> ")

def reversed_string(string):
    return string[::-1]

print(reversed_string(string))
print("-------------------------------------")



# Exercise G
def checking_for_sign():
    number = int(input("Please enter any intager:\n>> "))
    
    if number > 0:
        print("It's positive number!")
    elif number < 0:
        print("It's negative number!")
    else:
        print("It's ZERO!")

checking_for_sign()
print("-------------------------------------")



# Exercise H
bool_list = [True, False, True, True, False, False, True]

def bools_count(bool_list):
    true_count = 0
    false_count = 0

    for i in bool_list:
        if i == True:
            true_count += 1
        else:
            false_count += 1
    return true_count, false_count

true_count, false_count = bools_count(bool_list)
print(f"True values = {true_count}")
print(f"False values = {false_count}")
print("-------------------------------------")



# Exercise I
num = int(input("Please enter any number:\n>> "))

def checks_prime_number(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    else:
        return True
    
prime_numbers = checks_prime_number(num)
print(f"Prime numbers: {prime_numbers}")
print("-------------------------------------")


    
# Exercise J
num_list = [133, 89, 69, 182, 54, 29, 356]

def largest_number(num_list):
    largest = num_list[0]
    
    for num in num_list:
        if num > largest:
            largest = num  
    return largest

print(f"The largest number in this lisy: {largest_number(num_list)}")
print("-------------------------------------")



# Exercise K
n = int(input("Plaese enter any number:\n>> "))

def sum_even_numbers(n):
    sum = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(f"The sum of all even numbers from 1 to {n}: {sum_even_numbers(n)}")
print("-------------------------------------")



# Exercise L
def multiples_num():
    for i in range(1, 11):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
multiples_num()
print("-------------------------------------")



# Quiz.
# 1. b
# 2. a
# 3. c
# 4. a
# 5. c
# 6. a
# 7. c
# 8. d
# 9. b
# 10. b
# 11. a
# 12. c
# 13. a
# 14. c
# 15. a
# 16. a
# 17. a
# 18. b
# 19. a
# 20. b
# 21. b 
# 22. b