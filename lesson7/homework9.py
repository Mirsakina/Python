"""
Note. You should use indexing, negative indexing, slicing method,
mathematical operations and other techniques to accomplish tasks.

- Lists -
A. Create a list containing minimum seven different colors.
B. Create a list containing minimum five different countries.
C. Create a list containing three string values and two integer values.
D. Create a list containing all continents of the world.
E. Create a list containing minimum four car brands.
F. Create a list containing four different data types of Python.
G. Create a list containing only negative even numbers from -2 to -12.
H. Create a list containing only positive even numbers from 0 to 12.
I. Combine lists from Task G and H.
J. Create a list containing minimum six students' names. Print the first
student's name.
K. Create a list containing three different integers. Print the integer
at position two.
L. Print the last element of Task D's list.
M. Print the last 2 elements of Task A's list. You can use slicing
method only once. Separately printing those elements will not be accepted.
N. Given the following list:
three = [3, 3, 3]

Create a new list containing the triple value of that list.
O. Create any nested list. Print any value from the inner list and the whole
inner list.
P. Change the value of the color at position six of the list from Task A.
Q. From Task B's list print all countries except the first two.
R. Create two new lists containing the double value of the list from Task F 
using 2 different mathematical operations (methods).
S. From the following list change the value of the last element to "Bob":
friends = ["Kevin", "Karen", "Jim", "Carry"]
T. Create an empty list.

- Interview Question -
A. Reverse a list with slicing method.

Bonus:
A. Print the whole list from previous tasks using the slicing method.
B. Print the length of any list from previous tasks.
"""


# - Lists -
# Exercise A
colors = ["red", "white", "green", "blue", "tiffany", "yellow", "violet"]

# Exercise B
countries = ["Azerbaijan", "France", "USA", "Italy", "Egypt"] 

# Exercise C
values = ["table", "pen", "phone", 13, 5]

# Exercise D
continents = ["Africa", "Antarctica", "Asia", "Europe", "North America", "South America", "Australia"]

# Exercise E
car_brands = ["Toyota", "Ford", "Ferrari", "Tesla"]

# Exercise F
data_types = ["Python", 10, True, 3.14]

# Exercise G
negative_numbers = [-2, -4, -6, -8, -10, -12]

# Exercise H
positive_numbers = [2, 4, 6, 8, 10, 12]

# Exercisre I 
combined_lists = negative_numbers + positive_numbers
print(combined_lists)

# Exercise J
students = ["Melina", "Alexa", "Amur", "Sofi", "Samuel", "Teo"]
print(students[0])

# Exercise K
integers = [3, 5, 8]
print(integers[1])

# Exercise L
print(continents[-1])

# Exercise M
print(car_brands[-2:])

# Exercise N
three = [3, 3, 3]
triple_value_list = [x * 3 for x in three]
print(triple_value_list)

# Exercise O
nested_list = [[1, 2, 3], ['a', 'b', 'c'], [10, 20, 30]]
print(nested_list[0][1])
print(nested_list[1])

# Exercise P
colors.insert(6, "purple")
print(colors)

# Exercise Q
print(countries[2:])

# Exercise S
friends = ["Kevin", "Karen", "Jim", "Carry"]
friends.append("Bob")
print(friends)

# - Interview Question -
animals = ["cat", "dog", "rabbit", "lion", "tiger"]
reversed_list = animals[::-1]
print(reversed_list)

# Bonus:
# Exercise A
print(animals[:])

# Exercise B
print(len(animals))