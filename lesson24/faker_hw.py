"""
1. Generate 10 fake users with names and ages. 
Ask the user to enter a minimum age, and print only the users who are older.

2. Generate a list of 8 fake email addresses. 
Ask the user to input a domain (e.g. gmail.com) and show which emails match.

3. Generate 20 fake job titles and store them in a set to ensure uniqueness. 
Then display all unique job titles.

4. Generate a tuple of 5 fake countries. Show them to the user, then ask the 
user to guess one. Check if it’s in the list.

5. Generate a dictionary of 5 people with their names as keys and phone numbers as values. 
Let the user search for a name and display the phone number if it exists.
"""

from faker import Faker
import random

fake = Faker()
# Exercise 1
users = []

for i in range(10):
    names = fake.name()
    ages = random.randint(1, 100)
    print(names, ages)
    users.append({"names": names, "ages": ages})

min_age = int(input("Please enter minimal age:\n>> "))

for user in users:
    if user["ages"] > min_age:
        print(f"{user["names"]} {user["ages"]}")
print("----------------------------------------------")


# Exercise 2
email = []

for i in range(8):
    emails, domains = fake.free_email().split("@")
    print(f"{emails}@{domains}")
    email.append({"emails": emails, "domains": domains})

domain =  input("Please enter any domen (Example: gmail.com):\n>> ")

for dom in email:
    if dom["domains"] == domain:
        print(f"{dom["emails"]}@{dom["domains"]}")
print("----------------------------------------------")


# Exercise 3
job = []

for i in range(20):
    jobs = fake.job()
    print(jobs)
    job.append(jobs)

unique_jobs = set(job)
print("\nUnique Job Titles:")
for title in unique_jobs:
    print(title)
print("----------------------------------------------")


# Exercise 4
countries = []

for i in range(5):
    fake_country = fake.country()
    print(fake_country)
    countries.append({"country": fake_country})

guess_country = input("Please enter any country:\n>> ")

if guess_country in countries:
    print("This country is on the list.")
else:
    print("This country is not on the list.")
print("----------------------------------------------")


# Exercise 5
people = {}

for i in range(5):
    name = fake.name()
    phone = fake.basic_phone_number()
    people[name] = phone
    print(f"{name}: {phone}")

search_name = input("\nPlease enter a name to search:\n>> ")

if search_name in people:
    print(f"Phone number for {search_name}: {people[search_name]}")
else:
    print("This name is not in the list.")