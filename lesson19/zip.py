"""
- Zip (Parallel Iteration) & Enumerate (Counter) -
A. Write a program that takes a list and uses the enumerate method to print each 
element in the list along with its index. Use a suitable formatting for the output.
B. Parallelly iterate over the following collections and print the corresponding
pair values:
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]
C. Iterate over sequence of fruits and print the order of each fruit:
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
D. Write a program that takes two lists of equal lengths and uses the zip 
method to create a list of tuples, where each tuple contains elements from both 
lists at the corresponding index. Print the resulting list of tuples.

- Date & Time -
A. Write a program that prints 'Running...' each 1.5 seconds. The program should
be terminated after 5 executions of the print statement.
B. Write a program that uses the datetime module to display the current date and 
time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.
C. Write a program that takes a birthdate (year, month, day) and uses the datetime 
module to calculate the age in years.
D. Write a program calculate_elapsed_time(start_time, end_time) that takes two 
datetime objects representing a start time and an end time. Calculate and return 
the elapsed time in hours, minutes, and seconds.
E. Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
module to determine and return the number of days in that month.
F. Write a program that takes a birthdate (as a datetime object) and calculates the time 
remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.
G. Write a program that uses the time module to display the current time. However, 
add a delay of 5 seconds using time.sleep(5) before displaying the time.
H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
remaining seconds at each interval of 1 second.
I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
to achieve this. The program should display the time at each minute interval.
J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
module to select a random message from a predefined list and display it to the
K. Write a program in style of "Squid Game". First, create a list of ten random numbers.
Then, every 10 seconds remove (kill) the smallest value from the list.

- Chat GPT's Homework -
1. Write a program that uses the zip method to create a new list of tuples,
where each tuple contains elements from both lists at the corresponding 
index.

2. Write a program that takes two lists, keys and values and uses the zip 
method to create a dictionary where the elements from the keys list are the 
keys and the elements from the values list are the corresponding values. 

3. Write a program that takes an iterable and an optional starting index 
(default is 0). Implement the functionality of enumerate using a loop, and 
return a list of tuples where each tuple contains the index (starting from 
the provided start) and the corresponding element from the iterable.

4. Explain the difference between the time() method and the sleep() method 
in the time module. Provide use cases for each.

5. Describe the purpose and functionality of the strftime() method in the 
datetime module. Provide an example of how to use it.

6. Explain the significance of the epoch time (January 1, 1970) and how it's 
related to the time() method in the time module.

7. What is the purpose of the timedelta class in the datetime module? Provide 
an example use case where timedelta can be helpful.

Quiz.
1. The datetime module in Python provides a class for manipulating dates 
and times. What is the name of this class?
    a) Datetime
    b) Date
    c) Time
    d) datetime

2. Which method in the datetime module returns the current date and time?
    a) current()
    b) now()
    c) today()
    d) get_current_datetime()

3. In the strftime method, what does %Y represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Day of the week (Monday-Sunday)
    d) Hour (00-23)

4. Which module in Python provides functionality to work with time-related 
operations such as measuring time intervals, and converting between different 
time representations?
    a) time
    b) datetime
    c) timedelta
    d) timezone

5. Which method from the time module returns the current time in seconds since 
the epoch (January 1, 1970)?
    a) time()
    b) ctime()
    c) strftime()
    d) gmtime()

6. In the time module, which method pauses the program's execution for the specified 
number of seconds?
    a) sleep()
    b) wait()
    c) pause()
    d) delay()

7. Which method of the datetime class in the datetime module returns a formatted string 
representing the date and time?
    a) format()
    b) strftime()
    c) to_string()
    d) get_formatted()

8. In the datetime module, what does the timedelta class represent?
    a) A duration expressing the difference between two date or time instances
    b) A specific point in time
    c) A formatted date and time string
    d) A timezone offset

9. Which method of the timedelta class allows you to extract the number of days?
    a) days()
    b) total_days()
    c) get_days()
    d) days_total()

10. To get the current date and time, which method would you use in the datetime module?
    a) datetime.now()
    b) datetime.today()
    c) datetime.current()
    d) datetime.get_current()

11. In the strftime method, what does %d represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Day of the month (01-31)
    d) Hour (00-23)

12. In the strftime method, what does %H represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Hour (00-23)
    d) Minute (00-59)

13. In the strftime method, what does %M represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Minute (00-59)
    d) Second (00-59)

14. Consider the following Python code snippet:
    import time

    start_time = time.time()
    time.sleep(3)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds.")

    What is the purpose of this code, and what will be the output when it is executed?
    a) This code measures the execution time of the time.sleep(3) statement 
    and prints the elapsed time in seconds.
    b) This code creates a timer that prints "Execution took 3 seconds." 
    after waiting for 3 seconds.
    c) This code will throw an error because time.sleep() cannot be used 
    with a floating-point argument.
    d) This code will hang indefinitely without producing any output.
"""

import time
import datetime
import calendar
import random
from datetime import date, datetime
from datetime import timedelta

# - Zip (Parallel Iteration) & Enumerate (Counter)-
# Exercise A
colors = ["white", "blue", "red", "khaki", "purple"]

for index, color in enumerate(colors):
    print(f"{index} | {color}")
print("-------------------------------------")

# Exercise B
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]

for student, gift in zip(students, gifts):
    print(student, gift)
print("-------------------------------------")

# Exercise C
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]

for order, fruit in enumerate(fruits, start=1):
    print(f"{order} | {fruit}")
print("-------------------------------------")

# Exercise D
first_names = ["Alisa", "Esmeralda", "Samuel", "Teo", "Emili"]
last_names = ["Samoylova", "Pebanochi", "Arinovich", "Larionov", "Yenikeyeva"]

zipped_with_index = [(i, fn, ln) for i, (fn, ln) in enumerate(zip(first_names, last_names))]
print(zipped_with_index)
print("-------------------------------------")



# - Date & Time -
# Exercise A
for i in range(5):
    print("Running...")
    time.sleep(1.5)
print("-------------------------------------")

# Exercise B
current_datetime = datetime.datetime.now()
print(current_datetime)
print("-------------------------------------")

# Exercise C
while True:
    try:
        birth_date = input("Please enter your date of birth (YYYY-MM-DD):\n>> ")
        birthdate = datetime.strptime(birth_date, "%Y-%m-%d").date()      # Метод strptime() — это функция из модуля datetime в Python, которая преобразует строку в объект даты или времени согласно заданному формату.
        break                                                             # strftime() - метод который выводит объекты типа datetime в обычную строку

    except ValueError:
        print("Please enter the date correctly in (YYYY-MM-DD) format!")
        
today = date.today()
age = today.year - birthdate.year

if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1
print(f"You are {age} years old!")
print("-------------------------------------")

# Exercise D
start = datetime(2025, 5, 31, 14, 30, 0)
end = datetime(2025, 5, 31, 18, 45, 30)

def calculate_elapsed_time(start_time, end_time):             # Функция calculate elapsed time(start, end) в Python, как правило, предназначена для подсчета промежутка времени между двумя точками во времени.
    diff = end_time - start_time  
    seconds = diff.seconds         
    hours = seconds // 3600        
    minutes = (seconds % 3600) // 60  
    seconds = seconds % 60            
    return hours, minutes, seconds

h, m, s = calculate_elapsed_time(start, end)
print(h, "hours", m, "minutes", s, "seconds")
print("-------------------------------------")

# Exercise E
while True:
    try:
        year = int(input("Please enter any year:\n>> ")) 
        month = int(input("Please enter any month(1-12):\n>> "))
        break
    except ValueError:
        print("Invalid input! Please enter date correctly!")

def month_days(year, month):
    num_days = calendar.monthrange(year, month)
    return num_days

days = month_days(year, month)
print(f"Number of days in {month}.{year}: {days}")
print("-------------------------------------")

# Exercise G
time.sleep(5)
current_time = time.strftime("%H:%M:%S")
print(f"Current time: {current_time}")
print("-------------------------------------")
 
# Exercise H
time_in_seconds = int(input("Please enter the time in seconds:\n>> "))

while time_in_seconds > 0:
    print(f"{time_in_seconds}...")
    time.sleep(1)
    time_in_seconds -= 1
print("Time's up!")
print("-------------------------------------")

# Exercise I
try:
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current time: {current_time}")
        time.sleep(60)
except KeyboardInterrupt:
    print("Finish!")
print("-------------------------------------")

# Exercise J
messages = [
    "Stay positive and work hard!",
    "Remember to take breaks!",
    "Keep pushing forward!",
    "Success is a journey, not a destination.",
    "Believe in yourself!",
    "Focus on what you can control.",
    "Every day is a fresh start."
]

try:
    while True:
        message = random.choice(messages)
        print(message)
        wait_time = random.uniform(2, 5)
        time.sleep(wait_time)

except KeyboardInterrupt:
    print("Program stopped for you.")
print("-------------------------------------")

# Exercise K
numbers = []

for i in range(10):
    number = random.randint(1,100)
    numbers.append(number)

print(f"Here is the list of participants in the game: {numbers}")
numbers.sort()

while len(numbers) > 1:
    print(f"Leaves the game: {numbers[0]}")
    numbers.pop(0)
    time.sleep(1)

print(f"Winner: {numbers[0]}")
print("-------------------------------------")



# - Chat GPT's Homework -
# Exercise 1
first_names = ["Alisa", "Esmeralda", "Samuel", "Teo", "Emili"]
last_names = ["Samoylova", "Pebanochi", "Arinovich", "Larionov", "Yenikeyeva"]

zipped_with_index = [(i, fn, ln) for i, (fn, ln) in enumerate(zip(first_names, last_names))]
print(zipped_with_index)
print("-------------------------------------")

# Exercise 2
first_names = ["Alisa", "Esmeralda", "Samuel", "Teo", "Emili"]
last_names = ["Samoylova", "Pebanochi", "Arinovich", "Larionov", "Yenikeyeva"]

full_name = dict(zip(first_names, last_names))
print(full_name)
print("-------------------------------------")

# Exercise 3
def list_enumerate(iterable, start=0):
    result = []
    index = start
    for item in iterable:
        result.append((index, item))
        index += 1
    return result

list = ['pen', 'eraiser', 'book']
print(list_enumerate(list))     
print(list_enumerate(list, 3)) 
print("-------------------------------------")

# Exercise 4
epoch_time = time.time()          # time() возвращает текущее время в секундах с начала эпохи (1 января 1970 года)
print("Current epoch time:", epoch_time)
print("-------------------------------------")

print("Starting...")              
time.sleep(3)                      # sleep() приостанавливает выполнение программы на определенное количество секунд. 
print("3 seconds have passed, continuing now.")
print("-------------------------------------")

# Exercise 5
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")          # strftime() - метод который выводит объекты типа datetime в обычную строку
print("Current date and time:", current_time)
print("-------------------------------------")

# Exercise 6
epoch_time = time.time()          
print("-------------------------------------")
""" time() возвращает текущее время в секундах с начала эпохи (1 января 1970 года). 
Потому что 1 января 1970 год считается началом этохи Unix.Операционная система Unix, 
разработанная в лаборатории AT&T Bell Labs в конце 1960-х годов, начала свою работу в 1970 году. 
Для упрощения работы с датами и временем было решено использовать 1 января 1970 года как начало отсчета времени. 
Это решение позволило унифицировать представление времени в системе и упростить вычисления."""

# Exercise 7
delta = timedelta(days=1, hours=2, minutes=30)    
print(delta.total_seconds())
# Класс timedelta в Python представляет собой промежуток времени и предоставляет удобные средства для работы с датами и временем.



# Quiz.
# 1. d
# 2. b 
# 3. b
# 4. a
# 5. a
# 6. a
# 7. b
# 8. a
# 9. a
# 10. a
# 11. c
# 12. c
# 13. с
# 14. a