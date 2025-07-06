"""
======================
=   FOR LOOP TASKS   =
======================

# EASY

1. Print numbers from 1 to 10 using a for loop.

2. Print each character of a string entered by the user.

3. Create a list of 5 numbers. Use a for loop to print their squares.

4. Loop through a list of names and greet each person.

5. Use a for loop to count how many vowels are in a user-entered string.

# MEDIUM

6. Ask the user to enter 5 numbers. Store them in a list and print the average.

7. Given a list of words, print only the words longer than 5 characters.

8. Use a for loop to reverse a list manually and print the reversed list.

9. Generate the first 10 multiples of a number entered by the user.

10. Print a simple triangle pattern with `*` symbols using a nested for loop.

# UPPER MEDIUM

11. Let the user input 3 student names and 3 scores each. Print the average score per student.

12. Given a sentence, print each word and the number of letters it contains.

13. Loop through numbers 1–30. Print “Fizz” for multiples of 3, “Buzz” for 5, and “FizzBuzz” for both.

14. Loop through a list of dictionaries representing people, and print only names of adults (age ≥ 18).

15. Create a for loop that finds all prime numbers from 1 to 100 and prints them.

# HARDER

16. Build a mini multiplication table (up to 10x10) using nested for loops.

17. Simulate a mini voting system: ask 5 users to vote for candidates A/B/C. Show total votes per candidate.

18. Given a list of numbers, create a new list with only the unique numbers (no duplicates).

19. Implement a Caesar cipher: ask user for text and a shift, and encrypt the text using a for loop.

20. Ask the user for 5 file names, and check which of them end with `.txt` or `.csv`. Show the valid ones.
"""



# ======================
# =   FOR LOOP TASKS   =
# ======================

# EASY
# Exercise 1
for i in range(1, 11):
    print(i)


# Exrcise 2
user_input = input("Please enter any string:\n>> ")

for char in user_input:
    print(char)


# Exercise 3
num_ls = [3, 5, 7, 9, 11]

for sq in num_ls:
    print(sq**2)


# Exercise 4
name_ls = ["Bob", "Alice", "Mike", "Diana"]

for name in name_ls:
    print(f"Hello {name}!")


# Exercise 5
user_input = input("Please enter any string:\n>> ")
vowels = "aeuioAEUIO"
vowels_count = 0

for char in user_input:
    if char in vowels:
        vowels_count += 1
print(vowels_count)


# MEDIUM
# Exercise 6
ls = []

for i in range(5):
    numbers = int(input("Please enter any number:\n>> "))
    ls.append(numbers)

average = sum(ls)/len(ls)
print(average)


# Exercise 7
word_ls = ["apple", "table", "bag", "fish", "multiplication"]

for word in word_ls:
    if len(word) >= 5:
        print(word) 


# Exercise 8
word_ls = ["apple", "table", "bag", "fish", "multiplication"]

for _ in word_ls:
    reversed_ls = word_ls [::-1]
print(reversed_ls)


# Exercise 9
user_num = int(input("Please enter any integer:\n>> "))

for i in range(1, 11):
    print(f"{user_num} x {i} = {user_num * i}")


# Exercise 10
# Example 1
for i in range(1, 6):
    print(i * "*")

# Example 2
for i in range(1, 6):
    for _ in range(i):
        print("*", end="")
    print()


# UPPER MEDIUM
# Exercise 11
for n in range(3):
    scores_ls = []
    name = input(f"Please enter name{n + 1}:\n>> ")
    
    for s in range(3):
        scores = int(input("Please enter scores:\n>> "))
        scores_ls.append(scores)

    print(f"{name.capitalize()} average score: {sum(scores_ls) / len(scores_ls)}")


# Exercise 12
sentence = input("Please enter any sentence:\n>> ")

words = sentence.split()

for letters in words:
    word = ''.join(char for char in letters if char.isalpha())
    print(f"{word} count of letters: {len(word)}")
    

# Exercise 13
for i in range(1, 31):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)


# Exercise 14
people = [
    {
        "name": "Alice", 
        "age": 17
    },
    {
        "name": "Bob", 
        "age": 20
    },
    {
        "name": "Carol", 
        "age": 18
    },
    {   
        "name": "Dave", 
        "age": 15
    }
]

for person in people:
    if person["age"] >= 18:
        print(person["name"])


# Exercise 15
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)


# HARDER
# Exercise 16
for n in range(1, 11):
    for m in range(1, 11):
        print(f"{n} x {m} = {n * m}")
    print("\n")


# Exrcise 17
vote_A = 0
vote_B = 0
vote_C = 0

for i in range(5):
    vote = input("Please vote (A, B, C):\n>> ").strip().upper()
    if vote == "A":
        vote_A += 1
    elif vote == "B":
        vote_B += 1
    elif vote == "C":
        vote_C += 1
    else:
        print("Please try again!")

print(f"""
Candidate A: {vote_A}
Candidate B: {vote_B}
Candidate C: {vote_C}
""")


# Exercise 18
# Example 1
ls = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_ls = []

for i in ls:
    if i not in unique_ls:
        unique_ls.append(i)
print(unique_ls)

# Example 2
ls = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_ls = list(set(ls))
print(unique_ls)
    

# Exercise 20
files = []

for i in range(1, 6):
    filename = input(f"Please enter file name{i}:\n>> ").strip()
    
    if filename.endswith(".txt") or filename.endswith(".csv"):
        files.append(filename)

for file in files:
    print(file)