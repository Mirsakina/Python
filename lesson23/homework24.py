"""
- Functions -
A. Define a function greet_with_message that takes a username and a 
message (with a default value of "Hello") as parameters and prints 
the message along with the username.
B. Write a function calculate_discount that calculates the discounted 
price of an item based on the original price and a discount rate 
(default to 10%). Return the discounted price.
C. Create a function sum_all that takes any number of arguments using 
the asterisk operator in the parameter definition and returns the sum 
of all the arguments.
D. Write a function calculate_product that takes at least two arguments
and calculates their product. Use the asterisk operator in the parameter 
definition to handle multiple arguments.
E. Write a function sum_of_numbers that takes a variable number of integers
as parameters and returns their sum.
F. Create a function calculate_power that takes two parameters: a base number
and an exponent, and returns the result of raising the base to the given exponent.
G. Define a function named greet_user that takes a parameter username and prints 
a greeting message like: "Hello, [username]!".
H. Write a function called calculate_area that takes the radius of a circle as a 
parameter and returns the area of the circle.
I. Create a function average that takes a list of numbers as a parameter and calculates 
the average of those numbers.
J. Implement a function maximum_number that takes a variable number of integers as 
parameters and returns the largest number.
K. Define a function greet_with_salutation that takes a username and a salutation 
(with a default value of "Mr.") as parameters and prints a greeting using the provided salutation.
L. Write a function calculate_cost that calculates the total cost of purchasing a
given quantity of items, considering a unit price and tax rate (default tax rate is 5%).
M. Create a function concatenate_strings that takes a variable number of strings as parameters 
and concatenates them into a single string, separated by spaces.
N. Write a function calculate_sum_and_product that takes at least two numbers as arguments 
and returns both their sum and product. Use the asterisk operator in the parameter definition 
to handle multiple arguments.
O. Write a function find_max_min that takes a list of numbers as a parameter and returns both 
the maximum and minimum numbers from the list. Use if statements to handle edge cases.
P. Create a function calculate_grade that takes a student's numerical score as a parameter and
returns their corresponding letter grade based on the following scale:
90-100: 'A'
80-89: 'B'
70-79: 'C'
60-69: 'D'
Below 60: 'F'
Handle any invalid scores (less than 0 or greater than 100) by returning 'Invalid Score'.
Q. Write a function solve_quadratic that takes the coefficients of a quadratic equation 
(a, b, c) as parameters and returns the real roots (if any) of the quadratic equation. 
Use the quadratic formula.
R. Implement a function is_palindrome that takes a string as a parameter and returns True
if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
S. Create a function sort_numbers that takes three numbers as parameters and returns them in 
ascending order as a tuple.
T. Write a function calculate_tax that takes an income amount and a tax rate as parameters 
and calculates the tax amount. Return a tuple containing the tax amount and the net income 
(income after tax).
U. Create a function calculate_discounted_price that takes the original price and a discount 
percentage as parameters. Return a tuple containing the discounted price and the amount saved.

Quiz.
1. What does the following function do?
    def greet_user(username):
        print("Hello, " + username + "!")

    a) Greets the user with a customized message.
    b) Prints "Hello, user!".
    c) Defines a function but doesn't execute any action.
    d) Raises an error due to an invalid function definition.

2. Which of the following functions best describes the calculations of the area of a circle?
    a) calculate_circle_area(radius)
    b) compute_circle_area(diameter)
    c) get_circle_area(radius)
    d) calculate_area_circle(radius)

3. What is the purpose of a default parameter in a function?
    a) It ensures the function returns a default value.
    b) It allows the function to have optional parameters.
    c) It restricts the function to accept a specific type of argument.
    d) It is used to specify the default return value of the function.

4. In Python, how do you pass a variable number of arguments to a function?
    a) Using lists as arguments
    b) Using tuples as arguments
    c) Using the asterisk (*) operator in the parameter definition
    d) Using the exclamation mark (!) in the parameter definition

5. Which of the following functions best describes the calculations of the sum of a list of numbers?
    a) sum_list(numbers)
    b) calculate_sum(numbers)
    c) add_numbers(*numbers)
    d) sum_all(*numbers)

6. What does the asterisk (*) operator do in the function definition?
    a) Multiplies the function's output by the provided argument.
    b) Allows the function to take a variable number of arguments.
    c) Raises an error due to an invalid operator usage.
    d) Converts the argument to a string before passing it to the function.

7. Consider the following function:
    def greet_user(username="Guest"):
        print("Hello, " + username + "!")

    What is the default value for the username parameter in this function?
    a) "Guest"
    b) "User"
    c) None
    d) "Hello"

8. In the following function, what happens if no value is provided for the message parameter?
    def greet_with_message(username, message="Hello"):
        print(message + ", " + username + "!")

    a) The function raises an error.
    b) The function uses the default value "Hello" for the message.
    c) The function uses the default value "World" for the message.
    d) The function uses the default value "Hi" for the message.

9. Which of the following is a valid function definition using default parameters?
    a) def calculate_area(radius, pi=3.14159):
    b) def calculate_area(pi=3.14159, radius):
    c) def calculate_area(radius=, pi=3.14159):
    d) def calculate_area(radius=3.14159, pi):

10. Consider the function below:
    def calculate_discount(price, discount_rate=0.1):
        return price * (1 - discount_rate)

    What is the default discount rate used if not provided?
    a) 10%
    b) 20%
    c) 5%
    d) 15%

11. Given the function:
    def multiply(a, b=2):
        return a * b

    If we call multiply(5), what will be the result?
    a) 10
    b) 5
    c) 7
    d) 15

12. In the following function definition, what does the * represent?
    def display_names(*names):
        for name in names:
            print(name)

    a) It denotes multiplication in the function.
    b) It allows passing a variable number of names as arguments.
    c) It signifies that 'names' is a string.
    d) It raises an error in the function.

13. Given the function below:
    def greet_with_messages(*messages):
        for message in messages:
            print(message)

    If we call greet_with_messages("Hello", "Bonjour", "Hola"), how many messages will be printed?
    a) 3
    b) 2
    c) 1
    d) 0

14. Consider the function definition:
    def generate_pattern(symbol='*', count=5):
        return symbol * count

    If we call generate_pattern(count=3), what will be the result?
    a) '***'
    b) '***'
    c) '**'
    d) '*****'

15. You have a list of numbers: [12, 5, 78, 43, 67, 89, 45, 23]. What will the function find_max_min return for this list?
    a) (12, 5)
    b) (5, 89)
    c) (5, 12)
    d) (89, 5)

16. If the score provided to the function calculate_grade is 75, what will be the output of the function?
    a) 'C'
    b) 'B'
    c) 'D'
    d) 'F'
   
17. For the quadratic equation with coefficients a=1, b=-5 and
c=6, what will the function solve_quadratic return?
    a) (-2, 3)
    b) (-3, 2)
    c) (2, 3)
    d) (-2, -3)

18. If the input string to the function is_palindrome is "radar", 
what will the function return?
    a) True
    b) False
      
19. For the input numbers 5, 2, 8, what will be the output of the function sort_numbers?
    a) (2, 5, 8)
    b) (8, 5, 2)
    c) (5, 2, 8)
    d) (2, 8, 5)

20. If the income is $5000 and the tax rate is 20%, what will be the output of 
the function calculate_tax?
    a) (1000, 4000)
    b) (4000, 1000)
    c) (2000, 3000)
    d) (2500, 2500)

21. If the original price is $100 and the discount rate is 25%, what will be the 
output of the function calculate_discounted_price?
    a) (75.0, 25.0)
    b) (25.0, 75.0)
    c) (100.0, 25.0)
    d) (75.0, 100.0)
"""



import math

# Exercise A
def greet_with_message(name, message = "Hello"):
    print(f"{message} {name.capitalize()}!")

greet_with_message("Alice")
greet_with_message("Alice", "Hi")
print("-------------------------------------")


# Exercise B
def calculate_discount(price, discount = 10):
    return price - (price * discount / 100)

discounted_price = calculate_discount(100, 20)
print(f"Discounted price: {discounted_price}")

discounted_price = calculate_discount(100)
print(f"Discounted price: {discounted_price}")
print("-------------------------------------")


# Exercise C
def sum_all(*arguments):
    return sum(arguments)

arguments_count = sum_all(2, 3, 5, 10)
print(f"The sum of all entered arguments {arguments_count}")

arguments_count = sum_all(7, 334, 10)
print(f"The sum of all entered arguments {arguments_count}")
print("-------------------------------------")


# Exercise D
def calculate_product(a, b, *arguments):
    product = a * b
    for i in arguments:
        product *= i
    return product

arguments = calculate_product(2, 3, 5, 9, 10)
print(f"The product of all entered arguments {arguments}")

arguments = calculate_product(2, 3)
print(f"The product of all entered arguments {arguments}")
print("-------------------------------------")


# Exercise E
def sum_of_numbers(*integers):
    return sum(integers)

integers = sum_of_numbers(2, 5, 6, 7) 
print(f"The sum of all entered integers {integers}")

integers = sum_of_numbers(2) 
print(f"The sum of all entered integers {integers}")
print("-------------------------------------")


# Exercise F
def calculate_power(number, exponent):
    return number ** exponent

value = calculate_power(2, 4)
print(f"Result {value}")
    
value = calculate_power(3, 9)
print(f"Result {value}")
print("-------------------------------------")


# Exercise G
def great_user(username):
    print(f"Hello, {username.capitalize()}!")

username = input("Please enter your name:\n>> ")
great_user(username)
print("-------------------------------------")


# Exercise H
def calculate_area(radius):
    s = math.pi * (radius ** 2)
    return s

radius = calculate_area(5)
print(f"The area of the circle {radius}")

radius = calculate_area(2)
print(f"The area of the circle {radius}")
print("-------------------------------------")


# Exercise I
num_list = [1, 4, 5, 4, 2]

def average(num_list):
    return sum(num_list) / len(num_list)

num_average = average(num_list)
print(f"The average of those numbers: {num_average}")
print("-------------------------------------")


# Exercise J
def maximum_number(*integer):
    return max(integer)

integer = maximum_number(434, 324, 116, 12908, 31242, 32)
print(f"The largest number: {integer}")
print("-------------------------------------")


# Exercise K
def greet_with_salutation(user_name, salutation = "Mr."):
    print(f"Hello {salutation} {user_name}!")

greet_with_salutation("Anna",  "Ms.")
greet_with_salutation("Jake")
print("-------------------------------------")


# Exrcise L
def calculate_cost(quantity, unit_price, tax_rate = 5):
    total = quantity * unit_price
    tax = total * tax_rate / 100
    return total + tax

parameters = calculate_cost(5, 24, 3)
print(f"The total cost of purchasing: {parameters}")

parameters = calculate_cost(2, 12)
print(f"The total cost of purchasing: {parameters}")
print("-------------------------------------")


# Exercise M
def concatenate_strings(*strings):
    return " ".join(strings)

strings = concatenate_strings("Hello", "world!")
print(f"The concatenates string: {strings}")
print("-------------------------------------")


# Exercise N
def calculate_sum_and_product(n, m, *arguments):
    numbers = (n, m) + arguments
    total_sum = sum(numbers)
    total_product = 1

    for i in numbers:
        total_product *= i
    return total_sum, total_product

arguments = calculate_sum_and_product(2, 6, 3)
print(f"Sum and product: {arguments}")

arguments = calculate_sum_and_product(3, 4)
print(f"Sum and product: {arguments}")
print("-------------------------------------")


# Exercise O
num_list = [6, 3, 9, 2, 1]

def find_max_min(num_list):
    return max(num_list), min(num_list)

result = find_max_min(num_list)
print(f"Max and min of this list {result}")
print("-------------------------------------")


# Exercise P
def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = int(input("Please enter your numeric score:\n>> "))
letter_grade = calculate_grade(score)
print(f"Your letter grade: {letter_grade}")
print("-------------------------------------")


# Exercise R
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
string = input("Please enter any string:\n>> ")
print(is_palindrome(string))
print("-------------------------------------")


# Exercise S
def sort_numbers(k, l, m):
    return tuple(sorted([k, l, m]))

print(sort_numbers(4, 5, 2))
print("-------------------------------------")


# Exercise T
def calculate_tax(income_amount, tax_rate):
    tax_amount = income_amount * tax_rate / 100
    net_income = income_amount - tax_amount
    return tax_amount, net_income

print(calculate_tax(230, 3))
print(calculate_tax(5000, 20))
print("-------------------------------------")


# Exercise U
def calculate_discounted_price(original_price, discount):
    amount_saved = original_price * discount / 100
    discounted_price = original_price - amount_saved
    return discounted_price, amount_saved

print(calculate_discounted_price(34, 20))
print(calculate_discounted_price(100, 25))
print("-------------------------------------")


# Quiz
# 1. a
# 2. a
# 3. b
# 4. c
# 5. a
# 6. b
# 7. a
# 8. b
# 9. a
# 10. a
# 11. a
# 12. b
# 13. a
# 14. a
# 15. d
# 16. a
# 17. c
# 18. a
# 19. a
# 20. a
# 21. a