"""
- For Loops -
A. Write a Python program that uses a for loop to print 
all even numbers from 1 to 20, inclusive. Use the continue 
statement to skip odd numbers during the iteration.
B. Write a Python program that asks the user to input 10 numbers. 
Use a for loop to iterate through the numbers. Print the sum of 
all numbers entered by the user. Use the break statement to exit 
the loop early if the user inputs a negative number.
C. Write a Python program that takes an integer as input from 
the user and prints its multiplication table up to 10 using a for loop. 
Use the continue statement to skip the multiplication if the result 
is less than 30.
D. Write a Python program to find and print all prime numbers between 
1 and 50 using a for loop. Use the break statement to exit the loop 
early if a non-prime number is encountered.
E. Write a Python program to generate and print the first 10 numbers 
in the Fibonacci sequence using a for loop. Use the continue statement 
to skip printing a number if it is greater than 100.
F. Write a Python program that asks the user to input an integer n. 
Using a for loop, print all even numbers in reverse order from n down 
to 2. Use the continue statement to skip odd numbers during the iteration.
G. Write a Python program that prompts the user for a password. Use a for 
loop to iterate over a predefined list of passwords. If the entered password 
matches any of the predefined passwords, print "Access granted" and use the 
break statement to exit the loop. If no match is found, print "Access denied".
H. Write a Python program that asks the user to enter a series of numbers. 
Use a for loop to iterate through the numbers. Compute and print the average 
of all positive numbers entered by the user. Use the continue statement 
to skip negative numbers during the calculation.
I. Write a Python program that prompts the user to input a sentence. 
Use a for loop to iterate through the characters in the sentence and count 
the number of vowels (a, e, i, o, u). Print the total count of vowels. 
Use the continue statement to skip counting for non-alphabetic characters.
J. Write a Python program that generates a random password of a specified 
length based on user input. Ask the user to input the desired password 
length and use a for loop to generate and print the password. Use the 
break statement to exit the loop after generating the password.
K. Write a Python program that prompts the user to enter the names of 
three cities and their corresponding populations. Use a for loop to populate 
a dictionary where the city names are keys and the populations are values.
L. Write a Python program that asks the user to input a sentence. Use a for 
loop to iterate through the characters in the sentence and count the number 
of vowels (a, e, i, o, u). Store the counts in a dictionary where the vowels 
are keys and the counts are values.
M. Write a Python program that allows the user to enter key-value pairs into 
a dictionary. Prompt the user to input a key and a value, and use a for loop 
to allow them to enter multiple pairs. Print the dictionary after each addition.
N. Write a Python program that prompts the user to input a word or phrase. 
Use a for loop to iterate through the characters and count the frequency of 
each letter in the input. Store the counts in a dictionary where the letters 
are keys and the counts are values.
O. Write a program to use for loop to print the following reverse number pattern:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
P. Display numbers from -10 to -1 using for loop. The step of your range
method should be positive, not negative. The output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

- EXTRA HARD -
Task 1.
Count the total number of digits in a number.
Write a program to count the sum of digits in a number.
For example, the number is 75869, so the output should be 35 (7 + 5 + 8 + 6 + 9).
Task 2.
Write a program to calculate the sum of series up to n term. 
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
Task 3.
Write a program to display whether the number is prime or not.
Prime numbers are natural numbers that are divisible by only 1 and the number itself.

- Chat GPT's Project -
Project: Password Validation

Write a Python program that prompts the user to enter a password. The program 
should check the validity of the password based on the following conditions:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter, one lowercase letter, 
and one numeric digit.
The password must not contain the word "password" (case insensitive).
Use a for loop to iterate through the characters of the password and implement 
the following actions:

If the current character is a space, use continue to skip the rest of the loop 
and move to the next character.
If the password contains the word "password" (case insensitive), use break to 
immediately exit the loop and print "Invalid password".
After the loop, check if the password meets all the conditions. If it does, 
print "Valid password". Otherwise, print "Invalid password".
Ensure that the program provides appropriate messages to guide the user and 
thoroughly tests the input for validity.

This task challenges the usage of for loops, break, and continue to handle 
complex conditions and ensure secure password validation. Happy coding!

Quiz.
1. What is the purpose of the continue statement in a for loop?
    a) It terminates the loop and exits the loop block.
    b) It skips the rest of the loop and moves to the next iteration.
    c) It restarts the loop from the beginning.
    d) It checks if the loop condition is met.

2. In a for loop, the break statement is used to:
    a) Skip the current iteration and proceed to the next.
    b) Exit the loop and move to the next block of code.
    c) Restart the loop from the beginning.
    d) None of the above.

3. Which of the following statements is true about the for loop in Python?
    a) The loop variable can only be a numeric data type.
    b) The loop variable can be of any data type.
    c) The loop variable is optional.
    d) The loop variable is not required in a for loop.

4. For the following code snippet, determine the output or the result of the operation:
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        else:
            continue
    print(total)

5. For the following code snippet, determine the output or the result of the operation:
    numbers = [10, 20, 30, 40, 50]
    total = 0
    for num in numbers:
        if num > 30:
            break
        if num % 2 == 0:
            total += num
        else:
            continue
    print(total)

6. What is the value of the var after the for loop completes its execution:
    var = 10
    for i in range(10):
        for j in range(2, 10, 1):
            if var % 2 == 0:
                continue
                var += 1
        var += 1
    else:
        var += 1
    print(var)

    a) 20
    b) 21
    c) 10
    d) 30

7. What is the output of the following range() function:
    for num in range(2,-5,-1):
        print(num, end=", ")

    a) 2, 1, 0
    b) 2, 1, 0, -1, -2, -3, -4, -5
    c) 2, 1, 0, -1, -2, -3, -4

8. What is the value of x after the following nested for loop completes its execution:
    x = 0
    for i in range(10):
        for j in range(-1, -10, -1):
            x += 1
            print(x)
    
    a) 99
    b) 90
    c) 100

9. What is the output of the following nested loop?
    for num in range(10, 14):
        for i in range(2, num):
            if num % i == 1:
                print(num)
                break
                
10. What is the output of the following nested loop?
    numbers = [10, 20]
    items = ["Chair", "Table"]

    for x in numbers:
        for y in items:
            print(x, y)
        
    a)
    10 Chair
    10 Table
    20 Chair
    20 Table
    b)
    10 Chair
    10 Table

11. What is the output of the following loop?
    for l in 'Jhon':
        if l == 'o':
            pass
        print(l, end=", ")
            
    a) J, h, n,
    b) J, h, o, n,

- True or False -
True or False: A for loop in Python can be nested within another for loop.
True or False: The continue statement is used to immediately exit the loop
and terminate the program.
True or False: The break statement is used to exit the loop prematurely, 
regardless of whether the loop condition is met.
True or False: The break statement is used to skip the rest of the loop and 
move to the next iteration.
True or False: The continue statement is used to exit the loop prematurely, 
regardless of whether the loop condition is met.
True or False: Using break is more appropriate when you want to exit the 
loop prematurely based on a certain condition, regardless of whether the 
loop has completed all iterations. It allows you to terminate the loop early 
and continue with the rest of the program.
True or False: Using continue is more appropriate when you want to skip the 
current iteration and proceed to the next iteration based on a certain condition, 
but you still want to continue the loop.
"""



# - For Loops -
import random
import string

# Exercise A
for num in range(1, 21):
    if num % 2 != 0:
        continue
    print(num)

# Exercise B
total = 0
for i in range(10):
    numbers = int(input(f"Please enter number {i+1}:\n>> "))
    if numbers < 0:
        break
    total += numbers
print(f"Sum: {total}")

# Exercise C
num = int(input("Please enter the integer:\n>> "))
for i in range(1, 11):
    result = num * i
    if result < 30:
        continue
    print(f"{num} x {i} = {result}")

# Exercise D
for num in range (1, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  
    if is_prime:
        print(num)

# Exercise E
a, b = 0, 1
for _ in range(10):
    if a > 100:
        continue
    print(a)
    a, b = b, a + b

# Exercise F
n = int(input("Please enter an integer:\n>> "))
for i in range(n, 1, -1):
    if i % 2 != 0:
        continue
    print(i)

# Exercise G
passwords = ["admin123", "for123loop", "p9th0n"]
user_input = input("Please enter your password:\n>> ")
for pwd in passwords:
    if user_input == pwd:
        print("Access granted")
        break
else:
    print("Access denied")

# Exercise H
numbers = list(map(int, input("Please enter numbers separated by space:\n>> ").split()))
total = count = 0
for num in numbers:
    if num < 0:
        continue
    total += num
    count += 1
if count > 0:
    print("Average:", total / count)
else:
    print("No positive numbers entered.")

# Exercise I
sentence = input("Please enter a sentence:\n>> ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if not char.isalpha():
        continue
    if char in vowels:
        count += 1
print(count)

# Exercise J
length = int(input("Please enter desired password length:\n>> "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''
for i in range(length):
    password += random.choice(chars)
    if len(password) == length:
        break
print(password)

# Exercise K
cities = {}
for _ in range(3):
    city = input("Enter city name: ")
    population = int(input(f"Please enter population for {city}:\n>> "))
    cities[city] = population
print(cities)

# Exercise L
sentence = input("Please enter a sentence:\n>> ").lower()
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for char in sentence:
    if char in vowel_count:
        vowel_count[char] += 1
print(vowel_count)

# Exercise M
data = {}
for _ in range(5):  
    key = input("Please enter key:\n>> ")
    value = input("Please enter value:\n>> ")
    data[key] = value
    print(data)

# Exercise N
text = input("Enter a word or phrase:\n>> ").lower()
frequency = {}
for char in text:
    if char.isalpha():
        frequency[char] = frequency.get(char, 0) + 1
print(frequency)

# Exercise O
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise P
for i in range(1, 11):
    print(-11 + i)


# - EXTRA HARD -
# Task 1.
number = input("Please enter a number:\n>> ")
digit_sum = 0
digit_count = 0
for char in number:
    if char.isdigit():
        digit_count += 1
        digit_sum += int(char)
print(f"Total digits: {digit_count}")
print(f"Sum of digits: {digit_sum}")


# Task 2.
n = int(input("Please enter number of terms:\n>> "))
term = ""
total = 0
for i in range(n):
    term += "2"
    total += int(term)
print(f"Sum of the series: {total}")


# Task 3.
num = int(input("Please enter a number:\n>> "))
if num <= 1:
    print("Not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            break
    else:
        print("Prime number.")

# Quiz.
# 1. b
# 2. b
# 3. b
# 4. 6
# 5. 60
# 6. b
# 7. c
# 8. b
# 9. 10 11 12 13
# 10. a
# 11. b

# - True or False -
# 1. True
# 2. False
# 3. True
# 4. False
# 5. False
# 6. True
# 7. True