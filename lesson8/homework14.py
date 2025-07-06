"""
- For Loops -
A. Write a program that prints "Python" four times in a row.
B. Write a program that prints "Python" four times in one row. Expected output:
PythonPythonPythonPython
C. Write a program that prints numbers from 0 to 7.
D. Write a program that asks the user how many time the phrase should
be printed. Depending on that input the program should print prints the
"Loops are very good" phrase.
E. Using f-strings and looping five times print the following output:
Looping No.1
Looping No.2
Looping No.3
Looping No.4
Looping No.5
F. Write a program that asks user for six student name. Add those names
to a list. Then print their name with corresponding order number. Ex. o.:
1. Leyla
2. Aysel
3. Gunel
4. Murad
5. Mark
6. John

- Chat GPT's Homework -
1. Write a program that uses a for loop to print the numbers from 1 to 10.
2. Write a program that calculates and prints the sum of all numbers from 1 to 100 using a for loop.
3. Write a program that takes an integer input from the user and uses a for loop to print the multiplication table for that number up to 10.
4. Write a program that takes a string input from the user and uses a for loop to count and print the number of characters in the string.
5. Write a program that takes a string input from the user and uses a for loop to print the characters of the string in reverse order.
6. Write a program that takes an integer input from the user and uses a for loop to calculate and print the factorial of that number.
7. Write a program that takes an integer input from the user and uses a for loop to print a table of powers for that number up to the 5th power.

Quiz.
1. What is the purpose of loops in programming?
    a) To confuse the programmer
    b) To repeat a block of code multiple times
    c) To delete variables
    d) To make code run faster

2. Which type of loop is commonly used to repeat a block of code a fixed number of times?
    a) do-while loop
    b) for loop
    c) if-else loop
    d) switch loop

3. How is the range() function used in a for loop?
    a) It generates a random number within a range
    b) It creates a list of numbers in a given range
    c) It defines the number of iterations for the loop
    d) It calculates the sum of all numbers in a range

4. What's a scenario in real life that can be likened to a loop in programming?
    a) Listening to a song on repeat
    b) Going on a spontaneous road trip
    c) Writing a novel in one sitting
    d) Solving a complex math problem

5. Which of the following code snippets will print "Hello, Loop!" five times?
    a) 
    for i in range(5):
        print("Hello, Loop!")
    b) 
    for i in range(1, 6):
        print("Hello, Loop!")
    c)
    for i in range(0, 5, 2):
        print("Hello, Loop!")
    d) 
    for i in range(5, 0, -1):
        print("Hello, Loop!")

6. What will the following code snippet print?
    for i in range(3):
        print("*" * (i + 1))

    a)
    *
    **
    ***
    b)
    ***
    **
    *
    c)
    *
    **
    *
    d) ****

7. Loops are essential in programming because they help to:
    a) Create complex user interfaces
    b) Repeat code without any restrictions
    c) Make the code more difficult to understand
    d) Automate repetitive tasks and process collections of data

8. Which of the following options correctly describes an infinite loop?
    a) A loop that runs exactly one time
    b) A loop that only runs when the program is launched
    c) A loop that repeats a specific number of times
    d) A loop that continues running endlessly

9. What does the range() function return?
    a) A list of numbers
    b) A sequence of numbers
    c) A single random number
    d) A boolean value

10. Which of the following is NOT an iterable that can be used with a for loop?
    a) Lists
    b) Dictionaries
    c) Strings
    d) Integers
"""

# - For Loops -
# Exercise A
for i in range(4):
    print("Phyton")

# Exercise B
for i in range(4):
    print("Python", end = "")
    
# Exercise C
for i in range(8):
    print(i)

# Exercise D
number_of_prints = int(input("Please enter how many time the phrase should be printed:\n>> "))
for i in range(number_of_prints):
    print("Loops are very good")

# Exercise E
for i in range(1, 6):
    print(f"Looping No.{i}")

# Exercise F
students = []
for i in range(6):
    names = input(f"Please enter the student{i+1} name:")
    students.append(names)
print("Student List:")
for i in range(len(students)):
    print(f"{i + 1}. {students[i]}")

    

# - Chat GPT's Homework -
# Task 1
for i in range(1, 11):
    print(i)

# Task 2
total = 0
for i in range (1, 101):
    total += i
print(f"Sum: {total}")

# Task 3
num = int(input("Please enter the integer:\n>> "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 4
word = input("Please enter any string:\n>> ")
count = 0
for char in word:
    count += 1
print(f"The number of characters in the string is: {count}")

# Task 5
user_input = input("Please enter the string:\n>> ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print(reversed_string)

# Task 6
num = int(input("Please enter any integer:\n>> "))
factorial = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
print(f"The factorial of {num} is {factorial}")

# Task 7
num = int(input("Please enter an integer:\n>> "))
print(f"Table of powers for {num}:")
for power in range(1, 6):
    result = num ** power
print(result)


# Quiz.
# 1. b
# 2. b
# 3. c
# 4. a
# 5. a b d
# 6. a
# 7. d
# 8. d
# 9. b
# 10. d