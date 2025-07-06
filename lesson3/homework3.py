"""
Note. Use clear and descriptive variable names throughout the code.
Make sure to add comments to explain the purpose and functionality of 
your code.

- String Formattings -
A. Create a variable called 'genre'. Give it a string value.
B. Create a variable called 'producer'. Give it a string value.
C. Create a variable called 'song'. Give it a string value.
D. Using three Python String Formatting types (f-strings, .format(), %s) 
create 3 variables accordingly to the formats count, and make it equal 
to little text (story) using all variables from Task A to C.
E. Create a variable called 'firstname'. Give it an appropriate value.
F. Create a variable called 'lastname'. Give it an appropriate value.
G. Create a variable called 'age'. Give it an appropriate value.
H. Create a variable called 'gender'. Give it an appropriate value.
I. Using all of string formatting methods and variables from Task E to H, 
print as the following:
My name is John Smith, and I am 27 years old. My gender is - Male.
J. Create a variable called 'language'. Make it equal 'Python'. Using f-strings
print 'I love Python. I will repeat this word 5 times: PythonPythonPythonPythonPython.'
K. Create a variable called 'hello'. Make it equal 'Hello'.
Create a variable called 'world'. Make it equal 'World'. 
Using math operations and '.format' string-formatting method print 'Hello World!'.
L. Create a variable called 'hello'. Make it equal the date of your birthday in
the following format => "01.01.2001". Using '%s' string-formatting method print
the following:
My birth date is 01.01.2001.
M. Create a text-story using all variables created through all tasks in this
homework file. You should use multi-line strings.
N. Create a variable with a string value that will contain 4 curly brackets 
(you will fill them soon). Additionally, create 4 different variables of any type 
on your own. Using '.format' string-formatting method and those 4 variables fill 
the previous string with 4 curly brackets. Print it.
O. Perform math operations with strings in a 'f-string' string-formatting method.
P. Create a variable called 'expression'. Give it any string value.
Using a variable which you have created previously and contains 4 curly brackets
print the 'expression's value 4 times using '.format' string-formatting method.

Quiz:
A. In the following code, 'Hello' is a string literal. True or false?

    ---------------------
    |    s = 'Hello'    | 
    ---------------------

    a) True
    b) False
    c) It's not a string literal.
    d) It's not a pythonic code

B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
    a) Yes
    b) No

C. Is there a problem in the code below? If yes, then how can we rectify it?

    ------------------------------
    |    s = 'Python's call!'    | 
    ------------------------------

    a) No
    b) Yes, by using a backslash
    c) Yes, bu using a multiline string
    d) Yes, by using either (b) or (c)

D. How to denote a multiline string in Python?
    a) Using ''' '''
    b) Using """ """
    c) Using either (b) and (c)

E. When used on strings, what does the * operator do?
    a) Replicates them
    b) Strips whitespace characters from their ends
    c) Raises an error
"""

# - String Formattings -
# Exercise A
genre = "pop"
# Exercise B
producer = "Elman, Andro, Tony and Mona"
# Exercise C
song = "\"Zari\""
# Exercise D
first_format = f"My favorite song is {song}, which is performed by {producer} in a {genre} style."
print(first_format)
second_format = "My favorite song is {}, which is performed by {} in a {} style.".format(song, producer, genre)
print(second_format)
third_format = "My favorite song is %s, which is performed by %s in a %s style." % (song, producer, genre)
print(third_format)
# Exercise E
firstname = "Mirsakina"
# Exercise F
lastname = "Xankishiyeva"
# Exercise G
age = 18
# Exercise H
gender = "Female"
# Exercise I
first_format_method = f"My name is {firstname} {lastname}, and I am {age} years old. My gender is - {gender}."
print(first_format_method)
second_format_method = "My name is {} {}, and I am {} years old. My gender is - {}.".format(firstname, lastname, age, gender)
print(second_format_method)
third_format_method = "My name is %s %s, and I am %s years old. My gender is - %s." % (firstname, lastname, age, gender)
print(third_format_method)
# Exercise J
language = "Python"
format = f"I love {language*5}"
print(format)
# Exercise K
hello = "Hello"
world = "World"
math_method = hello + " " + world + "!"
print(math_method)
format_method = "{} {}!".format(hello, world)
print(format_method)
# Exercise L
birth_date = "16.01.2007"
string_formatting_method = "My birth date is %s." % (birth_date)
print(string_formatting_method)
# Exercise M
text_story = f"""{hello} {world}! My name is {firstname} {lastname}, and I am {age} years old. My gender is - {gender}. My birth date is {birth_date}. I love {language}. My favorite song is {song}, which is performed by {producer} in a {genre} style."""
print(text_story)
# Exercise N
cake = "Description of the cake: {}, {}, {}, {}"
name = "Brownie"
diameter = "30 sm"
taste = "chocolate"
price = "50 manat"
format_sentence = cake.format(name, diameter, taste, price)
print(format_sentence)
# Exercise O
pine = "pine"
apple = "apple"
f_string = f"My favorite fruit is {pine + apple}"
print(f_string)
# Exercise P
expression = "Python is fun"
formatter = "{} {} {} {}"
print(formatter.format(expression, expression, expression, expression))

# Quiz:
# A. In the following code, 'Hello' is a string literal. True or false?

#     ---------------------
#     |    s = 'Hello'    | 
#     ---------------------

#     a) True
#     b) False
#     c) It's not a string literal.
#     d) It's not a pythonic code
print("answer: a) True")

# B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
#     a) Yes
#     b) No
print("answer: a) Yes")
# C. Is there a problem in the code below? If yes, then how can we rectify it?

#     ------------------------------
#     |    s = 'Python's call!'    | 
#     ------------------------------

#     a) No
#     b) Yes, by using a backslash
#     c) Yes, bu using a multiline string
#     d) Yes, by using either (b) or (c)
print("answer: d) Yes, by using either (b) or (c)")
# D. How to denote a multiline string in Python?
#     a) Using ''' '''
#     b) Using """ """
#     c) Using either (a) and (b)
print("answer: c) Using either (a) and (b)")
# E. When used on strings, what does the * operator do?
#     a) Replicates them
#     b) Strips whitespace characters from their ends
#     c) Raises an error
print("answer: a) Replicates them")