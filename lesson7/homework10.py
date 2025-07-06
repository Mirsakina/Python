"""
Note. Add the following list at the top of your code. You will use this list
during the homework in certain tasks:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

Also print the list's modification versions to see the difference.
- List Methods -
A. Make up a formula with built-in python 'len' method that finds helps 
to get the last element from the 'fruits' list.
B. Add any two fruits to the 'fruits' list.
C. Remove third fruit so you can assign it to a variable.
D. Add a fruit to the 'fruits' list twice, and then print the amount of 
this fruit
in the 'fruits' list.
E. Find the index of 'Grape' object in the 'fruits' list.
F. Add 'Avocado' to the 'fruits' list at position four. 
G. Remove third fruit without getting the removed fruit.
H. Remove a fruit at position one.
I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop' 
method
by finding its positive index.
J. Reverse the 'fruits' list with two different methods. Each time print 
the reversed
list.
K. Sort alphabetically the 'fruits' list. Print the sorted version of the 
list.
L. Suppose you have the following list:
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]

Extend the 'fruits' list with the new list.
M. Make a copy of the 'fruits' list. Remove the last three fruits. Print 
both of the
lists ('fruits' and the modified copied version).
N. Create a variable named 'occurrence'. Make it equal True if the 
'Papaya' is in the
'fruits' list, otherwise False.
O. Clear the 'fruits' list.

- Variables -
A. Suppose you have the following variables:
x = 60
y = 70

You need to swap these variables values in one line of code.

- ChatGPT's homework (List Methods) -
1. Append and Extend:
a. Write a Python program that creates an empty list and then appends 
the following elements to it: 10, 20, 30, 40, and 50. Print the list 
after each append operation.
b. Create a second list containing elements [60, 70, 80]. Extend the 
first list using this second list and print the updated list.

2. Insert and Remove:
a. Write a Python program that creates a list containing the following 

elements: 'apple', 'banana', 'orange', 'grape', 'apple', 'kiwi'.
b. Use the 'insert' method to add 'pear' between 'banana' and 'orange' 
in the list. Print the updated list.
c. Use the 'remove' method to remove the first occurrence of 'apple' from 
the list. Print the updated list.

3. Count and Index:
a. Create a list containing the following elements: 2, 4, 6, 8, 4, 10, 4, 
12, 14.
b. Use the 'count' method to find how many times the number 4 appears in the 
list and print the count.
c. Use the 'index' method to find the index of the first occurrence of 4 in 
the list and print the index.

4. Sort and Reverse:
a. Create a list containing the following integers in random order: 45, 23, 
78, 12, 98, 56.
b. Use the 'sort' method to sort the list in ascending order and print the 
sorted list.
c. Use the 'reverse' method to reverse the sorted list and print the reversed 
list.



5. Slice and Concatenate:
a. Create a list containing the following elements: 'red', 'blue', 'green', 
'yellow', 'orange', 'purple'.
b. Use slicing to extract a new list that contains only the first three 
colors. Print the new list.
c. Use slicing again to extract a new list that contains the last three 
colors. Print the new list.
d. Concatenate the two sliced lists and print the final combined list.
"""


fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]


# - List Methods -
# Exercise A
last_fruit = fruits[len(fruits) - 1]
print(last_fruit)

# Exercise B
fruits.append("Pomegranate")
fruits.append("Mango")
print(fruits)

# Exercise C
fruits.pop(2)
print(fruits)

# Exercise D
fruits.append("Papaya")
fruits.append("Papaya")
papaya_counts = fruits.count("Papaya")
print(papaya_counts)

# Exercise E
grape_index = fruits.index("Grape")
print(grape_index)

# Exercise F
fruits.insert(3, "Avocado")
print(fruits)

# Exercise G
fruits.pop(2)
print(fruits)

# Exercise H
fruits.pop(1)
print(fruits)

# Exercise I
fruits.append("Blackberry")
blackberry_index = fruits.index("Blackberry")
fruits.pop(blackberry_index)
print(fruits)

# Exercise J
fruits.reverse()
print(fruits)
print(fruits[::-1])

# Exercise K
fruits.sort()
print(fruits)

# Exercise L
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
fruits.extend(new_fruits)
print(fruits)
  
# Exercise M
fruits_copy = fruits.copy()
fruits_copy = fruits_copy[:-3]
print(fruits)
print(fruits_copy)

# Exercise N
occurrence = "Papaya" in fruits
print(occurrence)

# Exercise O
fruits.clear()
print(fruits)


# - Variables -
# Exercise A
x = 60
y = 70
x, y = y, x
print("x:", x)
print("y:", y)


# - ChatGPT's homework (List Methods) -
# Task 1
my_list = []
my_list.append(10)
print(my_list)
my_list.append(20)
print(my_list)
my_list.append(30)
print(my_list)
my_list.append(40)
print(my_list)
my_list.append(50)
print(my_list)
second_list = [60, 70, 80]
my_list.extend(second_list)
print(my_list)

# Task 2
fruits = ['apple', 'banana', 'orange', 'grape', 'apple', 'kiwi']
print(fruits)
fruits.insert(2, 'pear') 
print(fruits)
fruits.remove('apple')
print(fruits)

# Task 3
numbers_list = [2, 4, 6, 8, 4, 10, 4, 12, 14]
print(numbers_list)
count_4 = numbers_list.count(4)
print(count_4)
index_4 = numbers_list.index(4)
print(index_4)

# Task 4
num_list = [45, 23, 78, 12, 98, 56]
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)

# Task 5
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
print(colors)
first_three_colors = colors[:3]
print(first_three_colors)
last_three_colors = colors[-3:]
print(last_three_colors)
combined_list = first_three_colors + last_three_colors
print(combined_list)