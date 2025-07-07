"""
===============================
=   *args & **kwargs TASKS    =
===============================

# EASY

1. Write a function that accepts any number of positional arguments and prints them.

2. Write a function that sums all the numbers passed via *args.

3. Create a function that multiplies all numbers using *args.

4. Write a function that accepts any number of keyword arguments and prints them in key=value format.

5. Write a function that prints only the values from **kwargs.

6. Create a function that prints a greeting message using **kwargs with keys: name and age.

7. Write a function that combines *args and **kwargs and prints both.

8. Write a function that checks if a specific key exists in **kwargs.

9. Create a function that returns the longest word passed in *args.

10. Create a function that prints a formatted address using **kwargs (e.g., street, city, zip).

# MEDIUM

11. Write a function that filters only even numbers from *args.

12. Create a function that returns a dictionary combining both *args (as values) and **kwargs.

13. Create a function that takes a default tax rate via **kwargs and applies it to all *args prices.

14. Write a function that accepts student scores via **kwargs and returns the average.

15. Create a logger function that accepts *args as log messages and **kwargs for metadata (e.g., level, timestamp).

16. Build a function that uses *args to take any strings and **kwargs for formatting options like upper=True, reverse=True.

17. Create a function that finds the max of numbers from both *args and values in **kwargs.

18. Write a function that accepts any number of named configurations (**kwargs) and validates that required keys exist.

19. Write a decorator that uses *args and **kwargs to wrap and log function calls.

20. Implement a function that creates a formatted table where columns are defined via **kwargs and values via *args.

# HARD

21. Create a class with a method that accepts *args for dynamic field names and **kwargs for their values.

22. Write a function that groups items passed via **kwargs based on data type.

23. Design a function that builds a nested dictionary structure from **kwargs with dot notation (e.g., 'user.name': 'Ali').

24. Write a function that recursively sums all numbers passed via nested **kwargs.

25. Create a dynamic API router simulator function where *args represent endpoints and **kwargs represent methods and handlers.

"""


# ===============================
# =   *args & **kwargs TASKS    =
# ===============================

# EASY
# Exercise 1
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 4.8, "Alice", None, True)


# Exercise 2
# Example 1
def sum_args(*args):
    sum = 0
    for a in args:
        if isinstance(a,(int, float)):                 # isinstance() проверяет, является ли объект a экземпляром (объектом) указанного типа или типов.
            sum += a
    return sum

result = sum_args(5, 2.5, True, 6.9, 8, "apple")
print(result)

# Example 2
def sum_args(*args):
    return sum(a for a in args if isinstance(a, (int, float)))
result = sum_args(5, 2.5, True, 6.9, 8, "apple")
print(result)


# Exercise 3
def multiplies_args(*args):
    multp = 1
    for a in args:
        if isinstance(a,(int, float)):
            multp *= a
    return multp

result = multiplies_args(5, 2.5, True, 6.9, 8, "apple")
print(result)


# Exercise 4
def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}={v}") 

print_kwargs(name="Bob", salary=2_500)


# Exercise 5
def only_values(**kwargs):
    for value in kwargs.values():
        print(value)
only_values(name="Alice", age=18)


# Exercise 6
def greeting_message(**kwargs):
    if "name" in kwargs and "age" in kwargs:
        print(f"Hi, {kwargs["name"]}! You're {kwargs["age"]} years old.")
    else:
        print("Please enter your name and age!")
greeting_message(name="Sisilya", age=25)


# Exercise 7
def combines_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

combines_args_kwargs(1, 'hello', key='value', number=42)

# Exercise 8
def key_exists_in_kwargs(key, **kwargs):
    return key in kwargs

result = key_exists_in_kwargs('name', name='Mike', age=90)
print(result)

# Exercise 9
def longest_word(*args):
    return max(args, key=len)                     #параметр key=len в функции max() — это функция ключа, которая говорит max(), по какому признаку сравнивать элементы.

print(longest_word("apple", "banana", "cherry", "date"))


# Exercise 10
def formatted_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

formatted_address(city="New York", street="5th Avenue")


# MEDIUM
# Exercise 11
# Example 1
def filtered_even_numbers(*args):
    return [num for num in args if isinstance(num, int) and num % 2 == 0]

print(filtered_even_numbers(1, 2, 3, 4, 5, 6, 7, 8))

# Example 2
def filtered_even_numbers(*args):
    return list(filter(lambda num: isinstance(num, int) and num % 2 == 0, args))

print(filtered_even_numbers(1, 2, 3, 4, 5, 6, 7, 8))


# Exercise 13
def apply_tax(*args, **kwargs):
    if "tax_rate" in kwargs:
        tax = kwargs["tax_rate"]
    else:
        tax = 0
    return [price + price * tax for price in args]

print(apply_tax(100, 200, tax_rate=5))


# Exercise 14
def average_score(**kwargs):
    scores = kwargs.values()
    if not scores:
        return None
    return sum(scores) / len(scores)

print(average_score(Alice=35, Bob=90, Aren=78))



