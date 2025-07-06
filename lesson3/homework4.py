"""
- Strings -
A. Create a variable called 'long_sentence'. Make it equal a sentence
minimum. Print 'long_sentence's length.
B. Replace Print function's 'end' parameter from default '\n' to '\t'.
Write 2 Print functions with it.
C. Change Print function's 'end' parameter, so that it links values with
stars. Example:
Today*is*a*good*day!
D. Write 3 different Print functions with according string ("He", "is", "cool.")  
in such way so you can see this on your console (you can use any method):
He is cool.
E. The same task as previous (D), but now make it look like:
He#is#cool.
F. Create a variable named 'color'. Give it a string 'Python' value.
G. Create a variable named 'item'. Give it a string 'Developer' value.
H. Use all methods you know about string-formattings and Print function
to concatenate these two variables, so you can see 'Python Developer' on your
console (terminal).
I. Replace Print function's 'end' parameter from default value to '...'.
Write 3 Print functions with it.
J. Suppose you have the following variable:
word = "Hello. I am Taylor."

Using slicing method:
1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.
2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.
3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.

Create a variable named 'recreated_word' or 'result' and use all previous variables 
(prefix, middle_part, name) to recreate the 'word' phrase.
K. Suppose you have the following value:
"abababababa"

Using slicing method, get all 'a' characters from the value and assign it to a
variable, then print that variable.
L. Create a formula that finds the last index of a string.
M. What is the difference between 1 and "1"? Are they equal values, why?
N. Using all your Python knowledge, find the amount of words the following sentence:
"The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."

- String Methods -
A. Use all these string methods and test it in your code:
1. title
2. capitalize
3. count
4. endswith
5. find
6. index
7. isalpha
8. isdigit
9. islower
10. isupper
11. lower
12. upper
13. replace
14. split
15. strip
16. startswith
17. join
B. Combine several string methods at once.
C. Create any string-valued variable. First, call the 'lower' method on it,
then call 'islower' method. What value will it always give you and why?
D. Suppose you have the following variable:
my_value = "Obviously, today is a hot day."
Replace all 'o' characters with 0 (zeros). 
E. Count how many times the word 'likes' occured in the following string:
"Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."

- String Formattings -
A. Create a variable 'name' and assign your name to it.
Create a variable 'age' and assign your age to it.
Using the f-string method, create a formatted string that displays your name 
and age in the following format:
"My name is [name] and I am [age] years old."
B. Create a variable item and assign a string representing an item name.
Create a variable quantity and assign an integer representing the quantity of the item.
Create a formatted string using the old-style % formatting that displays the item 
name and quantity in the following format:
"I want to buy %d units of %s."
C. Make your best and create a hard task by your own using string formattings.

- Chat GPT's Homework -
A. Use the len() function to find the length of the following strings:
1. "programming"
2. "python is fun"
3. "12345"
B. Convert the following string to uppercase string:
"hello world"
C. Check if the string "python" is present in the following sentence:
"I enjoy programming in Python."
D. Given the string "programming", access the following elements using positive and negative indexing:
1. The first character
2. The last character
3. The third character
4. The second-to-last character
E. Using string slicing, extract the word "is" from the string:
"Python is a versatile programming language."
F. Retrieve the substring "quick brown" from the following sentence:
"The quick brown fox jumps over the lazy dog."
G. Reverse the following string using slicing:
"redivider"
H. Write a program that capitalizes the first letter of each word in the following sentence:
"welcome to the world of programming"

- Interview Questions -
A. Reverse any string using slicing method.
B. Print the whole string using slicing method, not knowing the length of a string.

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz:
A. What does len('Hello ') return?
    a) 4
    b) 5
    c) 6
    d) 'Hello'
    e) "Hello"

B. What is the output of the following code snippet:

    sphere = "Web Development" * 2 + "" * 6
    length = len(sphere)
    print(length)

    a) 15
    b) 20
    c) 25
    d) 30

C. Which of the operator can be used in Strings?
    a) +
    b) *
    c) Both of the above
    d) None of the above

D. What is the output of the following code snippet:

    comment = "I like your blue pants"
    pattern = comment[19:4:-3]
    print(pattern, len(pattern))

    a) "n lry", 5
    b) "n lry", 4
    c) "n ly", 4
    d) "p ly", 4
    e) "p l ", 4

E. Is the following variable named correctly, why?

    myVariable = "Python is best!"

    a) yes, follows the rules of naming a variable, pythonic code
    b) no, doesn't follow the rules of naming a variable, non-pythonic code
    c) it depends on the code editor you type
    d) it's not a code written in Python
"""
# - Strings -
# Exercise A
long_sentence = "I love my family very much because I always feel safe and happy with them. No matter what happens, I know that they will always be there for me, and it means a lot to me."
print(len(long_sentence))
# Exercise B
print("Welcome", end="\t")
print("Milan", end="\t")
# Exercise C
print("My", end="*")
print("favorite", end="*")
print("flower", end="*")
print("is", end="*")
print("camellias.")
# Exercise D
# First print function
print("He", end=" ")
print("is", end=" ")
print("cool.")
# Second print function
print("He", "is", "cool.")
# Third print function
word = ["He", "is", "cool."]
print(" ".join(word))
# Exercise E
# First print function
print("He", end="#")
print("is", end="#")
print("cool.")
# Second print function
print("He" + "#" + "is" + "#" + "cool.")
# Third print function
word = ["He", "is", "cool."]
print("#".join(word))
# Exercise F
color = "Python"
# Exercise G
item = "Developer"
# Exercise H
print(f"{color} {item}")
print("{} {}".format(color, item))
print("%s %s" % (color, item))
print(color, item)
print(color + " " + item)
print(color, end=" ")
print(item)
# Exercise I
print("She", end="...")
print("has", end="...")
print("a", end="...")
print("cat.")
# Exercise J
word = "Hello. I am Taylor."
prefix = "Hello"
middle_part = "I am"
name = "Taylor"
recreated_word = f"{prefix}. {middle_part} {name}."
print(recreated_word)
# Exercise K
value = "abababababa"
a = value[::2]
print(a)
# Exercise L 
sentence = "Hi Maria!"
print(sentence.count(""))
# Exercise M
# В Python 1 — это целое число, а "1" — строка. Они не равны друг другу
# Exercise N
text = """The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."""
word_count = text.split()
print(len(word_count))

# - String Methods -
# Exercise A
words_list = "python is the best"
# Task 1 (title)                    В Python, title() — это метод строки, который преобразует первую букву каждого слова в строке в заглавную, а все остальные буквы в строчные.     
print(words_list.title())           
# Task 2 (capitalize)               Метод capitalize() в Python преобразует первую букву строки в заглавную, а все остальные буквы — в строчные.
print(words_list.capitalize())          
# Task 3 (count)                    Метод count() в Python подсчитывает, сколько раз заданное значение встречается в строке.
print(words_list.count("is"))        
# Task 4 (endswith)                 Метод endswith() в Python проверяет, заканчивается ли строка на заданное значение.
print(words_list.endswith("best"))
# Task 5 (find)                     Метод find() в Python используется для поиска заданного значение в строке.
print(words_list.find("is"))
# Task 6 (index)                    Метод index() в Python используетс0я для нахождения индекса первого вхождения элемента в строку, список или кортеж. Если элемент не найден, он вызывает исключение ValueError.
print(words_list.index("the"))
# Task 7 (isalpha)                  Метод isalpha() в Python используется для проверки, состоит ли строка только из букв (буквенных символов) и не пуста ли она. Этот метод возвращает True, если все символы строки являются буквами (латинскими или другими алфавитами) и строка не пуста. В противном случае он возвращает False.
print(words_list.isalpha())
# Task 8 (isdigit)                  Метод isdigit() в Python используется для проверки, состоит ли строка исключительно из цифр. Если строка состоит только из числовых символов (0-9), метод возвращает True. В противном случае — False.
print(words_list.isdigit())
# Task 9 (islower)                  Метод islower() в Python проверяет, состоит ли строка полностью из строчных букв (маленьких букв). Если все символы строки — строчные буквы, и строка не пуста, метод возвращает True. В противном случае возвращает False.
print(words_list.islower())
# Task 10 (isupper)                 Метод isupper() в Python используется для проверки, состоит ли строка полностью из заглавных букв. Если все символы строки — заглавные буквы, и строка не пуста, метод возвращает True. В противном случае возвращает False.
print(words_list.isupper())        
# Task 11 (lower)                   Метод lower() в Python используется для преобразования всех символов строки в строчные (маленькие) буквы. Этот метод возвращает новую строку, где все заглавные буквы были заменены на строчные.
print(words_list.lower())
# Task 12 (upper)                   Метод upper() в Python используется для преобразования всех символов строки в заглавные (большие) буквы. Этот метод возвращает новую строку, где все строчные буквы заменены на заглавные. 
print(words_list.upper())
# Task 13 (replace)                 Метод replace() в Python используется для замены части строки на другую. Он возвращает новую строку, в которой все вхождения старой подстроки заменены на новую подстроку. 
print(words_list.replace("is", "are"))
# Task 14 (split)                   Метод split() в Python используется для разделения строки на несколько частей (подстрок) по указанному разделителю. Метод возвращает список, содержащий части строки. 
print(words_list.split())
# Task 15 (strip)                   Метод strip() в Python используется для удаления пробельных символов (или любых других символов, указанных в аргументе) с начала и конца строки. Этот метод не изменяет исходную строку, а возвращает новую строку без этих символов.
print(words_list.strip())
# Task 16 (startswith)              Метод startswith() в Python используется для проверки, начинается ли строка с указанного префикса (подстроки). Он возвращает True, если строка начинается с этого префикса, и False, если нет.
print(words_list.startswith("python"))
# Task 17 (join)                    Метод join() в Python используется для объединения элементов итерируемого объекта (например, списка, кортежа, множества) в одну строку, используя строку, на которой этот метод был вызван, в качестве разделителя. Метод возвращает новую строку, в которой элементы объединены с разделителем между ними.
join_method = ["Привет", "мир", "Python"]
print(" ".join(join_method))
# Exercise B
main = "   hello, PROGRAMMING world!   "
result = main.strip().lower().replace("programming", "python").capitalize()
print(result)
# Exercise C
lower_text = "The variable will always be true."
low = lower_text.lower()
print(low)
is_low = low.islower()
print(is_low)
# Exercise D
my_value = "Obviously, today is a hot day."
print(my_value.replace("o", "0").replace("O", "0"))
# Exercise E
likes_count = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print(likes_count.count("likes"))

# - String Formattings -
# Exercise A
name = "Mirsakina"
age = 18
name_age = f"My name is {name} and I am {age} years old."
print(name_age)
# Exercise B
item = "notebook"
quantity = 5
message = "I want to buy %d units of %s." % (quantity, item)
print(message)

# - Chat GPT's Homework -
# Exercise A
# Task 1
string1 = "proqramming"
print(len(string1))
# Task 2
string2 = "python is fun"
print(len(string2))
# Task 3
string3 = "12345"
print(len(string3))
# Exercise B
new_string = "hello world"
print(new_string.upper())
# Exercise C
new_sentence = "I enjoy programming in Python."
python_in_sentence = "python" in "I enjoy programming in Python.".lower()  
print(python_in_sentence)
# Exercise D
string = "programming"
# Task 1
print(string[0])
print(string[-11])
# Task 2
print(string[10])
print(string[-1])
# Task 3
print(string[2])
print(string[-9])
# Task 4
print(string[9])
print(string[-2])
# Exercise E
programming_language = "Python is a versatile programming language."
print(programming_language[7:9])
# Exercise F
substring = "The quick brown fox jumps over the lazy dog."
print(substring[4:15])
# Exercise G
string_slicing = "redivider"
print(string_slicing[::-1])
# Exercise H
title_string = "welcome to the world of programming"
print(title_string.title())

# - Interview Questions -
# Exercise A
hobby = "My hobby is baking."
print(hobby[::-1])
# Exercise B
print(hobby[:])

# Quiz:
# A. What does len('Hello ') return?
#     a) 4
#     b) 5
#     c) 6
#     d) 'Hello'
#     e) "Hello"
print("answer: c) 6")
# B. What is the output of the following code snippet:

#     sphere = "Web Development" * 2 + "" * 6
#     length = len(sphere)
#     print(length)

#     a) 15
#     b) 20
#     c) 25
#     d) 30
print("answer: d) 30")
# C. Which of the operator can be used in Strings?
#     a) +
#     b) *
#     c) Both of the above
#     d) None of the above
print("answer: c) Both of the above")
# D. What is the output of the following code snippet:

#     comment = "I like your blue pants"
#     pattern = comment[19:4:-3]
#     print(pattern, len(pattern))

#     a) "n lry", 5
#     b) "n lry", 4
#     c) "n ly", 4
#     d) "p ly", 4
#     e) "p l ", 4
print("answer: a) \"n lry\", 5")
# E. Is the following variable named correctly, why?

#     myVariable = "Python is best!"

#     a) yes, follows the rules of naming a variable, pythonic code
#     b) no, doesn't follow the rules of naming a variable, non-pythonic code
#     c) it depends on the code editor you type
#     d) it's not a code written in Python
print("answer:  b) no, doesn't follow the rules of naming a variable, non-pythonic code")