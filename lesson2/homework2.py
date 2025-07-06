"""
- Variables -
A. Create a variable which's name consists of 2 words. Assign appropriate String value to it.
B. Create a variable which's name consists of 3 words. Assign appropriate String value to it.
C. What's the name of the standard variable naming principle in Python?
D. What's the label (name) of any imaginary created box in computer memory?

- Strings -
Create variables with appropriate names according to the following topics:
A. Genre of music
B. Color
C. Car brand
D. Digit
E. Hobby
F. Language
G. Firstname
H. Lastname
I. Address

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz:
A. A line of text that Python won't try to run as code:
    a) comment
    b) module
    c) variable
    d) boolean

B. Which is used to make single line comments?
    a) %
    b) #
    c) /
    d) """ """
    e) \

C. Which Python command (function) is used to output information
to the screen (terminal, console)?
    a) read
    b) output
    c) print
    d) display

D. What is the output of the print() function call?
--------------------------
|    a = 'foo'           |
|    b = 'bar'           |
|    print(a * 2 + b)    |
--------------------------
    a) foobar
    b) barfoo
    c) barbarfoo
    d) farboofar
    e) foofoobar

E. What is the output of the print() function call?
--------------------------------------
|    salary = "17000"                |
|    phrase = "My salary is"         |
|    print(phrase, salary)           |
--------------------------------------
    a) it's not pythonic code
    b) My salary is17000.
    c) My salary is 17000
    d) My salary is17000
    e) My salary is 17000.
    f) error

F. What is the output of the print() function call?
--------------------------------------
|    salary = "17000"                |
|    phrase = "My salary is"         |
|    print(salary, pnrase)           |
--------------------------------------
    a) it's not pythonic code
    b) My salary is17000.
    c) My salary is 17000
    d) My salary is17000
    e) My salary is 17000.
    f) error
"""

# - Variables -
# Exercise A 
school_number = 162            #Snake Case - имя переменного каждое слово которого разделяется символом подчеркивания
print(school_number)
# Exercise B
new_lesson_name = "Phyton"       #Pascal Case - имя переменного каждое слово которого начинается с заглавной буквы
print(new_lesson_name)
# Exercise C
"""Имя переменной должно начинаться с буквы или символа подчеркивания.
Имя переменной не может начинаться с цифры
Имя переменной может содержать только буквенные,цифровые и символы подчеркивания (Az, 0-9 и _ ).
Имена переменных могут быть разной величины которые присваивают новую переменную(возраст, Возраст и ВОЗРАСТ — это три разные переменные)
Имя переменной не может быть названием команды в Python."""
# Exercise D
imaginary_created_box= ("ROM (Read-Only Memory) — это тип компьютерной памяти, предназначенной только для чтения. Данные, записанные в ROM, сохраняются даже при выключении питания устройства. Такая память используется для хранения постоянной информации, которая необходима для начальной загрузки и базового функционирования системы — например, BIOS в компьютерах или прошивки (firmware) в других устройствах.")    
#Camel Case - имя переменного в котором каждое слово, кроме первого, начинается с заглавной буквы
print(imaginary_created_box)

# - Strings -
# Exercise A 
genre_of_music = "Pop"
print(genre_of_music)
# Exercise B
color = "Red"
print(color)
# Exercise C
car_brand = "Ferrari"
print(car_brand)
# Exercise D
digit = "13"
print(digit)
# Exercise E
hobby = "cooking"
print(hobby)
# Exercise F
language = "Azerbaijanian"
print(language)
# Exercise G
firstname = "Mirsakina"
print(firstname)
# Exercise H
lastname = "Xankishiyeva"
print(lastname)
# Exercise I
address = "Yasamal Abbas Mirza Sharifzade"
print(address)


# -Quiz-
# A. A line of text that Python won't try to run as code:
#     a) comment
#     b) module
#     c) variable
#     d) boolean
print("answer: a)comment")

# B. Which is used to make single line comments?
#     a) %
#     b) #
#     c) /
#     d) """ """
#     e) \
print("answer: b)#")

# C. Which Python command (function) is used to output information to the screen (terminal, console)?
#     a) read
#     b) output
#     c) print
#     d) display
print("answer: c)print")

# D. What is the output of the print() function call?
# --------------------------
# |    a = 'foo'           |
# |    b = 'bar'           |
# |    print(a * 2 + b)    |
# --------------------------
#     a) foobar
#     b) barfoo
#     c) barbarfoo
#     d) farboofar
#     e) foofoobar
print("answer: e)foofoobar")

# E. What is the output of the print() function call?
# --------------------------------------
# |    salary = "17000"                |
# |    phrase = "My salary is"         |
# |    print(phrase, salary)           |
# --------------------------------------
#     a) it's not pythonic code
#     b) My salary is17000.
#     c) My salary is 17000
#     d) My salary is17000
#     e) My salary is 17000.
#     f) error
print("answer: c)My salary is 17000")


# F. What is the output of the print() function call?
# --------------------------------------
# |    salary = "17000"                |
# |    phrase = "My salary is"         |
# |    print(salary, pnrase)           |
# --------------------------------------
#     a) it's not pythonic code
#     b) My salary is17000.
#     c) My salary is 17000
#     d) My salary is17000
#     e) My salary is 17000.
#     f) error
print("answer: f)error")