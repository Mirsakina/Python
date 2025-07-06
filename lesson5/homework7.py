"""
Note. All tasks should be written as in the following example (you can
use variable naming method or adding a comment after the expression):
# A
expression = True and False or True
step_one = (True and False) or (True)
step_two = (False) or (True)
step_three = True
print(step_three == expression)

At the end, your program should only print 'True's, so that will mean
you have accomplished and simplified all expressions correctly.

- Booleans -
Simplify these expressions:
A. True or False and True
B. False and False or False
C. (True or False) and True
D. True or (True or False and True) and True
E. False or False and False and not False
F. (True or True or False) and True
G. False or (True and False)
H. False and False and False and False and False or True and False
I. True or False or True
J. False or (not False)
K. not True or not False
L. False and not False or not False
M. True or not False and True or not not True
N. not not not False
O. not N (previous task N's value)
P. True or False and not True or (not True and False) and not True or False
Q. True or not False or not True or True
R. False and (not True or False or (False or not True and True or False)) and True
S. False and not not not True and (False or True or not False) and True or False
T. not (True or False) or not False or (True and False or False)
U. (True or not not False) and (True or (True or (False)))
V. False and False or (not False and (not False))
W. (not True or not False) and (not True or (not False))
X. False or False and not True or not False and (not True and False)
Y. True and True and True and True and not True and True and True or False
Z. False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
"""


# - Booleans -
# Exercise A
expression = True or False and True
step_one = (True) or (False and True)
step_two = (True) or (False)
step_three = True
print(step_three == expression)
# Exercise B
expression = False and False or False
step_one = (False and False) or (False)
step_two = (False) or (False)
step_three = False
print(step_three == expression)
# Exercise C
expression = (True or False) and True
step_one = (True or False) and (True)
step_two = (True) and (True)
step_three = True
print(step_three == expression)
# Exercise D
expression = True or (True or False and True) and True
step_one = (True) or (True or False and True) and (True)
step_two = (True) or (True or (False and True)) and (True)
step_three = (True) or (True or False) and (True)
step_four = (True) or (True) and (True)
step_five = (True) or (True and True)
step_six = (True) or (True)
step_seven = True
print(step_seven == expression)
# Exercise E
expression = False or False and False and not False
step_one = (False) or (False and False and not False)
step_two = (False) or ((False and False) and (not False))
step_three = (False) or (False and True)
step_four = (False) or (False)
step_five = False
print(step_five == expression)
# Exercise F
expression = (True or True or False) and True
step_one = (True or True or False) and (True)
step_two = ((True or True) or False) and (True)
step_three = (True or False) and (True)
step_four = (True) and (True)
step_five = True
print(step_five == expression)
# Exercise G
expression = False or (True and False)
step_one = (False) or (True and False)
step_two = (False) or (False)
step_three = False
print(step_three == expression)
# Exercise H
expression = False and False and False and False and False or True and False
step_one = (False and False and False and False and False) or (True and False)
step_two = ((False and False) and (False and False) and False) or (True and False)
step_three = (False and False and False) or (True and False)
step_four = ((False and False) and False) or (True and False)
step_five = (False and False) or (True and False)
step_six = (False) or (False)
step_seven = False
print(step_seven == expression)
# Exercise I
expression = True or False or True
step_one = (True or False) or (True)
step_two = (True) or (True)
step_three = True
print(step_three == expression)
# Exercise J
expression = False or (not False)
step_one = (False) or (not False)
step_two = (False) or (True)
step_three = True
print(step_three == expression)
# Exercise K
expression = not True or not False
step_one = (not True) or (not False)
step_two = (False) or (True)
step_three = True
print(step_three == expression)
# Exercise L
expression = False and not False or not False
step_one = (False and not False) or (not False)
step_two = (False and (not False)) or (not False)
step_three = (False and True) or (not False)
step_four = (False) or (True)
step_five = True
print(step_five == expression)
# Exercise M
expression = True or not False and True or not not True
step_one = (True) or (not False and True) or (not not True)
step_two = (True) or ((not False) and True) or (not (not True))
step_three = (True) or ((not False) and True) or (not (not True))
step_four = (True) or (True and True) or (not False)
step_five = (True) or (True) or (True)
step_six = (True or True) or (True)
step_seven = (True) or (True)
step_eight = True
print(step_eight == expression)
# Exercise N
expression = not not not False
step_one = (not not not False)
step_two = (not not (not False))
step_three = (not not True)
step_four = (not (not True))
step_five = (not False)
step_six = True
print(step_six == expression)
# Exercise O
expression = not not not not False
step_one = (not not not not False)
step_two = (not not not (not False))
step_three = (not not not True)
step_four = (not not (not True))
step_five = (not not False)
step_six = (not (not False))
step_seven = (not True)
step_eight = False
print(step_eight == expression)
# Exercise P
expression = True or False and not True or (not True and False) and not True or False
step_one = (True) or (False and not True) or ((not True and False) and not True) or (False)
step_two = (True) or (False and not True) or (((not True) and False) and not True) or (False)
step_three = (True) or (False and not True) or ((False and False) and not True) or (False)
step_four = (True) or (False and not True) or (False and not True) or (False)
step_five = (True) or (False and (not True)) or (False and (not True)) or (False)
step_six = (True) or (False and False) or (False and False) or (False)
step_seven = (True) or (False) or (False) or (False)
step_eight = (True or False) or (False or False)
step_nine = (True) or (False)
step_ten = True
print(step_ten == expression)
# Exercise Q
expression = True or not False or not True or True
step_one = (True) or (not False) or (not True) or (True)
step_two = (True) or (True) or (False) or (True)
step_three = (True or True) or (False or True)
step_four = (True) or (True)
step_five = True
print(step_five == expression)
# Exercise R
expression = False and (not True or False or (False or not True and True or False)) and True
step_one = False and (not True or False or ((False) or ((not True) and True) or (False))) and True
step_two = False and (not True or False or ((False) or (False and True) or (False))) and True
step_three = False and (not True or False or ((False) or (False) or (False))) and True
step_four = False and (not True or False or ((False or False) or (False))) and True
step_five = False and (not True or False or ((False) or (False))) and True
step_six = False and (not True or False or (False or False)) and True
step_seven = False and ((not True) or (False) or (False)) and True
step_eight = False and ((False) or (False) or (False)) and True
step_nine = False and ((False or False) or (False)) and True
step_ten = False and ((False or False)) and True
step_eleven = False and (False) and True
step_twelve = (False and False) and (True)
step_thirteen = (False) and (True)
step_fourteen = False
print(step_fourteen == expression)
# Exercise S
expression = False and not not not True and (False or True or not False) and True or False
step_one = (False and not not not True and (False or True or not False) and True) or (False)
step_two = (False and not not not True and ((False) or (True) or (not False)) and True) or (False)
step_three = (False and not not not True and ((False) or (True) or (True)) and True) or (False)
step_four = (False and not not not True and ((False or True) or (True)) and True) or (False)
step_five = (False and not not not True and ((True) or (True)) and True) or (False)
step_five = (False and (not not not True) and (True) and True) or (False)
step_six = (False and (False) and (True) and True) or (False)
step_seven = ((False and False) and (True and True)) or (False)
step_eight = (False and True) or (False)
step_nine = (False) or (False)
step_ten = False
print(step_ten == expression)
# Exercise T
expression = not (True or False) or not False or (True and False or False)
step_one = not (True or False) or (not False) or ((True and False) or False)
step_two = not (True or False) or (not False) or (False or False)
step_three = not (True) or (True) or (False)
step_four = (not True) or (True) or (False)
step_five = (False) or (True) or (False)
step_six = (False or True) or (False)
step_seven = (True) or (False)
step_eight = True
print(step_eight == expression)
# Exercise U
expression = (True or not not False) and (True or (True or (False)))
step_one = (True or (not not False)) and (True or (True or (False)))
step_two = (True or False) and (True or True)
step_three = (True) and (True)
step_four = True
print(step_four == expression)
# Exercise V
expression = False and False or (not False and (not False))
step_one = (False and False) or (not False and (not False))
step_two = (False) or (not (False and True))
step_three = (False) or (not False)
step_four = (False) or (True)
step_five = True
print(step_five == expression)
# Exercise W
expression = (not True or not False) and (not True or (not False))
step_one = ((not True) or (not False)) and ((not True) or (not False))
step_two = (False or True) and (False or True)
step_three = (True) and (True)
step_four = True
print(step_four == expression)
# Exercise X
expression = False or False and not True or not False and (not True and False)
step_one = (False) or (False and not True) or (not False and (not True and False))
step_two = (False) or (False and False) or (True and (False and False))
step_three = (False) or (False) or (True and False)
step_four = (False) or (False) or (False)
step_five = False
print(step_five == expression)
# Exercise Y
expression = True and True and True and True and not True and True and True or False
step_one = (True and True and True and True and not True and True and True) or (False)
step_two = (True and True and True and True and (not True) and True and True) or (False)
step_three = (True and True and True and True and (False) and True and True) or (False)
step_four = (False) or (False)
step_five = False
print(step_five == expression)
# Exercise Z
expression = False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
step_one = (False and False and (True or not False and (True or (False and True)))) or (not True and False and (not False or not True))
step_two = (False and False and (True or True and (True or False))) or (False and False and (True or False))
step_three = (False and False and (True or (True and True))) or (False and False and True)
step_four = (False and False and (True or True)) or (False and False and True)
step_five = (False and False and True) or (False and False and True)
step_six = False or False
step_seven = False
print(step_seven == expression)  