"""
=======================
   WHILE LOOP TASKS
=======================

# EASY

1. Ask the user to enter a number. Keep asking until they enter a positive number.

2. Create a list of numbers from user input. Stop when the user types "stop".

3. Count from 1 to 10 using a while loop and print each number.

4. Ask for the user's name until they type a name longer than 3 characters.

5. Use a while loop to reverse a string manually (without using slicing).

# MEDIUM

6. Ask for numbers until user types "0", then print the sum of all entered numbers.

7. Store words entered by the user into a list until they type "done". Then print the list sorted.

8. Create a small login loop: ask username and password until they match "admin" / "1234".

9. Generate a random number between 1–10. Keep asking the user to guess until they get it right.

10. Ask the user to enter 5 numbers one by one, and then print the largest one.

# UPPER MEDIUM

11. Simulate a simple ATM: start with a balance of 100. Allow deposit, withdraw, check balance, exit.

12. Read integers from the user until a duplicate is entered. Then stop and show all unique numbers.

13. Let user enter numbers until they type "done". Print how many even and odd numbers were entered.

14. While loop that removes all vowels from a user input sentence and prints the result.

15. Ask for string inputs until a palindrome is entered. Then print all previously entered strings.

# HARDER

16. Simulate a typing game: show a random word from a list and ask the user to type it. Score how many are typed correctly out of 5 attempts.

17. Create a simple quiz loop with 3 questions. If the user gets 2 right, they pass.

18. Let the user build a dictionary: ask for key and value pairs. Stop on "exit", then print the dictionary.

19. Implement a password strength checker: ask until the password has min 8 chars, 1 digit, and 1 uppercase.

20. Let the user manage a list: add, remove, view items using commands in a loop until they type "exit".
"""




# =======================
#    WHILE LOOP TASKS
# =======================

# import random

# # EASY
# # Exercise 1
# while True:
#     num = int(input("Please enter any number:\n>> "))
#     if num > 0:
#         print("It is a positive number!")
#         break
#     elif num == 0:
#         print("Please try again!")
#     else:
#         print("It is a negative number!")


# # Exercise 2
# ls = []
# while True: 
#     n = input("Please enter any number:\n>> ")
#     if n =="stop":
#         print(ls)
#         break
#     else:
#         ls.append(int(n))


# # Exercise 3
# c = 1
# while c < 11:
#     print(c)
#     c += 1


# # Exercise 4
# while True:
#     name = input("Please enter a name longer than 3 characters:\n>> ")
#     if len(name) >= 3:
#         print("A name longer than 3 characters")
#         break
#     print("A name not consist 3 characters")


# # Exercise 5
# while True:
#     word = input("Please enter any word:\n>> ")
#     reversed_word = word[::-1]
#     print(reversed_word)
#     break


# # MEDIUM
# # Exercise 6
# ls = []
# while True:
#     nums = int(input("Please enter any number:\n>> "))
#     if nums == 0:
#         print(sum(ls))
#         break
#     else:
#         ls.append(nums)
#         print("Please try again!")


# # Exercise 7
# ls = []
# while True:
#     words = input("Please enter any word:\n>> ")
#     if words == "done":
#         print(sorted(ls))
#         break
#     else:
#         ls.append(words)


# # Exercise 8
# user_name = "admin"
# pass_word = "1234"
# while True:
#     username = input("Please enter your username:\n>> ")
#     password = input("Please enter your password:\n>> ")
#     if user_name == username and pass_word == password:
#         print("It is true login!")
#         break


# # Exercise 9
# x = random.randint(1, 10)
# while True:
#     user_guess = int(input("Please enter a random number between 1–10:\n>> "))
#     if x == user_guess:
#         print("You guessed right!")
#         break


# # Exercise 10
# ls = []
# while True:
#     for i in range(5):
#         user_nums = int(input("Please enter any number:\n>> "))
#         ls.append(user_nums)
#     print(max(ls))
#     break


# # UPPER MEDIUM
# # Exercise 11
# balance = 100
# while True:
#     print("\nWelcome to the ATM!")
#     print("[1] Check balance")
#     print("[2] Deposit money")
#     print("[3] Withdraw money")
#     print("[4] Exit")
#     choice = input("Please choose an option:\n>> ")
    
#     if choice == "1":
#         print(f"Your current balance is: {balance:}AZN")
    
#     elif choice == "2":
#         deposit_input = int(input("Please enter amount to deposit:\n>> "))
#         try:
#             if deposit_input <= 0:
#                 print("Amount must be positive.")
#             else:
#                 balance += deposit_input
#                 print(f"Deposit successful. New balance: ${balance:}AZN")
#         except ValueError:
#             print("Please try again!")
    
#     elif choice == "3":
#         withdraw_input = int(input("Please enter amount to withdraw:\n>> "))
#         try:
#             if withdraw_input <= 0:
#                 print("Amount must be positive.")
#             elif withdraw_input > balance:
#                 print("Not enough money in the balance.")
#             else:
#                 balance -= withdraw_input
#                 print(f"You withdrew {withdraw_input:}AZN. Balance: {round(balance):}AZN")
#         except ValueError:
#             print("Please try again!")

#     elif choice == "4":
#         print("Thank you for using the ATM. Goodbye!")
#         break

#     else:
#         print("Please try again!")


# # Exercise 12
# num = []
# check_duplicate = set()
# while True:
#     try:
#         user_input = int(input("Please enter an integer:\n>> "))
#         if user_input in check_duplicate:
#             print("It is duplicate number.")
#             break
#         else:
#             num.append(user_input)
#             check_duplicate.add(user_input)
#     except ValueError:
#         print("Please try again!")
# print(f"Unique numbers: {num}")


# # Exercise 13
# even_nums = 0
# odd_nums = 0
# while True:
#     user_input = input("Please enter any number:\n>> ")
#     if user_input == "done":
#         print(f"Even numbers count = {even_nums}")
#         print(f"Odd numbers count = {odd_nums}")
#         break
#     elif int(user_input) <= 0:
#         print("These are not even or odd numbers.")
#     elif int(user_input) % 2 == 0:
#         even_nums +=1
#     elif int(user_input) % 2 != 0:
#         odd_nums +=1
#     else:
#         print("Please try again!")


# # Exercise 14
# vowels = "aoueiAOUEI"
# user_input = list(input("Please enter any sentence:\n>> "))
# i = 0
# while i < len(user_input):
#     if user_input[i] in vowels:
#         user_input.pop(i)
#     else:
#         i += 1
# print("".join(user_input))


# # Exercise 15
# ls = []
# while True:
#     user_input = input("Please enter any string:\n>> ")
#     if user_input == user_input[::-1]:
#         print(f"Previously entered strings: {ls}")
#         break
#     else:
#         ls.append(user_input)


# # HARDER
# # Exercise 16
# fruits = ["mangosteens", "pomegranate", "rambutans", "durians", "guava", "jabuticaba", "langsat", "salak"]
# while True:
#     score = 0
#     selected_word = random.sample(fruits, 5)
#     for i, word in enumerate(selected_word, 1):
#         print(f"Word {i}: {word}")
#         user_input = input("Please enter your input:\n>> ").lower()
#         if user_input == word:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Wrong! The word was: {word}")
#     print(f"Game over! You got {score} out of 5.")
#     break


# # Exercise 17
# questions = [
#      {
#         "question": "What is the capital of Azerbaijan?",
#         "options": ["A. Baku", "B. Ganja", "C. Agdam", "D. London"],
#         "answer": "A"
#     },
#     {
#         "question": "How many planets are in the Solar System?",
#         "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
#         "answer": "B"
#     },
#     {
#         "question": "Which programming language are you learning now?",
#         "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
#         "answer": "C"
#     }
# ]

# while True:
#         score = 0
#         for q in questions:
#             print(q["question"])
#             for option in q["options"]:
#                 print(option)
        
#             while True:
#                 answer = input("Please enter your answer:\n>> ").upper()
#                 if answer in ['A', 'B', 'C', 'D']:
#                     break
#                 else:
#                     print("Invalid input. Please enter A, B, C, or D.")

#             if answer == q["answer"]:
#                 print("Correct!")
#                 score += 1
#             else:
#                 print(f"Wrong. The correct answer was: {q['answer']}")
#         break
# if score >= 2:
#     print(f"You passed! Score: {score}/3")
# else:
#     print(f"You failed. Score: {score}/3")


# # Exercise 18
# dict = {}

# while True:
#     key = input("Please enter any key word:\n>> ")
#     if key.lower() == 'exit':
#         break
#     value = input("Please enter a value for key:\n>> ")
#     dict[key] = value
# print(dict)


# # Exercise 19
# while True:
#     p = input("Please enter a password:\n>> ")
#     if len(p) >= 8 and any(c.isdigit() for c in p) and any(c.isupper() for c in p):
#         print("Reliable password!")
#         break
#     print("The password must consist of at least 8 chars, 1 digit and 1 capital letter.")

