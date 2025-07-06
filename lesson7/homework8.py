"""
Note. Try to clear the terminal if appropriate.

- Comments -
If it's appropriate:
A. One-line comment 
B. Multi-line comment

- Programs -
A. Write a program that asks user for their personal data (name, age, nationality).
The program should decoratively print this values to the terminal.
B. Write a simple calculator program that can only sum the values.
If user inputs 10 and 5, the program should print 15
C. Write a string calculator program that adds strings to strings.
If user inputs:
1. 'Hello' and 'World', the program should print 'HelloWorld'.
2. 10 and 5, the program should print 105.
3. 'Hello' and 10, the program should print Hello10

- Modules -
A. Which Python module provides a collection of string constants, such as ascii_letters?
B. If you want to create a password generator that includes both uppercase 
and lowercase letters, which constant from the 'string' module might be useful?
C. What is the purpose of using constants like ascii_letters from the string module in Python programming?
D. What is 'getpass' function from 'getpass' module for?

- Python Tricks -
A. Suppose you have the following variables:
a = "Hello"
b = 5

One-line change the value of 'a' to value of 'b', and vice versa.
Print their values

- Constants -
A. Create a constant variable related to Mathematics.
B. Create a constant variable related to Physics.
C. Create a constant variable related to Price.
D. Create a constant variable related to Time.
E. Are Python constants really carry constant values?

- Math -
A. Round down 57_999.99 to the nearest integer.
B. Find the square root of 57_999.99. Round it to one decimal point.
C. Round up 0.0592481 to the nearest integer.
D. Find the value of 5.5 raised to power 5.

- NoneType -
A. What is None in Python? How is this value described in other programming
languages?
B. What is the best practices of using None in Python?
C. How Python evaluates the NoneType? (True / False)
D. Create any NoneType object. Print it.

- Built-ins -
A. Create two variables (x and y). Using built in function raise 'y' to 'x' power.
B. Using built in function and variables from Task A raise 'x' to 'y' power.
C. Ask user for two integers. Raise first integer to second integer power.

- String Formattings -
A. You have the math's Pi number. Using f-strings, round it to two decimal points.
B. Write a program that represents 5_000_000 as (5,000,000) in console
C. Write a program that calculates the percentage of apples left in the fridge.
Initially you got 28 apples, but you ate 4. Using f-strings print the percentage
of the apples left.

- Chat GPT's Homework -
1. What does the random.choice(seq) function do?
A) Generates a random float number between 0 and 1.
B) Selects a random element from the sequence seq.
C) Generates a random integer from a given range.
D) Shuffles the elements of the sequence seq.

2. How do you generate a random integer between 5 and 10 (inclusive) 
using random.randint(a, b)?

3. Write a code snippet that generates a random float between 0 and 1 
(exclusive) using random.random().

4. What does the random.sample(seq, k) function do?
A) Chooses multiple random elements from the sequence with replacement.
B) Selects multiple unique random elements from the sequence.
C) Generates a random integer from the given range.
D) Returns the first k elements from the sequence.

5. Calculate the square root of 25 using the math.sqrt() function.

6. How do you access the value of pi using the math module?

7. If you have a float value x = 7.6, how would you round it up to the nearest 
integer using the math.ceil() function?

8. Write a Python program that generates and prints 5 random integers between 
50 and 100 (inclusive) using the random.randint() function.

9. Write a Python program that takes a floating-point number as input and prints 
its square root using the math.sqrt() function.

10. Implement a Python "Roll Dice" program that simulates rolling a six-sided die. 
The program should return a random number between 1 and 6.

- Interview Questions -
1. Reverse a string with slicing method.

Quiz.
1. What does the None keyword represent in Python?
    a) A special value that represents an empty string
    b) A placeholder for missing or undefined values
    c) A reserved keyword for creating new variables
    d) An operator for performing null checks

2. Which type is assigned to a variable that has no value assigned to it in Python?
    a) EmptyType
    b) NoneType
    c) NullType
    d) UndefinedType

3. What is the result of evaluating the expression: type(None)?
    a) <class 'NoneType'>
    b) <class 'None'>
    c) <class 'NullType'>
    d) <class 'Undefined'>

4. Which statement assigns the value None to the variable 'result'?
    a) result = null
    b) result = None
    c) result = void
    d) result = undefined

5. What is the correct way to check if a variable value is set to None?
    a) if value is not None:
    b) if value != None:
    c) if value == None:
    d) if value is None:

6. Can None be used in arithmetic operations in Python?
    a) Yes, it can be treated as the integer value 0.
    b) No, trying to perform arithmetic with None will result in an error.
    c) Only in certain cases, depending on the context.
    d) Yes, it can be treated as a float value of 0.0.

7. What does the math.floor(x) function do?
    a) Returns the smallest integer greater than or equal to x.
    b) Returns the largest integer less than or equal to x.
    c) Rounds x to the nearest integer.
    d) Returns the square root of x.

8. Which of the following is the correct way to import the 'math' module in Python?
    a) import math.module
    b) import math
    c) from math import *
    d) import math as m

9. The math.ceil(x) function does what?
    a) Returns the square root of x rounded up to the nearest integer.
    b) Returns the value of x rounded up to the nearest integer.
    c) Returns the value of x rounded down to the nearest integer.
    d) Returns the largest integer less than or equal to x.

10. What does the math.pow(x, y) function do?
    a) Calculates the power of x raised to the yth root.
    b) Calculates the exponential of x raised to the power of y.
    c) Calculates the power of x raised to the yth power.
    d) Calculates the logarithm of x with base y.

11. The math.sqrt(x) function is used to:
    a) Calculate the square root of x.
    b) Calculate the cube root of x.
    c) Calculate the logarithm of x.
    d) Calculate the factorial of x.

12. What is the output of the following code:
    import math
    value = 3.05
    print(math.floor(value))

    a) 3
    b) 3.0
    c) 4
    d) 4.0

13. What is the output of the following code:
    from math import pi
    a = round(pi, 2)
    print(a * 2)

    a) 3.14
    b) 3.18
    c) 6.28
    d) 6.38
    e) None

14. What is the purpose of the random.choice(seq) function?
    a) It generates a random float number between 0 and 1.
    b) It selects a random element from the sequence seq.
    c) It generates a random integer from a given range.
    d) It shuffles the elements of the sequence seq.

15. Which of the following methods is used to select multiple unique random 
elements from a sequence?
    a) random.select(seq, count)
    b) random.sample(seq, count)
    c) random.choose(seq, count)
    d) random.pick(seq, count)

16. How would you import the random module correctly in Python?
    a) import random as rnd
    b) from random import *
    c) import randommodule
    d) import random

17. If you want to generate a random integer between 1 and 100 (inclusive), 
which random module method would you use?
    a) random.randint(1, 100)
    b) random.randomint(1, 100)
    c) random.random(1, 100)
    d) random.randint(100)

18. In Python, what is the process of combining multiple strings into one?
    a) Concatenation
    b) Merging
    c) Joining
    d) Binding

19. What does the ascii_letters constant include?
    a) Uppercase letters only
    b) Lowercase letters only
    c) Both uppercase and lowercase letters
    d) Digits and punctuation marks

20. Which PEP provides recommendations and guidelines for writing clean, readable, and maintainable Python code?
    a) PEP 20
    b) PEP 8
    c) PEP 4
    d) PEP 12

21. What is the primary purpose of the "as" keyword in Python's "import" statement?
    a) It renames the module being imported.
    b) It allows importing multiple modules at once.
    c) It imports all the functions and classes from the module.
    d) It enables conditional imports based on runtime conditions.
"""




import string
import math
import random


# - Programs -
# Exercise A
name = input("Please enter your name:\n>> ")
age = int(input("Please enter your age:\n>> "))
nationality = input("Please enter your nationality:\n>> ")
print(f"""User name: {name}
User age: {age}
User nationality: {nationality}""")

# Exercise B
a = int(input("Please enter the first summand:\n>> "))
b = int(input("Please enter the second summand:\n>> "))
print(f"Sum: {a} + {b} = {a + b}")

# Exercise C
first_string = input("Please enter first value:\n>> ")
second_string = input("Please enter second value:\n>> ")
result = first_string + second_string
print(result)


# - Modules -
#  A. Which Python module provides a collection of string constants, such as ascii_letters?
print(string.ascii_letters)
#  B. If you want to create a password generator that includes both uppercase and lowercase letters, which constant from the 'string' module might be useful?
print(string.ascii_letters)
# C. What is the purpose of using constants like ascii_letters from the string module in Python programming?
print("Константы, такие как ascii_letters из модуля string в Python, используются для удобного и безопасного обращения к наборам символов, например, при генерации случайных строк, проверке ввода пользователя или фильтрации текста.")
# D. What is 'getpass' function from 'getpass' module for?
print("Функция getpass() из модуля getpass используется для безопасного ввода пароля, при котором введённые символы не отображаются на экране.")


# - Python Tricks -
a = "Hello"
b = 5
a, b = b, a
print("a:", a)
print("b:", b)


# - Constants -
# Exercise A
PI = 3.141592653589793
# Exercise B
AVOGADRO_NUMBER = 6.022
# Exercise C
CURRENCY_USD = 1.7
# Exercise D
SECONDS_IN_MINUTE = 60
# Exercise E
print("No, there are no real constants in Python.Constants are usually written in capital letters, but this is just a convention. Python does not forbid changing their values.")


# - Math -
# Exercise A
number = 57_999.99
round_down = math.floor(number)
print(round_down)

# Exercise B
sqrt_value = math.sqrt(number)
round_sqrt = round(sqrt_value, 1)
print(round_sqrt)

# Exercise C
num = 0.0592481
round_up = math.ceil(num)
print(round_up)

# Exercise D
digit = 5.5
powered_digit = pow(5.5, 5)
print(powered_digit)


# - NoneType -
# A. What is None in Python? How is this value described in other programming languages?
print("None в Python означает отсутствие значения, аналогично null в других языках, например, JavaScript.")
# B. What is the best practices of using None in Python?
print("Использовать None как значение по умолчанию для аргументов функций или для проверки, есть ли значение.")
# C. How Python evaluates the NoneType? (True / False)
print("В Python None оценивается как False.")
# D. Create any NoneType object. Print it.
none_object = None
print(none_object)


# - Built-ins -
# Exercise A
x = 5
y = 3
print(pow(y, x))

# Exercise B
print(pow(x, y))

# Exercise C
a = int(input("Please enter the first integers:\n>> "))
b = int(input("Please enter the second integers:\n>> "))
print(pow(a, b))


# - String Formattings -
# Exercise A
print(f"{math.pi:.2f}")

# Exercise B
number = 5_000_000
print(f"{number:,}")

# Exercise C
apples = 28
ate = 4
apples_left = apples - ate
percentage_left = (apples_left / apples) * 100
print(f"Percentage of apples left: {percentage_left:.2f}%")


# - Chat GPT's Homework -
# Task 1
# What does the random.choice(seq) function do?
# A) Generates a random float number between 0 and 1.
# B) Selects a random element from the sequence seq.
# C) Generates a random integer from a given range.
# D) Shuffles the elements of the sequence seq.
print("answer: B) Selects a random element from the sequence seq.")

# Task 2 
a = 5
b = 10
random_num = random.randint(a, b)
print(random_num)

# Task 3
random_float = random.random()
print(random_float)

# Task 4
# What does the random.sample(seq, k) function do?
# A) Chooses multiple random elements from the sequence with replacement.
# B) Selects multiple unique random elements from the sequence.
# C) Generates a random integer from the given range.
# D) Returns the first k elements from the sequence.
print("answer: B) Selects multiple unique random elements from the sequence.")

# Task 5
square_root = math.sqrt(25)
print(square_root)

# Task 6
pi_value = math.pi
print(pi_value)

# Task 7
x = 7.6
round_up = math.ceil(x)
print(round_up)

# Task 8
for _ in range(5):
    random_integer = random.randint(50, 100)
print(random_integer)

# Task 9
float_number = float(input("Please enter the float number:\n>> "))
square_root = math.sqrt(float_number)
print(square_root)

# Task 10
roll = random.randint(1, 6)
print(f"You rolled a {roll}")


# - Interview Questions -
sentence = "Python is the best!"
reverse = sentence[::-1]
print(reverse)


# Quiz.
# 1. b
# 2. b
# 3. a
# 4. b 
# 5. d
# 6. b
# 7. b
# 8. b
# 9. b
# 10. c
# 11. a
# 12. a
# 13. c
# 14. b
# 15. b
# 16. d
# 17. a
# 18. a
# 19. c
# 20. b
# 21. a